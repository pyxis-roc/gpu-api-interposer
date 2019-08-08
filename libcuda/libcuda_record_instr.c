#include <cuda.h>
#include "libcuda_record_pre_instr.h"
#include "libcuda_record_post_instr.h"
#include "libcuda_record-tracepoints.h"

int cuDriverGetVersion_pre(int *driverVersion, CUresult *_retval, void *_ctx) {
  tracepoint(libcuda_interposer, cuDriverGetVersion_pre, driverVersion);
}

int cuDriverGetVersion_post(int *driverVersion, CUresult *_retval, void *_ctx) {
  tracepoint(libcuda_interposer, cuDriverGetVersion_post, driverVersion, _retval);
}


int cuMemAlloc_v2_pre(CUdeviceptr *dptr, size_t bytesize, CUresult *_retval, void *_ctx) {
  tracepoint(libcuda_interposer, cuMemAlloc_v2_pre, dptr, bytesize);
}

void cuGetErrorString_post(CUresult error, const char **pStr, CUresult *_retval, void *_ctx) {
  tracepoint(libcuda_interposer, cuGetErrorString_post, error, pStr, _retval);
}
void cuMemAlloc_v2_post(CUdeviceptr *dptr, size_t bytesize, CUresult *_retval, void *_ctx) {
  tracepoint(libcuda_interposer, cuMemAlloc_v2_post, dptr, bytesize, _retval);
}

