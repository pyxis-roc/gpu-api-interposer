/* automatically generated */
#include <stddef.h>
#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <cuda.h>

static void * orig_handle;
static FILE * trace_handle;

CUresult cuGetErrorString(CUresult error, const char **pStr)
{
  static CUresult (*cuGetErrorString_orig)(CUresult, const char **) = NULL;
  if (!cuGetErrorString_orig)
  {
    cuGetErrorString_orig = dlsym(orig_handle, "cuGetErrorString");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGetErrorString\n");
  _retval = cuGetErrorString_orig(error, pStr);
  return _retval;
}


CUresult cuGetErrorName(CUresult error, const char **pStr)
{
  static CUresult (*cuGetErrorName_orig)(CUresult, const char **) = NULL;
  if (!cuGetErrorName_orig)
  {
    cuGetErrorName_orig = dlsym(orig_handle, "cuGetErrorName");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGetErrorName\n");
  _retval = cuGetErrorName_orig(error, pStr);
  return _retval;
}


CUresult cuInit(unsigned int Flags)
{
  static CUresult (*cuInit_orig)(unsigned int) = NULL;
  if (!cuInit_orig)
  {
    cuInit_orig = dlsym(orig_handle, "cuInit");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuInit\n");
  _retval = cuInit_orig(Flags);
  return _retval;
}


CUresult cuDriverGetVersion(int *driverVersion)
{
  static CUresult (*cuDriverGetVersion_orig)(int *) = NULL;
  if (!cuDriverGetVersion_orig)
  {
    cuDriverGetVersion_orig = dlsym(orig_handle, "cuDriverGetVersion");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDriverGetVersion\n");
  _retval = cuDriverGetVersion_orig(driverVersion);
  return _retval;
}


CUresult cuDeviceGet(CUdevice *device, int ordinal)
{
  static CUresult (*cuDeviceGet_orig)(CUdevice *, int) = NULL;
  if (!cuDeviceGet_orig)
  {
    cuDeviceGet_orig = dlsym(orig_handle, "cuDeviceGet");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDeviceGet\n");
  _retval = cuDeviceGet_orig(device, ordinal);
  return _retval;
}


CUresult cuDeviceGetCount(int *count)
{
  static CUresult (*cuDeviceGetCount_orig)(int *) = NULL;
  if (!cuDeviceGetCount_orig)
  {
    cuDeviceGetCount_orig = dlsym(orig_handle, "cuDeviceGetCount");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDeviceGetCount\n");
  _retval = cuDeviceGetCount_orig(count);
  return _retval;
}


CUresult cuDeviceGetName(char *name, int len, CUdevice dev)
{
  static CUresult (*cuDeviceGetName_orig)(char *, int, CUdevice) = NULL;
  if (!cuDeviceGetName_orig)
  {
    cuDeviceGetName_orig = dlsym(orig_handle, "cuDeviceGetName");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDeviceGetName\n");
  _retval = cuDeviceGetName_orig(name, len, dev);
  return _retval;
}


CUresult cuDeviceGetUuid(CUuuid *uuid, CUdevice dev)
{
  static CUresult (*cuDeviceGetUuid_orig)(CUuuid *, CUdevice) = NULL;
  if (!cuDeviceGetUuid_orig)
  {
    cuDeviceGetUuid_orig = dlsym(orig_handle, "cuDeviceGetUuid");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDeviceGetUuid\n");
  _retval = cuDeviceGetUuid_orig(uuid, dev);
  return _retval;
}


CUresult cuDeviceTotalMem_v2(size_t *bytes, CUdevice dev)
{
  static CUresult (*cuDeviceTotalMem_v2_orig)(size_t *, CUdevice) = NULL;
  if (!cuDeviceTotalMem_v2_orig)
  {
    cuDeviceTotalMem_v2_orig = dlsym(orig_handle, "cuDeviceTotalMem_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDeviceTotalMem_v2\n");
  _retval = cuDeviceTotalMem_v2_orig(bytes, dev);
  return _retval;
}


CUresult cuDeviceGetAttribute(int *pi, CUdevice_attribute attrib, CUdevice dev)
{
  static CUresult (*cuDeviceGetAttribute_orig)(int *, CUdevice_attribute, CUdevice) = NULL;
  if (!cuDeviceGetAttribute_orig)
  {
    cuDeviceGetAttribute_orig = dlsym(orig_handle, "cuDeviceGetAttribute");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDeviceGetAttribute\n");
  _retval = cuDeviceGetAttribute_orig(pi, attrib, dev);
  return _retval;
}


CUresult cuDeviceGetProperties(CUdevprop *prop, CUdevice dev)
{
  static CUresult (*cuDeviceGetProperties_orig)(CUdevprop *, CUdevice) = NULL;
  if (!cuDeviceGetProperties_orig)
  {
    cuDeviceGetProperties_orig = dlsym(orig_handle, "cuDeviceGetProperties");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDeviceGetProperties\n");
  _retval = cuDeviceGetProperties_orig(prop, dev);
  return _retval;
}


CUresult cuDeviceComputeCapability(int *major, int *minor, CUdevice dev)
{
  static CUresult (*cuDeviceComputeCapability_orig)(int *, int *, CUdevice) = NULL;
  if (!cuDeviceComputeCapability_orig)
  {
    cuDeviceComputeCapability_orig = dlsym(orig_handle, "cuDeviceComputeCapability");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDeviceComputeCapability\n");
  _retval = cuDeviceComputeCapability_orig(major, minor, dev);
  return _retval;
}


CUresult cuDevicePrimaryCtxRetain(CUcontext *pctx, CUdevice dev)
{
  static CUresult (*cuDevicePrimaryCtxRetain_orig)(CUcontext *, CUdevice) = NULL;
  if (!cuDevicePrimaryCtxRetain_orig)
  {
    cuDevicePrimaryCtxRetain_orig = dlsym(orig_handle, "cuDevicePrimaryCtxRetain");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDevicePrimaryCtxRetain\n");
  _retval = cuDevicePrimaryCtxRetain_orig(pctx, dev);
  return _retval;
}


CUresult cuDevicePrimaryCtxRelease(CUdevice dev)
{
  static CUresult (*cuDevicePrimaryCtxRelease_orig)(CUdevice) = NULL;
  if (!cuDevicePrimaryCtxRelease_orig)
  {
    cuDevicePrimaryCtxRelease_orig = dlsym(orig_handle, "cuDevicePrimaryCtxRelease");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDevicePrimaryCtxRelease\n");
  _retval = cuDevicePrimaryCtxRelease_orig(dev);
  return _retval;
}


CUresult cuDevicePrimaryCtxSetFlags(CUdevice dev, unsigned int flags)
{
  static CUresult (*cuDevicePrimaryCtxSetFlags_orig)(CUdevice, unsigned int) = NULL;
  if (!cuDevicePrimaryCtxSetFlags_orig)
  {
    cuDevicePrimaryCtxSetFlags_orig = dlsym(orig_handle, "cuDevicePrimaryCtxSetFlags");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDevicePrimaryCtxSetFlags\n");
  _retval = cuDevicePrimaryCtxSetFlags_orig(dev, flags);
  return _retval;
}


CUresult cuDevicePrimaryCtxGetState(CUdevice dev, unsigned int *flags, int *active)
{
  static CUresult (*cuDevicePrimaryCtxGetState_orig)(CUdevice, unsigned int *, int *) = NULL;
  if (!cuDevicePrimaryCtxGetState_orig)
  {
    cuDevicePrimaryCtxGetState_orig = dlsym(orig_handle, "cuDevicePrimaryCtxGetState");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDevicePrimaryCtxGetState\n");
  _retval = cuDevicePrimaryCtxGetState_orig(dev, flags, active);
  return _retval;
}


CUresult cuDevicePrimaryCtxReset(CUdevice dev)
{
  static CUresult (*cuDevicePrimaryCtxReset_orig)(CUdevice) = NULL;
  if (!cuDevicePrimaryCtxReset_orig)
  {
    cuDevicePrimaryCtxReset_orig = dlsym(orig_handle, "cuDevicePrimaryCtxReset");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDevicePrimaryCtxReset\n");
  _retval = cuDevicePrimaryCtxReset_orig(dev);
  return _retval;
}


CUresult cuCtxCreate_v2(CUcontext *pctx, unsigned int flags, CUdevice dev)
{
  static CUresult (*cuCtxCreate_v2_orig)(CUcontext *, unsigned int, CUdevice) = NULL;
  if (!cuCtxCreate_v2_orig)
  {
    cuCtxCreate_v2_orig = dlsym(orig_handle, "cuCtxCreate_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxCreate_v2\n");
  _retval = cuCtxCreate_v2_orig(pctx, flags, dev);
  return _retval;
}


CUresult cuCtxDestroy_v2(CUcontext ctx)
{
  static CUresult (*cuCtxDestroy_v2_orig)(CUcontext) = NULL;
  if (!cuCtxDestroy_v2_orig)
  {
    cuCtxDestroy_v2_orig = dlsym(orig_handle, "cuCtxDestroy_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxDestroy_v2\n");
  _retval = cuCtxDestroy_v2_orig(ctx);
  return _retval;
}


CUresult cuCtxPushCurrent_v2(CUcontext ctx)
{
  static CUresult (*cuCtxPushCurrent_v2_orig)(CUcontext) = NULL;
  if (!cuCtxPushCurrent_v2_orig)
  {
    cuCtxPushCurrent_v2_orig = dlsym(orig_handle, "cuCtxPushCurrent_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxPushCurrent_v2\n");
  _retval = cuCtxPushCurrent_v2_orig(ctx);
  return _retval;
}


CUresult cuCtxPopCurrent_v2(CUcontext *pctx)
{
  static CUresult (*cuCtxPopCurrent_v2_orig)(CUcontext *) = NULL;
  if (!cuCtxPopCurrent_v2_orig)
  {
    cuCtxPopCurrent_v2_orig = dlsym(orig_handle, "cuCtxPopCurrent_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxPopCurrent_v2\n");
  _retval = cuCtxPopCurrent_v2_orig(pctx);
  return _retval;
}


CUresult cuCtxSetCurrent(CUcontext ctx)
{
  static CUresult (*cuCtxSetCurrent_orig)(CUcontext) = NULL;
  if (!cuCtxSetCurrent_orig)
  {
    cuCtxSetCurrent_orig = dlsym(orig_handle, "cuCtxSetCurrent");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxSetCurrent\n");
  _retval = cuCtxSetCurrent_orig(ctx);
  return _retval;
}


CUresult cuCtxGetCurrent(CUcontext *pctx)
{
  static CUresult (*cuCtxGetCurrent_orig)(CUcontext *) = NULL;
  if (!cuCtxGetCurrent_orig)
  {
    cuCtxGetCurrent_orig = dlsym(orig_handle, "cuCtxGetCurrent");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxGetCurrent\n");
  _retval = cuCtxGetCurrent_orig(pctx);
  return _retval;
}


CUresult cuCtxGetDevice(CUdevice *device)
{
  static CUresult (*cuCtxGetDevice_orig)(CUdevice *) = NULL;
  if (!cuCtxGetDevice_orig)
  {
    cuCtxGetDevice_orig = dlsym(orig_handle, "cuCtxGetDevice");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxGetDevice\n");
  _retval = cuCtxGetDevice_orig(device);
  return _retval;
}


CUresult cuCtxGetFlags(unsigned int *flags)
{
  static CUresult (*cuCtxGetFlags_orig)(unsigned int *) = NULL;
  if (!cuCtxGetFlags_orig)
  {
    cuCtxGetFlags_orig = dlsym(orig_handle, "cuCtxGetFlags");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxGetFlags\n");
  _retval = cuCtxGetFlags_orig(flags);
  return _retval;
}


CUresult cuCtxSynchronize(void)
{
  static CUresult (*cuCtxSynchronize_orig)(void) = NULL;
  if (!cuCtxSynchronize_orig)
  {
    cuCtxSynchronize_orig = dlsym(orig_handle, "cuCtxSynchronize");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxSynchronize\n");
  _retval = cuCtxSynchronize_orig();
  return _retval;
}


CUresult cuCtxSetLimit(CUlimit limit, size_t value)
{
  static CUresult (*cuCtxSetLimit_orig)(CUlimit, size_t) = NULL;
  if (!cuCtxSetLimit_orig)
  {
    cuCtxSetLimit_orig = dlsym(orig_handle, "cuCtxSetLimit");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxSetLimit\n");
  _retval = cuCtxSetLimit_orig(limit, value);
  return _retval;
}


CUresult cuCtxGetLimit(size_t *pvalue, CUlimit limit)
{
  static CUresult (*cuCtxGetLimit_orig)(size_t *, CUlimit) = NULL;
  if (!cuCtxGetLimit_orig)
  {
    cuCtxGetLimit_orig = dlsym(orig_handle, "cuCtxGetLimit");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxGetLimit\n");
  _retval = cuCtxGetLimit_orig(pvalue, limit);
  return _retval;
}


CUresult cuCtxGetCacheConfig(CUfunc_cache *pconfig)
{
  static CUresult (*cuCtxGetCacheConfig_orig)(CUfunc_cache *) = NULL;
  if (!cuCtxGetCacheConfig_orig)
  {
    cuCtxGetCacheConfig_orig = dlsym(orig_handle, "cuCtxGetCacheConfig");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxGetCacheConfig\n");
  _retval = cuCtxGetCacheConfig_orig(pconfig);
  return _retval;
}


CUresult cuCtxSetCacheConfig(CUfunc_cache config)
{
  static CUresult (*cuCtxSetCacheConfig_orig)(CUfunc_cache) = NULL;
  if (!cuCtxSetCacheConfig_orig)
  {
    cuCtxSetCacheConfig_orig = dlsym(orig_handle, "cuCtxSetCacheConfig");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxSetCacheConfig\n");
  _retval = cuCtxSetCacheConfig_orig(config);
  return _retval;
}


CUresult cuCtxGetSharedMemConfig(CUsharedconfig *pConfig)
{
  static CUresult (*cuCtxGetSharedMemConfig_orig)(CUsharedconfig *) = NULL;
  if (!cuCtxGetSharedMemConfig_orig)
  {
    cuCtxGetSharedMemConfig_orig = dlsym(orig_handle, "cuCtxGetSharedMemConfig");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxGetSharedMemConfig\n");
  _retval = cuCtxGetSharedMemConfig_orig(pConfig);
  return _retval;
}


CUresult cuCtxSetSharedMemConfig(CUsharedconfig config)
{
  static CUresult (*cuCtxSetSharedMemConfig_orig)(CUsharedconfig) = NULL;
  if (!cuCtxSetSharedMemConfig_orig)
  {
    cuCtxSetSharedMemConfig_orig = dlsym(orig_handle, "cuCtxSetSharedMemConfig");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxSetSharedMemConfig\n");
  _retval = cuCtxSetSharedMemConfig_orig(config);
  return _retval;
}


CUresult cuCtxGetApiVersion(CUcontext ctx, unsigned int *version)
{
  static CUresult (*cuCtxGetApiVersion_orig)(CUcontext, unsigned int *) = NULL;
  if (!cuCtxGetApiVersion_orig)
  {
    cuCtxGetApiVersion_orig = dlsym(orig_handle, "cuCtxGetApiVersion");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxGetApiVersion\n");
  _retval = cuCtxGetApiVersion_orig(ctx, version);
  return _retval;
}


CUresult cuCtxGetStreamPriorityRange(int *leastPriority, int *greatestPriority)
{
  static CUresult (*cuCtxGetStreamPriorityRange_orig)(int *, int *) = NULL;
  if (!cuCtxGetStreamPriorityRange_orig)
  {
    cuCtxGetStreamPriorityRange_orig = dlsym(orig_handle, "cuCtxGetStreamPriorityRange");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxGetStreamPriorityRange\n");
  _retval = cuCtxGetStreamPriorityRange_orig(leastPriority, greatestPriority);
  return _retval;
}


CUresult cuCtxAttach(CUcontext *pctx, unsigned int flags)
{
  static CUresult (*cuCtxAttach_orig)(CUcontext *, unsigned int) = NULL;
  if (!cuCtxAttach_orig)
  {
    cuCtxAttach_orig = dlsym(orig_handle, "cuCtxAttach");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxAttach\n");
  _retval = cuCtxAttach_orig(pctx, flags);
  return _retval;
}


CUresult cuCtxDetach(CUcontext ctx)
{
  static CUresult (*cuCtxDetach_orig)(CUcontext) = NULL;
  if (!cuCtxDetach_orig)
  {
    cuCtxDetach_orig = dlsym(orig_handle, "cuCtxDetach");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxDetach\n");
  _retval = cuCtxDetach_orig(ctx);
  return _retval;
}


CUresult cuModuleLoad(CUmodule *module, const char *fname)
{
  static CUresult (*cuModuleLoad_orig)(CUmodule *, const char *) = NULL;
  if (!cuModuleLoad_orig)
  {
    cuModuleLoad_orig = dlsym(orig_handle, "cuModuleLoad");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuModuleLoad\n");
  _retval = cuModuleLoad_orig(module, fname);
  return _retval;
}


CUresult cuModuleLoadData(CUmodule *module, const void *image)
{
  static CUresult (*cuModuleLoadData_orig)(CUmodule *, const void *) = NULL;
  if (!cuModuleLoadData_orig)
  {
    cuModuleLoadData_orig = dlsym(orig_handle, "cuModuleLoadData");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuModuleLoadData\n");
  _retval = cuModuleLoadData_orig(module, image);
  return _retval;
}


CUresult cuModuleLoadDataEx(CUmodule *module, const void *image, unsigned int numOptions, CUjit_option *options, void **optionValues)
{
  static CUresult (*cuModuleLoadDataEx_orig)(CUmodule *, const void *, unsigned int, CUjit_option *, void **) = NULL;
  if (!cuModuleLoadDataEx_orig)
  {
    cuModuleLoadDataEx_orig = dlsym(orig_handle, "cuModuleLoadDataEx");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuModuleLoadDataEx\n");
  _retval = cuModuleLoadDataEx_orig(module, image, numOptions, options, optionValues);
  return _retval;
}


CUresult cuModuleLoadFatBinary(CUmodule *module, const void *fatCubin)
{
  static CUresult (*cuModuleLoadFatBinary_orig)(CUmodule *, const void *) = NULL;
  if (!cuModuleLoadFatBinary_orig)
  {
    cuModuleLoadFatBinary_orig = dlsym(orig_handle, "cuModuleLoadFatBinary");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuModuleLoadFatBinary\n");
  _retval = cuModuleLoadFatBinary_orig(module, fatCubin);
  return _retval;
}


CUresult cuModuleUnload(CUmodule hmod)
{
  static CUresult (*cuModuleUnload_orig)(CUmodule) = NULL;
  if (!cuModuleUnload_orig)
  {
    cuModuleUnload_orig = dlsym(orig_handle, "cuModuleUnload");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuModuleUnload\n");
  _retval = cuModuleUnload_orig(hmod);
  return _retval;
}


CUresult cuModuleGetFunction(CUfunction *hfunc, CUmodule hmod, const char *name)
{
  static CUresult (*cuModuleGetFunction_orig)(CUfunction *, CUmodule, const char *) = NULL;
  if (!cuModuleGetFunction_orig)
  {
    cuModuleGetFunction_orig = dlsym(orig_handle, "cuModuleGetFunction");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuModuleGetFunction\n");
  _retval = cuModuleGetFunction_orig(hfunc, hmod, name);
  return _retval;
}


CUresult cuModuleGetGlobal_v2(CUdeviceptr *dptr, size_t *bytes, CUmodule hmod, const char *name)
{
  static CUresult (*cuModuleGetGlobal_v2_orig)(CUdeviceptr *, size_t *, CUmodule, const char *) = NULL;
  if (!cuModuleGetGlobal_v2_orig)
  {
    cuModuleGetGlobal_v2_orig = dlsym(orig_handle, "cuModuleGetGlobal_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuModuleGetGlobal_v2\n");
  _retval = cuModuleGetGlobal_v2_orig(dptr, bytes, hmod, name);
  return _retval;
}


CUresult cuModuleGetTexRef(CUtexref *pTexRef, CUmodule hmod, const char *name)
{
  static CUresult (*cuModuleGetTexRef_orig)(CUtexref *, CUmodule, const char *) = NULL;
  if (!cuModuleGetTexRef_orig)
  {
    cuModuleGetTexRef_orig = dlsym(orig_handle, "cuModuleGetTexRef");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuModuleGetTexRef\n");
  _retval = cuModuleGetTexRef_orig(pTexRef, hmod, name);
  return _retval;
}


CUresult cuModuleGetSurfRef(CUsurfref *pSurfRef, CUmodule hmod, const char *name)
{
  static CUresult (*cuModuleGetSurfRef_orig)(CUsurfref *, CUmodule, const char *) = NULL;
  if (!cuModuleGetSurfRef_orig)
  {
    cuModuleGetSurfRef_orig = dlsym(orig_handle, "cuModuleGetSurfRef");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuModuleGetSurfRef\n");
  _retval = cuModuleGetSurfRef_orig(pSurfRef, hmod, name);
  return _retval;
}


CUresult cuLinkCreate_v2(unsigned int numOptions, CUjit_option *options, void **optionValues, CUlinkState *stateOut)
{
  static CUresult (*cuLinkCreate_v2_orig)(unsigned int, CUjit_option *, void **, CUlinkState *) = NULL;
  if (!cuLinkCreate_v2_orig)
  {
    cuLinkCreate_v2_orig = dlsym(orig_handle, "cuLinkCreate_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuLinkCreate_v2\n");
  _retval = cuLinkCreate_v2_orig(numOptions, options, optionValues, stateOut);
  return _retval;
}


CUresult cuLinkAddData_v2(CUlinkState state, CUjitInputType type, void *data, size_t size, const char *name, unsigned int numOptions, CUjit_option *options, void **optionValues)
{
  static CUresult (*cuLinkAddData_v2_orig)(CUlinkState, CUjitInputType, void *, size_t, const char *, unsigned int, CUjit_option *, void **) = NULL;
  if (!cuLinkAddData_v2_orig)
  {
    cuLinkAddData_v2_orig = dlsym(orig_handle, "cuLinkAddData_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuLinkAddData_v2\n");
  _retval = cuLinkAddData_v2_orig(state, type, data, size, name, numOptions, options, optionValues);
  return _retval;
}


CUresult cuLinkAddFile_v2(CUlinkState state, CUjitInputType type, const char *path, unsigned int numOptions, CUjit_option *options, void **optionValues)
{
  static CUresult (*cuLinkAddFile_v2_orig)(CUlinkState, CUjitInputType, const char *, unsigned int, CUjit_option *, void **) = NULL;
  if (!cuLinkAddFile_v2_orig)
  {
    cuLinkAddFile_v2_orig = dlsym(orig_handle, "cuLinkAddFile_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuLinkAddFile_v2\n");
  _retval = cuLinkAddFile_v2_orig(state, type, path, numOptions, options, optionValues);
  return _retval;
}


CUresult cuLinkComplete(CUlinkState state, void **cubinOut, size_t *sizeOut)
{
  static CUresult (*cuLinkComplete_orig)(CUlinkState, void **, size_t *) = NULL;
  if (!cuLinkComplete_orig)
  {
    cuLinkComplete_orig = dlsym(orig_handle, "cuLinkComplete");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuLinkComplete\n");
  _retval = cuLinkComplete_orig(state, cubinOut, sizeOut);
  return _retval;
}


CUresult cuLinkDestroy(CUlinkState state)
{
  static CUresult (*cuLinkDestroy_orig)(CUlinkState) = NULL;
  if (!cuLinkDestroy_orig)
  {
    cuLinkDestroy_orig = dlsym(orig_handle, "cuLinkDestroy");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuLinkDestroy\n");
  _retval = cuLinkDestroy_orig(state);
  return _retval;
}


CUresult cuMemGetInfo_v2(size_t *free, size_t *total)
{
  static CUresult (*cuMemGetInfo_v2_orig)(size_t *, size_t *) = NULL;
  if (!cuMemGetInfo_v2_orig)
  {
    cuMemGetInfo_v2_orig = dlsym(orig_handle, "cuMemGetInfo_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemGetInfo_v2\n");
  _retval = cuMemGetInfo_v2_orig(free, total);
  return _retval;
}


CUresult cuMemAlloc_v2(CUdeviceptr *dptr, size_t bytesize)
{
  static CUresult (*cuMemAlloc_v2_orig)(CUdeviceptr *, size_t) = NULL;
  if (!cuMemAlloc_v2_orig)
  {
    cuMemAlloc_v2_orig = dlsym(orig_handle, "cuMemAlloc_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemAlloc_v2\n");
  _retval = cuMemAlloc_v2_orig(dptr, bytesize);
  return _retval;
}


CUresult cuMemAllocPitch_v2(CUdeviceptr *dptr, size_t *pPitch, size_t WidthInBytes, size_t Height, unsigned int ElementSizeBytes)
{
  static CUresult (*cuMemAllocPitch_v2_orig)(CUdeviceptr *, size_t *, size_t, size_t, unsigned int) = NULL;
  if (!cuMemAllocPitch_v2_orig)
  {
    cuMemAllocPitch_v2_orig = dlsym(orig_handle, "cuMemAllocPitch_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemAllocPitch_v2\n");
  _retval = cuMemAllocPitch_v2_orig(dptr, pPitch, WidthInBytes, Height, ElementSizeBytes);
  return _retval;
}


CUresult cuMemFree_v2(CUdeviceptr dptr)
{
  static CUresult (*cuMemFree_v2_orig)(CUdeviceptr) = NULL;
  if (!cuMemFree_v2_orig)
  {
    cuMemFree_v2_orig = dlsym(orig_handle, "cuMemFree_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemFree_v2\n");
  _retval = cuMemFree_v2_orig(dptr);
  return _retval;
}


CUresult cuMemGetAddressRange_v2(CUdeviceptr *pbase, size_t *psize, CUdeviceptr dptr)
{
  static CUresult (*cuMemGetAddressRange_v2_orig)(CUdeviceptr *, size_t *, CUdeviceptr) = NULL;
  if (!cuMemGetAddressRange_v2_orig)
  {
    cuMemGetAddressRange_v2_orig = dlsym(orig_handle, "cuMemGetAddressRange_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemGetAddressRange_v2\n");
  _retval = cuMemGetAddressRange_v2_orig(pbase, psize, dptr);
  return _retval;
}


CUresult cuMemAllocHost_v2(void **pp, size_t bytesize)
{
  static CUresult (*cuMemAllocHost_v2_orig)(void **, size_t) = NULL;
  if (!cuMemAllocHost_v2_orig)
  {
    cuMemAllocHost_v2_orig = dlsym(orig_handle, "cuMemAllocHost_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemAllocHost_v2\n");
  _retval = cuMemAllocHost_v2_orig(pp, bytesize);
  return _retval;
}


CUresult cuMemFreeHost(void *p)
{
  static CUresult (*cuMemFreeHost_orig)(void *) = NULL;
  if (!cuMemFreeHost_orig)
  {
    cuMemFreeHost_orig = dlsym(orig_handle, "cuMemFreeHost");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemFreeHost\n");
  _retval = cuMemFreeHost_orig(p);
  return _retval;
}


CUresult cuMemHostAlloc(void **pp, size_t bytesize, unsigned int Flags)
{
  static CUresult (*cuMemHostAlloc_orig)(void **, size_t, unsigned int) = NULL;
  if (!cuMemHostAlloc_orig)
  {
    cuMemHostAlloc_orig = dlsym(orig_handle, "cuMemHostAlloc");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemHostAlloc\n");
  _retval = cuMemHostAlloc_orig(pp, bytesize, Flags);
  return _retval;
}


CUresult cuMemHostGetDevicePointer_v2(CUdeviceptr *pdptr, void *p, unsigned int Flags)
{
  static CUresult (*cuMemHostGetDevicePointer_v2_orig)(CUdeviceptr *, void *, unsigned int) = NULL;
  if (!cuMemHostGetDevicePointer_v2_orig)
  {
    cuMemHostGetDevicePointer_v2_orig = dlsym(orig_handle, "cuMemHostGetDevicePointer_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemHostGetDevicePointer_v2\n");
  _retval = cuMemHostGetDevicePointer_v2_orig(pdptr, p, Flags);
  return _retval;
}


CUresult cuMemHostGetFlags(unsigned int *pFlags, void *p)
{
  static CUresult (*cuMemHostGetFlags_orig)(unsigned int *, void *) = NULL;
  if (!cuMemHostGetFlags_orig)
  {
    cuMemHostGetFlags_orig = dlsym(orig_handle, "cuMemHostGetFlags");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemHostGetFlags\n");
  _retval = cuMemHostGetFlags_orig(pFlags, p);
  return _retval;
}


CUresult cuMemAllocManaged(CUdeviceptr *dptr, size_t bytesize, unsigned int flags)
{
  static CUresult (*cuMemAllocManaged_orig)(CUdeviceptr *, size_t, unsigned int) = NULL;
  if (!cuMemAllocManaged_orig)
  {
    cuMemAllocManaged_orig = dlsym(orig_handle, "cuMemAllocManaged");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemAllocManaged\n");
  _retval = cuMemAllocManaged_orig(dptr, bytesize, flags);
  return _retval;
}


CUresult cuDeviceGetByPCIBusId(CUdevice *dev, const char *pciBusId)
{
  static CUresult (*cuDeviceGetByPCIBusId_orig)(CUdevice *, const char *) = NULL;
  if (!cuDeviceGetByPCIBusId_orig)
  {
    cuDeviceGetByPCIBusId_orig = dlsym(orig_handle, "cuDeviceGetByPCIBusId");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDeviceGetByPCIBusId\n");
  _retval = cuDeviceGetByPCIBusId_orig(dev, pciBusId);
  return _retval;
}


CUresult cuDeviceGetPCIBusId(char *pciBusId, int len, CUdevice dev)
{
  static CUresult (*cuDeviceGetPCIBusId_orig)(char *, int, CUdevice) = NULL;
  if (!cuDeviceGetPCIBusId_orig)
  {
    cuDeviceGetPCIBusId_orig = dlsym(orig_handle, "cuDeviceGetPCIBusId");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDeviceGetPCIBusId\n");
  _retval = cuDeviceGetPCIBusId_orig(pciBusId, len, dev);
  return _retval;
}


CUresult cuIpcGetEventHandle(CUipcEventHandle *pHandle, CUevent event)
{
  static CUresult (*cuIpcGetEventHandle_orig)(CUipcEventHandle *, CUevent) = NULL;
  if (!cuIpcGetEventHandle_orig)
  {
    cuIpcGetEventHandle_orig = dlsym(orig_handle, "cuIpcGetEventHandle");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuIpcGetEventHandle\n");
  _retval = cuIpcGetEventHandle_orig(pHandle, event);
  return _retval;
}


CUresult cuIpcOpenEventHandle(CUevent *phEvent, CUipcEventHandle handle)
{
  static CUresult (*cuIpcOpenEventHandle_orig)(CUevent *, CUipcEventHandle) = NULL;
  if (!cuIpcOpenEventHandle_orig)
  {
    cuIpcOpenEventHandle_orig = dlsym(orig_handle, "cuIpcOpenEventHandle");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuIpcOpenEventHandle\n");
  _retval = cuIpcOpenEventHandle_orig(phEvent, handle);
  return _retval;
}


CUresult cuIpcGetMemHandle(CUipcMemHandle *pHandle, CUdeviceptr dptr)
{
  static CUresult (*cuIpcGetMemHandle_orig)(CUipcMemHandle *, CUdeviceptr) = NULL;
  if (!cuIpcGetMemHandle_orig)
  {
    cuIpcGetMemHandle_orig = dlsym(orig_handle, "cuIpcGetMemHandle");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuIpcGetMemHandle\n");
  _retval = cuIpcGetMemHandle_orig(pHandle, dptr);
  return _retval;
}


CUresult cuIpcOpenMemHandle(CUdeviceptr *pdptr, CUipcMemHandle handle, unsigned int Flags)
{
  static CUresult (*cuIpcOpenMemHandle_orig)(CUdeviceptr *, CUipcMemHandle, unsigned int) = NULL;
  if (!cuIpcOpenMemHandle_orig)
  {
    cuIpcOpenMemHandle_orig = dlsym(orig_handle, "cuIpcOpenMemHandle");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuIpcOpenMemHandle\n");
  _retval = cuIpcOpenMemHandle_orig(pdptr, handle, Flags);
  return _retval;
}


CUresult cuIpcCloseMemHandle(CUdeviceptr dptr)
{
  static CUresult (*cuIpcCloseMemHandle_orig)(CUdeviceptr) = NULL;
  if (!cuIpcCloseMemHandle_orig)
  {
    cuIpcCloseMemHandle_orig = dlsym(orig_handle, "cuIpcCloseMemHandle");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuIpcCloseMemHandle\n");
  _retval = cuIpcCloseMemHandle_orig(dptr);
  return _retval;
}


CUresult cuMemHostRegister_v2(void *p, size_t bytesize, unsigned int Flags)
{
  static CUresult (*cuMemHostRegister_v2_orig)(void *, size_t, unsigned int) = NULL;
  if (!cuMemHostRegister_v2_orig)
  {
    cuMemHostRegister_v2_orig = dlsym(orig_handle, "cuMemHostRegister_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemHostRegister_v2\n");
  _retval = cuMemHostRegister_v2_orig(p, bytesize, Flags);
  return _retval;
}


CUresult cuMemHostUnregister(void *p)
{
  static CUresult (*cuMemHostUnregister_orig)(void *) = NULL;
  if (!cuMemHostUnregister_orig)
  {
    cuMemHostUnregister_orig = dlsym(orig_handle, "cuMemHostUnregister");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemHostUnregister\n");
  _retval = cuMemHostUnregister_orig(p);
  return _retval;
}


CUresult cuMemcpy(CUdeviceptr dst, CUdeviceptr src, size_t ByteCount)
{
  static CUresult (*cuMemcpy_orig)(CUdeviceptr, CUdeviceptr, size_t) = NULL;
  if (!cuMemcpy_orig)
  {
    cuMemcpy_orig = dlsym(orig_handle, "cuMemcpy");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpy\n");
  _retval = cuMemcpy_orig(dst, src, ByteCount);
  return _retval;
}


CUresult cuMemcpyPeer(CUdeviceptr dstDevice, CUcontext dstContext, CUdeviceptr srcDevice, CUcontext srcContext, size_t ByteCount)
{
  static CUresult (*cuMemcpyPeer_orig)(CUdeviceptr, CUcontext, CUdeviceptr, CUcontext, size_t) = NULL;
  if (!cuMemcpyPeer_orig)
  {
    cuMemcpyPeer_orig = dlsym(orig_handle, "cuMemcpyPeer");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyPeer\n");
  _retval = cuMemcpyPeer_orig(dstDevice, dstContext, srcDevice, srcContext, ByteCount);
  return _retval;
}


CUresult cuMemcpyHtoD_v2(CUdeviceptr dstDevice, const void *srcHost, size_t ByteCount)
{
  static CUresult (*cuMemcpyHtoD_v2_orig)(CUdeviceptr, const void *, size_t) = NULL;
  if (!cuMemcpyHtoD_v2_orig)
  {
    cuMemcpyHtoD_v2_orig = dlsym(orig_handle, "cuMemcpyHtoD_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyHtoD_v2\n");
  _retval = cuMemcpyHtoD_v2_orig(dstDevice, srcHost, ByteCount);
  return _retval;
}


CUresult cuMemcpyDtoH_v2(void *dstHost, CUdeviceptr srcDevice, size_t ByteCount)
{
  static CUresult (*cuMemcpyDtoH_v2_orig)(void *, CUdeviceptr, size_t) = NULL;
  if (!cuMemcpyDtoH_v2_orig)
  {
    cuMemcpyDtoH_v2_orig = dlsym(orig_handle, "cuMemcpyDtoH_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyDtoH_v2\n");
  _retval = cuMemcpyDtoH_v2_orig(dstHost, srcDevice, ByteCount);
  return _retval;
}


CUresult cuMemcpyDtoD_v2(CUdeviceptr dstDevice, CUdeviceptr srcDevice, size_t ByteCount)
{
  static CUresult (*cuMemcpyDtoD_v2_orig)(CUdeviceptr, CUdeviceptr, size_t) = NULL;
  if (!cuMemcpyDtoD_v2_orig)
  {
    cuMemcpyDtoD_v2_orig = dlsym(orig_handle, "cuMemcpyDtoD_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyDtoD_v2\n");
  _retval = cuMemcpyDtoD_v2_orig(dstDevice, srcDevice, ByteCount);
  return _retval;
}


CUresult cuMemcpyDtoA_v2(CUarray dstArray, size_t dstOffset, CUdeviceptr srcDevice, size_t ByteCount)
{
  static CUresult (*cuMemcpyDtoA_v2_orig)(CUarray, size_t, CUdeviceptr, size_t) = NULL;
  if (!cuMemcpyDtoA_v2_orig)
  {
    cuMemcpyDtoA_v2_orig = dlsym(orig_handle, "cuMemcpyDtoA_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyDtoA_v2\n");
  _retval = cuMemcpyDtoA_v2_orig(dstArray, dstOffset, srcDevice, ByteCount);
  return _retval;
}


CUresult cuMemcpyAtoD_v2(CUdeviceptr dstDevice, CUarray srcArray, size_t srcOffset, size_t ByteCount)
{
  static CUresult (*cuMemcpyAtoD_v2_orig)(CUdeviceptr, CUarray, size_t, size_t) = NULL;
  if (!cuMemcpyAtoD_v2_orig)
  {
    cuMemcpyAtoD_v2_orig = dlsym(orig_handle, "cuMemcpyAtoD_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyAtoD_v2\n");
  _retval = cuMemcpyAtoD_v2_orig(dstDevice, srcArray, srcOffset, ByteCount);
  return _retval;
}


CUresult cuMemcpyHtoA_v2(CUarray dstArray, size_t dstOffset, const void *srcHost, size_t ByteCount)
{
  static CUresult (*cuMemcpyHtoA_v2_orig)(CUarray, size_t, const void *, size_t) = NULL;
  if (!cuMemcpyHtoA_v2_orig)
  {
    cuMemcpyHtoA_v2_orig = dlsym(orig_handle, "cuMemcpyHtoA_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyHtoA_v2\n");
  _retval = cuMemcpyHtoA_v2_orig(dstArray, dstOffset, srcHost, ByteCount);
  return _retval;
}


CUresult cuMemcpyAtoH_v2(void *dstHost, CUarray srcArray, size_t srcOffset, size_t ByteCount)
{
  static CUresult (*cuMemcpyAtoH_v2_orig)(void *, CUarray, size_t, size_t) = NULL;
  if (!cuMemcpyAtoH_v2_orig)
  {
    cuMemcpyAtoH_v2_orig = dlsym(orig_handle, "cuMemcpyAtoH_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyAtoH_v2\n");
  _retval = cuMemcpyAtoH_v2_orig(dstHost, srcArray, srcOffset, ByteCount);
  return _retval;
}


CUresult cuMemcpyAtoA_v2(CUarray dstArray, size_t dstOffset, CUarray srcArray, size_t srcOffset, size_t ByteCount)
{
  static CUresult (*cuMemcpyAtoA_v2_orig)(CUarray, size_t, CUarray, size_t, size_t) = NULL;
  if (!cuMemcpyAtoA_v2_orig)
  {
    cuMemcpyAtoA_v2_orig = dlsym(orig_handle, "cuMemcpyAtoA_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyAtoA_v2\n");
  _retval = cuMemcpyAtoA_v2_orig(dstArray, dstOffset, srcArray, srcOffset, ByteCount);
  return _retval;
}


CUresult cuMemcpy2D_v2(const CUDA_MEMCPY2D *pCopy)
{
  static CUresult (*cuMemcpy2D_v2_orig)(const CUDA_MEMCPY2D *) = NULL;
  if (!cuMemcpy2D_v2_orig)
  {
    cuMemcpy2D_v2_orig = dlsym(orig_handle, "cuMemcpy2D_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpy2D_v2\n");
  _retval = cuMemcpy2D_v2_orig(pCopy);
  return _retval;
}


CUresult cuMemcpy2DUnaligned_v2(const CUDA_MEMCPY2D *pCopy)
{
  static CUresult (*cuMemcpy2DUnaligned_v2_orig)(const CUDA_MEMCPY2D *) = NULL;
  if (!cuMemcpy2DUnaligned_v2_orig)
  {
    cuMemcpy2DUnaligned_v2_orig = dlsym(orig_handle, "cuMemcpy2DUnaligned_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpy2DUnaligned_v2\n");
  _retval = cuMemcpy2DUnaligned_v2_orig(pCopy);
  return _retval;
}


CUresult cuMemcpy3D_v2(const CUDA_MEMCPY3D *pCopy)
{
  static CUresult (*cuMemcpy3D_v2_orig)(const CUDA_MEMCPY3D *) = NULL;
  if (!cuMemcpy3D_v2_orig)
  {
    cuMemcpy3D_v2_orig = dlsym(orig_handle, "cuMemcpy3D_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpy3D_v2\n");
  _retval = cuMemcpy3D_v2_orig(pCopy);
  return _retval;
}


CUresult cuMemcpy3DPeer(const CUDA_MEMCPY3D_PEER *pCopy)
{
  static CUresult (*cuMemcpy3DPeer_orig)(const CUDA_MEMCPY3D_PEER *) = NULL;
  if (!cuMemcpy3DPeer_orig)
  {
    cuMemcpy3DPeer_orig = dlsym(orig_handle, "cuMemcpy3DPeer");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpy3DPeer\n");
  _retval = cuMemcpy3DPeer_orig(pCopy);
  return _retval;
}


CUresult cuMemcpyAsync(CUdeviceptr dst, CUdeviceptr src, size_t ByteCount, CUstream hStream)
{
  static CUresult (*cuMemcpyAsync_orig)(CUdeviceptr, CUdeviceptr, size_t, CUstream) = NULL;
  if (!cuMemcpyAsync_orig)
  {
    cuMemcpyAsync_orig = dlsym(orig_handle, "cuMemcpyAsync");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyAsync\n");
  _retval = cuMemcpyAsync_orig(dst, src, ByteCount, hStream);
  return _retval;
}


CUresult cuMemcpyPeerAsync(CUdeviceptr dstDevice, CUcontext dstContext, CUdeviceptr srcDevice, CUcontext srcContext, size_t ByteCount, CUstream hStream)
{
  static CUresult (*cuMemcpyPeerAsync_orig)(CUdeviceptr, CUcontext, CUdeviceptr, CUcontext, size_t, CUstream) = NULL;
  if (!cuMemcpyPeerAsync_orig)
  {
    cuMemcpyPeerAsync_orig = dlsym(orig_handle, "cuMemcpyPeerAsync");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyPeerAsync\n");
  _retval = cuMemcpyPeerAsync_orig(dstDevice, dstContext, srcDevice, srcContext, ByteCount, hStream);
  return _retval;
}


CUresult cuMemcpyHtoDAsync_v2(CUdeviceptr dstDevice, const void *srcHost, size_t ByteCount, CUstream hStream)
{
  static CUresult (*cuMemcpyHtoDAsync_v2_orig)(CUdeviceptr, const void *, size_t, CUstream) = NULL;
  if (!cuMemcpyHtoDAsync_v2_orig)
  {
    cuMemcpyHtoDAsync_v2_orig = dlsym(orig_handle, "cuMemcpyHtoDAsync_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyHtoDAsync_v2\n");
  _retval = cuMemcpyHtoDAsync_v2_orig(dstDevice, srcHost, ByteCount, hStream);
  return _retval;
}


CUresult cuMemcpyDtoHAsync_v2(void *dstHost, CUdeviceptr srcDevice, size_t ByteCount, CUstream hStream)
{
  static CUresult (*cuMemcpyDtoHAsync_v2_orig)(void *, CUdeviceptr, size_t, CUstream) = NULL;
  if (!cuMemcpyDtoHAsync_v2_orig)
  {
    cuMemcpyDtoHAsync_v2_orig = dlsym(orig_handle, "cuMemcpyDtoHAsync_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyDtoHAsync_v2\n");
  _retval = cuMemcpyDtoHAsync_v2_orig(dstHost, srcDevice, ByteCount, hStream);
  return _retval;
}


CUresult cuMemcpyDtoDAsync_v2(CUdeviceptr dstDevice, CUdeviceptr srcDevice, size_t ByteCount, CUstream hStream)
{
  static CUresult (*cuMemcpyDtoDAsync_v2_orig)(CUdeviceptr, CUdeviceptr, size_t, CUstream) = NULL;
  if (!cuMemcpyDtoDAsync_v2_orig)
  {
    cuMemcpyDtoDAsync_v2_orig = dlsym(orig_handle, "cuMemcpyDtoDAsync_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyDtoDAsync_v2\n");
  _retval = cuMemcpyDtoDAsync_v2_orig(dstDevice, srcDevice, ByteCount, hStream);
  return _retval;
}


CUresult cuMemcpyHtoAAsync_v2(CUarray dstArray, size_t dstOffset, const void *srcHost, size_t ByteCount, CUstream hStream)
{
  static CUresult (*cuMemcpyHtoAAsync_v2_orig)(CUarray, size_t, const void *, size_t, CUstream) = NULL;
  if (!cuMemcpyHtoAAsync_v2_orig)
  {
    cuMemcpyHtoAAsync_v2_orig = dlsym(orig_handle, "cuMemcpyHtoAAsync_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyHtoAAsync_v2\n");
  _retval = cuMemcpyHtoAAsync_v2_orig(dstArray, dstOffset, srcHost, ByteCount, hStream);
  return _retval;
}


CUresult cuMemcpyAtoHAsync_v2(void *dstHost, CUarray srcArray, size_t srcOffset, size_t ByteCount, CUstream hStream)
{
  static CUresult (*cuMemcpyAtoHAsync_v2_orig)(void *, CUarray, size_t, size_t, CUstream) = NULL;
  if (!cuMemcpyAtoHAsync_v2_orig)
  {
    cuMemcpyAtoHAsync_v2_orig = dlsym(orig_handle, "cuMemcpyAtoHAsync_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpyAtoHAsync_v2\n");
  _retval = cuMemcpyAtoHAsync_v2_orig(dstHost, srcArray, srcOffset, ByteCount, hStream);
  return _retval;
}


CUresult cuMemcpy2DAsync_v2(const CUDA_MEMCPY2D *pCopy, CUstream hStream)
{
  static CUresult (*cuMemcpy2DAsync_v2_orig)(const CUDA_MEMCPY2D *, CUstream) = NULL;
  if (!cuMemcpy2DAsync_v2_orig)
  {
    cuMemcpy2DAsync_v2_orig = dlsym(orig_handle, "cuMemcpy2DAsync_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpy2DAsync_v2\n");
  _retval = cuMemcpy2DAsync_v2_orig(pCopy, hStream);
  return _retval;
}


CUresult cuMemcpy3DAsync_v2(const CUDA_MEMCPY3D *pCopy, CUstream hStream)
{
  static CUresult (*cuMemcpy3DAsync_v2_orig)(const CUDA_MEMCPY3D *, CUstream) = NULL;
  if (!cuMemcpy3DAsync_v2_orig)
  {
    cuMemcpy3DAsync_v2_orig = dlsym(orig_handle, "cuMemcpy3DAsync_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpy3DAsync_v2\n");
  _retval = cuMemcpy3DAsync_v2_orig(pCopy, hStream);
  return _retval;
}


CUresult cuMemcpy3DPeerAsync(const CUDA_MEMCPY3D_PEER *pCopy, CUstream hStream)
{
  static CUresult (*cuMemcpy3DPeerAsync_orig)(const CUDA_MEMCPY3D_PEER *, CUstream) = NULL;
  if (!cuMemcpy3DPeerAsync_orig)
  {
    cuMemcpy3DPeerAsync_orig = dlsym(orig_handle, "cuMemcpy3DPeerAsync");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemcpy3DPeerAsync\n");
  _retval = cuMemcpy3DPeerAsync_orig(pCopy, hStream);
  return _retval;
}


CUresult cuMemsetD8_v2(CUdeviceptr dstDevice, unsigned char uc, size_t N)
{
  static CUresult (*cuMemsetD8_v2_orig)(CUdeviceptr, unsigned char, size_t) = NULL;
  if (!cuMemsetD8_v2_orig)
  {
    cuMemsetD8_v2_orig = dlsym(orig_handle, "cuMemsetD8_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemsetD8_v2\n");
  _retval = cuMemsetD8_v2_orig(dstDevice, uc, N);
  return _retval;
}


CUresult cuMemsetD16_v2(CUdeviceptr dstDevice, unsigned short us, size_t N)
{
  static CUresult (*cuMemsetD16_v2_orig)(CUdeviceptr, unsigned short, size_t) = NULL;
  if (!cuMemsetD16_v2_orig)
  {
    cuMemsetD16_v2_orig = dlsym(orig_handle, "cuMemsetD16_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemsetD16_v2\n");
  _retval = cuMemsetD16_v2_orig(dstDevice, us, N);
  return _retval;
}


CUresult cuMemsetD32_v2(CUdeviceptr dstDevice, unsigned int ui, size_t N)
{
  static CUresult (*cuMemsetD32_v2_orig)(CUdeviceptr, unsigned int, size_t) = NULL;
  if (!cuMemsetD32_v2_orig)
  {
    cuMemsetD32_v2_orig = dlsym(orig_handle, "cuMemsetD32_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemsetD32_v2\n");
  _retval = cuMemsetD32_v2_orig(dstDevice, ui, N);
  return _retval;
}


CUresult cuMemsetD2D8_v2(CUdeviceptr dstDevice, size_t dstPitch, unsigned char uc, size_t Width, size_t Height)
{
  static CUresult (*cuMemsetD2D8_v2_orig)(CUdeviceptr, size_t, unsigned char, size_t, size_t) = NULL;
  if (!cuMemsetD2D8_v2_orig)
  {
    cuMemsetD2D8_v2_orig = dlsym(orig_handle, "cuMemsetD2D8_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemsetD2D8_v2\n");
  _retval = cuMemsetD2D8_v2_orig(dstDevice, dstPitch, uc, Width, Height);
  return _retval;
}


CUresult cuMemsetD2D16_v2(CUdeviceptr dstDevice, size_t dstPitch, unsigned short us, size_t Width, size_t Height)
{
  static CUresult (*cuMemsetD2D16_v2_orig)(CUdeviceptr, size_t, unsigned short, size_t, size_t) = NULL;
  if (!cuMemsetD2D16_v2_orig)
  {
    cuMemsetD2D16_v2_orig = dlsym(orig_handle, "cuMemsetD2D16_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemsetD2D16_v2\n");
  _retval = cuMemsetD2D16_v2_orig(dstDevice, dstPitch, us, Width, Height);
  return _retval;
}


CUresult cuMemsetD2D32_v2(CUdeviceptr dstDevice, size_t dstPitch, unsigned int ui, size_t Width, size_t Height)
{
  static CUresult (*cuMemsetD2D32_v2_orig)(CUdeviceptr, size_t, unsigned int, size_t, size_t) = NULL;
  if (!cuMemsetD2D32_v2_orig)
  {
    cuMemsetD2D32_v2_orig = dlsym(orig_handle, "cuMemsetD2D32_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemsetD2D32_v2\n");
  _retval = cuMemsetD2D32_v2_orig(dstDevice, dstPitch, ui, Width, Height);
  return _retval;
}


CUresult cuMemsetD8Async(CUdeviceptr dstDevice, unsigned char uc, size_t N, CUstream hStream)
{
  static CUresult (*cuMemsetD8Async_orig)(CUdeviceptr, unsigned char, size_t, CUstream) = NULL;
  if (!cuMemsetD8Async_orig)
  {
    cuMemsetD8Async_orig = dlsym(orig_handle, "cuMemsetD8Async");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemsetD8Async\n");
  _retval = cuMemsetD8Async_orig(dstDevice, uc, N, hStream);
  return _retval;
}


CUresult cuMemsetD16Async(CUdeviceptr dstDevice, unsigned short us, size_t N, CUstream hStream)
{
  static CUresult (*cuMemsetD16Async_orig)(CUdeviceptr, unsigned short, size_t, CUstream) = NULL;
  if (!cuMemsetD16Async_orig)
  {
    cuMemsetD16Async_orig = dlsym(orig_handle, "cuMemsetD16Async");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemsetD16Async\n");
  _retval = cuMemsetD16Async_orig(dstDevice, us, N, hStream);
  return _retval;
}


CUresult cuMemsetD32Async(CUdeviceptr dstDevice, unsigned int ui, size_t N, CUstream hStream)
{
  static CUresult (*cuMemsetD32Async_orig)(CUdeviceptr, unsigned int, size_t, CUstream) = NULL;
  if (!cuMemsetD32Async_orig)
  {
    cuMemsetD32Async_orig = dlsym(orig_handle, "cuMemsetD32Async");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemsetD32Async\n");
  _retval = cuMemsetD32Async_orig(dstDevice, ui, N, hStream);
  return _retval;
}


CUresult cuMemsetD2D8Async(CUdeviceptr dstDevice, size_t dstPitch, unsigned char uc, size_t Width, size_t Height, CUstream hStream)
{
  static CUresult (*cuMemsetD2D8Async_orig)(CUdeviceptr, size_t, unsigned char, size_t, size_t, CUstream) = NULL;
  if (!cuMemsetD2D8Async_orig)
  {
    cuMemsetD2D8Async_orig = dlsym(orig_handle, "cuMemsetD2D8Async");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemsetD2D8Async\n");
  _retval = cuMemsetD2D8Async_orig(dstDevice, dstPitch, uc, Width, Height, hStream);
  return _retval;
}


CUresult cuMemsetD2D16Async(CUdeviceptr dstDevice, size_t dstPitch, unsigned short us, size_t Width, size_t Height, CUstream hStream)
{
  static CUresult (*cuMemsetD2D16Async_orig)(CUdeviceptr, size_t, unsigned short, size_t, size_t, CUstream) = NULL;
  if (!cuMemsetD2D16Async_orig)
  {
    cuMemsetD2D16Async_orig = dlsym(orig_handle, "cuMemsetD2D16Async");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemsetD2D16Async\n");
  _retval = cuMemsetD2D16Async_orig(dstDevice, dstPitch, us, Width, Height, hStream);
  return _retval;
}


CUresult cuMemsetD2D32Async(CUdeviceptr dstDevice, size_t dstPitch, unsigned int ui, size_t Width, size_t Height, CUstream hStream)
{
  static CUresult (*cuMemsetD2D32Async_orig)(CUdeviceptr, size_t, unsigned int, size_t, size_t, CUstream) = NULL;
  if (!cuMemsetD2D32Async_orig)
  {
    cuMemsetD2D32Async_orig = dlsym(orig_handle, "cuMemsetD2D32Async");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemsetD2D32Async\n");
  _retval = cuMemsetD2D32Async_orig(dstDevice, dstPitch, ui, Width, Height, hStream);
  return _retval;
}


CUresult cuArrayCreate_v2(CUarray *pHandle, const CUDA_ARRAY_DESCRIPTOR *pAllocateArray)
{
  static CUresult (*cuArrayCreate_v2_orig)(CUarray *, const CUDA_ARRAY_DESCRIPTOR *) = NULL;
  if (!cuArrayCreate_v2_orig)
  {
    cuArrayCreate_v2_orig = dlsym(orig_handle, "cuArrayCreate_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuArrayCreate_v2\n");
  _retval = cuArrayCreate_v2_orig(pHandle, pAllocateArray);
  return _retval;
}


CUresult cuArrayGetDescriptor_v2(CUDA_ARRAY_DESCRIPTOR *pArrayDescriptor, CUarray hArray)
{
  static CUresult (*cuArrayGetDescriptor_v2_orig)(CUDA_ARRAY_DESCRIPTOR *, CUarray) = NULL;
  if (!cuArrayGetDescriptor_v2_orig)
  {
    cuArrayGetDescriptor_v2_orig = dlsym(orig_handle, "cuArrayGetDescriptor_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuArrayGetDescriptor_v2\n");
  _retval = cuArrayGetDescriptor_v2_orig(pArrayDescriptor, hArray);
  return _retval;
}


CUresult cuArrayDestroy(CUarray hArray)
{
  static CUresult (*cuArrayDestroy_orig)(CUarray) = NULL;
  if (!cuArrayDestroy_orig)
  {
    cuArrayDestroy_orig = dlsym(orig_handle, "cuArrayDestroy");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuArrayDestroy\n");
  _retval = cuArrayDestroy_orig(hArray);
  return _retval;
}


CUresult cuArray3DCreate_v2(CUarray *pHandle, const CUDA_ARRAY3D_DESCRIPTOR *pAllocateArray)
{
  static CUresult (*cuArray3DCreate_v2_orig)(CUarray *, const CUDA_ARRAY3D_DESCRIPTOR *) = NULL;
  if (!cuArray3DCreate_v2_orig)
  {
    cuArray3DCreate_v2_orig = dlsym(orig_handle, "cuArray3DCreate_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuArray3DCreate_v2\n");
  _retval = cuArray3DCreate_v2_orig(pHandle, pAllocateArray);
  return _retval;
}


CUresult cuArray3DGetDescriptor_v2(CUDA_ARRAY3D_DESCRIPTOR *pArrayDescriptor, CUarray hArray)
{
  static CUresult (*cuArray3DGetDescriptor_v2_orig)(CUDA_ARRAY3D_DESCRIPTOR *, CUarray) = NULL;
  if (!cuArray3DGetDescriptor_v2_orig)
  {
    cuArray3DGetDescriptor_v2_orig = dlsym(orig_handle, "cuArray3DGetDescriptor_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuArray3DGetDescriptor_v2\n");
  _retval = cuArray3DGetDescriptor_v2_orig(pArrayDescriptor, hArray);
  return _retval;
}


CUresult cuMipmappedArrayCreate(CUmipmappedArray *pHandle, const CUDA_ARRAY3D_DESCRIPTOR *pMipmappedArrayDesc, unsigned int numMipmapLevels)
{
  static CUresult (*cuMipmappedArrayCreate_orig)(CUmipmappedArray *, const CUDA_ARRAY3D_DESCRIPTOR *, unsigned int) = NULL;
  if (!cuMipmappedArrayCreate_orig)
  {
    cuMipmappedArrayCreate_orig = dlsym(orig_handle, "cuMipmappedArrayCreate");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMipmappedArrayCreate\n");
  _retval = cuMipmappedArrayCreate_orig(pHandle, pMipmappedArrayDesc, numMipmapLevels);
  return _retval;
}


CUresult cuMipmappedArrayGetLevel(CUarray *pLevelArray, CUmipmappedArray hMipmappedArray, unsigned int level)
{
  static CUresult (*cuMipmappedArrayGetLevel_orig)(CUarray *, CUmipmappedArray, unsigned int) = NULL;
  if (!cuMipmappedArrayGetLevel_orig)
  {
    cuMipmappedArrayGetLevel_orig = dlsym(orig_handle, "cuMipmappedArrayGetLevel");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMipmappedArrayGetLevel\n");
  _retval = cuMipmappedArrayGetLevel_orig(pLevelArray, hMipmappedArray, level);
  return _retval;
}


CUresult cuMipmappedArrayDestroy(CUmipmappedArray hMipmappedArray)
{
  static CUresult (*cuMipmappedArrayDestroy_orig)(CUmipmappedArray) = NULL;
  if (!cuMipmappedArrayDestroy_orig)
  {
    cuMipmappedArrayDestroy_orig = dlsym(orig_handle, "cuMipmappedArrayDestroy");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMipmappedArrayDestroy\n");
  _retval = cuMipmappedArrayDestroy_orig(hMipmappedArray);
  return _retval;
}


CUresult cuPointerGetAttribute(void *data, CUpointer_attribute attribute, CUdeviceptr ptr)
{
  static CUresult (*cuPointerGetAttribute_orig)(void *, CUpointer_attribute, CUdeviceptr) = NULL;
  if (!cuPointerGetAttribute_orig)
  {
    cuPointerGetAttribute_orig = dlsym(orig_handle, "cuPointerGetAttribute");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuPointerGetAttribute\n");
  _retval = cuPointerGetAttribute_orig(data, attribute, ptr);
  return _retval;
}


CUresult cuMemPrefetchAsync(CUdeviceptr devPtr, size_t count, CUdevice dstDevice, CUstream hStream)
{
  static CUresult (*cuMemPrefetchAsync_orig)(CUdeviceptr, size_t, CUdevice, CUstream) = NULL;
  if (!cuMemPrefetchAsync_orig)
  {
    cuMemPrefetchAsync_orig = dlsym(orig_handle, "cuMemPrefetchAsync");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemPrefetchAsync\n");
  _retval = cuMemPrefetchAsync_orig(devPtr, count, dstDevice, hStream);
  return _retval;
}


CUresult cuMemAdvise(CUdeviceptr devPtr, size_t count, CUmem_advise advice, CUdevice device)
{
  static CUresult (*cuMemAdvise_orig)(CUdeviceptr, size_t, CUmem_advise, CUdevice) = NULL;
  if (!cuMemAdvise_orig)
  {
    cuMemAdvise_orig = dlsym(orig_handle, "cuMemAdvise");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemAdvise\n");
  _retval = cuMemAdvise_orig(devPtr, count, advice, device);
  return _retval;
}


CUresult cuMemRangeGetAttribute(void *data, size_t dataSize, CUmem_range_attribute attribute, CUdeviceptr devPtr, size_t count)
{
  static CUresult (*cuMemRangeGetAttribute_orig)(void *, size_t, CUmem_range_attribute, CUdeviceptr, size_t) = NULL;
  if (!cuMemRangeGetAttribute_orig)
  {
    cuMemRangeGetAttribute_orig = dlsym(orig_handle, "cuMemRangeGetAttribute");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemRangeGetAttribute\n");
  _retval = cuMemRangeGetAttribute_orig(data, dataSize, attribute, devPtr, count);
  return _retval;
}


CUresult cuMemRangeGetAttributes(void **data, size_t *dataSizes, CUmem_range_attribute *attributes, size_t numAttributes, CUdeviceptr devPtr, size_t count)
{
  static CUresult (*cuMemRangeGetAttributes_orig)(void **, size_t *, CUmem_range_attribute *, size_t, CUdeviceptr, size_t) = NULL;
  if (!cuMemRangeGetAttributes_orig)
  {
    cuMemRangeGetAttributes_orig = dlsym(orig_handle, "cuMemRangeGetAttributes");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuMemRangeGetAttributes\n");
  _retval = cuMemRangeGetAttributes_orig(data, dataSizes, attributes, numAttributes, devPtr, count);
  return _retval;
}


CUresult cuPointerSetAttribute(const void *value, CUpointer_attribute attribute, CUdeviceptr ptr)
{
  static CUresult (*cuPointerSetAttribute_orig)(const void *, CUpointer_attribute, CUdeviceptr) = NULL;
  if (!cuPointerSetAttribute_orig)
  {
    cuPointerSetAttribute_orig = dlsym(orig_handle, "cuPointerSetAttribute");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuPointerSetAttribute\n");
  _retval = cuPointerSetAttribute_orig(value, attribute, ptr);
  return _retval;
}


CUresult cuPointerGetAttributes(unsigned int numAttributes, CUpointer_attribute *attributes, void **data, CUdeviceptr ptr)
{
  static CUresult (*cuPointerGetAttributes_orig)(unsigned int, CUpointer_attribute *, void **, CUdeviceptr) = NULL;
  if (!cuPointerGetAttributes_orig)
  {
    cuPointerGetAttributes_orig = dlsym(orig_handle, "cuPointerGetAttributes");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuPointerGetAttributes\n");
  _retval = cuPointerGetAttributes_orig(numAttributes, attributes, data, ptr);
  return _retval;
}


CUresult cuStreamCreate(CUstream *phStream, unsigned int Flags)
{
  static CUresult (*cuStreamCreate_orig)(CUstream *, unsigned int) = NULL;
  if (!cuStreamCreate_orig)
  {
    cuStreamCreate_orig = dlsym(orig_handle, "cuStreamCreate");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamCreate\n");
  _retval = cuStreamCreate_orig(phStream, Flags);
  return _retval;
}


CUresult cuStreamCreateWithPriority(CUstream *phStream, unsigned int flags, int priority)
{
  static CUresult (*cuStreamCreateWithPriority_orig)(CUstream *, unsigned int, int) = NULL;
  if (!cuStreamCreateWithPriority_orig)
  {
    cuStreamCreateWithPriority_orig = dlsym(orig_handle, "cuStreamCreateWithPriority");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamCreateWithPriority\n");
  _retval = cuStreamCreateWithPriority_orig(phStream, flags, priority);
  return _retval;
}


CUresult cuStreamGetPriority(CUstream hStream, int *priority)
{
  static CUresult (*cuStreamGetPriority_orig)(CUstream, int *) = NULL;
  if (!cuStreamGetPriority_orig)
  {
    cuStreamGetPriority_orig = dlsym(orig_handle, "cuStreamGetPriority");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamGetPriority\n");
  _retval = cuStreamGetPriority_orig(hStream, priority);
  return _retval;
}


CUresult cuStreamGetFlags(CUstream hStream, unsigned int *flags)
{
  static CUresult (*cuStreamGetFlags_orig)(CUstream, unsigned int *) = NULL;
  if (!cuStreamGetFlags_orig)
  {
    cuStreamGetFlags_orig = dlsym(orig_handle, "cuStreamGetFlags");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamGetFlags\n");
  _retval = cuStreamGetFlags_orig(hStream, flags);
  return _retval;
}


CUresult cuStreamGetCtx(CUstream hStream, CUcontext *pctx)
{
  static CUresult (*cuStreamGetCtx_orig)(CUstream, CUcontext *) = NULL;
  if (!cuStreamGetCtx_orig)
  {
    cuStreamGetCtx_orig = dlsym(orig_handle, "cuStreamGetCtx");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamGetCtx\n");
  _retval = cuStreamGetCtx_orig(hStream, pctx);
  return _retval;
}


CUresult cuStreamWaitEvent(CUstream hStream, CUevent hEvent, unsigned int Flags)
{
  static CUresult (*cuStreamWaitEvent_orig)(CUstream, CUevent, unsigned int) = NULL;
  if (!cuStreamWaitEvent_orig)
  {
    cuStreamWaitEvent_orig = dlsym(orig_handle, "cuStreamWaitEvent");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamWaitEvent\n");
  _retval = cuStreamWaitEvent_orig(hStream, hEvent, Flags);
  return _retval;
}


CUresult cuStreamAddCallback(CUstream hStream, CUstreamCallback callback, void *userData, unsigned int flags)
{
  static CUresult (*cuStreamAddCallback_orig)(CUstream, CUstreamCallback, void *, unsigned int) = NULL;
  if (!cuStreamAddCallback_orig)
  {
    cuStreamAddCallback_orig = dlsym(orig_handle, "cuStreamAddCallback");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamAddCallback\n");
  _retval = cuStreamAddCallback_orig(hStream, callback, userData, flags);
  return _retval;
}


CUresult cuStreamBeginCapture(CUstream hStream)
{
  static CUresult (*cuStreamBeginCapture_orig)(CUstream) = NULL;
  if (!cuStreamBeginCapture_orig)
  {
    cuStreamBeginCapture_orig = dlsym(orig_handle, "cuStreamBeginCapture");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamBeginCapture\n");
  _retval = cuStreamBeginCapture_orig(hStream);
  return _retval;
}


CUresult cuStreamEndCapture(CUstream hStream, CUgraph *phGraph)
{
  static CUresult (*cuStreamEndCapture_orig)(CUstream, CUgraph *) = NULL;
  if (!cuStreamEndCapture_orig)
  {
    cuStreamEndCapture_orig = dlsym(orig_handle, "cuStreamEndCapture");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamEndCapture\n");
  _retval = cuStreamEndCapture_orig(hStream, phGraph);
  return _retval;
}


CUresult cuStreamIsCapturing(CUstream hStream, CUstreamCaptureStatus *captureStatus)
{
  static CUresult (*cuStreamIsCapturing_orig)(CUstream, CUstreamCaptureStatus *) = NULL;
  if (!cuStreamIsCapturing_orig)
  {
    cuStreamIsCapturing_orig = dlsym(orig_handle, "cuStreamIsCapturing");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamIsCapturing\n");
  _retval = cuStreamIsCapturing_orig(hStream, captureStatus);
  return _retval;
}


CUresult cuStreamAttachMemAsync(CUstream hStream, CUdeviceptr dptr, size_t length, unsigned int flags)
{
  static CUresult (*cuStreamAttachMemAsync_orig)(CUstream, CUdeviceptr, size_t, unsigned int) = NULL;
  if (!cuStreamAttachMemAsync_orig)
  {
    cuStreamAttachMemAsync_orig = dlsym(orig_handle, "cuStreamAttachMemAsync");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamAttachMemAsync\n");
  _retval = cuStreamAttachMemAsync_orig(hStream, dptr, length, flags);
  return _retval;
}


CUresult cuStreamQuery(CUstream hStream)
{
  static CUresult (*cuStreamQuery_orig)(CUstream) = NULL;
  if (!cuStreamQuery_orig)
  {
    cuStreamQuery_orig = dlsym(orig_handle, "cuStreamQuery");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamQuery\n");
  _retval = cuStreamQuery_orig(hStream);
  return _retval;
}


CUresult cuStreamSynchronize(CUstream hStream)
{
  static CUresult (*cuStreamSynchronize_orig)(CUstream) = NULL;
  if (!cuStreamSynchronize_orig)
  {
    cuStreamSynchronize_orig = dlsym(orig_handle, "cuStreamSynchronize");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamSynchronize\n");
  _retval = cuStreamSynchronize_orig(hStream);
  return _retval;
}


CUresult cuStreamDestroy_v2(CUstream hStream)
{
  static CUresult (*cuStreamDestroy_v2_orig)(CUstream) = NULL;
  if (!cuStreamDestroy_v2_orig)
  {
    cuStreamDestroy_v2_orig = dlsym(orig_handle, "cuStreamDestroy_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamDestroy_v2\n");
  _retval = cuStreamDestroy_v2_orig(hStream);
  return _retval;
}


CUresult cuEventCreate(CUevent *phEvent, unsigned int Flags)
{
  static CUresult (*cuEventCreate_orig)(CUevent *, unsigned int) = NULL;
  if (!cuEventCreate_orig)
  {
    cuEventCreate_orig = dlsym(orig_handle, "cuEventCreate");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuEventCreate\n");
  _retval = cuEventCreate_orig(phEvent, Flags);
  return _retval;
}


CUresult cuEventRecord(CUevent hEvent, CUstream hStream)
{
  static CUresult (*cuEventRecord_orig)(CUevent, CUstream) = NULL;
  if (!cuEventRecord_orig)
  {
    cuEventRecord_orig = dlsym(orig_handle, "cuEventRecord");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuEventRecord\n");
  _retval = cuEventRecord_orig(hEvent, hStream);
  return _retval;
}


CUresult cuEventQuery(CUevent hEvent)
{
  static CUresult (*cuEventQuery_orig)(CUevent) = NULL;
  if (!cuEventQuery_orig)
  {
    cuEventQuery_orig = dlsym(orig_handle, "cuEventQuery");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuEventQuery\n");
  _retval = cuEventQuery_orig(hEvent);
  return _retval;
}


CUresult cuEventSynchronize(CUevent hEvent)
{
  static CUresult (*cuEventSynchronize_orig)(CUevent) = NULL;
  if (!cuEventSynchronize_orig)
  {
    cuEventSynchronize_orig = dlsym(orig_handle, "cuEventSynchronize");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuEventSynchronize\n");
  _retval = cuEventSynchronize_orig(hEvent);
  return _retval;
}


CUresult cuEventDestroy_v2(CUevent hEvent)
{
  static CUresult (*cuEventDestroy_v2_orig)(CUevent) = NULL;
  if (!cuEventDestroy_v2_orig)
  {
    cuEventDestroy_v2_orig = dlsym(orig_handle, "cuEventDestroy_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuEventDestroy_v2\n");
  _retval = cuEventDestroy_v2_orig(hEvent);
  return _retval;
}


CUresult cuEventElapsedTime(float *pMilliseconds, CUevent hStart, CUevent hEnd)
{
  static CUresult (*cuEventElapsedTime_orig)(float *, CUevent, CUevent) = NULL;
  if (!cuEventElapsedTime_orig)
  {
    cuEventElapsedTime_orig = dlsym(orig_handle, "cuEventElapsedTime");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuEventElapsedTime\n");
  _retval = cuEventElapsedTime_orig(pMilliseconds, hStart, hEnd);
  return _retval;
}


CUresult cuImportExternalMemory(CUexternalMemory *extMem_out, const CUDA_EXTERNAL_MEMORY_HANDLE_DESC *memHandleDesc)
{
  static CUresult (*cuImportExternalMemory_orig)(CUexternalMemory *, const CUDA_EXTERNAL_MEMORY_HANDLE_DESC *) = NULL;
  if (!cuImportExternalMemory_orig)
  {
    cuImportExternalMemory_orig = dlsym(orig_handle, "cuImportExternalMemory");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuImportExternalMemory\n");
  _retval = cuImportExternalMemory_orig(extMem_out, memHandleDesc);
  return _retval;
}


CUresult cuExternalMemoryGetMappedBuffer(CUdeviceptr *devPtr, CUexternalMemory extMem, const CUDA_EXTERNAL_MEMORY_BUFFER_DESC *bufferDesc)
{
  static CUresult (*cuExternalMemoryGetMappedBuffer_orig)(CUdeviceptr *, CUexternalMemory, const CUDA_EXTERNAL_MEMORY_BUFFER_DESC *) = NULL;
  if (!cuExternalMemoryGetMappedBuffer_orig)
  {
    cuExternalMemoryGetMappedBuffer_orig = dlsym(orig_handle, "cuExternalMemoryGetMappedBuffer");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuExternalMemoryGetMappedBuffer\n");
  _retval = cuExternalMemoryGetMappedBuffer_orig(devPtr, extMem, bufferDesc);
  return _retval;
}


CUresult cuExternalMemoryGetMappedMipmappedArray(CUmipmappedArray *mipmap, CUexternalMemory extMem, const CUDA_EXTERNAL_MEMORY_MIPMAPPED_ARRAY_DESC *mipmapDesc)
{
  static CUresult (*cuExternalMemoryGetMappedMipmappedArray_orig)(CUmipmappedArray *, CUexternalMemory, const CUDA_EXTERNAL_MEMORY_MIPMAPPED_ARRAY_DESC *) = NULL;
  if (!cuExternalMemoryGetMappedMipmappedArray_orig)
  {
    cuExternalMemoryGetMappedMipmappedArray_orig = dlsym(orig_handle, "cuExternalMemoryGetMappedMipmappedArray");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuExternalMemoryGetMappedMipmappedArray\n");
  _retval = cuExternalMemoryGetMappedMipmappedArray_orig(mipmap, extMem, mipmapDesc);
  return _retval;
}


CUresult cuDestroyExternalMemory(CUexternalMemory extMem)
{
  static CUresult (*cuDestroyExternalMemory_orig)(CUexternalMemory) = NULL;
  if (!cuDestroyExternalMemory_orig)
  {
    cuDestroyExternalMemory_orig = dlsym(orig_handle, "cuDestroyExternalMemory");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDestroyExternalMemory\n");
  _retval = cuDestroyExternalMemory_orig(extMem);
  return _retval;
}


CUresult cuImportExternalSemaphore(CUexternalSemaphore *extSem_out, const CUDA_EXTERNAL_SEMAPHORE_HANDLE_DESC *semHandleDesc)
{
  static CUresult (*cuImportExternalSemaphore_orig)(CUexternalSemaphore *, const CUDA_EXTERNAL_SEMAPHORE_HANDLE_DESC *) = NULL;
  if (!cuImportExternalSemaphore_orig)
  {
    cuImportExternalSemaphore_orig = dlsym(orig_handle, "cuImportExternalSemaphore");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuImportExternalSemaphore\n");
  _retval = cuImportExternalSemaphore_orig(extSem_out, semHandleDesc);
  return _retval;
}


CUresult cuSignalExternalSemaphoresAsync(const CUexternalSemaphore *extSemArray, const CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS *paramsArray, unsigned int numExtSems, CUstream stream)
{
  static CUresult (*cuSignalExternalSemaphoresAsync_orig)(const CUexternalSemaphore *, const CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS *, unsigned int, CUstream) = NULL;
  if (!cuSignalExternalSemaphoresAsync_orig)
  {
    cuSignalExternalSemaphoresAsync_orig = dlsym(orig_handle, "cuSignalExternalSemaphoresAsync");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuSignalExternalSemaphoresAsync\n");
  _retval = cuSignalExternalSemaphoresAsync_orig(extSemArray, paramsArray, numExtSems, stream);
  return _retval;
}


CUresult cuWaitExternalSemaphoresAsync(const CUexternalSemaphore *extSemArray, const CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS *paramsArray, unsigned int numExtSems, CUstream stream)
{
  static CUresult (*cuWaitExternalSemaphoresAsync_orig)(const CUexternalSemaphore *, const CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS *, unsigned int, CUstream) = NULL;
  if (!cuWaitExternalSemaphoresAsync_orig)
  {
    cuWaitExternalSemaphoresAsync_orig = dlsym(orig_handle, "cuWaitExternalSemaphoresAsync");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuWaitExternalSemaphoresAsync\n");
  _retval = cuWaitExternalSemaphoresAsync_orig(extSemArray, paramsArray, numExtSems, stream);
  return _retval;
}


CUresult cuDestroyExternalSemaphore(CUexternalSemaphore extSem)
{
  static CUresult (*cuDestroyExternalSemaphore_orig)(CUexternalSemaphore) = NULL;
  if (!cuDestroyExternalSemaphore_orig)
  {
    cuDestroyExternalSemaphore_orig = dlsym(orig_handle, "cuDestroyExternalSemaphore");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDestroyExternalSemaphore\n");
  _retval = cuDestroyExternalSemaphore_orig(extSem);
  return _retval;
}


CUresult cuStreamWaitValue32(CUstream stream, CUdeviceptr addr, cuuint32_t value, unsigned int flags)
{
  static CUresult (*cuStreamWaitValue32_orig)(CUstream, CUdeviceptr, cuuint32_t, unsigned int) = NULL;
  if (!cuStreamWaitValue32_orig)
  {
    cuStreamWaitValue32_orig = dlsym(orig_handle, "cuStreamWaitValue32");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamWaitValue32\n");
  _retval = cuStreamWaitValue32_orig(stream, addr, value, flags);
  return _retval;
}


CUresult cuStreamWaitValue64(CUstream stream, CUdeviceptr addr, cuuint64_t value, unsigned int flags)
{
  static CUresult (*cuStreamWaitValue64_orig)(CUstream, CUdeviceptr, cuuint64_t, unsigned int) = NULL;
  if (!cuStreamWaitValue64_orig)
  {
    cuStreamWaitValue64_orig = dlsym(orig_handle, "cuStreamWaitValue64");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamWaitValue64\n");
  _retval = cuStreamWaitValue64_orig(stream, addr, value, flags);
  return _retval;
}


CUresult cuStreamWriteValue32(CUstream stream, CUdeviceptr addr, cuuint32_t value, unsigned int flags)
{
  static CUresult (*cuStreamWriteValue32_orig)(CUstream, CUdeviceptr, cuuint32_t, unsigned int) = NULL;
  if (!cuStreamWriteValue32_orig)
  {
    cuStreamWriteValue32_orig = dlsym(orig_handle, "cuStreamWriteValue32");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamWriteValue32\n");
  _retval = cuStreamWriteValue32_orig(stream, addr, value, flags);
  return _retval;
}


CUresult cuStreamWriteValue64(CUstream stream, CUdeviceptr addr, cuuint64_t value, unsigned int flags)
{
  static CUresult (*cuStreamWriteValue64_orig)(CUstream, CUdeviceptr, cuuint64_t, unsigned int) = NULL;
  if (!cuStreamWriteValue64_orig)
  {
    cuStreamWriteValue64_orig = dlsym(orig_handle, "cuStreamWriteValue64");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamWriteValue64\n");
  _retval = cuStreamWriteValue64_orig(stream, addr, value, flags);
  return _retval;
}


CUresult cuStreamBatchMemOp(CUstream stream, unsigned int count, CUstreamBatchMemOpParams *paramArray, unsigned int flags)
{
  static CUresult (*cuStreamBatchMemOp_orig)(CUstream, unsigned int, CUstreamBatchMemOpParams *, unsigned int) = NULL;
  if (!cuStreamBatchMemOp_orig)
  {
    cuStreamBatchMemOp_orig = dlsym(orig_handle, "cuStreamBatchMemOp");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuStreamBatchMemOp\n");
  _retval = cuStreamBatchMemOp_orig(stream, count, paramArray, flags);
  return _retval;
}


CUresult cuFuncGetAttribute(int *pi, CUfunction_attribute attrib, CUfunction hfunc)
{
  static CUresult (*cuFuncGetAttribute_orig)(int *, CUfunction_attribute, CUfunction) = NULL;
  if (!cuFuncGetAttribute_orig)
  {
    cuFuncGetAttribute_orig = dlsym(orig_handle, "cuFuncGetAttribute");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuFuncGetAttribute\n");
  _retval = cuFuncGetAttribute_orig(pi, attrib, hfunc);
  return _retval;
}


CUresult cuFuncSetAttribute(CUfunction hfunc, CUfunction_attribute attrib, int value)
{
  static CUresult (*cuFuncSetAttribute_orig)(CUfunction, CUfunction_attribute, int) = NULL;
  if (!cuFuncSetAttribute_orig)
  {
    cuFuncSetAttribute_orig = dlsym(orig_handle, "cuFuncSetAttribute");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuFuncSetAttribute\n");
  _retval = cuFuncSetAttribute_orig(hfunc, attrib, value);
  return _retval;
}


CUresult cuFuncSetCacheConfig(CUfunction hfunc, CUfunc_cache config)
{
  static CUresult (*cuFuncSetCacheConfig_orig)(CUfunction, CUfunc_cache) = NULL;
  if (!cuFuncSetCacheConfig_orig)
  {
    cuFuncSetCacheConfig_orig = dlsym(orig_handle, "cuFuncSetCacheConfig");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuFuncSetCacheConfig\n");
  _retval = cuFuncSetCacheConfig_orig(hfunc, config);
  return _retval;
}


CUresult cuFuncSetSharedMemConfig(CUfunction hfunc, CUsharedconfig config)
{
  static CUresult (*cuFuncSetSharedMemConfig_orig)(CUfunction, CUsharedconfig) = NULL;
  if (!cuFuncSetSharedMemConfig_orig)
  {
    cuFuncSetSharedMemConfig_orig = dlsym(orig_handle, "cuFuncSetSharedMemConfig");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuFuncSetSharedMemConfig\n");
  _retval = cuFuncSetSharedMemConfig_orig(hfunc, config);
  return _retval;
}


CUresult cuLaunchKernel(CUfunction f, unsigned int gridDimX, unsigned int gridDimY, unsigned int gridDimZ, unsigned int blockDimX, unsigned int blockDimY, unsigned int blockDimZ, unsigned int sharedMemBytes, CUstream hStream, void **kernelParams, void **extra)
{
  static CUresult (*cuLaunchKernel_orig)(CUfunction, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, CUstream, void **, void **) = NULL;
  if (!cuLaunchKernel_orig)
  {
    cuLaunchKernel_orig = dlsym(orig_handle, "cuLaunchKernel");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuLaunchKernel\n");
  _retval = cuLaunchKernel_orig(f, gridDimX, gridDimY, gridDimZ, blockDimX, blockDimY, blockDimZ, sharedMemBytes, hStream, kernelParams, extra);
  return _retval;
}


CUresult cuLaunchCooperativeKernel(CUfunction f, unsigned int gridDimX, unsigned int gridDimY, unsigned int gridDimZ, unsigned int blockDimX, unsigned int blockDimY, unsigned int blockDimZ, unsigned int sharedMemBytes, CUstream hStream, void **kernelParams)
{
  static CUresult (*cuLaunchCooperativeKernel_orig)(CUfunction, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, CUstream, void **) = NULL;
  if (!cuLaunchCooperativeKernel_orig)
  {
    cuLaunchCooperativeKernel_orig = dlsym(orig_handle, "cuLaunchCooperativeKernel");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuLaunchCooperativeKernel\n");
  _retval = cuLaunchCooperativeKernel_orig(f, gridDimX, gridDimY, gridDimZ, blockDimX, blockDimY, blockDimZ, sharedMemBytes, hStream, kernelParams);
  return _retval;
}


CUresult cuLaunchCooperativeKernelMultiDevice(CUDA_LAUNCH_PARAMS *launchParamsList, unsigned int numDevices, unsigned int flags)
{
  static CUresult (*cuLaunchCooperativeKernelMultiDevice_orig)(CUDA_LAUNCH_PARAMS *, unsigned int, unsigned int) = NULL;
  if (!cuLaunchCooperativeKernelMultiDevice_orig)
  {
    cuLaunchCooperativeKernelMultiDevice_orig = dlsym(orig_handle, "cuLaunchCooperativeKernelMultiDevice");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuLaunchCooperativeKernelMultiDevice\n");
  _retval = cuLaunchCooperativeKernelMultiDevice_orig(launchParamsList, numDevices, flags);
  return _retval;
}


CUresult cuLaunchHostFunc(CUstream hStream, CUhostFn fn, void *userData)
{
  static CUresult (*cuLaunchHostFunc_orig)(CUstream, CUhostFn, void *) = NULL;
  if (!cuLaunchHostFunc_orig)
  {
    cuLaunchHostFunc_orig = dlsym(orig_handle, "cuLaunchHostFunc");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuLaunchHostFunc\n");
  _retval = cuLaunchHostFunc_orig(hStream, fn, userData);
  return _retval;
}


CUresult cuFuncSetBlockShape(CUfunction hfunc, int x, int y, int z)
{
  static CUresult (*cuFuncSetBlockShape_orig)(CUfunction, int, int, int) = NULL;
  if (!cuFuncSetBlockShape_orig)
  {
    cuFuncSetBlockShape_orig = dlsym(orig_handle, "cuFuncSetBlockShape");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuFuncSetBlockShape\n");
  _retval = cuFuncSetBlockShape_orig(hfunc, x, y, z);
  return _retval;
}


CUresult cuFuncSetSharedSize(CUfunction hfunc, unsigned int bytes)
{
  static CUresult (*cuFuncSetSharedSize_orig)(CUfunction, unsigned int) = NULL;
  if (!cuFuncSetSharedSize_orig)
  {
    cuFuncSetSharedSize_orig = dlsym(orig_handle, "cuFuncSetSharedSize");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuFuncSetSharedSize\n");
  _retval = cuFuncSetSharedSize_orig(hfunc, bytes);
  return _retval;
}


CUresult cuParamSetSize(CUfunction hfunc, unsigned int numbytes)
{
  static CUresult (*cuParamSetSize_orig)(CUfunction, unsigned int) = NULL;
  if (!cuParamSetSize_orig)
  {
    cuParamSetSize_orig = dlsym(orig_handle, "cuParamSetSize");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuParamSetSize\n");
  _retval = cuParamSetSize_orig(hfunc, numbytes);
  return _retval;
}


CUresult cuParamSeti(CUfunction hfunc, int offset, unsigned int value)
{
  static CUresult (*cuParamSeti_orig)(CUfunction, int, unsigned int) = NULL;
  if (!cuParamSeti_orig)
  {
    cuParamSeti_orig = dlsym(orig_handle, "cuParamSeti");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuParamSeti\n");
  _retval = cuParamSeti_orig(hfunc, offset, value);
  return _retval;
}


CUresult cuParamSetf(CUfunction hfunc, int offset, float value)
{
  static CUresult (*cuParamSetf_orig)(CUfunction, int, float) = NULL;
  if (!cuParamSetf_orig)
  {
    cuParamSetf_orig = dlsym(orig_handle, "cuParamSetf");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuParamSetf\n");
  _retval = cuParamSetf_orig(hfunc, offset, value);
  return _retval;
}


CUresult cuParamSetv(CUfunction hfunc, int offset, void *ptr, unsigned int numbytes)
{
  static CUresult (*cuParamSetv_orig)(CUfunction, int, void *, unsigned int) = NULL;
  if (!cuParamSetv_orig)
  {
    cuParamSetv_orig = dlsym(orig_handle, "cuParamSetv");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuParamSetv\n");
  _retval = cuParamSetv_orig(hfunc, offset, ptr, numbytes);
  return _retval;
}


CUresult cuLaunch(CUfunction f)
{
  static CUresult (*cuLaunch_orig)(CUfunction) = NULL;
  if (!cuLaunch_orig)
  {
    cuLaunch_orig = dlsym(orig_handle, "cuLaunch");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuLaunch\n");
  _retval = cuLaunch_orig(f);
  return _retval;
}


CUresult cuLaunchGrid(CUfunction f, int grid_width, int grid_height)
{
  static CUresult (*cuLaunchGrid_orig)(CUfunction, int, int) = NULL;
  if (!cuLaunchGrid_orig)
  {
    cuLaunchGrid_orig = dlsym(orig_handle, "cuLaunchGrid");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuLaunchGrid\n");
  _retval = cuLaunchGrid_orig(f, grid_width, grid_height);
  return _retval;
}


CUresult cuLaunchGridAsync(CUfunction f, int grid_width, int grid_height, CUstream hStream)
{
  static CUresult (*cuLaunchGridAsync_orig)(CUfunction, int, int, CUstream) = NULL;
  if (!cuLaunchGridAsync_orig)
  {
    cuLaunchGridAsync_orig = dlsym(orig_handle, "cuLaunchGridAsync");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuLaunchGridAsync\n");
  _retval = cuLaunchGridAsync_orig(f, grid_width, grid_height, hStream);
  return _retval;
}


CUresult cuParamSetTexRef(CUfunction hfunc, int texunit, CUtexref hTexRef)
{
  static CUresult (*cuParamSetTexRef_orig)(CUfunction, int, CUtexref) = NULL;
  if (!cuParamSetTexRef_orig)
  {
    cuParamSetTexRef_orig = dlsym(orig_handle, "cuParamSetTexRef");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuParamSetTexRef\n");
  _retval = cuParamSetTexRef_orig(hfunc, texunit, hTexRef);
  return _retval;
}


CUresult cuGraphCreate(CUgraph *phGraph, unsigned int flags)
{
  static CUresult (*cuGraphCreate_orig)(CUgraph *, unsigned int) = NULL;
  if (!cuGraphCreate_orig)
  {
    cuGraphCreate_orig = dlsym(orig_handle, "cuGraphCreate");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphCreate\n");
  _retval = cuGraphCreate_orig(phGraph, flags);
  return _retval;
}


CUresult cuGraphAddKernelNode(CUgraphNode *phGraphNode, CUgraph hGraph, CUgraphNode *dependencies, size_t numDependencies, const CUDA_KERNEL_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphAddKernelNode_orig)(CUgraphNode *, CUgraph, CUgraphNode *, size_t, const CUDA_KERNEL_NODE_PARAMS *) = NULL;
  if (!cuGraphAddKernelNode_orig)
  {
    cuGraphAddKernelNode_orig = dlsym(orig_handle, "cuGraphAddKernelNode");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphAddKernelNode\n");
  _retval = cuGraphAddKernelNode_orig(phGraphNode, hGraph, dependencies, numDependencies, nodeParams);
  return _retval;
}


CUresult cuGraphKernelNodeGetParams(CUgraphNode hNode, CUDA_KERNEL_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphKernelNodeGetParams_orig)(CUgraphNode, CUDA_KERNEL_NODE_PARAMS *) = NULL;
  if (!cuGraphKernelNodeGetParams_orig)
  {
    cuGraphKernelNodeGetParams_orig = dlsym(orig_handle, "cuGraphKernelNodeGetParams");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphKernelNodeGetParams\n");
  _retval = cuGraphKernelNodeGetParams_orig(hNode, nodeParams);
  return _retval;
}


CUresult cuGraphKernelNodeSetParams(CUgraphNode hNode, const CUDA_KERNEL_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphKernelNodeSetParams_orig)(CUgraphNode, const CUDA_KERNEL_NODE_PARAMS *) = NULL;
  if (!cuGraphKernelNodeSetParams_orig)
  {
    cuGraphKernelNodeSetParams_orig = dlsym(orig_handle, "cuGraphKernelNodeSetParams");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphKernelNodeSetParams\n");
  _retval = cuGraphKernelNodeSetParams_orig(hNode, nodeParams);
  return _retval;
}


CUresult cuGraphAddMemcpyNode(CUgraphNode *phGraphNode, CUgraph hGraph, CUgraphNode *dependencies, size_t numDependencies, const CUDA_MEMCPY3D *copyParams, CUcontext ctx)
{
  static CUresult (*cuGraphAddMemcpyNode_orig)(CUgraphNode *, CUgraph, CUgraphNode *, size_t, const CUDA_MEMCPY3D *, CUcontext) = NULL;
  if (!cuGraphAddMemcpyNode_orig)
  {
    cuGraphAddMemcpyNode_orig = dlsym(orig_handle, "cuGraphAddMemcpyNode");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphAddMemcpyNode\n");
  _retval = cuGraphAddMemcpyNode_orig(phGraphNode, hGraph, dependencies, numDependencies, copyParams, ctx);
  return _retval;
}


CUresult cuGraphMemcpyNodeGetParams(CUgraphNode hNode, CUDA_MEMCPY3D *nodeParams)
{
  static CUresult (*cuGraphMemcpyNodeGetParams_orig)(CUgraphNode, CUDA_MEMCPY3D *) = NULL;
  if (!cuGraphMemcpyNodeGetParams_orig)
  {
    cuGraphMemcpyNodeGetParams_orig = dlsym(orig_handle, "cuGraphMemcpyNodeGetParams");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphMemcpyNodeGetParams\n");
  _retval = cuGraphMemcpyNodeGetParams_orig(hNode, nodeParams);
  return _retval;
}


CUresult cuGraphMemcpyNodeSetParams(CUgraphNode hNode, const CUDA_MEMCPY3D *nodeParams)
{
  static CUresult (*cuGraphMemcpyNodeSetParams_orig)(CUgraphNode, const CUDA_MEMCPY3D *) = NULL;
  if (!cuGraphMemcpyNodeSetParams_orig)
  {
    cuGraphMemcpyNodeSetParams_orig = dlsym(orig_handle, "cuGraphMemcpyNodeSetParams");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphMemcpyNodeSetParams\n");
  _retval = cuGraphMemcpyNodeSetParams_orig(hNode, nodeParams);
  return _retval;
}


CUresult cuGraphAddMemsetNode(CUgraphNode *phGraphNode, CUgraph hGraph, CUgraphNode *dependencies, size_t numDependencies, const CUDA_MEMSET_NODE_PARAMS *memsetParams, CUcontext ctx)
{
  static CUresult (*cuGraphAddMemsetNode_orig)(CUgraphNode *, CUgraph, CUgraphNode *, size_t, const CUDA_MEMSET_NODE_PARAMS *, CUcontext) = NULL;
  if (!cuGraphAddMemsetNode_orig)
  {
    cuGraphAddMemsetNode_orig = dlsym(orig_handle, "cuGraphAddMemsetNode");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphAddMemsetNode\n");
  _retval = cuGraphAddMemsetNode_orig(phGraphNode, hGraph, dependencies, numDependencies, memsetParams, ctx);
  return _retval;
}


CUresult cuGraphMemsetNodeGetParams(CUgraphNode hNode, CUDA_MEMSET_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphMemsetNodeGetParams_orig)(CUgraphNode, CUDA_MEMSET_NODE_PARAMS *) = NULL;
  if (!cuGraphMemsetNodeGetParams_orig)
  {
    cuGraphMemsetNodeGetParams_orig = dlsym(orig_handle, "cuGraphMemsetNodeGetParams");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphMemsetNodeGetParams\n");
  _retval = cuGraphMemsetNodeGetParams_orig(hNode, nodeParams);
  return _retval;
}


CUresult cuGraphMemsetNodeSetParams(CUgraphNode hNode, const CUDA_MEMSET_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphMemsetNodeSetParams_orig)(CUgraphNode, const CUDA_MEMSET_NODE_PARAMS *) = NULL;
  if (!cuGraphMemsetNodeSetParams_orig)
  {
    cuGraphMemsetNodeSetParams_orig = dlsym(orig_handle, "cuGraphMemsetNodeSetParams");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphMemsetNodeSetParams\n");
  _retval = cuGraphMemsetNodeSetParams_orig(hNode, nodeParams);
  return _retval;
}


CUresult cuGraphAddHostNode(CUgraphNode *phGraphNode, CUgraph hGraph, CUgraphNode *dependencies, size_t numDependencies, const CUDA_HOST_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphAddHostNode_orig)(CUgraphNode *, CUgraph, CUgraphNode *, size_t, const CUDA_HOST_NODE_PARAMS *) = NULL;
  if (!cuGraphAddHostNode_orig)
  {
    cuGraphAddHostNode_orig = dlsym(orig_handle, "cuGraphAddHostNode");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphAddHostNode\n");
  _retval = cuGraphAddHostNode_orig(phGraphNode, hGraph, dependencies, numDependencies, nodeParams);
  return _retval;
}


CUresult cuGraphHostNodeGetParams(CUgraphNode hNode, CUDA_HOST_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphHostNodeGetParams_orig)(CUgraphNode, CUDA_HOST_NODE_PARAMS *) = NULL;
  if (!cuGraphHostNodeGetParams_orig)
  {
    cuGraphHostNodeGetParams_orig = dlsym(orig_handle, "cuGraphHostNodeGetParams");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphHostNodeGetParams\n");
  _retval = cuGraphHostNodeGetParams_orig(hNode, nodeParams);
  return _retval;
}


CUresult cuGraphHostNodeSetParams(CUgraphNode hNode, const CUDA_HOST_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphHostNodeSetParams_orig)(CUgraphNode, const CUDA_HOST_NODE_PARAMS *) = NULL;
  if (!cuGraphHostNodeSetParams_orig)
  {
    cuGraphHostNodeSetParams_orig = dlsym(orig_handle, "cuGraphHostNodeSetParams");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphHostNodeSetParams\n");
  _retval = cuGraphHostNodeSetParams_orig(hNode, nodeParams);
  return _retval;
}


CUresult cuGraphAddChildGraphNode(CUgraphNode *phGraphNode, CUgraph hGraph, CUgraphNode *dependencies, size_t numDependencies, CUgraph childGraph)
{
  static CUresult (*cuGraphAddChildGraphNode_orig)(CUgraphNode *, CUgraph, CUgraphNode *, size_t, CUgraph) = NULL;
  if (!cuGraphAddChildGraphNode_orig)
  {
    cuGraphAddChildGraphNode_orig = dlsym(orig_handle, "cuGraphAddChildGraphNode");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphAddChildGraphNode\n");
  _retval = cuGraphAddChildGraphNode_orig(phGraphNode, hGraph, dependencies, numDependencies, childGraph);
  return _retval;
}


CUresult cuGraphChildGraphNodeGetGraph(CUgraphNode hNode, CUgraph *phGraph)
{
  static CUresult (*cuGraphChildGraphNodeGetGraph_orig)(CUgraphNode, CUgraph *) = NULL;
  if (!cuGraphChildGraphNodeGetGraph_orig)
  {
    cuGraphChildGraphNodeGetGraph_orig = dlsym(orig_handle, "cuGraphChildGraphNodeGetGraph");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphChildGraphNodeGetGraph\n");
  _retval = cuGraphChildGraphNodeGetGraph_orig(hNode, phGraph);
  return _retval;
}


CUresult cuGraphAddEmptyNode(CUgraphNode *phGraphNode, CUgraph hGraph, CUgraphNode *dependencies, size_t numDependencies)
{
  static CUresult (*cuGraphAddEmptyNode_orig)(CUgraphNode *, CUgraph, CUgraphNode *, size_t) = NULL;
  if (!cuGraphAddEmptyNode_orig)
  {
    cuGraphAddEmptyNode_orig = dlsym(orig_handle, "cuGraphAddEmptyNode");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphAddEmptyNode\n");
  _retval = cuGraphAddEmptyNode_orig(phGraphNode, hGraph, dependencies, numDependencies);
  return _retval;
}


CUresult cuGraphClone(CUgraph *phGraphClone, CUgraph originalGraph)
{
  static CUresult (*cuGraphClone_orig)(CUgraph *, CUgraph) = NULL;
  if (!cuGraphClone_orig)
  {
    cuGraphClone_orig = dlsym(orig_handle, "cuGraphClone");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphClone\n");
  _retval = cuGraphClone_orig(phGraphClone, originalGraph);
  return _retval;
}


CUresult cuGraphNodeFindInClone(CUgraphNode *phNode, CUgraphNode hOriginalNode, CUgraph hClonedGraph)
{
  static CUresult (*cuGraphNodeFindInClone_orig)(CUgraphNode *, CUgraphNode, CUgraph) = NULL;
  if (!cuGraphNodeFindInClone_orig)
  {
    cuGraphNodeFindInClone_orig = dlsym(orig_handle, "cuGraphNodeFindInClone");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphNodeFindInClone\n");
  _retval = cuGraphNodeFindInClone_orig(phNode, hOriginalNode, hClonedGraph);
  return _retval;
}


CUresult cuGraphNodeGetType(CUgraphNode hNode, CUgraphNodeType *type)
{
  static CUresult (*cuGraphNodeGetType_orig)(CUgraphNode, CUgraphNodeType *) = NULL;
  if (!cuGraphNodeGetType_orig)
  {
    cuGraphNodeGetType_orig = dlsym(orig_handle, "cuGraphNodeGetType");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphNodeGetType\n");
  _retval = cuGraphNodeGetType_orig(hNode, type);
  return _retval;
}


CUresult cuGraphGetNodes(CUgraph hGraph, CUgraphNode *nodes, size_t *numNodes)
{
  static CUresult (*cuGraphGetNodes_orig)(CUgraph, CUgraphNode *, size_t *) = NULL;
  if (!cuGraphGetNodes_orig)
  {
    cuGraphGetNodes_orig = dlsym(orig_handle, "cuGraphGetNodes");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphGetNodes\n");
  _retval = cuGraphGetNodes_orig(hGraph, nodes, numNodes);
  return _retval;
}


CUresult cuGraphGetRootNodes(CUgraph hGraph, CUgraphNode *rootNodes, size_t *numRootNodes)
{
  static CUresult (*cuGraphGetRootNodes_orig)(CUgraph, CUgraphNode *, size_t *) = NULL;
  if (!cuGraphGetRootNodes_orig)
  {
    cuGraphGetRootNodes_orig = dlsym(orig_handle, "cuGraphGetRootNodes");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphGetRootNodes\n");
  _retval = cuGraphGetRootNodes_orig(hGraph, rootNodes, numRootNodes);
  return _retval;
}


CUresult cuGraphGetEdges(CUgraph hGraph, CUgraphNode *from, CUgraphNode *to, size_t *numEdges)
{
  static CUresult (*cuGraphGetEdges_orig)(CUgraph, CUgraphNode *, CUgraphNode *, size_t *) = NULL;
  if (!cuGraphGetEdges_orig)
  {
    cuGraphGetEdges_orig = dlsym(orig_handle, "cuGraphGetEdges");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphGetEdges\n");
  _retval = cuGraphGetEdges_orig(hGraph, from, to, numEdges);
  return _retval;
}


CUresult cuGraphNodeGetDependencies(CUgraphNode hNode, CUgraphNode *dependencies, size_t *numDependencies)
{
  static CUresult (*cuGraphNodeGetDependencies_orig)(CUgraphNode, CUgraphNode *, size_t *) = NULL;
  if (!cuGraphNodeGetDependencies_orig)
  {
    cuGraphNodeGetDependencies_orig = dlsym(orig_handle, "cuGraphNodeGetDependencies");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphNodeGetDependencies\n");
  _retval = cuGraphNodeGetDependencies_orig(hNode, dependencies, numDependencies);
  return _retval;
}


CUresult cuGraphNodeGetDependentNodes(CUgraphNode hNode, CUgraphNode *dependentNodes, size_t *numDependentNodes)
{
  static CUresult (*cuGraphNodeGetDependentNodes_orig)(CUgraphNode, CUgraphNode *, size_t *) = NULL;
  if (!cuGraphNodeGetDependentNodes_orig)
  {
    cuGraphNodeGetDependentNodes_orig = dlsym(orig_handle, "cuGraphNodeGetDependentNodes");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphNodeGetDependentNodes\n");
  _retval = cuGraphNodeGetDependentNodes_orig(hNode, dependentNodes, numDependentNodes);
  return _retval;
}


CUresult cuGraphAddDependencies(CUgraph hGraph, CUgraphNode *from, CUgraphNode *to, size_t numDependencies)
{
  static CUresult (*cuGraphAddDependencies_orig)(CUgraph, CUgraphNode *, CUgraphNode *, size_t) = NULL;
  if (!cuGraphAddDependencies_orig)
  {
    cuGraphAddDependencies_orig = dlsym(orig_handle, "cuGraphAddDependencies");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphAddDependencies\n");
  _retval = cuGraphAddDependencies_orig(hGraph, from, to, numDependencies);
  return _retval;
}


CUresult cuGraphRemoveDependencies(CUgraph hGraph, CUgraphNode *from, CUgraphNode *to, size_t numDependencies)
{
  static CUresult (*cuGraphRemoveDependencies_orig)(CUgraph, CUgraphNode *, CUgraphNode *, size_t) = NULL;
  if (!cuGraphRemoveDependencies_orig)
  {
    cuGraphRemoveDependencies_orig = dlsym(orig_handle, "cuGraphRemoveDependencies");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphRemoveDependencies\n");
  _retval = cuGraphRemoveDependencies_orig(hGraph, from, to, numDependencies);
  return _retval;
}


CUresult cuGraphDestroyNode(CUgraphNode hNode)
{
  static CUresult (*cuGraphDestroyNode_orig)(CUgraphNode) = NULL;
  if (!cuGraphDestroyNode_orig)
  {
    cuGraphDestroyNode_orig = dlsym(orig_handle, "cuGraphDestroyNode");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphDestroyNode\n");
  _retval = cuGraphDestroyNode_orig(hNode);
  return _retval;
}


CUresult cuGraphInstantiate(CUgraphExec *phGraphExec, CUgraph hGraph, CUgraphNode *phErrorNode, char *logBuffer, size_t bufferSize)
{
  static CUresult (*cuGraphInstantiate_orig)(CUgraphExec *, CUgraph, CUgraphNode *, char *, size_t) = NULL;
  if (!cuGraphInstantiate_orig)
  {
    cuGraphInstantiate_orig = dlsym(orig_handle, "cuGraphInstantiate");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphInstantiate\n");
  _retval = cuGraphInstantiate_orig(phGraphExec, hGraph, phErrorNode, logBuffer, bufferSize);
  return _retval;
}


CUresult cuGraphLaunch(CUgraphExec hGraphExec, CUstream hStream)
{
  static CUresult (*cuGraphLaunch_orig)(CUgraphExec, CUstream) = NULL;
  if (!cuGraphLaunch_orig)
  {
    cuGraphLaunch_orig = dlsym(orig_handle, "cuGraphLaunch");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphLaunch\n");
  _retval = cuGraphLaunch_orig(hGraphExec, hStream);
  return _retval;
}


CUresult cuGraphExecDestroy(CUgraphExec hGraphExec)
{
  static CUresult (*cuGraphExecDestroy_orig)(CUgraphExec) = NULL;
  if (!cuGraphExecDestroy_orig)
  {
    cuGraphExecDestroy_orig = dlsym(orig_handle, "cuGraphExecDestroy");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphExecDestroy\n");
  _retval = cuGraphExecDestroy_orig(hGraphExec);
  return _retval;
}


CUresult cuGraphDestroy(CUgraph hGraph)
{
  static CUresult (*cuGraphDestroy_orig)(CUgraph) = NULL;
  if (!cuGraphDestroy_orig)
  {
    cuGraphDestroy_orig = dlsym(orig_handle, "cuGraphDestroy");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphDestroy\n");
  _retval = cuGraphDestroy_orig(hGraph);
  return _retval;
}


CUresult cuOccupancyMaxActiveBlocksPerMultiprocessor(int *numBlocks, CUfunction func, int blockSize, size_t dynamicSMemSize)
{
  static CUresult (*cuOccupancyMaxActiveBlocksPerMultiprocessor_orig)(int *, CUfunction, int, size_t) = NULL;
  if (!cuOccupancyMaxActiveBlocksPerMultiprocessor_orig)
  {
    cuOccupancyMaxActiveBlocksPerMultiprocessor_orig = dlsym(orig_handle, "cuOccupancyMaxActiveBlocksPerMultiprocessor");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuOccupancyMaxActiveBlocksPerMultiprocessor\n");
  _retval = cuOccupancyMaxActiveBlocksPerMultiprocessor_orig(numBlocks, func, blockSize, dynamicSMemSize);
  return _retval;
}


CUresult cuOccupancyMaxActiveBlocksPerMultiprocessorWithFlags(int *numBlocks, CUfunction func, int blockSize, size_t dynamicSMemSize, unsigned int flags)
{
  static CUresult (*cuOccupancyMaxActiveBlocksPerMultiprocessorWithFlags_orig)(int *, CUfunction, int, size_t, unsigned int) = NULL;
  if (!cuOccupancyMaxActiveBlocksPerMultiprocessorWithFlags_orig)
  {
    cuOccupancyMaxActiveBlocksPerMultiprocessorWithFlags_orig = dlsym(orig_handle, "cuOccupancyMaxActiveBlocksPerMultiprocessorWithFlags");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuOccupancyMaxActiveBlocksPerMultiprocessorWithFlags\n");
  _retval = cuOccupancyMaxActiveBlocksPerMultiprocessorWithFlags_orig(numBlocks, func, blockSize, dynamicSMemSize, flags);
  return _retval;
}


CUresult cuOccupancyMaxPotentialBlockSize(int *minGridSize, int *blockSize, CUfunction func, CUoccupancyB2DSize blockSizeToDynamicSMemSize, size_t dynamicSMemSize, int blockSizeLimit)
{
  static CUresult (*cuOccupancyMaxPotentialBlockSize_orig)(int *, int *, CUfunction, CUoccupancyB2DSize, size_t, int) = NULL;
  if (!cuOccupancyMaxPotentialBlockSize_orig)
  {
    cuOccupancyMaxPotentialBlockSize_orig = dlsym(orig_handle, "cuOccupancyMaxPotentialBlockSize");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuOccupancyMaxPotentialBlockSize\n");
  _retval = cuOccupancyMaxPotentialBlockSize_orig(minGridSize, blockSize, func, blockSizeToDynamicSMemSize, dynamicSMemSize, blockSizeLimit);
  return _retval;
}


CUresult cuOccupancyMaxPotentialBlockSizeWithFlags(int *minGridSize, int *blockSize, CUfunction func, CUoccupancyB2DSize blockSizeToDynamicSMemSize, size_t dynamicSMemSize, int blockSizeLimit, unsigned int flags)
{
  static CUresult (*cuOccupancyMaxPotentialBlockSizeWithFlags_orig)(int *, int *, CUfunction, CUoccupancyB2DSize, size_t, int, unsigned int) = NULL;
  if (!cuOccupancyMaxPotentialBlockSizeWithFlags_orig)
  {
    cuOccupancyMaxPotentialBlockSizeWithFlags_orig = dlsym(orig_handle, "cuOccupancyMaxPotentialBlockSizeWithFlags");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuOccupancyMaxPotentialBlockSizeWithFlags\n");
  _retval = cuOccupancyMaxPotentialBlockSizeWithFlags_orig(minGridSize, blockSize, func, blockSizeToDynamicSMemSize, dynamicSMemSize, blockSizeLimit, flags);
  return _retval;
}


CUresult cuTexRefSetArray(CUtexref hTexRef, CUarray hArray, unsigned int Flags)
{
  static CUresult (*cuTexRefSetArray_orig)(CUtexref, CUarray, unsigned int) = NULL;
  if (!cuTexRefSetArray_orig)
  {
    cuTexRefSetArray_orig = dlsym(orig_handle, "cuTexRefSetArray");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefSetArray\n");
  _retval = cuTexRefSetArray_orig(hTexRef, hArray, Flags);
  return _retval;
}


CUresult cuTexRefSetMipmappedArray(CUtexref hTexRef, CUmipmappedArray hMipmappedArray, unsigned int Flags)
{
  static CUresult (*cuTexRefSetMipmappedArray_orig)(CUtexref, CUmipmappedArray, unsigned int) = NULL;
  if (!cuTexRefSetMipmappedArray_orig)
  {
    cuTexRefSetMipmappedArray_orig = dlsym(orig_handle, "cuTexRefSetMipmappedArray");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefSetMipmappedArray\n");
  _retval = cuTexRefSetMipmappedArray_orig(hTexRef, hMipmappedArray, Flags);
  return _retval;
}


CUresult cuTexRefSetAddress_v2(size_t *ByteOffset, CUtexref hTexRef, CUdeviceptr dptr, size_t bytes)
{
  static CUresult (*cuTexRefSetAddress_v2_orig)(size_t *, CUtexref, CUdeviceptr, size_t) = NULL;
  if (!cuTexRefSetAddress_v2_orig)
  {
    cuTexRefSetAddress_v2_orig = dlsym(orig_handle, "cuTexRefSetAddress_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefSetAddress_v2\n");
  _retval = cuTexRefSetAddress_v2_orig(ByteOffset, hTexRef, dptr, bytes);
  return _retval;
}


CUresult cuTexRefSetAddress2D_v3(CUtexref hTexRef, const CUDA_ARRAY_DESCRIPTOR *desc, CUdeviceptr dptr, size_t Pitch)
{
  static CUresult (*cuTexRefSetAddress2D_v3_orig)(CUtexref, const CUDA_ARRAY_DESCRIPTOR *, CUdeviceptr, size_t) = NULL;
  if (!cuTexRefSetAddress2D_v3_orig)
  {
    cuTexRefSetAddress2D_v3_orig = dlsym(orig_handle, "cuTexRefSetAddress2D_v3");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefSetAddress2D_v3\n");
  _retval = cuTexRefSetAddress2D_v3_orig(hTexRef, desc, dptr, Pitch);
  return _retval;
}


CUresult cuTexRefSetFormat(CUtexref hTexRef, CUarray_format fmt, int NumPackedComponents)
{
  static CUresult (*cuTexRefSetFormat_orig)(CUtexref, CUarray_format, int) = NULL;
  if (!cuTexRefSetFormat_orig)
  {
    cuTexRefSetFormat_orig = dlsym(orig_handle, "cuTexRefSetFormat");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefSetFormat\n");
  _retval = cuTexRefSetFormat_orig(hTexRef, fmt, NumPackedComponents);
  return _retval;
}


CUresult cuTexRefSetAddressMode(CUtexref hTexRef, int dim, CUaddress_mode am)
{
  static CUresult (*cuTexRefSetAddressMode_orig)(CUtexref, int, CUaddress_mode) = NULL;
  if (!cuTexRefSetAddressMode_orig)
  {
    cuTexRefSetAddressMode_orig = dlsym(orig_handle, "cuTexRefSetAddressMode");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefSetAddressMode\n");
  _retval = cuTexRefSetAddressMode_orig(hTexRef, dim, am);
  return _retval;
}


CUresult cuTexRefSetFilterMode(CUtexref hTexRef, CUfilter_mode fm)
{
  static CUresult (*cuTexRefSetFilterMode_orig)(CUtexref, CUfilter_mode) = NULL;
  if (!cuTexRefSetFilterMode_orig)
  {
    cuTexRefSetFilterMode_orig = dlsym(orig_handle, "cuTexRefSetFilterMode");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefSetFilterMode\n");
  _retval = cuTexRefSetFilterMode_orig(hTexRef, fm);
  return _retval;
}


CUresult cuTexRefSetMipmapFilterMode(CUtexref hTexRef, CUfilter_mode fm)
{
  static CUresult (*cuTexRefSetMipmapFilterMode_orig)(CUtexref, CUfilter_mode) = NULL;
  if (!cuTexRefSetMipmapFilterMode_orig)
  {
    cuTexRefSetMipmapFilterMode_orig = dlsym(orig_handle, "cuTexRefSetMipmapFilterMode");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefSetMipmapFilterMode\n");
  _retval = cuTexRefSetMipmapFilterMode_orig(hTexRef, fm);
  return _retval;
}


CUresult cuTexRefSetMipmapLevelBias(CUtexref hTexRef, float bias)
{
  static CUresult (*cuTexRefSetMipmapLevelBias_orig)(CUtexref, float) = NULL;
  if (!cuTexRefSetMipmapLevelBias_orig)
  {
    cuTexRefSetMipmapLevelBias_orig = dlsym(orig_handle, "cuTexRefSetMipmapLevelBias");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefSetMipmapLevelBias\n");
  _retval = cuTexRefSetMipmapLevelBias_orig(hTexRef, bias);
  return _retval;
}


CUresult cuTexRefSetMipmapLevelClamp(CUtexref hTexRef, float minMipmapLevelClamp, float maxMipmapLevelClamp)
{
  static CUresult (*cuTexRefSetMipmapLevelClamp_orig)(CUtexref, float, float) = NULL;
  if (!cuTexRefSetMipmapLevelClamp_orig)
  {
    cuTexRefSetMipmapLevelClamp_orig = dlsym(orig_handle, "cuTexRefSetMipmapLevelClamp");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefSetMipmapLevelClamp\n");
  _retval = cuTexRefSetMipmapLevelClamp_orig(hTexRef, minMipmapLevelClamp, maxMipmapLevelClamp);
  return _retval;
}


CUresult cuTexRefSetMaxAnisotropy(CUtexref hTexRef, unsigned int maxAniso)
{
  static CUresult (*cuTexRefSetMaxAnisotropy_orig)(CUtexref, unsigned int) = NULL;
  if (!cuTexRefSetMaxAnisotropy_orig)
  {
    cuTexRefSetMaxAnisotropy_orig = dlsym(orig_handle, "cuTexRefSetMaxAnisotropy");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefSetMaxAnisotropy\n");
  _retval = cuTexRefSetMaxAnisotropy_orig(hTexRef, maxAniso);
  return _retval;
}


CUresult cuTexRefSetBorderColor(CUtexref hTexRef, float *pBorderColor)
{
  static CUresult (*cuTexRefSetBorderColor_orig)(CUtexref, float *) = NULL;
  if (!cuTexRefSetBorderColor_orig)
  {
    cuTexRefSetBorderColor_orig = dlsym(orig_handle, "cuTexRefSetBorderColor");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefSetBorderColor\n");
  _retval = cuTexRefSetBorderColor_orig(hTexRef, pBorderColor);
  return _retval;
}


CUresult cuTexRefSetFlags(CUtexref hTexRef, unsigned int Flags)
{
  static CUresult (*cuTexRefSetFlags_orig)(CUtexref, unsigned int) = NULL;
  if (!cuTexRefSetFlags_orig)
  {
    cuTexRefSetFlags_orig = dlsym(orig_handle, "cuTexRefSetFlags");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefSetFlags\n");
  _retval = cuTexRefSetFlags_orig(hTexRef, Flags);
  return _retval;
}


CUresult cuTexRefGetAddress_v2(CUdeviceptr *pdptr, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetAddress_v2_orig)(CUdeviceptr *, CUtexref) = NULL;
  if (!cuTexRefGetAddress_v2_orig)
  {
    cuTexRefGetAddress_v2_orig = dlsym(orig_handle, "cuTexRefGetAddress_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefGetAddress_v2\n");
  _retval = cuTexRefGetAddress_v2_orig(pdptr, hTexRef);
  return _retval;
}


CUresult cuTexRefGetArray(CUarray *phArray, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetArray_orig)(CUarray *, CUtexref) = NULL;
  if (!cuTexRefGetArray_orig)
  {
    cuTexRefGetArray_orig = dlsym(orig_handle, "cuTexRefGetArray");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefGetArray\n");
  _retval = cuTexRefGetArray_orig(phArray, hTexRef);
  return _retval;
}


CUresult cuTexRefGetMipmappedArray(CUmipmappedArray *phMipmappedArray, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetMipmappedArray_orig)(CUmipmappedArray *, CUtexref) = NULL;
  if (!cuTexRefGetMipmappedArray_orig)
  {
    cuTexRefGetMipmappedArray_orig = dlsym(orig_handle, "cuTexRefGetMipmappedArray");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefGetMipmappedArray\n");
  _retval = cuTexRefGetMipmappedArray_orig(phMipmappedArray, hTexRef);
  return _retval;
}


CUresult cuTexRefGetAddressMode(CUaddress_mode *pam, CUtexref hTexRef, int dim)
{
  static CUresult (*cuTexRefGetAddressMode_orig)(CUaddress_mode *, CUtexref, int) = NULL;
  if (!cuTexRefGetAddressMode_orig)
  {
    cuTexRefGetAddressMode_orig = dlsym(orig_handle, "cuTexRefGetAddressMode");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefGetAddressMode\n");
  _retval = cuTexRefGetAddressMode_orig(pam, hTexRef, dim);
  return _retval;
}


CUresult cuTexRefGetFilterMode(CUfilter_mode *pfm, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetFilterMode_orig)(CUfilter_mode *, CUtexref) = NULL;
  if (!cuTexRefGetFilterMode_orig)
  {
    cuTexRefGetFilterMode_orig = dlsym(orig_handle, "cuTexRefGetFilterMode");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefGetFilterMode\n");
  _retval = cuTexRefGetFilterMode_orig(pfm, hTexRef);
  return _retval;
}


CUresult cuTexRefGetFormat(CUarray_format *pFormat, int *pNumChannels, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetFormat_orig)(CUarray_format *, int *, CUtexref) = NULL;
  if (!cuTexRefGetFormat_orig)
  {
    cuTexRefGetFormat_orig = dlsym(orig_handle, "cuTexRefGetFormat");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefGetFormat\n");
  _retval = cuTexRefGetFormat_orig(pFormat, pNumChannels, hTexRef);
  return _retval;
}


CUresult cuTexRefGetMipmapFilterMode(CUfilter_mode *pfm, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetMipmapFilterMode_orig)(CUfilter_mode *, CUtexref) = NULL;
  if (!cuTexRefGetMipmapFilterMode_orig)
  {
    cuTexRefGetMipmapFilterMode_orig = dlsym(orig_handle, "cuTexRefGetMipmapFilterMode");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefGetMipmapFilterMode\n");
  _retval = cuTexRefGetMipmapFilterMode_orig(pfm, hTexRef);
  return _retval;
}


CUresult cuTexRefGetMipmapLevelBias(float *pbias, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetMipmapLevelBias_orig)(float *, CUtexref) = NULL;
  if (!cuTexRefGetMipmapLevelBias_orig)
  {
    cuTexRefGetMipmapLevelBias_orig = dlsym(orig_handle, "cuTexRefGetMipmapLevelBias");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefGetMipmapLevelBias\n");
  _retval = cuTexRefGetMipmapLevelBias_orig(pbias, hTexRef);
  return _retval;
}


CUresult cuTexRefGetMipmapLevelClamp(float *pminMipmapLevelClamp, float *pmaxMipmapLevelClamp, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetMipmapLevelClamp_orig)(float *, float *, CUtexref) = NULL;
  if (!cuTexRefGetMipmapLevelClamp_orig)
  {
    cuTexRefGetMipmapLevelClamp_orig = dlsym(orig_handle, "cuTexRefGetMipmapLevelClamp");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefGetMipmapLevelClamp\n");
  _retval = cuTexRefGetMipmapLevelClamp_orig(pminMipmapLevelClamp, pmaxMipmapLevelClamp, hTexRef);
  return _retval;
}


CUresult cuTexRefGetMaxAnisotropy(int *pmaxAniso, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetMaxAnisotropy_orig)(int *, CUtexref) = NULL;
  if (!cuTexRefGetMaxAnisotropy_orig)
  {
    cuTexRefGetMaxAnisotropy_orig = dlsym(orig_handle, "cuTexRefGetMaxAnisotropy");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefGetMaxAnisotropy\n");
  _retval = cuTexRefGetMaxAnisotropy_orig(pmaxAniso, hTexRef);
  return _retval;
}


CUresult cuTexRefGetBorderColor(float *pBorderColor, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetBorderColor_orig)(float *, CUtexref) = NULL;
  if (!cuTexRefGetBorderColor_orig)
  {
    cuTexRefGetBorderColor_orig = dlsym(orig_handle, "cuTexRefGetBorderColor");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefGetBorderColor\n");
  _retval = cuTexRefGetBorderColor_orig(pBorderColor, hTexRef);
  return _retval;
}


CUresult cuTexRefGetFlags(unsigned int *pFlags, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetFlags_orig)(unsigned int *, CUtexref) = NULL;
  if (!cuTexRefGetFlags_orig)
  {
    cuTexRefGetFlags_orig = dlsym(orig_handle, "cuTexRefGetFlags");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefGetFlags\n");
  _retval = cuTexRefGetFlags_orig(pFlags, hTexRef);
  return _retval;
}


CUresult cuTexRefCreate(CUtexref *pTexRef)
{
  static CUresult (*cuTexRefCreate_orig)(CUtexref *) = NULL;
  if (!cuTexRefCreate_orig)
  {
    cuTexRefCreate_orig = dlsym(orig_handle, "cuTexRefCreate");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefCreate\n");
  _retval = cuTexRefCreate_orig(pTexRef);
  return _retval;
}


CUresult cuTexRefDestroy(CUtexref hTexRef)
{
  static CUresult (*cuTexRefDestroy_orig)(CUtexref) = NULL;
  if (!cuTexRefDestroy_orig)
  {
    cuTexRefDestroy_orig = dlsym(orig_handle, "cuTexRefDestroy");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexRefDestroy\n");
  _retval = cuTexRefDestroy_orig(hTexRef);
  return _retval;
}


CUresult cuSurfRefSetArray(CUsurfref hSurfRef, CUarray hArray, unsigned int Flags)
{
  static CUresult (*cuSurfRefSetArray_orig)(CUsurfref, CUarray, unsigned int) = NULL;
  if (!cuSurfRefSetArray_orig)
  {
    cuSurfRefSetArray_orig = dlsym(orig_handle, "cuSurfRefSetArray");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuSurfRefSetArray\n");
  _retval = cuSurfRefSetArray_orig(hSurfRef, hArray, Flags);
  return _retval;
}


CUresult cuSurfRefGetArray(CUarray *phArray, CUsurfref hSurfRef)
{
  static CUresult (*cuSurfRefGetArray_orig)(CUarray *, CUsurfref) = NULL;
  if (!cuSurfRefGetArray_orig)
  {
    cuSurfRefGetArray_orig = dlsym(orig_handle, "cuSurfRefGetArray");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuSurfRefGetArray\n");
  _retval = cuSurfRefGetArray_orig(phArray, hSurfRef);
  return _retval;
}


CUresult cuTexObjectCreate(CUtexObject *pTexObject, const CUDA_RESOURCE_DESC *pResDesc, const CUDA_TEXTURE_DESC *pTexDesc, const CUDA_RESOURCE_VIEW_DESC *pResViewDesc)
{
  static CUresult (*cuTexObjectCreate_orig)(CUtexObject *, const CUDA_RESOURCE_DESC *, const CUDA_TEXTURE_DESC *, const CUDA_RESOURCE_VIEW_DESC *) = NULL;
  if (!cuTexObjectCreate_orig)
  {
    cuTexObjectCreate_orig = dlsym(orig_handle, "cuTexObjectCreate");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexObjectCreate\n");
  _retval = cuTexObjectCreate_orig(pTexObject, pResDesc, pTexDesc, pResViewDesc);
  return _retval;
}


CUresult cuTexObjectDestroy(CUtexObject texObject)
{
  static CUresult (*cuTexObjectDestroy_orig)(CUtexObject) = NULL;
  if (!cuTexObjectDestroy_orig)
  {
    cuTexObjectDestroy_orig = dlsym(orig_handle, "cuTexObjectDestroy");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexObjectDestroy\n");
  _retval = cuTexObjectDestroy_orig(texObject);
  return _retval;
}


CUresult cuTexObjectGetResourceDesc(CUDA_RESOURCE_DESC *pResDesc, CUtexObject texObject)
{
  static CUresult (*cuTexObjectGetResourceDesc_orig)(CUDA_RESOURCE_DESC *, CUtexObject) = NULL;
  if (!cuTexObjectGetResourceDesc_orig)
  {
    cuTexObjectGetResourceDesc_orig = dlsym(orig_handle, "cuTexObjectGetResourceDesc");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexObjectGetResourceDesc\n");
  _retval = cuTexObjectGetResourceDesc_orig(pResDesc, texObject);
  return _retval;
}


CUresult cuTexObjectGetTextureDesc(CUDA_TEXTURE_DESC *pTexDesc, CUtexObject texObject)
{
  static CUresult (*cuTexObjectGetTextureDesc_orig)(CUDA_TEXTURE_DESC *, CUtexObject) = NULL;
  if (!cuTexObjectGetTextureDesc_orig)
  {
    cuTexObjectGetTextureDesc_orig = dlsym(orig_handle, "cuTexObjectGetTextureDesc");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexObjectGetTextureDesc\n");
  _retval = cuTexObjectGetTextureDesc_orig(pTexDesc, texObject);
  return _retval;
}


CUresult cuTexObjectGetResourceViewDesc(CUDA_RESOURCE_VIEW_DESC *pResViewDesc, CUtexObject texObject)
{
  static CUresult (*cuTexObjectGetResourceViewDesc_orig)(CUDA_RESOURCE_VIEW_DESC *, CUtexObject) = NULL;
  if (!cuTexObjectGetResourceViewDesc_orig)
  {
    cuTexObjectGetResourceViewDesc_orig = dlsym(orig_handle, "cuTexObjectGetResourceViewDesc");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuTexObjectGetResourceViewDesc\n");
  _retval = cuTexObjectGetResourceViewDesc_orig(pResViewDesc, texObject);
  return _retval;
}


CUresult cuSurfObjectCreate(CUsurfObject *pSurfObject, const CUDA_RESOURCE_DESC *pResDesc)
{
  static CUresult (*cuSurfObjectCreate_orig)(CUsurfObject *, const CUDA_RESOURCE_DESC *) = NULL;
  if (!cuSurfObjectCreate_orig)
  {
    cuSurfObjectCreate_orig = dlsym(orig_handle, "cuSurfObjectCreate");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuSurfObjectCreate\n");
  _retval = cuSurfObjectCreate_orig(pSurfObject, pResDesc);
  return _retval;
}


CUresult cuSurfObjectDestroy(CUsurfObject surfObject)
{
  static CUresult (*cuSurfObjectDestroy_orig)(CUsurfObject) = NULL;
  if (!cuSurfObjectDestroy_orig)
  {
    cuSurfObjectDestroy_orig = dlsym(orig_handle, "cuSurfObjectDestroy");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuSurfObjectDestroy\n");
  _retval = cuSurfObjectDestroy_orig(surfObject);
  return _retval;
}


CUresult cuSurfObjectGetResourceDesc(CUDA_RESOURCE_DESC *pResDesc, CUsurfObject surfObject)
{
  static CUresult (*cuSurfObjectGetResourceDesc_orig)(CUDA_RESOURCE_DESC *, CUsurfObject) = NULL;
  if (!cuSurfObjectGetResourceDesc_orig)
  {
    cuSurfObjectGetResourceDesc_orig = dlsym(orig_handle, "cuSurfObjectGetResourceDesc");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuSurfObjectGetResourceDesc\n");
  _retval = cuSurfObjectGetResourceDesc_orig(pResDesc, surfObject);
  return _retval;
}


CUresult cuDeviceCanAccessPeer(int *canAccessPeer, CUdevice dev, CUdevice peerDev)
{
  static CUresult (*cuDeviceCanAccessPeer_orig)(int *, CUdevice, CUdevice) = NULL;
  if (!cuDeviceCanAccessPeer_orig)
  {
    cuDeviceCanAccessPeer_orig = dlsym(orig_handle, "cuDeviceCanAccessPeer");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDeviceCanAccessPeer\n");
  _retval = cuDeviceCanAccessPeer_orig(canAccessPeer, dev, peerDev);
  return _retval;
}


CUresult cuCtxEnablePeerAccess(CUcontext peerContext, unsigned int Flags)
{
  static CUresult (*cuCtxEnablePeerAccess_orig)(CUcontext, unsigned int) = NULL;
  if (!cuCtxEnablePeerAccess_orig)
  {
    cuCtxEnablePeerAccess_orig = dlsym(orig_handle, "cuCtxEnablePeerAccess");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxEnablePeerAccess\n");
  _retval = cuCtxEnablePeerAccess_orig(peerContext, Flags);
  return _retval;
}


CUresult cuCtxDisablePeerAccess(CUcontext peerContext)
{
  static CUresult (*cuCtxDisablePeerAccess_orig)(CUcontext) = NULL;
  if (!cuCtxDisablePeerAccess_orig)
  {
    cuCtxDisablePeerAccess_orig = dlsym(orig_handle, "cuCtxDisablePeerAccess");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuCtxDisablePeerAccess\n");
  _retval = cuCtxDisablePeerAccess_orig(peerContext);
  return _retval;
}


CUresult cuDeviceGetP2PAttribute(int *value, CUdevice_P2PAttribute attrib, CUdevice srcDevice, CUdevice dstDevice)
{
  static CUresult (*cuDeviceGetP2PAttribute_orig)(int *, CUdevice_P2PAttribute, CUdevice, CUdevice) = NULL;
  if (!cuDeviceGetP2PAttribute_orig)
  {
    cuDeviceGetP2PAttribute_orig = dlsym(orig_handle, "cuDeviceGetP2PAttribute");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuDeviceGetP2PAttribute\n");
  _retval = cuDeviceGetP2PAttribute_orig(value, attrib, srcDevice, dstDevice);
  return _retval;
}


CUresult cuGraphicsUnregisterResource(CUgraphicsResource resource)
{
  static CUresult (*cuGraphicsUnregisterResource_orig)(CUgraphicsResource) = NULL;
  if (!cuGraphicsUnregisterResource_orig)
  {
    cuGraphicsUnregisterResource_orig = dlsym(orig_handle, "cuGraphicsUnregisterResource");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphicsUnregisterResource\n");
  _retval = cuGraphicsUnregisterResource_orig(resource);
  return _retval;
}


CUresult cuGraphicsSubResourceGetMappedArray(CUarray *pArray, CUgraphicsResource resource, unsigned int arrayIndex, unsigned int mipLevel)
{
  static CUresult (*cuGraphicsSubResourceGetMappedArray_orig)(CUarray *, CUgraphicsResource, unsigned int, unsigned int) = NULL;
  if (!cuGraphicsSubResourceGetMappedArray_orig)
  {
    cuGraphicsSubResourceGetMappedArray_orig = dlsym(orig_handle, "cuGraphicsSubResourceGetMappedArray");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphicsSubResourceGetMappedArray\n");
  _retval = cuGraphicsSubResourceGetMappedArray_orig(pArray, resource, arrayIndex, mipLevel);
  return _retval;
}


CUresult cuGraphicsResourceGetMappedMipmappedArray(CUmipmappedArray *pMipmappedArray, CUgraphicsResource resource)
{
  static CUresult (*cuGraphicsResourceGetMappedMipmappedArray_orig)(CUmipmappedArray *, CUgraphicsResource) = NULL;
  if (!cuGraphicsResourceGetMappedMipmappedArray_orig)
  {
    cuGraphicsResourceGetMappedMipmappedArray_orig = dlsym(orig_handle, "cuGraphicsResourceGetMappedMipmappedArray");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphicsResourceGetMappedMipmappedArray\n");
  _retval = cuGraphicsResourceGetMappedMipmappedArray_orig(pMipmappedArray, resource);
  return _retval;
}


CUresult cuGraphicsResourceGetMappedPointer_v2(CUdeviceptr *pDevPtr, size_t *pSize, CUgraphicsResource resource)
{
  static CUresult (*cuGraphicsResourceGetMappedPointer_v2_orig)(CUdeviceptr *, size_t *, CUgraphicsResource) = NULL;
  if (!cuGraphicsResourceGetMappedPointer_v2_orig)
  {
    cuGraphicsResourceGetMappedPointer_v2_orig = dlsym(orig_handle, "cuGraphicsResourceGetMappedPointer_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphicsResourceGetMappedPointer_v2\n");
  _retval = cuGraphicsResourceGetMappedPointer_v2_orig(pDevPtr, pSize, resource);
  return _retval;
}


CUresult cuGraphicsResourceSetMapFlags_v2(CUgraphicsResource resource, unsigned int flags)
{
  static CUresult (*cuGraphicsResourceSetMapFlags_v2_orig)(CUgraphicsResource, unsigned int) = NULL;
  if (!cuGraphicsResourceSetMapFlags_v2_orig)
  {
    cuGraphicsResourceSetMapFlags_v2_orig = dlsym(orig_handle, "cuGraphicsResourceSetMapFlags_v2");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphicsResourceSetMapFlags_v2\n");
  _retval = cuGraphicsResourceSetMapFlags_v2_orig(resource, flags);
  return _retval;
}


CUresult cuGraphicsMapResources(unsigned int count, CUgraphicsResource *resources, CUstream hStream)
{
  static CUresult (*cuGraphicsMapResources_orig)(unsigned int, CUgraphicsResource *, CUstream) = NULL;
  if (!cuGraphicsMapResources_orig)
  {
    cuGraphicsMapResources_orig = dlsym(orig_handle, "cuGraphicsMapResources");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphicsMapResources\n");
  _retval = cuGraphicsMapResources_orig(count, resources, hStream);
  return _retval;
}


CUresult cuGraphicsUnmapResources(unsigned int count, CUgraphicsResource *resources, CUstream hStream)
{
  static CUresult (*cuGraphicsUnmapResources_orig)(unsigned int, CUgraphicsResource *, CUstream) = NULL;
  if (!cuGraphicsUnmapResources_orig)
  {
    cuGraphicsUnmapResources_orig = dlsym(orig_handle, "cuGraphicsUnmapResources");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGraphicsUnmapResources\n");
  _retval = cuGraphicsUnmapResources_orig(count, resources, hStream);
  return _retval;
}


CUresult cuGetExportTable(const void **ppExportTable, const CUuuid *pExportTableId)
{
  static CUresult (*cuGetExportTable_orig)(const void **, const CUuuid *) = NULL;
  if (!cuGetExportTable_orig)
  {
    cuGetExportTable_orig = dlsym(orig_handle, "cuGetExportTable");
  }

  CUresult _retval;
  fprintf(trace_handle, "cuGetExportTable\n");
  _retval = cuGetExportTable_orig(ppExportTable, pExportTableId);
  return _retval;
}


static __attribute__((constructor)) void init_orig_handle() {
    char *original_library_path = getenv("DLOPEN_LIBRARY");

    if(original_library_path == NULL) {
        fprintf(stderr, "ERROR: Environment variable 'DLOPEN_LIBRARY' must contain path to original library\n");
        exit(1);
    }

    orig_handle = dlopen(original_library_path, RTLD_NOW);

    if(!orig_handle) {
        fprintf(stderr, "ERROR: Could not load original library (%s)\n", dlerror());
        exit(1);
    }
}

static __attribute__((destructor)) void deinit_orig_handle() {
  if(orig_handle) {
    dlclose(orig_handle);
  }
}
static __attribute__((constructor)) void init_trace_output() {
    char *trace_output_path = getenv("TRACE_OUTPUT");

    if(trace_output_path == NULL) {
        fprintf(stderr, "ERROR: Environment variable 'TRACE_OUTPUT' must contain output filename for trace\n");
        exit(1);
    }

    trace_handle = fopen(trace_output_path, "w");

    if(!trace_handle) {
        int sverr = errno;
        fprintf(stderr, "ERROR: Could not open trace output '%s' (%d: %s)\n", trace_output_path, sverr, strerror(sverr));
        exit(1);
    }
}

static __attribute__((destructor)) void deinit_trace_handle() {
  if(trace_handle) {
    fclose(trace_handle);
  }
}
