#!/usr/bin/env python3
#
# cuda_device_runtime.py
#
# "Implementation" of the CUDA device runtime API, actually just maintains API state.
#
# Author: Sreepathi Pai
# Author: Amr Elhelw
# Author: Benjamin Valpey
#
# Copyright (C) 2019, University of Rochester
#
# SPDX-FileCopyrightText: 2019,2021,2022 University of Rochester
#
# SPDX-License-Identifier: MIT


# fmt: off

import logging
from typing import Set, Dict
import struct

from harmonv import nvfatbin, compression, loader
from .cuda_api_objects import *
from .cuda_api_constants import *
from .cuda_devices import *
from .cuda_remote_devices import *
import itertools

_logger = logging.getLogger(__name__)


class CUDADefaultFactory(object):
    gpu = CUDAGPU
    function = CUDAFunction
    module = CUDAModule
    memory_region = CUDAMemoryRegion
    stream = CUDAStream
    context = CUDAContext
    array = CUDAArray
    tex_ref = CUDATexRef

class CUDARemoteFactory(object):
    gpu = RemoteCUDAGPU
    function = CUDAFunction
    module = CUDAModule
    memory_region = CUDAMemoryRegion
    stream = CUDAStream
    context = CUDAContext
    array = CUDAArray
    tex_ref = CUDATexRef

def check_retval(f):
    def checker(self, *args, **kwargs):
        if self.callee_ctx.retval is not None and self.callee_ctx.retval != 0:
            _logger.warning(f"Function call {f.__name__} failed in trace with error code {self.callee_ctx.retval}, not calling handler")
            return

        return f(self, *args, **kwargs)

    return checker


class CUDADeviceAPIInstr(object):
    # set of API functions that should be instrumented
    instr_fns = None

    def __init__(self):
        self.instr_fns: Set[str] = set()

    def cuMemcpyDtoH(self, dstHost, srcDevice, ByteCount, _data, _gpudata):
        pass


class CUDADeviceAPIHandler(object):
    """Tracks state across CUDA Device API calls. Called by the TraceHandler."""
    def __init__(self, binary, factory, config = None):
        self.binary = binary
        self._factory = factory
        self.gpu_handles = CUDAHandles("CUDevice")
        self.thread_contexts = CUDAHandles("CUcontext")
        self.function_handles = CUDAHandles("CUfunction")
        self.module_handles = CUDAHandles("CUmodule")
        self.memory_handles = CUDAHandles("CUdeviceptr")
        self.stream_handles = CUDAHandles("CUstream")
        self.array_handles = CUDAHandles("CUArray")
        self.tex_ref_handles = CUDAHandles("CUTexRef")
        self.config = config
        self.module_globals = {} # handle: set

        if self.config and self.config.api_instr:
            self.api_instr = self.config.api_instr
        else:
            self.api_instr = CUDADeviceAPIInstr()

        self.gpu_kwargs = {}
        if self.config and self.config.emu_class:
            self.gpu_kwargs['emu_cls'] = self.config.emu_class

        self.gpus = []
        self.main_module = self.load_binary(self.binary)

    def load_binary(self, binary):
        fatbin = nvfatbin.NVFatBinary(binary, compression.DefaultDecompressor)
        fatbin.parse_fatbin()

        return fatbin

    def set_callee_context(self, ctx):
        self.callee_ctx = ctx

    @check_retval
    def cuDriverGetVersion(self, driverVersion):
        _logger.debug(f'Setting driverVersion to {driverVersion}')
        self.driverVersion = driverVersion

    @check_retval
    def cuInit(self, Flags):
        _logger.info(f"cuInit called from thread {self.callee_ctx.thread_id}")

    @check_retval
    def cuDeviceGetCount(self, count):
        self.gpus = [self._factory.gpu(i, **self.gpu_kwargs) for i in range(count)]

    @check_retval
    def cuDeviceGet(self, device, ordinal):
        self.gpu_handles.register(device, self.gpus[ordinal])

    @check_retval
    def cuDeviceGetName(self, name, dev):
        self.gpu_handles[dev].name = name

    @check_retval
    def cuDeviceTotalMem(self, bytes_, dev):
        self.gpu_handles[dev].total_memory = bytes_

    @check_retval
    def cuDeviceGetAttribute(self, pi, attrib, dev):
        # this is not a typo, we're recording the values returned by the trace
        self.gpu_handles[dev].set_attribute(attrib, pi)
        if 'cuDeviceGetAttribute' in self.api_instr.instr_fns:
            self.api_instr.cuDeviceGetAttribute(pi, attrib, dev)

    @check_retval
    def cuDeviceGetUuid(self, uuid, dev):
        self.gpu_handles[dev].uuid = uuid

    @check_retval
    def cuCtxGetCurrent(self, pctx):
        tid = self.callee_ctx.thread_id
        if tid  not in self.thread_contexts:
            self.thread_contexts.register(tid, CUDAContextThreadStack())

        if pctx == 0:
            assert self.thread_contexts[tid].is_empty(), "Per-thread context stack is not empty, state inconsistent!"
        else:
            assert self.thread_contexts[tid].top.addr == pctx, "State inconsistent"

    @check_retval
    def cuCtxSetCurrent(self, ctx):
        tid = self.callee_ctx.thread_id
        if tid  not in self.thread_contexts:
            self.thread_contexts.register(tid, CUDAContextThreadStack())

        self.thread_contexts[tid].push(CUDAContext(ctx))

    @check_retval
    def cuDevicePrimaryCtxRetain(self, ctx, dev):
        self.gpu_handles[dev].primary_ctx_retain(ctx)

    @check_retval
    def cuDevicePrimaryCtxRelease(self, dev):
        self.gpu_handles[dev].primary_ctx_release()

    @check_retval
    def cuCtxGetDevice(self, dev):
        tid = self.callee_ctx.thread_id
        if tid not in self.thread_contexts:
            self.thread_contexts.register(tid, CUDAContextThreadStack())

        assert not self.thread_contexts[tid].is_empty(), "Stack is empty, inconsistent state"

        self.thread_contexts[tid].top.dev = dev

    def _get_thread_ctx(self):
        # errors here indicate inconsistent state ...
        # not handling right now

        tid = self.callee_ctx.thread_id
        assert tid in self.thread_contexts

        assert not self.thread_contexts[tid].is_empty()
        ctx = self.thread_contexts[tid].top

        return ctx

    def _load_module(self, gpu, module):
        elf = loader.extract_elf(module, gpu.cc)
        ptx, compat_ptx = loader.extract_ptx(module, gpu.cc)
        for m in itertools.chain(elf, ptx, compat_ptx):
            m.parse()

        mod = self._factory.module(gpu.cc, elf, ptx, compat_ptx)
        gpu.register_module(mod)
        return mod

    @check_retval
    def cuModuleGetFunction(self, hfunc, hmod, name):
        # I'm assuming the current context determines which variant of a function is loaded ...
        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]

        _logger.info(f'cuModuleGetFunction {name} for compute capability {gpu.compute_capability}')

        # this implicit registration is because the CUDA Runtime seems
        # to register modules for the main executable out-of-band.
        if hmod not in self.module_handles:
            # module handles are per context,
            # each context contains one gpu device
            self.module_handles.register(hmod, self._load_module(gpu,
                                                                 self.main_module))

        module = self.module_handles[hmod]

        assert len(module.elf) > 0 or len(module.ptx) > 0 or len(module.compat_ptx) > 0, "Unable to find ELF suitable for arch {cc}, or any PTX at all"

        elf = None
        ptx = None
        for m in module.elf:
            for g in m.get_globals():
                if g.name == name:
                    elf = m
                    break

        nb = name.encode('ascii')
        for m in itertools.chain(module.ptx, module.compat_ptx):
            a = m.get_data()
            #print(a)
            if nb in a:
                #TODO: need to parse ptx to get globals...
                ptx = m
                break

        _logger.info(f"Using ELF:{elf} and PTX:{ptx} for {name}")
        assert not (elf is None and ptx is None), "Unable to find ELF/PTX containing function {name}"

        self.function_handles.register(hfunc, self._factory.function(name, elf, ptx, hmod))

    @check_retval
    def cuMemAlloc(self, dptr, bytesize):
        ctx = self._get_thread_ctx()

        _logger.info(f'cuMemAlloc on device {ctx.dev}: {bytesize} bytes at 0x{dptr:x}')

        # TODO: actually convey to GPU that memory has been allocated
        gpu = self.gpu_handles[ctx.dev]

        mr = self._factory.memory_region(ctx.dev, dptr, bytesize)

        assert gpu.alloc_memory_region(mr)

        self.memory_handles.register(dptr, mr)

        if 'cuMemAlloc' in self.api_instr.instr_fns:
            self.api_instr.cuMemAlloc(dptr, bytesize)

    @check_retval
    def cuModuleGetGlobal(self, dptr, bytesize, hmod, name):
        ctx = self._get_thread_ctx()

        _logger.info(f'cuModuleGetGlobal on device {ctx.dev}: {bytesize} bytes at 0x{dptr:x} for symbol {name}')
        self.module_globals[hmod] = self.module_globals.get(hmod, set())

        if dptr != 0 and bytesize != 0:
            if name not in self.module_globals[hmod]:
                gpu = self.gpu_handles[ctx.dev]

                mr = self._factory.memory_region(ctx.dev, dptr, bytesize)

                assert gpu.alloc_memory_region(mr)

                self.memory_handles.register(dptr, mr)

                self.module_globals[hmod].add(name)
        else:
            _logger.warning(f'One of dptr ({dptr:x}) or bytesize ({bytesize}) was NULL/0, not registering cuModuleGetGlobal for {name}')
        if 'cuModuleGetGlobal' in self.api_instr.instr_fns:
            self.api_instr.cuModuleGetGlobal(dptr, bytesize, hmod, name)

    @check_retval
    def cuMemFree(self, dptr):
        if dptr == 0:
            _logger.info("cuMemFree on NULL pointer, ignoring.")
        else:
            mr = self.memory_handles[dptr]

            # TODO: convey to GPU that memory has been freed
            gpu = self.gpu_handles[mr.dev]
            assert gpu.dealloc_memory_region(mr) is not None

            _logger.info(f'cuMemFree on device {mr.dev}: {mr.bytesize} bytes at 0x{mr.dptr:x}')
            self.memory_handles.unregister(dptr)

        if 'cuMemFree' in self.api_instr.instr_fns:
            self.api_instr.cuMemFree(dptr)

    @check_retval
    def cuMemcpyHtoD(self, dstDevice, srcHost, ByteCount, _data):
        # TODO: handle multi-GPU correctly
        # i.e. identify gpus from dstDevice pointers

        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]

        assert gpu.has_dptr(dstDevice, ByteCount)
        #_logger.info(f'cuMemcpyHtoD on device {ctx.dev}: {ByteCount} bytes to 0x{dstDevice:x} from 0x{srcHost:x}')
        gpu.set_memory(dstDevice, _data)
        if 'cuMemcpyHtoD' in self.api_instr.instr_fns:
            self.api_instr.cuMemcpyHtoD(dstDevice, srcHost, ByteCount, _data)

    @check_retval
    def cuMemcpyDtoH(self, dstHost, srcDevice, ByteCount, _data):
        # this function really has no meaning in a trace, however we
        # simply implement a byte-wise comparison with the _data
        # recorded at runtime

        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]

        assert gpu.has_dptr(srcDevice, ByteCount)
        _logger.info(f'cuMemcpyDtoH on device {ctx.dev}: {ByteCount} bytes from device 0x{srcDevice:x} to host 0x{dstHost:x}')

        if 'cuMemcpyDtoH' in self.api_instr.instr_fns:
            # TODO: should we send gpu object?
            self.api_instr.cuMemcpyDtoH(dstHost, srcDevice, ByteCount, _data,
                                        gpu.get_memory(srcDevice, ByteCount))

    @check_retval
    def cuLaunchKernel(self, f, gridDimX, gridDimY, gridDimZ, blockDimX, blockDimY, blockDimZ, sharedMemBytes, hStream, kernelParams):
        assert f in self.function_handles

        if hStream not in self.stream_handles:
            self.stream_handles.register(hStream, self._factory.stream())

        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]

        gpu.launch_kernel(self.function_handles[f],
                          dim(gridDimX, gridDimY, gridDimZ),
                          dim(blockDimX, blockDimY, blockDimZ),
                          sharedMemBytes,
                          self.stream_handles[hStream],
                          kernelParams)

        if 'cuLaunchKernel' in self.api_instr.instr_fns:
            self.api_instr.cuLaunchKernel(self.function_handles[f].name,
                gridDimX,
                gridDimY,
                gridDimZ,
                blockDimX,
                blockDimY,
                blockDimZ,
                sharedMemBytes,
                self.stream_handles[hStream],
                kernelParams,
                {k: v for k,v in self.tex_ref_handles.handles.items() if v.hmod == self.function_handles[f].hmod})

    @check_retval
    def cuModuleUnload(self, hmod):
        # TODO: check _retval
        if hmod in self.module_handles:
            self.module_handles.unregister(hmod)

    @check_retval
    def cuMemcpyToArray(self, dst, wOffset, hOffset, src, count, kind):
        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]
        assert gpu.has_dptr(dst)

        _logger.info(
            f"cuMemcpyToArray on device {ctx.dev}: {count} bytes from device 0x{src:x} to host 0x{dst:x}"
        )

        if "cuMemcpyToArray" in self.api_instr.instr_fns:
            self.api_instr.cuMemcpyToArray(dst, wOffset, hOffset, src, count, kind)


    @check_retval
    def cuMemcpyDtoD(self, dstDevice, srcDevice, ByteCount, _data=None):
        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]

        _logger.info(
            f"cuMemcpyDtoD on device {ctx.dev}: {ByteCount} bytes to 0x{dstDevice:x} from 0x{srcDevice:x}"
        )

        assert gpu.has_dptr(dstDevice, ByteCount)
        assert gpu.has_dptr(srcDevice, ByteCount)

        gpu.set_memory(dstDevice, gpu.get_memory(srcDevice, ByteCount))

        if "cuMemcpyDtoD" in self.api_instr.instr_fns:
            self.api_instr.cuMemcpyDtoD(dstDevice, srcDevice, ByteCount, _data)


    @staticmethod
    def _unpackStructField(data: bytes):
        """
        Unpack a struct into an integer if width is either 4 or 8
        :param data: The data that should be unpacked
        :returns: The unpacked data
        :Raises: ``ValueError`` if width is not 4 or 8
        """
        if len(data) == 4:
            return struct.unpack('I', data)[0]
        elif len(data) == 8:
            return struct.unpack('Q', data)[0]
        else:
            raise ValueError(f"Attempting to unpack a struct with unsupported width: {len(data)}.")

    def _check_memcpy3d_dptr(self, gpu, s_or_d: str, data_dict):
        """
        Helper method for cuMemcpy3D that ensure that the gpu has a dptr for the data
        """
        copy_size = (
            (self._unpackStructField(data_dict["Depth"]) - 1)
            * (
                self._unpackStructField(data_dict[f"{s_or_d}Pitch"])
                * self._unpackStructField(data_dict[f"{s_or_d}Height"])
            )
            + (
                (self._unpackStructField(data_dict["Height"]) - 1)
                * self._unpackStructField(data_dict[f"{s_or_d}Pitch"])
            )
            + self._unpackStructField(data_dict["WidthInBytes"])
        )
        assert gpu.has_dptr(self._unpackStructField(data_dict[f'{s_or_d}Device']), copy_size)

    @check_retval
    def cuMemcpy3D(self, pCopy, _data_dict: Dict):
        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]
        
        _logger.info(f"cuMemcpy3D on device {ctx.dev} described by 0x{pCopy:x}")


        dstMemoryType = CUDA_MEMORYTYPE_ENUM_MAP[self._unpackStructField(_data_dict['dstMemoryType'])]
        srcMemoryType = CUDA_MEMORYTYPE_ENUM_MAP[self._unpackStructField(_data_dict['srcMemoryType'])]

        dstArrayHandle = None
        if dstMemoryType == "CU_MEMORYTYPE_ARRAY":
            assert self._unpackStructField(_data_dict['dstArray']) in self.array_handles
            dstArrayHandle = self.array_handles[self._unpackStructField(_data_dict['dstArray'])]
        elif dstMemoryType == "CU_MEMORYTYPE_DEVICE":
            self._check_memcpy3d_dptr(gpu, 'dst', _data_dict)

        srcArrayHandle = None
        if srcMemoryType == "CU_MEMORYTYPE_ARRAY":
            assert self._unpackStructField(_data_dict['srcArray']) in self.array_handles
            srcArrayHandle = self.array_handles[self._unpackStructField(_data_dict['srcArray'])]
        elif srcMemoryType == "CU_MEMORYTYPE_DEVICE":
            self._check_memcpy3d_dptr(gpu, 'src', _data_dict)

        # NOTE: Memcpy3D can set gpu memory, but this will not be captured here

        if "cuMemcpy3D" in self.api_instr.instr_fns:
            self.api_instr.cuMemcpy3D(pCopy, _data_dict, srcArrayHandle, dstArrayHandle)

    @check_retval
    def cuModuleGetTexRef(self, pTexRef, hmod, name):
        # Are texture references per module? This won't work if two separate .o files 
        # reference textures with the same name.  Might be an edge case, though.
        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]

        _logger.info(f"cuModuleGetTexRef on device {ctx.dev}: {name} at 0x{pTexRef:x}")

        if pTexRef not in self.tex_ref_handles:
            new_texref = self._factory.tex_ref(ctx.dev, hmod, pTexRef, name)
            self.tex_ref_handles.register(pTexRef, new_texref)
        else:
            new_texref = self.tex_ref_handles[pTexRef]

        if 'cuModuleGetTexRef' in self.api_instr.instr_fns:
            self.api_instr.cuModuleGetTexRef(pTexRef, hmod, name, new_texref)

    @check_retval
    def cuTexRefSetFlags(self, hTexRef: int, Flags: int):
        ctx = self._get_thread_ctx()

        _logger.info(
            f"cuTexRefSetFlags on device {ctx.dev}: 0x{hTexRef:x} with flags 0x{Flags:x}"
        )

        # ensure that the textureReference object has been registered

        assert hTexRef in self.tex_ref_handles, f"Texture reference 0x{hTexRef:x} is not registered"

        self.tex_ref_handles[hTexRef].set_flags(Flags)

        if "cuTexRefSetFlags" in self.api_instr.instr_fns:
            self.api_instr.cuTexRefSetFlags(hTexRef, Flags)

    @check_retval
    def cuTexRefSetFormat(self, hTexRef, fmt, NumPackedComponents: int):
        ctx = self._get_thread_ctx()

        _logger.info(
            f"cuTexRefSetFlags on device {ctx.dev}: 0x{hTexRef:x} with fmt: {fmt} and NumPackedComponents: {NumPackedComponents}"
        )

        assert hTexRef in self.tex_ref_handles, f"Texture reference 0x{hTexRef:x} is not registered"

        self.tex_ref_handles[hTexRef].set_format(fmt, NumPackedComponents)

        if "cuTexRefSetFormat" in self.api_instr.instr_fns:
            self.api_instr.cuTexRefSetFormat(hTexRef, fmt, NumPackedComponents)

    @check_retval
    def cuTexRefSetFilterMode(self, hTexRef, fm: int):
        ctx = self._get_thread_ctx()

        _logger.info(
            f"cuTexRefSetFilterMode on device {ctx.dev}: 0x{hTexRef:x} with fm: {fm}"
        )

        assert hTexRef in self.tex_ref_handles, f"Texture reference 0x{hTexRef:x} is not registered"

        self.tex_ref_handles[hTexRef].set_filterMode(fm)

        if "cuTexRefSetFilterMode" in self.api_instr.instr_fns:
            self.api_instr.cuTexRefSetFilterMode(hTexRef, fm)

    @check_retval
    def cuTexRefSetMaxAnisotropy(self, hTexRef: int, maxAniso: int):
        ctx = self._get_thread_ctx()

        _logger.info(
            f"cuTexRefSetMaxAnisotropy on device {ctx.dev}: 0x{hTexRef:x} with maxAniso: {maxAniso}"
        )

        assert hTexRef in self.tex_ref_handles, f"Texture reference 0x{hTexRef:x} is not registered"

        self.tex_ref_handles[hTexRef].set_maxAnisotropy(maxAniso)

        if "cuTexRefSetMaxAnisotropy" in self.api_instr.instr_fns:
            self.api_instr.cuTexRefSetMaxAnisotropy(hTexRef, maxAniso)

    @check_retval
    def cuTexRefSetMipmapFilterMode(self, hTexRef: int, fm: int):
        ctx = self._get_thread_ctx()

        _logger.info(
            f"cuTexRefSetMipmapFilterMode on device {ctx.dev}: 0x{hTexRef:x} with fm: {fm}"
        )

        assert hTexRef in self.tex_ref_handles, f"Texture reference 0x{hTexRef:x} is not registered"

        self.tex_ref_handles[hTexRef].set_mipmapFilterMode(fm)

        if "cuTexRefSetMipmapFilterMode" in self.api_instr.instr_fns:
            self.api_instr.cuTexRefSetMipmapFilterMode(hTexRef, fm)

    @check_retval
    def cuTexRefSetMipmapLevelBias(self, hTexRef: int, bias: int):
        ctx = self._get_thread_ctx()

        _logger.info(
            f"cuTexRefSetMipmapLevelBias on device {ctx.dev}: 0x{hTexRef:x} with bias: {bias}"
        )

        assert hTexRef in self.tex_ref_handles, f"Texture reference 0x{hTexRef:x} is not registered"

        self.tex_ref_handles[hTexRef].set_mipmapLevelBias(bias)

        if "cuTexRefSetMipmapLevelBias" in self.api_instr.instr_fns:
            self.api_instr.cuTexRefSetMipmapLevelBias(hTexRef, bias)

    @check_retval
    def cuTexRefSetMipmapLevelClamp(self, hTexRef: int, mn: int, mx: int):
        ctx = self._get_thread_ctx()

        _logger.info(
            f"cuTexRefSetMipmapLevelClamp on device {ctx.dev}: 0x{hTexRef:x} with min: {mn}, max: {mx}"
        )

        assert hTexRef in self.tex_ref_handles, f"Texture reference 0x{hTexRef:x} is not registered"

        self.tex_ref_handles[hTexRef].set_mipmapLevelClamp(mn, mx)

        if "cuTexRefSetMipmapLevelClamp" in self.api_instr.instr_fns:
            self.api_instr.cuTexRefSetMipmapLevelClamp(hTexRef, mn, mx)

    @check_retval
    def cuTexRefSetAddressMode(self, hTexRef: int, dim: int, am: int):
        ctx = self._get_thread_ctx()

        _logger.info(
            f"cuTexRefSetAddressMode on device {ctx.dev}: 0x{hTexRef:x} with dim: {dim}, am: {am}"
        )

        assert dim < 3
        assert hTexRef in self.tex_ref_handles, f"Texture reference 0x{hTexRef:x} is not registered"
        
        self.tex_ref_handles[hTexRef].set_addressMode(dim, am)

        if "cuTexRefSetAddressMode" in self.api_instr.instr_fns:
            self.api_instr.cuTexRefSetAddressMode(hTexRef, dim, am)

    @check_retval
    def cuTexRefSetArray(self, hTexRef: int, hArray: int, Flags: int):
        ctx = self._get_thread_ctx()

        _logger.info(
            f"cuTexRefSetArray on device {ctx.dev}: 0x{hTexRef:x} with hArray: 0x{hArray:x} and Flags {Flags}"
        )

        assert hArray in self.array_handles, "No handle for hArray found during cuTexRefSetArray"
        assert hTexRef in self.tex_ref_handles, f"Texture reference 0x{hTexRef:x} is not registered"

        self.tex_ref_handles[hTexRef].set_array(hArray, Flags, self.array_handles[hArray])

        if "cuTexRefSetArray" in self.api_instr.instr_fns:
            self.api_instr.cuTexRefSetArray(hTexRef, hArray, Flags)

    @check_retval
    def cuTexRefSetAddress(
        self, ByteOffset: int, hTexRef: int, dptr: int, bytes: int):
        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]

        _logger.info(
            f"cuTexRefSetAddress on device {ctx.dev}: 0x{hTexRef:x} - {bytes} bytes to 0x{dptr:x} with offset {ByteOffset}"
        )

        if dptr != 0:
            # cuTexRefSetAddress is passed with dptr of 0 if the address is being bound to
            # an array.
            assert gpu.has_dptr(dptr+ByteOffset, bytes)

        assert hTexRef in self.tex_ref_handles, f"Texture reference 0x{hTexRef:x} is not registered"

        self.tex_ref_handles[hTexRef].set_address(ByteOffset, dptr, bytes)

        if "cuTexRefSetAddress" in self.api_instr.instr_fns:
            self.api_instr.cuTexRefSetAddress(ByteOffset, hTexRef, dptr, bytes)

    # Arrays

    @check_retval
    def cuArray3DCreate(self, pHandle: int, pAllocateArray: int, Width, Height, Depth, Format, NumChannels, Flags):
        ctx = self._get_thread_ctx()
        _logger.info(
            f"cuArray3DCreate on device {ctx.dev}: pHandle: 0x{pHandle:x} from pAllocateArray 0x{pAllocateArray:x}"
        )

        array_handler = self._factory.array(
            ctx.dev,
            pHandle,
            self._unpackStructField(Width),
            self._unpackStructField(Height),
            self._unpackStructField(Depth),
            self._unpackStructField(Format),
            self._unpackStructField(NumChannels),
            self._unpackStructField(Flags),
        )

        self.array_handles.register(pHandle, array_handler)

        if "cuArray3DCreate" in self.api_instr.instr_fns:
            self.api_instr.cuArray3DCreate(pHandle, pAllocateArray, Width, Height, Depth, Format, NumChannels, Flags)

    # Memset
    @check_retval
    def cuMemsetD8(self, dstDevice: int, uc: int, N: int):
        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]
        assert gpu.has_dptr(dstDevice, N)
        gpu.set_memory(dstDevice, struct.pack('B', uc) * N)
        _logger.info(f"cuMemsetD8 on device {ctx.dev}: {N} elements to 0x{dstDevice:x}")
        if "cuMemsetD8" in self.api_instr.instr_fns:
            self.api_instr.cuMemsetD8(dstDevice, uc, N)

    @check_retval
    def cuMemsetD16(self, dstDevice: int, us: int, N: int):
        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]

        _logger.info(
            f"cuMemsetD16 on device: {ctx.dev}: {N} elements to 0x{dstDevice:x}"
        )

        assert gpu.has_dptr(dstDevice, N*2)

        gpu.set_memory(dstDevice, struct.pack('H', us) * N)

        if "cuMemsetD16" in self.api_instr.instr_fns:
            self.api_instr.cuMemsetD16(dstDevice, us, N)

    @check_retval
    def cuMemsetD32(self, dstDevice: int, ui: int, N: int):
        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]
        
        _logger.info(
            f"cuMemsetD32 on device: {ctx.dev}: {N} elements to 0x{dstDevice:x}"
        )
        assert gpu.has_dptr(dstDevice, N*4)
        gpu.set_memory(dstDevice, struct.pack('I', ui)*N)
        if "cuMemsetD32" in self.api_instr.instr_fns:
            self.api_instr.cuMemsetD32(dstDevice, ui, N)

    @check_retval
    def cuMemsetD2D8(
        self, dstDevice: int, dstPitch: int, uc: int, Width: int, Height: int
    ):
        ctx = self._get_thread_ctx()
        _logger.info(
            f"cuMemsetD2D8 on device: {ctx.dev}: {Height} rows of {Width} elements with pitch {dstPitch} to 0x{dstDevice:x}"
        )
        # TODO: Issue gpu.set_memory() for these api calls.  
        _logger.warn("cuMemsetD2D8 memory is not tracked in libcuda-replay")
        if "cuMemsetD2D8" in self.api_instr.instr_fns:
            self.api_instr.cuMemsetD2D8(dstDevice, dstPitch, uc, Width, Height)

    @check_retval
    def cuMemsetD2D16(self, dstDevice: int, dstPitch: int, us, Width: int, Height: int):
        ctx = self._get_thread_ctx()
        _logger.info(
            f"cuMemsetD2D16 on device: {ctx.dev}: {Height} rows of {Width} elements with pitch {dstPitch} to 0x{dstDevice:x}"
        )

        # TODO: Issue gpu.set_memory() for these api calls.  
        _logger.warn("cuMemsetD2D16 memory is not tracked in libcuda-replay")

        if "cuMemsetD2D16" in self.api_instr.instr_fns:
            self.api_instr.cuMemsetD2D16(dstDevice, dstPitch, us, Width, Height)

    @check_retval
    def cuMemsetD2D32(
        self, dstDevice: int, dstPitch: int, ui: int, Width: int, Height: int
    ):
        ctx = self._get_thread_ctx()
        _logger.info(
            f"cuMemsetD2D32 on device: {ctx.dev}: {Height} rows of {Width} elements with pitch {dstPitch} to 0x{dstDevice:x}"
        )
        # TODO: Issue gpu.set_memory() for these api calls.  
        _logger.warn("cuMemsetD2D32 memory is not tracked in libcuda-replay")
        if "cuMemsetD2D32" in self.api_instr.instr_fns:
            self.api_instr.cuMemsetD2D32(dstDevice, dstPitch, ui, Width, Height)
