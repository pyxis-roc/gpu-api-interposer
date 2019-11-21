#!/usr/bin/env python3
#
# libcuda_replay.py
#
# Decodes the trace produced by libcuda instrumentation, connecting to
# CUDA Device API implementations.
#
# Author: Sreepathi Pai
#
# Copyright (c) 2019, University of Rochester

import sqlite3
import yaml
import babeltrace
import argparse
import glob
import os
import yaml
import logging
from .cuda_device_runtime import CUDADeviceAPIHandler, CUDADefaultFactory, CUDARemoteFactory

_logger = logging.getLogger(__name__)

def get_actual_tracedir(tracedir):
    if os.path.exists(os.path.join(tracedir, "metadata")):
        return [tracedir]

    out = []
    if os.path.exists(os.path.join(tracedir, "ust", "uid")):
        for uid in glob.iglob(os.path.join(tracedir, "ust", "uid", "*")):
            if os.path.exists(os.path.join(uid, "64-bit", "metadata")):
                out.append(os.path.join(uid, "64-bit"))

    return out

class NVArgHandler(object):
    def __init__(self, argfile):
        self.argfile = argfile

        with open(self.argfile, "r") as f:
            self.args = yaml.load(f)

    def unpack(self, fn, argdata, arch = 0, is_extra = False):
        out = []
        if fn in self.args:
            fna = self.args[fn]

            for d in fna:
                if d['arch'] == arch:
                    off = 0
                    if is_extra:
                        for off, sz in zip(d['param_offsets'], d['param_sizes']):
                            out.append(argdata[off:off+sz])
                    else:
                        for sz in d['param_sizes']:
                            out.append(argdata[off:off+sz])
                            off += sz

                    return out
            else:
                print(f"Unable to find description for arch={arch}")
        else:
            print(f"Unable to unpack for {fn}")

class PrePostLinker(object):
    def __init__(self):
        self.pre = dict()

    def register_pre(self, evname, pre_ev, pre_bsdata, fields = None):
        assert (evname, pre_ev['_ctx']) not in self.pre

        # data from one event must be consumed before the next ...
        # so make copies for post

        if fields is None:
            fields = pre_ev.field_list_with_scope(babeltrace.CTFScope.EVENT_FIELDS)

        evdata = {'.name': pre_ev.name}
        for f in fields:
            evdata[f] = pre_ev[f]

        self.pre[(evname, pre_ev['_ctx'])] = (evdata, pre_bsdata)

    def get_pre(self, evname, post_ev):
        k = (evname, post_ev['_ctx'])
        assert k in self.pre

        x = self.pre[k]
        del self.pre[k]

        return x

class NVTraceHandler(object):
    function_handles = None
    def __init__(self, arghandler, apihandler):
        self.arghandler = arghandler
        self.apihandler = apihandler

        self.pre_post = PrePostLinker()

    def set_callee_context(self, ctx):
        self.callee_ctx = ctx
        self.apihandler.set_callee_context(ctx)

    def cuInit_post(self, ev, bsdata):
        self.apihandler.cuInit(ev['Flags'])

    def cuGetExportTable_post(self, ev, bsdata):
        pass

    def cuDeviceGetCount_post(self, ev, bsdata):
        self.apihandler.cuDeviceGetCount(ev['count'])

    def cuDeviceGet_post(self, ev, bsdata):
        self.apihandler.cuDeviceGet(ev['device_contents'], ev['ordinal'])

    def cuDeviceGetName_post(self, ev, bsdata):
        self.apihandler.cuDeviceGetName(ev['name'], ev['dev'])

    def cuDeviceTotalMem_v2_post(self, ev, bsdata):
        self.apihandler.cuDeviceTotalMem(ev['bytes_contents'], ev['dev'])

    def cuDeviceTotalMem_post(self, ev, bsdata):
        self.apihandler.cuDeviceTotalMem(ev['bytes_contents'], ev['dev'])

    def cuDeviceGetAttribute_post(self, ev, bsdata):
        self.apihandler.cuDeviceGetAttribute(ev['pi_contents'], ev['attrib'], ev['dev'])

    def cuDeviceGetUuid_post(self, ev, bsdata):
        self.apihandler.cuDeviceGetUuid(ev['uuid'], ev['dev'])

    def cuCtxGetCurrent_post(self, ev, bsdata):
        self.apihandler.cuCtxGetCurrent(ev['pctx_contents'])

    def cuCtxSetCurrent_post(self, ev, bsdata):
        self.apihandler.cuCtxSetCurrent(ev['ctx'])

    def cuDriverGetVersion_pre(self, ev, bsdata):
        self.pre_post.register_pre('cuDriverGetVersion', ev, bsdata)

    def cuDevicePrimaryCtxRetain_post(self, ev, bsdata):
        self.apihandler.cuDevicePrimaryCtxRetain(ev['pctx_contents'], ev['dev'])

    def cuDevicePrimaryCtxRelease_post(self, ev, bsdata):
        self.apihandler.cuDevicePrimaryCtxRelease(ev['dev'])

    def cuCtxGetDevice_post(self, ev, bsdata):
        self.apihandler.cuCtxGetDevice(ev['device_contents'])

    def cuModuleGetFunction_post(self, ev, bsdata):
        self.apihandler.cuCtxGetDevice(ev['hfunc_contents'], ev['hmod'], ev['name'])

    def cuMemAlloc_v2_pre(self, ev, bsdata):
        self.pre_post.register_pre('cuMemAlloc_v2', ev, bsdata)

    def cuMemAlloc_v2_post(self, ev, bsdata):
        pre_ev, pre_bsdata = self.pre_post.get_pre('cuMemAlloc_v2', ev)
        self.apihandler.cuMemAlloc(ev['dptr_contents'], pre_ev['bytesize'])

    def cuMemFree_v2_post(self, ev, bsdata):
        self.apihandler.cuMemFree(ev['dptr'])

    def cuModuleUnload_post(self, ev, bsdata):
        self.apihandler.cuModuleUnload(ev['hmod'])

    def cuMemcpyHtoD_v2_pre(self, ev, bsdata):
        # this has no post
        data = None
        for r in bsdata:
            if r['name'] == 'srcHost':
                data = r['contents']
                break
        else:
            assert False, "No 'srcHost' found in blobstore for cuMemcpyHtoD"

        self.apihandler.cuMemcpyHtoD(ev['dstDevice'], ev['srcHost'],
                                     ev['ByteCount'], data)

    def cuMemcpyDtoH_v2_post(self, ev, bsdata):
        data = None
        for r in bsdata:
            if r['name'] == 'dstHost':
                data = r['contents']
                break
        else:
            assert False, "No 'dstHost' found in blobstore for cuMemcpyDtoH"

        #WARNING: if DtoH was asynchronous, then dstHost is invalid!

        self.apihandler.cuMemcpyDtoH(ev['dstHost'], ev['srcDevice'], ev['ByteCount'], data)

    def cuDriverGetVersion_post(self, ev, bsdata):
        pre_ev, pre_bsdata = self.pre_post.get_pre('cuDriverGetVersion', ev)
        self.apihandler.cuDriverGetVersion(ev['driverVersion'])

    def cuModuleGetFunction_post(self, ev, bsdata):
        self.apihandler.cuModuleGetFunction(ev['hfunc_contents'], ev['hmod'], ev['name'])

    def cuLaunchKernel_post(self, ev, bsdata):
        fn = self.apihandler.function_handles[ev['f']].name

        args = []
        for bsd in bsdata:
            if bsd['name'] == "kernelParams":
                kernelParams = bsd['contents']
                args = self.arghandler.unpack(fn, kernelParams)
                break
            elif bsd['name'] == 'extra':
                extra = bsd['contents']
                args = self.arghandler.unpack(fn, extra, is_extra = True)
                break
            else:
                raise NotImplementedError
        else:
            # TODO: check if this could happen for empty kernelParams and extra?
            assert False, "Unable to find kernelParams or extra in bsdata"

        self.apihandler.cuLaunchKernel(ev['f'],
                                       ev['gridDim'][0], ev['gridDim'][1], ev['gridDim'][2],
                                       ev['blockDim'][0], ev['blockDim'][1], ev['blockDim'][2],
                                       ev['sharedMemBytes'], ev['hStream'], args)

class TraceContext(object):
    cpu_id = None
    vtid = None
    thread_id = None   # portable

    # API-specific
    retval = None

class Replay(object):
    prefix = "libcuda_interposer:"

    def __init__(self, trace, blobstore):
        self.trace = trace

        self.tc = babeltrace.TraceCollection()
        self.th = self.tc.add_trace(self.trace, 'ctf')

        assert self.th is not None, "Unable to add trace"

        assert os.path.exists(blobstore), f"{blobstore} does not exit"

        self.bs = sqlite3.connect(blobstore)
        self.bs.row_factory = sqlite3.Row

        self.tctx = TraceContext()

    def set_trace_context(self, ev):
        self.tctx.cpu_id = ev['cpu_id']
        self.tctx.vtid = ev['vtid']
        self.tctx.thread_id = self.tctx.vtid

        if '_retval' in ev:
            self.tctx.retval = ev['_retval']
        else:
            # can happen for -pre
            self.tctx.retval = None

    @property
    def trace_context(self):
        return self.tctx

    def replay(self, handler):

        handler.set_callee_context(self.trace_context)

        conn = self.bs.cursor()
        rows = conn.execute("SELECT * FROM blobstore ORDER BY ctx, content_part")
        last_row = None

        lprefix = len(self.prefix)
        for event in self.tc.events:
            if event.name[:lprefix] == self.prefix:
                ctx = event['_ctx']
                blobstore_data = []
                while True:
                    if last_row is not None:
                        r = last_row
                        last_row = None
                    else:
                        r = rows.fetchone()

                    if r is None:
                        break

                    if r['ctx'] == ctx:
                        blobstore_data.append(r)
                    else:
                        last_row = r
                        break

                evname = event.name[lprefix:]
                self.set_trace_context(event)

                if hasattr(handler, evname):
                    hf = getattr(handler, evname)
                    _logger.debug(f'Invoking handler for {evname} from thread {self.trace_context.thread_id}')
                    hf(event, blobstore_data)
                else:
                    _logger.warning(f'No handler for {evname} found')

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Replay a captured CUDA trace.")
    p.add_argument("trace", help="Directory containing trace")
    p.add_argument("blobstore", help="Blobstore file")
    p.add_argument("binary", help="Binary file")
    p.add_argument("argfile", help="Argument format description (YAML)")
    p.add_argument("-d", dest="debug", action="store_true", help="Debug")
    p.add_argument("--factory", choices=['default', 'remote'], default='default')

    args = p.parse_args()

    rootLogger = logging.getLogger('')

    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter('%(name)s: %(levelname)s: %(message)s'))
    rootLogger.addHandler(ch)

    if args.debug:
        rootLogger.setLevel(logging.DEBUG)
    else:
        rootLogger.setLevel(logging.INFO)

    td = get_actual_tracedir(args.trace)
    assert len(td) == 1, td # do not support more than one tracedir yet ...

    ah = NVArgHandler(args.argfile)
    r = Replay(td[0], args.blobstore)

    if args.factory == 'default':
        factory = CUDADefaultFactory()
    elif args.factory == 'remote':
        factory = CUDARemoteFactory()

    r.replay(NVTraceHandler(ah, CUDADeviceAPIHandler(args.binary, factory)))
