#!/usr/bin/env python3

import sqlite3
import yaml
import babeltrace
import argparse
import glob
import os
import yaml


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

class NVTraceHandler(object):
    function_handles = None
    def __init__(self, arghandler):
        self.arghandler = arghandler
        self.function_handles = {}

    def cuModuleGetFunction_post(self, ev, bsdata):
        self.function_handles[ev['hfunc_contents']] = ev['name']

    def cuLaunchKernel_post(self, ev, bsdata):
        if ev['f'] in self.function_handles:
            fn = self.function_handles[ev['f']]
            print(f"in cuLaunchKernel_post for {fn}")
            print(ev['gridDim'])
            print(ev['blockDim'])

            for bsd in bsdata:
                if bsd['name'] == "kernelParams":
                    kernelParams = bsd['contents']
                    args = self.arghandler.unpack(fn, kernelParams)
                    print(args)
                elif bsd['name'] == 'extra':
                    extra = bsd['contents']
                    args = self.arghandler.unpack(fn, extra, is_extra = True)
                    print(args)
                else:
                    raise NotImplementedError

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

    def replay(self, handler):
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
                if hasattr(handler, evname):
                    hf = getattr(handler, evname)
                    hf(event, blobstore_data)

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="")
    p.add_argument("trace", help="Directory containing trace")
    p.add_argument("blobstore", help="Blobstore file")
    p.add_argument("argfile", help="Argument format description (YAML)")

    args = p.parse_args()

    td = get_actual_tracedir(args.trace)
    assert len(td) == 1, td # do not support more than one tracedir yet ...

    ah = NVArgHandler(args.argfile)
    r = Replay(td[0], args.blobstore)
    r.replay(NVTraceHandler(ah))
