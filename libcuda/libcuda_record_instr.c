#include "libcuda_record_pre_instr.h"
#include "libcuda_record_post_instr.h"
#include "libcuda_record_tp.h"
int cuDriverGetVersion_pre(int *driverVersion, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuDriverGetVersion_pre, driverVersion);
  return 0;
}

int cuMemAlloc_v2_pre(CUdeviceptr *dptr, size_t bytesize, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuMemAlloc_v2_pre, dptr, bytesize);
  return 0;
}

int cuMemcpyHtoD_v2_pre(CUdeviceptr dstDevice, const void *srcHost, size_t ByteCount, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuMemcpyHtoD_v2_pre, dstDevice, srcHost, ByteCount);
  return 0;
}

void cuGetErrorString_post(CUresult error, const char **pStr, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuGetErrorString_post, error, pStr, _retval);
}

void cuDriverGetVersion_post(int *driverVersion, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuDriverGetVersion_post, driverVersion, _retval);
}

void cuDeviceGet_post(CUdevice *device, int ordinal, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuDeviceGet_post, device, ordinal, _retval);
}

void cuDeviceGetCount_post(int *count, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuDeviceGetCount_post, count, _retval);
}

void cuDeviceGetName_post(char *name, int len, CUdevice dev, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuDeviceGetName_post, name, len, dev, _retval);
}

void cuDeviceGetUuid_post(CUuuid *uuid, CUdevice dev, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuDeviceGetUuid_post, uuid, dev, _retval);
}

void cuDeviceTotalMem_v2_post(size_t *bytes, CUdevice dev, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuDeviceTotalMem_v2_post, bytes, dev, _retval);
}

void cuDeviceGetAttribute_post(int *pi, CUdevice_attribute attrib, CUdevice dev, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuDeviceGetAttribute_post, pi, attrib, dev, _retval);
}

void cuCtxSetCurrent_post(CUcontext ctx, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuCtxSetCurrent_post, ctx, _retval);
}

void cuCtxGetCurrent_post(CUcontext *pctx, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuCtxGetCurrent_post, pctx, _retval);
}

void cuCtxGetDevice_post(CUdevice *device, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuCtxGetDevice_post, device, _retval);
}

void cuCtxSynchronize_post(CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuCtxSynchronize_post, _retval);
}

void cuModuleUnload_post(CUmodule hmod, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuModuleUnload_post, hmod, _retval);
}

void cuModuleGetFunction_post(CUfunction *hfunc, CUmodule hmod, const char *name, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuModuleGetFunction_post, hfunc, hmod, name, _retval);
}

void cuModuleGetGlobal_v2_post(CUdeviceptr *dptr, size_t *bytes, CUmodule hmod, const char *name, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuModuleGetGlobal_v2_post, dptr, bytes, hmod, name, _retval);
}

void cuMemAlloc_v2_post(CUdeviceptr *dptr, size_t bytesize, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuMemAlloc_v2_post, dptr, bytesize, _retval);
}

void cuMemFree_v2_post(CUdeviceptr dptr, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuMemFree_v2_post, dptr, _retval);
}

void cuMemHostAlloc_post(void **pp, size_t bytesize, unsigned int Flags, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuMemHostAlloc_post, pp, bytesize, Flags, _retval);
}

void cuMemcpyDtoH_v2_post(void *dstHost, CUdeviceptr srcDevice, size_t ByteCount, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuMemcpyDtoH_v2_post, dstHost, srcDevice, ByteCount, _retval);
}

void cuStreamCreate_post(CUstream *phStream, unsigned int Flags, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuStreamCreate_post, phStream, Flags, _retval);
}

void cuEventCreate_post(CUevent *phEvent, unsigned int Flags, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuEventCreate_post, phEvent, Flags, _retval);
}

void cuFuncGetAttribute_post(int *pi, CUfunction_attribute attrib, CUfunction hfunc, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuFuncGetAttribute_post, pi, attrib, hfunc, _retval);
}

void cuLaunchKernel_post(CUfunction f, unsigned int gridDimX, unsigned int gridDimY, unsigned int gridDimZ, unsigned int blockDimX, unsigned int blockDimY, unsigned int blockDimZ, unsigned int sharedMemBytes, CUstream hStream, void **kernelParams, void **extra, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuLaunchKernel_post, f, gridDimX, gridDimY, gridDimZ, blockDimX, blockDimY, blockDimZ, sharedMemBytes, hStream, _retval);
}

void cuTexObjectCreate_post(CUtexObject *pTexObject, const CUDA_RESOURCE_DESC *pResDesc, const CUDA_TEXTURE_DESC *pTexDesc, const CUDA_RESOURCE_VIEW_DESC *pResViewDesc, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuTexObjectCreate_post, pTexObject, pResDesc, pTexDesc, pResViewDesc, _retval);
}

