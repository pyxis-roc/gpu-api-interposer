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

void cuGetErrorString_post(CUresult error, const char **pStr, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuGetErrorString_post, error, pStr, _retval);
}

void cuDriverGetVersion_post(int *driverVersion, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuDriverGetVersion_post, driverVersion, _retval);
}

void cuCtxGetCurrent_post(CUcontext *pctx, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuCtxGetCurrent_post, pctx, _retval);
}

void cuCtxGetDevice_post(CUdevice *device, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuCtxGetDevice_post, device, _retval);
}

void cuMemAlloc_v2_post(CUdeviceptr *dptr, size_t bytesize, CUresult *_retval, void *_ctx)
{
  tracepoint(libcuda_interposer, cuMemAlloc_v2_post, dptr, bytesize, _retval);
}

