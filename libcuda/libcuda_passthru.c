/* automatically generated */
#include <dlfcn.h>
#include <cuda.h>
#include <stdio.h>
#include <stdlib.h>

static void * orig_handle;CUresult cuGetErrorString(CUresult error, const char **pStr)
{
  static CUresult (*cuGetErrorString_orig)(CUresult, const char **) = NULL;
  if (!cuGetErrorString_orig)
  {
    cuGetErrorString_orig = dlsym(orig_handle, "cuGetErrorString");
  }

  return cuGetErrorString_orig(error, pStr);
}


CUresult cuGetErrorName(CUresult error, const char **pStr)
{
  static CUresult (*cuGetErrorName_orig)(CUresult, const char **) = NULL;
  if (!cuGetErrorName_orig)
  {
    cuGetErrorName_orig = dlsym(orig_handle, "cuGetErrorName");
  }

  return cuGetErrorName_orig(error, pStr);
}


CUresult cuInit(unsigned int Flags)
{
  static CUresult (*cuInit_orig)(unsigned int) = NULL;
  if (!cuInit_orig)
  {
    cuInit_orig = dlsym(orig_handle, "cuInit");
  }

  return cuInit_orig(Flags);
}


CUresult cuDriverGetVersion(int *driverVersion)
{
  static CUresult (*cuDriverGetVersion_orig)(int *) = NULL;
  if (!cuDriverGetVersion_orig)
  {
    cuDriverGetVersion_orig = dlsym(orig_handle, "cuDriverGetVersion");
  }

  return cuDriverGetVersion_orig(driverVersion);
}


CUresult cuDeviceGet(CUdevice *device, int ordinal)
{
  static CUresult (*cuDeviceGet_orig)(CUdevice *, int) = NULL;
  if (!cuDeviceGet_orig)
  {
    cuDeviceGet_orig = dlsym(orig_handle, "cuDeviceGet");
  }

  return cuDeviceGet_orig(device, ordinal);
}


CUresult cuDeviceGetCount(int *count)
{
  static CUresult (*cuDeviceGetCount_orig)(int *) = NULL;
  if (!cuDeviceGetCount_orig)
  {
    cuDeviceGetCount_orig = dlsym(orig_handle, "cuDeviceGetCount");
  }

  return cuDeviceGetCount_orig(count);
}


CUresult cuDeviceGetName(char *name, int len, CUdevice dev)
{
  static CUresult (*cuDeviceGetName_orig)(char *, int, CUdevice) = NULL;
  if (!cuDeviceGetName_orig)
  {
    cuDeviceGetName_orig = dlsym(orig_handle, "cuDeviceGetName");
  }

  return cuDeviceGetName_orig(name, len, dev);
}


CUresult cuDeviceGetUuid(CUuuid *uuid, CUdevice dev)
{
  static CUresult (*cuDeviceGetUuid_orig)(CUuuid *, CUdevice) = NULL;
  if (!cuDeviceGetUuid_orig)
  {
    cuDeviceGetUuid_orig = dlsym(orig_handle, "cuDeviceGetUuid");
  }

  return cuDeviceGetUuid_orig(uuid, dev);
}


CUresult cuDeviceTotalMem_v2(size_t *bytes, CUdevice dev)
{
  static CUresult (*cuDeviceTotalMem_v2_orig)(size_t *, CUdevice) = NULL;
  if (!cuDeviceTotalMem_v2_orig)
  {
    cuDeviceTotalMem_v2_orig = dlsym(orig_handle, "cuDeviceTotalMem_v2");
  }

  return cuDeviceTotalMem_v2_orig(bytes, dev);
}


CUresult cuDeviceGetAttribute(int *pi, CUdevice_attribute attrib, CUdevice dev)
{
  static CUresult (*cuDeviceGetAttribute_orig)(int *, CUdevice_attribute, CUdevice) = NULL;
  if (!cuDeviceGetAttribute_orig)
  {
    cuDeviceGetAttribute_orig = dlsym(orig_handle, "cuDeviceGetAttribute");
  }

  return cuDeviceGetAttribute_orig(pi, attrib, dev);
}


CUresult cuDeviceGetProperties(CUdevprop *prop, CUdevice dev)
{
  static CUresult (*cuDeviceGetProperties_orig)(CUdevprop *, CUdevice) = NULL;
  if (!cuDeviceGetProperties_orig)
  {
    cuDeviceGetProperties_orig = dlsym(orig_handle, "cuDeviceGetProperties");
  }

  return cuDeviceGetProperties_orig(prop, dev);
}


CUresult cuDeviceComputeCapability(int *major, int *minor, CUdevice dev)
{
  static CUresult (*cuDeviceComputeCapability_orig)(int *, int *, CUdevice) = NULL;
  if (!cuDeviceComputeCapability_orig)
  {
    cuDeviceComputeCapability_orig = dlsym(orig_handle, "cuDeviceComputeCapability");
  }

  return cuDeviceComputeCapability_orig(major, minor, dev);
}


CUresult cuDevicePrimaryCtxRetain(CUcontext *pctx, CUdevice dev)
{
  static CUresult (*cuDevicePrimaryCtxRetain_orig)(CUcontext *, CUdevice) = NULL;
  if (!cuDevicePrimaryCtxRetain_orig)
  {
    cuDevicePrimaryCtxRetain_orig = dlsym(orig_handle, "cuDevicePrimaryCtxRetain");
  }

  return cuDevicePrimaryCtxRetain_orig(pctx, dev);
}


CUresult cuDevicePrimaryCtxRelease(CUdevice dev)
{
  static CUresult (*cuDevicePrimaryCtxRelease_orig)(CUdevice) = NULL;
  if (!cuDevicePrimaryCtxRelease_orig)
  {
    cuDevicePrimaryCtxRelease_orig = dlsym(orig_handle, "cuDevicePrimaryCtxRelease");
  }

  return cuDevicePrimaryCtxRelease_orig(dev);
}


CUresult cuDevicePrimaryCtxSetFlags(CUdevice dev, unsigned int flags)
{
  static CUresult (*cuDevicePrimaryCtxSetFlags_orig)(CUdevice, unsigned int) = NULL;
  if (!cuDevicePrimaryCtxSetFlags_orig)
  {
    cuDevicePrimaryCtxSetFlags_orig = dlsym(orig_handle, "cuDevicePrimaryCtxSetFlags");
  }

  return cuDevicePrimaryCtxSetFlags_orig(dev, flags);
}


CUresult cuDevicePrimaryCtxGetState(CUdevice dev, unsigned int *flags, int *active)
{
  static CUresult (*cuDevicePrimaryCtxGetState_orig)(CUdevice, unsigned int *, int *) = NULL;
  if (!cuDevicePrimaryCtxGetState_orig)
  {
    cuDevicePrimaryCtxGetState_orig = dlsym(orig_handle, "cuDevicePrimaryCtxGetState");
  }

  return cuDevicePrimaryCtxGetState_orig(dev, flags, active);
}


CUresult cuDevicePrimaryCtxReset(CUdevice dev)
{
  static CUresult (*cuDevicePrimaryCtxReset_orig)(CUdevice) = NULL;
  if (!cuDevicePrimaryCtxReset_orig)
  {
    cuDevicePrimaryCtxReset_orig = dlsym(orig_handle, "cuDevicePrimaryCtxReset");
  }

  return cuDevicePrimaryCtxReset_orig(dev);
}


CUresult cuCtxCreate_v2(CUcontext *pctx, unsigned int flags, CUdevice dev)
{
  static CUresult (*cuCtxCreate_v2_orig)(CUcontext *, unsigned int, CUdevice) = NULL;
  if (!cuCtxCreate_v2_orig)
  {
    cuCtxCreate_v2_orig = dlsym(orig_handle, "cuCtxCreate_v2");
  }

  return cuCtxCreate_v2_orig(pctx, flags, dev);
}


CUresult cuCtxDestroy_v2(CUcontext ctx)
{
  static CUresult (*cuCtxDestroy_v2_orig)(CUcontext) = NULL;
  if (!cuCtxDestroy_v2_orig)
  {
    cuCtxDestroy_v2_orig = dlsym(orig_handle, "cuCtxDestroy_v2");
  }

  return cuCtxDestroy_v2_orig(ctx);
}


CUresult cuCtxPushCurrent_v2(CUcontext ctx)
{
  static CUresult (*cuCtxPushCurrent_v2_orig)(CUcontext) = NULL;
  if (!cuCtxPushCurrent_v2_orig)
  {
    cuCtxPushCurrent_v2_orig = dlsym(orig_handle, "cuCtxPushCurrent_v2");
  }

  return cuCtxPushCurrent_v2_orig(ctx);
}


CUresult cuCtxPopCurrent_v2(CUcontext *pctx)
{
  static CUresult (*cuCtxPopCurrent_v2_orig)(CUcontext *) = NULL;
  if (!cuCtxPopCurrent_v2_orig)
  {
    cuCtxPopCurrent_v2_orig = dlsym(orig_handle, "cuCtxPopCurrent_v2");
  }

  return cuCtxPopCurrent_v2_orig(pctx);
}


CUresult cuCtxSetCurrent(CUcontext ctx)
{
  static CUresult (*cuCtxSetCurrent_orig)(CUcontext) = NULL;
  if (!cuCtxSetCurrent_orig)
  {
    cuCtxSetCurrent_orig = dlsym(orig_handle, "cuCtxSetCurrent");
  }

  return cuCtxSetCurrent_orig(ctx);
}


CUresult cuCtxGetCurrent(CUcontext *pctx)
{
  static CUresult (*cuCtxGetCurrent_orig)(CUcontext *) = NULL;
  if (!cuCtxGetCurrent_orig)
  {
    cuCtxGetCurrent_orig = dlsym(orig_handle, "cuCtxGetCurrent");
  }

  return cuCtxGetCurrent_orig(pctx);
}


CUresult cuCtxGetDevice(CUdevice *device)
{
  static CUresult (*cuCtxGetDevice_orig)(CUdevice *) = NULL;
  if (!cuCtxGetDevice_orig)
  {
    cuCtxGetDevice_orig = dlsym(orig_handle, "cuCtxGetDevice");
  }

  return cuCtxGetDevice_orig(device);
}


CUresult cuCtxGetFlags(unsigned int *flags)
{
  static CUresult (*cuCtxGetFlags_orig)(unsigned int *) = NULL;
  if (!cuCtxGetFlags_orig)
  {
    cuCtxGetFlags_orig = dlsym(orig_handle, "cuCtxGetFlags");
  }

  return cuCtxGetFlags_orig(flags);
}


CUresult cuCtxSynchronize(void)
{
  static CUresult (*cuCtxSynchronize_orig)(void) = NULL;
  if (!cuCtxSynchronize_orig)
  {
    cuCtxSynchronize_orig = dlsym(orig_handle, "cuCtxSynchronize");
  }

  return cuCtxSynchronize_orig();
}


CUresult cuCtxSetLimit(CUlimit limit, size_t value)
{
  static CUresult (*cuCtxSetLimit_orig)(CUlimit, size_t) = NULL;
  if (!cuCtxSetLimit_orig)
  {
    cuCtxSetLimit_orig = dlsym(orig_handle, "cuCtxSetLimit");
  }

  return cuCtxSetLimit_orig(limit, value);
}


CUresult cuCtxGetLimit(size_t *pvalue, CUlimit limit)
{
  static CUresult (*cuCtxGetLimit_orig)(size_t *, CUlimit) = NULL;
  if (!cuCtxGetLimit_orig)
  {
    cuCtxGetLimit_orig = dlsym(orig_handle, "cuCtxGetLimit");
  }

  return cuCtxGetLimit_orig(pvalue, limit);
}


CUresult cuCtxGetCacheConfig(CUfunc_cache *pconfig)
{
  static CUresult (*cuCtxGetCacheConfig_orig)(CUfunc_cache *) = NULL;
  if (!cuCtxGetCacheConfig_orig)
  {
    cuCtxGetCacheConfig_orig = dlsym(orig_handle, "cuCtxGetCacheConfig");
  }

  return cuCtxGetCacheConfig_orig(pconfig);
}


CUresult cuCtxSetCacheConfig(CUfunc_cache config)
{
  static CUresult (*cuCtxSetCacheConfig_orig)(CUfunc_cache) = NULL;
  if (!cuCtxSetCacheConfig_orig)
  {
    cuCtxSetCacheConfig_orig = dlsym(orig_handle, "cuCtxSetCacheConfig");
  }

  return cuCtxSetCacheConfig_orig(config);
}


CUresult cuCtxGetSharedMemConfig(CUsharedconfig *pConfig)
{
  static CUresult (*cuCtxGetSharedMemConfig_orig)(CUsharedconfig *) = NULL;
  if (!cuCtxGetSharedMemConfig_orig)
  {
    cuCtxGetSharedMemConfig_orig = dlsym(orig_handle, "cuCtxGetSharedMemConfig");
  }

  return cuCtxGetSharedMemConfig_orig(pConfig);
}


CUresult cuCtxSetSharedMemConfig(CUsharedconfig config)
{
  static CUresult (*cuCtxSetSharedMemConfig_orig)(CUsharedconfig) = NULL;
  if (!cuCtxSetSharedMemConfig_orig)
  {
    cuCtxSetSharedMemConfig_orig = dlsym(orig_handle, "cuCtxSetSharedMemConfig");
  }

  return cuCtxSetSharedMemConfig_orig(config);
}


CUresult cuCtxGetApiVersion(CUcontext ctx, unsigned int *version)
{
  static CUresult (*cuCtxGetApiVersion_orig)(CUcontext, unsigned int *) = NULL;
  if (!cuCtxGetApiVersion_orig)
  {
    cuCtxGetApiVersion_orig = dlsym(orig_handle, "cuCtxGetApiVersion");
  }

  return cuCtxGetApiVersion_orig(ctx, version);
}


CUresult cuCtxGetStreamPriorityRange(int *leastPriority, int *greatestPriority)
{
  static CUresult (*cuCtxGetStreamPriorityRange_orig)(int *, int *) = NULL;
  if (!cuCtxGetStreamPriorityRange_orig)
  {
    cuCtxGetStreamPriorityRange_orig = dlsym(orig_handle, "cuCtxGetStreamPriorityRange");
  }

  return cuCtxGetStreamPriorityRange_orig(leastPriority, greatestPriority);
}


CUresult cuCtxAttach(CUcontext *pctx, unsigned int flags)
{
  static CUresult (*cuCtxAttach_orig)(CUcontext *, unsigned int) = NULL;
  if (!cuCtxAttach_orig)
  {
    cuCtxAttach_orig = dlsym(orig_handle, "cuCtxAttach");
  }

  return cuCtxAttach_orig(pctx, flags);
}


CUresult cuCtxDetach(CUcontext ctx)
{
  static CUresult (*cuCtxDetach_orig)(CUcontext) = NULL;
  if (!cuCtxDetach_orig)
  {
    cuCtxDetach_orig = dlsym(orig_handle, "cuCtxDetach");
  }

  return cuCtxDetach_orig(ctx);
}


CUresult cuModuleLoad(CUmodule *module, const char *fname)
{
  static CUresult (*cuModuleLoad_orig)(CUmodule *, const char *) = NULL;
  if (!cuModuleLoad_orig)
  {
    cuModuleLoad_orig = dlsym(orig_handle, "cuModuleLoad");
  }

  return cuModuleLoad_orig(module, fname);
}


CUresult cuModuleLoadData(CUmodule *module, const void *image)
{
  static CUresult (*cuModuleLoadData_orig)(CUmodule *, const void *) = NULL;
  if (!cuModuleLoadData_orig)
  {
    cuModuleLoadData_orig = dlsym(orig_handle, "cuModuleLoadData");
  }

  return cuModuleLoadData_orig(module, image);
}


CUresult cuModuleLoadDataEx(CUmodule *module, const void *image, unsigned int numOptions, CUjit_option *options, void **optionValues)
{
  static CUresult (*cuModuleLoadDataEx_orig)(CUmodule *, const void *, unsigned int, CUjit_option *, void **) = NULL;
  if (!cuModuleLoadDataEx_orig)
  {
    cuModuleLoadDataEx_orig = dlsym(orig_handle, "cuModuleLoadDataEx");
  }

  return cuModuleLoadDataEx_orig(module, image, numOptions, options, optionValues);
}


CUresult cuModuleLoadFatBinary(CUmodule *module, const void *fatCubin)
{
  static CUresult (*cuModuleLoadFatBinary_orig)(CUmodule *, const void *) = NULL;
  if (!cuModuleLoadFatBinary_orig)
  {
    cuModuleLoadFatBinary_orig = dlsym(orig_handle, "cuModuleLoadFatBinary");
  }

  return cuModuleLoadFatBinary_orig(module, fatCubin);
}


CUresult cuModuleUnload(CUmodule hmod)
{
  static CUresult (*cuModuleUnload_orig)(CUmodule) = NULL;
  if (!cuModuleUnload_orig)
  {
    cuModuleUnload_orig = dlsym(orig_handle, "cuModuleUnload");
  }

  return cuModuleUnload_orig(hmod);
}


CUresult cuModuleGetFunction(CUfunction *hfunc, CUmodule hmod, const char *name)
{
  static CUresult (*cuModuleGetFunction_orig)(CUfunction *, CUmodule, const char *) = NULL;
  if (!cuModuleGetFunction_orig)
  {
    cuModuleGetFunction_orig = dlsym(orig_handle, "cuModuleGetFunction");
  }

  return cuModuleGetFunction_orig(hfunc, hmod, name);
}


CUresult cuModuleGetGlobal_v2(CUdeviceptr *dptr, size_t *bytes, CUmodule hmod, const char *name)
{
  static CUresult (*cuModuleGetGlobal_v2_orig)(CUdeviceptr *, size_t *, CUmodule, const char *) = NULL;
  if (!cuModuleGetGlobal_v2_orig)
  {
    cuModuleGetGlobal_v2_orig = dlsym(orig_handle, "cuModuleGetGlobal_v2");
  }

  return cuModuleGetGlobal_v2_orig(dptr, bytes, hmod, name);
}


CUresult cuModuleGetTexRef(CUtexref *pTexRef, CUmodule hmod, const char *name)
{
  static CUresult (*cuModuleGetTexRef_orig)(CUtexref *, CUmodule, const char *) = NULL;
  if (!cuModuleGetTexRef_orig)
  {
    cuModuleGetTexRef_orig = dlsym(orig_handle, "cuModuleGetTexRef");
  }

  return cuModuleGetTexRef_orig(pTexRef, hmod, name);
}


CUresult cuModuleGetSurfRef(CUsurfref *pSurfRef, CUmodule hmod, const char *name)
{
  static CUresult (*cuModuleGetSurfRef_orig)(CUsurfref *, CUmodule, const char *) = NULL;
  if (!cuModuleGetSurfRef_orig)
  {
    cuModuleGetSurfRef_orig = dlsym(orig_handle, "cuModuleGetSurfRef");
  }

  return cuModuleGetSurfRef_orig(pSurfRef, hmod, name);
}


CUresult cuLinkCreate_v2(unsigned int numOptions, CUjit_option *options, void **optionValues, CUlinkState *stateOut)
{
  static CUresult (*cuLinkCreate_v2_orig)(unsigned int, CUjit_option *, void **, CUlinkState *) = NULL;
  if (!cuLinkCreate_v2_orig)
  {
    cuLinkCreate_v2_orig = dlsym(orig_handle, "cuLinkCreate_v2");
  }

  return cuLinkCreate_v2_orig(numOptions, options, optionValues, stateOut);
}


CUresult cuLinkAddData_v2(CUlinkState state, CUjitInputType type, void *data, size_t size, const char *name, unsigned int numOptions, CUjit_option *options, void **optionValues)
{
  static CUresult (*cuLinkAddData_v2_orig)(CUlinkState, CUjitInputType, void *, size_t, const char *, unsigned int, CUjit_option *, void **) = NULL;
  if (!cuLinkAddData_v2_orig)
  {
    cuLinkAddData_v2_orig = dlsym(orig_handle, "cuLinkAddData_v2");
  }

  return cuLinkAddData_v2_orig(state, type, data, size, name, numOptions, options, optionValues);
}


CUresult cuLinkAddFile_v2(CUlinkState state, CUjitInputType type, const char *path, unsigned int numOptions, CUjit_option *options, void **optionValues)
{
  static CUresult (*cuLinkAddFile_v2_orig)(CUlinkState, CUjitInputType, const char *, unsigned int, CUjit_option *, void **) = NULL;
  if (!cuLinkAddFile_v2_orig)
  {
    cuLinkAddFile_v2_orig = dlsym(orig_handle, "cuLinkAddFile_v2");
  }

  return cuLinkAddFile_v2_orig(state, type, path, numOptions, options, optionValues);
}


CUresult cuLinkComplete(CUlinkState state, void **cubinOut, size_t *sizeOut)
{
  static CUresult (*cuLinkComplete_orig)(CUlinkState, void **, size_t *) = NULL;
  if (!cuLinkComplete_orig)
  {
    cuLinkComplete_orig = dlsym(orig_handle, "cuLinkComplete");
  }

  return cuLinkComplete_orig(state, cubinOut, sizeOut);
}


CUresult cuLinkDestroy(CUlinkState state)
{
  static CUresult (*cuLinkDestroy_orig)(CUlinkState) = NULL;
  if (!cuLinkDestroy_orig)
  {
    cuLinkDestroy_orig = dlsym(orig_handle, "cuLinkDestroy");
  }

  return cuLinkDestroy_orig(state);
}


CUresult cuMemGetInfo_v2(size_t *free, size_t *total)
{
  static CUresult (*cuMemGetInfo_v2_orig)(size_t *, size_t *) = NULL;
  if (!cuMemGetInfo_v2_orig)
  {
    cuMemGetInfo_v2_orig = dlsym(orig_handle, "cuMemGetInfo_v2");
  }

  return cuMemGetInfo_v2_orig(free, total);
}


CUresult cuMemAlloc_v2(CUdeviceptr *dptr, size_t bytesize)
{
  static CUresult (*cuMemAlloc_v2_orig)(CUdeviceptr *, size_t) = NULL;
  if (!cuMemAlloc_v2_orig)
  {
    cuMemAlloc_v2_orig = dlsym(orig_handle, "cuMemAlloc_v2");
  }

  return cuMemAlloc_v2_orig(dptr, bytesize);
}


CUresult cuMemAllocPitch_v2(CUdeviceptr *dptr, size_t *pPitch, size_t WidthInBytes, size_t Height, unsigned int ElementSizeBytes)
{
  static CUresult (*cuMemAllocPitch_v2_orig)(CUdeviceptr *, size_t *, size_t, size_t, unsigned int) = NULL;
  if (!cuMemAllocPitch_v2_orig)
  {
    cuMemAllocPitch_v2_orig = dlsym(orig_handle, "cuMemAllocPitch_v2");
  }

  return cuMemAllocPitch_v2_orig(dptr, pPitch, WidthInBytes, Height, ElementSizeBytes);
}


CUresult cuMemFree_v2(CUdeviceptr dptr)
{
  static CUresult (*cuMemFree_v2_orig)(CUdeviceptr) = NULL;
  if (!cuMemFree_v2_orig)
  {
    cuMemFree_v2_orig = dlsym(orig_handle, "cuMemFree_v2");
  }

  return cuMemFree_v2_orig(dptr);
}


CUresult cuMemGetAddressRange_v2(CUdeviceptr *pbase, size_t *psize, CUdeviceptr dptr)
{
  static CUresult (*cuMemGetAddressRange_v2_orig)(CUdeviceptr *, size_t *, CUdeviceptr) = NULL;
  if (!cuMemGetAddressRange_v2_orig)
  {
    cuMemGetAddressRange_v2_orig = dlsym(orig_handle, "cuMemGetAddressRange_v2");
  }

  return cuMemGetAddressRange_v2_orig(pbase, psize, dptr);
}


CUresult cuMemAllocHost_v2(void **pp, size_t bytesize)
{
  static CUresult (*cuMemAllocHost_v2_orig)(void **, size_t) = NULL;
  if (!cuMemAllocHost_v2_orig)
  {
    cuMemAllocHost_v2_orig = dlsym(orig_handle, "cuMemAllocHost_v2");
  }

  return cuMemAllocHost_v2_orig(pp, bytesize);
}


CUresult cuMemFreeHost(void *p)
{
  static CUresult (*cuMemFreeHost_orig)(void *) = NULL;
  if (!cuMemFreeHost_orig)
  {
    cuMemFreeHost_orig = dlsym(orig_handle, "cuMemFreeHost");
  }

  return cuMemFreeHost_orig(p);
}


CUresult cuMemHostAlloc(void **pp, size_t bytesize, unsigned int Flags)
{
  static CUresult (*cuMemHostAlloc_orig)(void **, size_t, unsigned int) = NULL;
  if (!cuMemHostAlloc_orig)
  {
    cuMemHostAlloc_orig = dlsym(orig_handle, "cuMemHostAlloc");
  }

  return cuMemHostAlloc_orig(pp, bytesize, Flags);
}


CUresult cuMemHostGetDevicePointer_v2(CUdeviceptr *pdptr, void *p, unsigned int Flags)
{
  static CUresult (*cuMemHostGetDevicePointer_v2_orig)(CUdeviceptr *, void *, unsigned int) = NULL;
  if (!cuMemHostGetDevicePointer_v2_orig)
  {
    cuMemHostGetDevicePointer_v2_orig = dlsym(orig_handle, "cuMemHostGetDevicePointer_v2");
  }

  return cuMemHostGetDevicePointer_v2_orig(pdptr, p, Flags);
}


CUresult cuMemHostGetFlags(unsigned int *pFlags, void *p)
{
  static CUresult (*cuMemHostGetFlags_orig)(unsigned int *, void *) = NULL;
  if (!cuMemHostGetFlags_orig)
  {
    cuMemHostGetFlags_orig = dlsym(orig_handle, "cuMemHostGetFlags");
  }

  return cuMemHostGetFlags_orig(pFlags, p);
}


CUresult cuMemAllocManaged(CUdeviceptr *dptr, size_t bytesize, unsigned int flags)
{
  static CUresult (*cuMemAllocManaged_orig)(CUdeviceptr *, size_t, unsigned int) = NULL;
  if (!cuMemAllocManaged_orig)
  {
    cuMemAllocManaged_orig = dlsym(orig_handle, "cuMemAllocManaged");
  }

  return cuMemAllocManaged_orig(dptr, bytesize, flags);
}


CUresult cuDeviceGetByPCIBusId(CUdevice *dev, const char *pciBusId)
{
  static CUresult (*cuDeviceGetByPCIBusId_orig)(CUdevice *, const char *) = NULL;
  if (!cuDeviceGetByPCIBusId_orig)
  {
    cuDeviceGetByPCIBusId_orig = dlsym(orig_handle, "cuDeviceGetByPCIBusId");
  }

  return cuDeviceGetByPCIBusId_orig(dev, pciBusId);
}


CUresult cuDeviceGetPCIBusId(char *pciBusId, int len, CUdevice dev)
{
  static CUresult (*cuDeviceGetPCIBusId_orig)(char *, int, CUdevice) = NULL;
  if (!cuDeviceGetPCIBusId_orig)
  {
    cuDeviceGetPCIBusId_orig = dlsym(orig_handle, "cuDeviceGetPCIBusId");
  }

  return cuDeviceGetPCIBusId_orig(pciBusId, len, dev);
}


CUresult cuIpcGetEventHandle(CUipcEventHandle *pHandle, CUevent event)
{
  static CUresult (*cuIpcGetEventHandle_orig)(CUipcEventHandle *, CUevent) = NULL;
  if (!cuIpcGetEventHandle_orig)
  {
    cuIpcGetEventHandle_orig = dlsym(orig_handle, "cuIpcGetEventHandle");
  }

  return cuIpcGetEventHandle_orig(pHandle, event);
}


CUresult cuIpcOpenEventHandle(CUevent *phEvent, CUipcEventHandle handle)
{
  static CUresult (*cuIpcOpenEventHandle_orig)(CUevent *, CUipcEventHandle) = NULL;
  if (!cuIpcOpenEventHandle_orig)
  {
    cuIpcOpenEventHandle_orig = dlsym(orig_handle, "cuIpcOpenEventHandle");
  }

  return cuIpcOpenEventHandle_orig(phEvent, handle);
}


CUresult cuIpcGetMemHandle(CUipcMemHandle *pHandle, CUdeviceptr dptr)
{
  static CUresult (*cuIpcGetMemHandle_orig)(CUipcMemHandle *, CUdeviceptr) = NULL;
  if (!cuIpcGetMemHandle_orig)
  {
    cuIpcGetMemHandle_orig = dlsym(orig_handle, "cuIpcGetMemHandle");
  }

  return cuIpcGetMemHandle_orig(pHandle, dptr);
}


CUresult cuIpcOpenMemHandle(CUdeviceptr *pdptr, CUipcMemHandle handle, unsigned int Flags)
{
  static CUresult (*cuIpcOpenMemHandle_orig)(CUdeviceptr *, CUipcMemHandle, unsigned int) = NULL;
  if (!cuIpcOpenMemHandle_orig)
  {
    cuIpcOpenMemHandle_orig = dlsym(orig_handle, "cuIpcOpenMemHandle");
  }

  return cuIpcOpenMemHandle_orig(pdptr, handle, Flags);
}


CUresult cuIpcCloseMemHandle(CUdeviceptr dptr)
{
  static CUresult (*cuIpcCloseMemHandle_orig)(CUdeviceptr) = NULL;
  if (!cuIpcCloseMemHandle_orig)
  {
    cuIpcCloseMemHandle_orig = dlsym(orig_handle, "cuIpcCloseMemHandle");
  }

  return cuIpcCloseMemHandle_orig(dptr);
}


CUresult cuMemHostRegister_v2(void *p, size_t bytesize, unsigned int Flags)
{
  static CUresult (*cuMemHostRegister_v2_orig)(void *, size_t, unsigned int) = NULL;
  if (!cuMemHostRegister_v2_orig)
  {
    cuMemHostRegister_v2_orig = dlsym(orig_handle, "cuMemHostRegister_v2");
  }

  return cuMemHostRegister_v2_orig(p, bytesize, Flags);
}


CUresult cuMemHostUnregister(void *p)
{
  static CUresult (*cuMemHostUnregister_orig)(void *) = NULL;
  if (!cuMemHostUnregister_orig)
  {
    cuMemHostUnregister_orig = dlsym(orig_handle, "cuMemHostUnregister");
  }

  return cuMemHostUnregister_orig(p);
}


CUresult cuMemcpy(CUdeviceptr dst, CUdeviceptr src, size_t ByteCount)
{
  static CUresult (*cuMemcpy_orig)(CUdeviceptr, CUdeviceptr, size_t) = NULL;
  if (!cuMemcpy_orig)
  {
    cuMemcpy_orig = dlsym(orig_handle, "cuMemcpy");
  }

  return cuMemcpy_orig(dst, src, ByteCount);
}


CUresult cuMemcpyPeer(CUdeviceptr dstDevice, CUcontext dstContext, CUdeviceptr srcDevice, CUcontext srcContext, size_t ByteCount)
{
  static CUresult (*cuMemcpyPeer_orig)(CUdeviceptr, CUcontext, CUdeviceptr, CUcontext, size_t) = NULL;
  if (!cuMemcpyPeer_orig)
  {
    cuMemcpyPeer_orig = dlsym(orig_handle, "cuMemcpyPeer");
  }

  return cuMemcpyPeer_orig(dstDevice, dstContext, srcDevice, srcContext, ByteCount);
}


CUresult cuMemcpyHtoD_v2(CUdeviceptr dstDevice, const void *srcHost, size_t ByteCount)
{
  static CUresult (*cuMemcpyHtoD_v2_orig)(CUdeviceptr, const void *, size_t) = NULL;
  if (!cuMemcpyHtoD_v2_orig)
  {
    cuMemcpyHtoD_v2_orig = dlsym(orig_handle, "cuMemcpyHtoD_v2");
  }

  return cuMemcpyHtoD_v2_orig(dstDevice, srcHost, ByteCount);
}


CUresult cuMemcpyDtoH_v2(void *dstHost, CUdeviceptr srcDevice, size_t ByteCount)
{
  static CUresult (*cuMemcpyDtoH_v2_orig)(void *, CUdeviceptr, size_t) = NULL;
  if (!cuMemcpyDtoH_v2_orig)
  {
    cuMemcpyDtoH_v2_orig = dlsym(orig_handle, "cuMemcpyDtoH_v2");
  }

  return cuMemcpyDtoH_v2_orig(dstHost, srcDevice, ByteCount);
}


CUresult cuMemcpyDtoD_v2(CUdeviceptr dstDevice, CUdeviceptr srcDevice, size_t ByteCount)
{
  static CUresult (*cuMemcpyDtoD_v2_orig)(CUdeviceptr, CUdeviceptr, size_t) = NULL;
  if (!cuMemcpyDtoD_v2_orig)
  {
    cuMemcpyDtoD_v2_orig = dlsym(orig_handle, "cuMemcpyDtoD_v2");
  }

  return cuMemcpyDtoD_v2_orig(dstDevice, srcDevice, ByteCount);
}


CUresult cuMemcpyDtoA_v2(CUarray dstArray, size_t dstOffset, CUdeviceptr srcDevice, size_t ByteCount)
{
  static CUresult (*cuMemcpyDtoA_v2_orig)(CUarray, size_t, CUdeviceptr, size_t) = NULL;
  if (!cuMemcpyDtoA_v2_orig)
  {
    cuMemcpyDtoA_v2_orig = dlsym(orig_handle, "cuMemcpyDtoA_v2");
  }

  return cuMemcpyDtoA_v2_orig(dstArray, dstOffset, srcDevice, ByteCount);
}


CUresult cuMemcpyAtoD_v2(CUdeviceptr dstDevice, CUarray srcArray, size_t srcOffset, size_t ByteCount)
{
  static CUresult (*cuMemcpyAtoD_v2_orig)(CUdeviceptr, CUarray, size_t, size_t) = NULL;
  if (!cuMemcpyAtoD_v2_orig)
  {
    cuMemcpyAtoD_v2_orig = dlsym(orig_handle, "cuMemcpyAtoD_v2");
  }

  return cuMemcpyAtoD_v2_orig(dstDevice, srcArray, srcOffset, ByteCount);
}


CUresult cuMemcpyHtoA_v2(CUarray dstArray, size_t dstOffset, const void *srcHost, size_t ByteCount)
{
  static CUresult (*cuMemcpyHtoA_v2_orig)(CUarray, size_t, const void *, size_t) = NULL;
  if (!cuMemcpyHtoA_v2_orig)
  {
    cuMemcpyHtoA_v2_orig = dlsym(orig_handle, "cuMemcpyHtoA_v2");
  }

  return cuMemcpyHtoA_v2_orig(dstArray, dstOffset, srcHost, ByteCount);
}


CUresult cuMemcpyAtoH_v2(void *dstHost, CUarray srcArray, size_t srcOffset, size_t ByteCount)
{
  static CUresult (*cuMemcpyAtoH_v2_orig)(void *, CUarray, size_t, size_t) = NULL;
  if (!cuMemcpyAtoH_v2_orig)
  {
    cuMemcpyAtoH_v2_orig = dlsym(orig_handle, "cuMemcpyAtoH_v2");
  }

  return cuMemcpyAtoH_v2_orig(dstHost, srcArray, srcOffset, ByteCount);
}


CUresult cuMemcpyAtoA_v2(CUarray dstArray, size_t dstOffset, CUarray srcArray, size_t srcOffset, size_t ByteCount)
{
  static CUresult (*cuMemcpyAtoA_v2_orig)(CUarray, size_t, CUarray, size_t, size_t) = NULL;
  if (!cuMemcpyAtoA_v2_orig)
  {
    cuMemcpyAtoA_v2_orig = dlsym(orig_handle, "cuMemcpyAtoA_v2");
  }

  return cuMemcpyAtoA_v2_orig(dstArray, dstOffset, srcArray, srcOffset, ByteCount);
}


CUresult cuMemcpy2D_v2(const CUDA_MEMCPY2D *pCopy)
{
  static CUresult (*cuMemcpy2D_v2_orig)(const CUDA_MEMCPY2D *) = NULL;
  if (!cuMemcpy2D_v2_orig)
  {
    cuMemcpy2D_v2_orig = dlsym(orig_handle, "cuMemcpy2D_v2");
  }

  return cuMemcpy2D_v2_orig(pCopy);
}


CUresult cuMemcpy2DUnaligned_v2(const CUDA_MEMCPY2D *pCopy)
{
  static CUresult (*cuMemcpy2DUnaligned_v2_orig)(const CUDA_MEMCPY2D *) = NULL;
  if (!cuMemcpy2DUnaligned_v2_orig)
  {
    cuMemcpy2DUnaligned_v2_orig = dlsym(orig_handle, "cuMemcpy2DUnaligned_v2");
  }

  return cuMemcpy2DUnaligned_v2_orig(pCopy);
}


CUresult cuMemcpy3D_v2(const CUDA_MEMCPY3D *pCopy)
{
  static CUresult (*cuMemcpy3D_v2_orig)(const CUDA_MEMCPY3D *) = NULL;
  if (!cuMemcpy3D_v2_orig)
  {
    cuMemcpy3D_v2_orig = dlsym(orig_handle, "cuMemcpy3D_v2");
  }

  return cuMemcpy3D_v2_orig(pCopy);
}


CUresult cuMemcpy3DPeer(const CUDA_MEMCPY3D_PEER *pCopy)
{
  static CUresult (*cuMemcpy3DPeer_orig)(const CUDA_MEMCPY3D_PEER *) = NULL;
  if (!cuMemcpy3DPeer_orig)
  {
    cuMemcpy3DPeer_orig = dlsym(orig_handle, "cuMemcpy3DPeer");
  }

  return cuMemcpy3DPeer_orig(pCopy);
}


CUresult cuMemcpyAsync(CUdeviceptr dst, CUdeviceptr src, size_t ByteCount, CUstream hStream)
{
  static CUresult (*cuMemcpyAsync_orig)(CUdeviceptr, CUdeviceptr, size_t, CUstream) = NULL;
  if (!cuMemcpyAsync_orig)
  {
    cuMemcpyAsync_orig = dlsym(orig_handle, "cuMemcpyAsync");
  }

  return cuMemcpyAsync_orig(dst, src, ByteCount, hStream);
}


CUresult cuMemcpyPeerAsync(CUdeviceptr dstDevice, CUcontext dstContext, CUdeviceptr srcDevice, CUcontext srcContext, size_t ByteCount, CUstream hStream)
{
  static CUresult (*cuMemcpyPeerAsync_orig)(CUdeviceptr, CUcontext, CUdeviceptr, CUcontext, size_t, CUstream) = NULL;
  if (!cuMemcpyPeerAsync_orig)
  {
    cuMemcpyPeerAsync_orig = dlsym(orig_handle, "cuMemcpyPeerAsync");
  }

  return cuMemcpyPeerAsync_orig(dstDevice, dstContext, srcDevice, srcContext, ByteCount, hStream);
}


CUresult cuMemcpyHtoDAsync_v2(CUdeviceptr dstDevice, const void *srcHost, size_t ByteCount, CUstream hStream)
{
  static CUresult (*cuMemcpyHtoDAsync_v2_orig)(CUdeviceptr, const void *, size_t, CUstream) = NULL;
  if (!cuMemcpyHtoDAsync_v2_orig)
  {
    cuMemcpyHtoDAsync_v2_orig = dlsym(orig_handle, "cuMemcpyHtoDAsync_v2");
  }

  return cuMemcpyHtoDAsync_v2_orig(dstDevice, srcHost, ByteCount, hStream);
}


CUresult cuMemcpyDtoHAsync_v2(void *dstHost, CUdeviceptr srcDevice, size_t ByteCount, CUstream hStream)
{
  static CUresult (*cuMemcpyDtoHAsync_v2_orig)(void *, CUdeviceptr, size_t, CUstream) = NULL;
  if (!cuMemcpyDtoHAsync_v2_orig)
  {
    cuMemcpyDtoHAsync_v2_orig = dlsym(orig_handle, "cuMemcpyDtoHAsync_v2");
  }

  return cuMemcpyDtoHAsync_v2_orig(dstHost, srcDevice, ByteCount, hStream);
}


CUresult cuMemcpyDtoDAsync_v2(CUdeviceptr dstDevice, CUdeviceptr srcDevice, size_t ByteCount, CUstream hStream)
{
  static CUresult (*cuMemcpyDtoDAsync_v2_orig)(CUdeviceptr, CUdeviceptr, size_t, CUstream) = NULL;
  if (!cuMemcpyDtoDAsync_v2_orig)
  {
    cuMemcpyDtoDAsync_v2_orig = dlsym(orig_handle, "cuMemcpyDtoDAsync_v2");
  }

  return cuMemcpyDtoDAsync_v2_orig(dstDevice, srcDevice, ByteCount, hStream);
}


CUresult cuMemcpyHtoAAsync_v2(CUarray dstArray, size_t dstOffset, const void *srcHost, size_t ByteCount, CUstream hStream)
{
  static CUresult (*cuMemcpyHtoAAsync_v2_orig)(CUarray, size_t, const void *, size_t, CUstream) = NULL;
  if (!cuMemcpyHtoAAsync_v2_orig)
  {
    cuMemcpyHtoAAsync_v2_orig = dlsym(orig_handle, "cuMemcpyHtoAAsync_v2");
  }

  return cuMemcpyHtoAAsync_v2_orig(dstArray, dstOffset, srcHost, ByteCount, hStream);
}


CUresult cuMemcpyAtoHAsync_v2(void *dstHost, CUarray srcArray, size_t srcOffset, size_t ByteCount, CUstream hStream)
{
  static CUresult (*cuMemcpyAtoHAsync_v2_orig)(void *, CUarray, size_t, size_t, CUstream) = NULL;
  if (!cuMemcpyAtoHAsync_v2_orig)
  {
    cuMemcpyAtoHAsync_v2_orig = dlsym(orig_handle, "cuMemcpyAtoHAsync_v2");
  }

  return cuMemcpyAtoHAsync_v2_orig(dstHost, srcArray, srcOffset, ByteCount, hStream);
}


CUresult cuMemcpy2DAsync_v2(const CUDA_MEMCPY2D *pCopy, CUstream hStream)
{
  static CUresult (*cuMemcpy2DAsync_v2_orig)(const CUDA_MEMCPY2D *, CUstream) = NULL;
  if (!cuMemcpy2DAsync_v2_orig)
  {
    cuMemcpy2DAsync_v2_orig = dlsym(orig_handle, "cuMemcpy2DAsync_v2");
  }

  return cuMemcpy2DAsync_v2_orig(pCopy, hStream);
}


CUresult cuMemcpy3DAsync_v2(const CUDA_MEMCPY3D *pCopy, CUstream hStream)
{
  static CUresult (*cuMemcpy3DAsync_v2_orig)(const CUDA_MEMCPY3D *, CUstream) = NULL;
  if (!cuMemcpy3DAsync_v2_orig)
  {
    cuMemcpy3DAsync_v2_orig = dlsym(orig_handle, "cuMemcpy3DAsync_v2");
  }

  return cuMemcpy3DAsync_v2_orig(pCopy, hStream);
}


CUresult cuMemcpy3DPeerAsync(const CUDA_MEMCPY3D_PEER *pCopy, CUstream hStream)
{
  static CUresult (*cuMemcpy3DPeerAsync_orig)(const CUDA_MEMCPY3D_PEER *, CUstream) = NULL;
  if (!cuMemcpy3DPeerAsync_orig)
  {
    cuMemcpy3DPeerAsync_orig = dlsym(orig_handle, "cuMemcpy3DPeerAsync");
  }

  return cuMemcpy3DPeerAsync_orig(pCopy, hStream);
}


CUresult cuMemsetD8_v2(CUdeviceptr dstDevice, unsigned char uc, size_t N)
{
  static CUresult (*cuMemsetD8_v2_orig)(CUdeviceptr, unsigned char, size_t) = NULL;
  if (!cuMemsetD8_v2_orig)
  {
    cuMemsetD8_v2_orig = dlsym(orig_handle, "cuMemsetD8_v2");
  }

  return cuMemsetD8_v2_orig(dstDevice, uc, N);
}


CUresult cuMemsetD16_v2(CUdeviceptr dstDevice, unsigned short us, size_t N)
{
  static CUresult (*cuMemsetD16_v2_orig)(CUdeviceptr, unsigned short, size_t) = NULL;
  if (!cuMemsetD16_v2_orig)
  {
    cuMemsetD16_v2_orig = dlsym(orig_handle, "cuMemsetD16_v2");
  }

  return cuMemsetD16_v2_orig(dstDevice, us, N);
}


CUresult cuMemsetD32_v2(CUdeviceptr dstDevice, unsigned int ui, size_t N)
{
  static CUresult (*cuMemsetD32_v2_orig)(CUdeviceptr, unsigned int, size_t) = NULL;
  if (!cuMemsetD32_v2_orig)
  {
    cuMemsetD32_v2_orig = dlsym(orig_handle, "cuMemsetD32_v2");
  }

  return cuMemsetD32_v2_orig(dstDevice, ui, N);
}


CUresult cuMemsetD2D8_v2(CUdeviceptr dstDevice, size_t dstPitch, unsigned char uc, size_t Width, size_t Height)
{
  static CUresult (*cuMemsetD2D8_v2_orig)(CUdeviceptr, size_t, unsigned char, size_t, size_t) = NULL;
  if (!cuMemsetD2D8_v2_orig)
  {
    cuMemsetD2D8_v2_orig = dlsym(orig_handle, "cuMemsetD2D8_v2");
  }

  return cuMemsetD2D8_v2_orig(dstDevice, dstPitch, uc, Width, Height);
}


CUresult cuMemsetD2D16_v2(CUdeviceptr dstDevice, size_t dstPitch, unsigned short us, size_t Width, size_t Height)
{
  static CUresult (*cuMemsetD2D16_v2_orig)(CUdeviceptr, size_t, unsigned short, size_t, size_t) = NULL;
  if (!cuMemsetD2D16_v2_orig)
  {
    cuMemsetD2D16_v2_orig = dlsym(orig_handle, "cuMemsetD2D16_v2");
  }

  return cuMemsetD2D16_v2_orig(dstDevice, dstPitch, us, Width, Height);
}


CUresult cuMemsetD2D32_v2(CUdeviceptr dstDevice, size_t dstPitch, unsigned int ui, size_t Width, size_t Height)
{
  static CUresult (*cuMemsetD2D32_v2_orig)(CUdeviceptr, size_t, unsigned int, size_t, size_t) = NULL;
  if (!cuMemsetD2D32_v2_orig)
  {
    cuMemsetD2D32_v2_orig = dlsym(orig_handle, "cuMemsetD2D32_v2");
  }

  return cuMemsetD2D32_v2_orig(dstDevice, dstPitch, ui, Width, Height);
}


CUresult cuMemsetD8Async(CUdeviceptr dstDevice, unsigned char uc, size_t N, CUstream hStream)
{
  static CUresult (*cuMemsetD8Async_orig)(CUdeviceptr, unsigned char, size_t, CUstream) = NULL;
  if (!cuMemsetD8Async_orig)
  {
    cuMemsetD8Async_orig = dlsym(orig_handle, "cuMemsetD8Async");
  }

  return cuMemsetD8Async_orig(dstDevice, uc, N, hStream);
}


CUresult cuMemsetD16Async(CUdeviceptr dstDevice, unsigned short us, size_t N, CUstream hStream)
{
  static CUresult (*cuMemsetD16Async_orig)(CUdeviceptr, unsigned short, size_t, CUstream) = NULL;
  if (!cuMemsetD16Async_orig)
  {
    cuMemsetD16Async_orig = dlsym(orig_handle, "cuMemsetD16Async");
  }

  return cuMemsetD16Async_orig(dstDevice, us, N, hStream);
}


CUresult cuMemsetD32Async(CUdeviceptr dstDevice, unsigned int ui, size_t N, CUstream hStream)
{
  static CUresult (*cuMemsetD32Async_orig)(CUdeviceptr, unsigned int, size_t, CUstream) = NULL;
  if (!cuMemsetD32Async_orig)
  {
    cuMemsetD32Async_orig = dlsym(orig_handle, "cuMemsetD32Async");
  }

  return cuMemsetD32Async_orig(dstDevice, ui, N, hStream);
}


CUresult cuMemsetD2D8Async(CUdeviceptr dstDevice, size_t dstPitch, unsigned char uc, size_t Width, size_t Height, CUstream hStream)
{
  static CUresult (*cuMemsetD2D8Async_orig)(CUdeviceptr, size_t, unsigned char, size_t, size_t, CUstream) = NULL;
  if (!cuMemsetD2D8Async_orig)
  {
    cuMemsetD2D8Async_orig = dlsym(orig_handle, "cuMemsetD2D8Async");
  }

  return cuMemsetD2D8Async_orig(dstDevice, dstPitch, uc, Width, Height, hStream);
}


CUresult cuMemsetD2D16Async(CUdeviceptr dstDevice, size_t dstPitch, unsigned short us, size_t Width, size_t Height, CUstream hStream)
{
  static CUresult (*cuMemsetD2D16Async_orig)(CUdeviceptr, size_t, unsigned short, size_t, size_t, CUstream) = NULL;
  if (!cuMemsetD2D16Async_orig)
  {
    cuMemsetD2D16Async_orig = dlsym(orig_handle, "cuMemsetD2D16Async");
  }

  return cuMemsetD2D16Async_orig(dstDevice, dstPitch, us, Width, Height, hStream);
}


CUresult cuMemsetD2D32Async(CUdeviceptr dstDevice, size_t dstPitch, unsigned int ui, size_t Width, size_t Height, CUstream hStream)
{
  static CUresult (*cuMemsetD2D32Async_orig)(CUdeviceptr, size_t, unsigned int, size_t, size_t, CUstream) = NULL;
  if (!cuMemsetD2D32Async_orig)
  {
    cuMemsetD2D32Async_orig = dlsym(orig_handle, "cuMemsetD2D32Async");
  }

  return cuMemsetD2D32Async_orig(dstDevice, dstPitch, ui, Width, Height, hStream);
}


CUresult cuArrayCreate_v2(CUarray *pHandle, const CUDA_ARRAY_DESCRIPTOR *pAllocateArray)
{
  static CUresult (*cuArrayCreate_v2_orig)(CUarray *, const CUDA_ARRAY_DESCRIPTOR *) = NULL;
  if (!cuArrayCreate_v2_orig)
  {
    cuArrayCreate_v2_orig = dlsym(orig_handle, "cuArrayCreate_v2");
  }

  return cuArrayCreate_v2_orig(pHandle, pAllocateArray);
}


CUresult cuArrayGetDescriptor_v2(CUDA_ARRAY_DESCRIPTOR *pArrayDescriptor, CUarray hArray)
{
  static CUresult (*cuArrayGetDescriptor_v2_orig)(CUDA_ARRAY_DESCRIPTOR *, CUarray) = NULL;
  if (!cuArrayGetDescriptor_v2_orig)
  {
    cuArrayGetDescriptor_v2_orig = dlsym(orig_handle, "cuArrayGetDescriptor_v2");
  }

  return cuArrayGetDescriptor_v2_orig(pArrayDescriptor, hArray);
}


CUresult cuArrayDestroy(CUarray hArray)
{
  static CUresult (*cuArrayDestroy_orig)(CUarray) = NULL;
  if (!cuArrayDestroy_orig)
  {
    cuArrayDestroy_orig = dlsym(orig_handle, "cuArrayDestroy");
  }

  return cuArrayDestroy_orig(hArray);
}


CUresult cuArray3DCreate_v2(CUarray *pHandle, const CUDA_ARRAY3D_DESCRIPTOR *pAllocateArray)
{
  static CUresult (*cuArray3DCreate_v2_orig)(CUarray *, const CUDA_ARRAY3D_DESCRIPTOR *) = NULL;
  if (!cuArray3DCreate_v2_orig)
  {
    cuArray3DCreate_v2_orig = dlsym(orig_handle, "cuArray3DCreate_v2");
  }

  return cuArray3DCreate_v2_orig(pHandle, pAllocateArray);
}


CUresult cuArray3DGetDescriptor_v2(CUDA_ARRAY3D_DESCRIPTOR *pArrayDescriptor, CUarray hArray)
{
  static CUresult (*cuArray3DGetDescriptor_v2_orig)(CUDA_ARRAY3D_DESCRIPTOR *, CUarray) = NULL;
  if (!cuArray3DGetDescriptor_v2_orig)
  {
    cuArray3DGetDescriptor_v2_orig = dlsym(orig_handle, "cuArray3DGetDescriptor_v2");
  }

  return cuArray3DGetDescriptor_v2_orig(pArrayDescriptor, hArray);
}


CUresult cuMipmappedArrayCreate(CUmipmappedArray *pHandle, const CUDA_ARRAY3D_DESCRIPTOR *pMipmappedArrayDesc, unsigned int numMipmapLevels)
{
  static CUresult (*cuMipmappedArrayCreate_orig)(CUmipmappedArray *, const CUDA_ARRAY3D_DESCRIPTOR *, unsigned int) = NULL;
  if (!cuMipmappedArrayCreate_orig)
  {
    cuMipmappedArrayCreate_orig = dlsym(orig_handle, "cuMipmappedArrayCreate");
  }

  return cuMipmappedArrayCreate_orig(pHandle, pMipmappedArrayDesc, numMipmapLevels);
}


CUresult cuMipmappedArrayGetLevel(CUarray *pLevelArray, CUmipmappedArray hMipmappedArray, unsigned int level)
{
  static CUresult (*cuMipmappedArrayGetLevel_orig)(CUarray *, CUmipmappedArray, unsigned int) = NULL;
  if (!cuMipmappedArrayGetLevel_orig)
  {
    cuMipmappedArrayGetLevel_orig = dlsym(orig_handle, "cuMipmappedArrayGetLevel");
  }

  return cuMipmappedArrayGetLevel_orig(pLevelArray, hMipmappedArray, level);
}


CUresult cuMipmappedArrayDestroy(CUmipmappedArray hMipmappedArray)
{
  static CUresult (*cuMipmappedArrayDestroy_orig)(CUmipmappedArray) = NULL;
  if (!cuMipmappedArrayDestroy_orig)
  {
    cuMipmappedArrayDestroy_orig = dlsym(orig_handle, "cuMipmappedArrayDestroy");
  }

  return cuMipmappedArrayDestroy_orig(hMipmappedArray);
}


CUresult cuPointerGetAttribute(void *data, CUpointer_attribute attribute, CUdeviceptr ptr)
{
  static CUresult (*cuPointerGetAttribute_orig)(void *, CUpointer_attribute, CUdeviceptr) = NULL;
  if (!cuPointerGetAttribute_orig)
  {
    cuPointerGetAttribute_orig = dlsym(orig_handle, "cuPointerGetAttribute");
  }

  return cuPointerGetAttribute_orig(data, attribute, ptr);
}


CUresult cuMemPrefetchAsync(CUdeviceptr devPtr, size_t count, CUdevice dstDevice, CUstream hStream)
{
  static CUresult (*cuMemPrefetchAsync_orig)(CUdeviceptr, size_t, CUdevice, CUstream) = NULL;
  if (!cuMemPrefetchAsync_orig)
  {
    cuMemPrefetchAsync_orig = dlsym(orig_handle, "cuMemPrefetchAsync");
  }

  return cuMemPrefetchAsync_orig(devPtr, count, dstDevice, hStream);
}


CUresult cuMemAdvise(CUdeviceptr devPtr, size_t count, CUmem_advise advice, CUdevice device)
{
  static CUresult (*cuMemAdvise_orig)(CUdeviceptr, size_t, CUmem_advise, CUdevice) = NULL;
  if (!cuMemAdvise_orig)
  {
    cuMemAdvise_orig = dlsym(orig_handle, "cuMemAdvise");
  }

  return cuMemAdvise_orig(devPtr, count, advice, device);
}


CUresult cuMemRangeGetAttribute(void *data, size_t dataSize, CUmem_range_attribute attribute, CUdeviceptr devPtr, size_t count)
{
  static CUresult (*cuMemRangeGetAttribute_orig)(void *, size_t, CUmem_range_attribute, CUdeviceptr, size_t) = NULL;
  if (!cuMemRangeGetAttribute_orig)
  {
    cuMemRangeGetAttribute_orig = dlsym(orig_handle, "cuMemRangeGetAttribute");
  }

  return cuMemRangeGetAttribute_orig(data, dataSize, attribute, devPtr, count);
}


CUresult cuMemRangeGetAttributes(void **data, size_t *dataSizes, CUmem_range_attribute *attributes, size_t numAttributes, CUdeviceptr devPtr, size_t count)
{
  static CUresult (*cuMemRangeGetAttributes_orig)(void **, size_t *, CUmem_range_attribute *, size_t, CUdeviceptr, size_t) = NULL;
  if (!cuMemRangeGetAttributes_orig)
  {
    cuMemRangeGetAttributes_orig = dlsym(orig_handle, "cuMemRangeGetAttributes");
  }

  return cuMemRangeGetAttributes_orig(data, dataSizes, attributes, numAttributes, devPtr, count);
}


CUresult cuPointerSetAttribute(const void *value, CUpointer_attribute attribute, CUdeviceptr ptr)
{
  static CUresult (*cuPointerSetAttribute_orig)(const void *, CUpointer_attribute, CUdeviceptr) = NULL;
  if (!cuPointerSetAttribute_orig)
  {
    cuPointerSetAttribute_orig = dlsym(orig_handle, "cuPointerSetAttribute");
  }

  return cuPointerSetAttribute_orig(value, attribute, ptr);
}


CUresult cuPointerGetAttributes(unsigned int numAttributes, CUpointer_attribute *attributes, void **data, CUdeviceptr ptr)
{
  static CUresult (*cuPointerGetAttributes_orig)(unsigned int, CUpointer_attribute *, void **, CUdeviceptr) = NULL;
  if (!cuPointerGetAttributes_orig)
  {
    cuPointerGetAttributes_orig = dlsym(orig_handle, "cuPointerGetAttributes");
  }

  return cuPointerGetAttributes_orig(numAttributes, attributes, data, ptr);
}


CUresult cuStreamCreate(CUstream *phStream, unsigned int Flags)
{
  static CUresult (*cuStreamCreate_orig)(CUstream *, unsigned int) = NULL;
  if (!cuStreamCreate_orig)
  {
    cuStreamCreate_orig = dlsym(orig_handle, "cuStreamCreate");
  }

  return cuStreamCreate_orig(phStream, Flags);
}


CUresult cuStreamCreateWithPriority(CUstream *phStream, unsigned int flags, int priority)
{
  static CUresult (*cuStreamCreateWithPriority_orig)(CUstream *, unsigned int, int) = NULL;
  if (!cuStreamCreateWithPriority_orig)
  {
    cuStreamCreateWithPriority_orig = dlsym(orig_handle, "cuStreamCreateWithPriority");
  }

  return cuStreamCreateWithPriority_orig(phStream, flags, priority);
}


CUresult cuStreamGetPriority(CUstream hStream, int *priority)
{
  static CUresult (*cuStreamGetPriority_orig)(CUstream, int *) = NULL;
  if (!cuStreamGetPriority_orig)
  {
    cuStreamGetPriority_orig = dlsym(orig_handle, "cuStreamGetPriority");
  }

  return cuStreamGetPriority_orig(hStream, priority);
}


CUresult cuStreamGetFlags(CUstream hStream, unsigned int *flags)
{
  static CUresult (*cuStreamGetFlags_orig)(CUstream, unsigned int *) = NULL;
  if (!cuStreamGetFlags_orig)
  {
    cuStreamGetFlags_orig = dlsym(orig_handle, "cuStreamGetFlags");
  }

  return cuStreamGetFlags_orig(hStream, flags);
}


CUresult cuStreamGetCtx(CUstream hStream, CUcontext *pctx)
{
  static CUresult (*cuStreamGetCtx_orig)(CUstream, CUcontext *) = NULL;
  if (!cuStreamGetCtx_orig)
  {
    cuStreamGetCtx_orig = dlsym(orig_handle, "cuStreamGetCtx");
  }

  return cuStreamGetCtx_orig(hStream, pctx);
}


CUresult cuStreamWaitEvent(CUstream hStream, CUevent hEvent, unsigned int Flags)
{
  static CUresult (*cuStreamWaitEvent_orig)(CUstream, CUevent, unsigned int) = NULL;
  if (!cuStreamWaitEvent_orig)
  {
    cuStreamWaitEvent_orig = dlsym(orig_handle, "cuStreamWaitEvent");
  }

  return cuStreamWaitEvent_orig(hStream, hEvent, Flags);
}


CUresult cuStreamAddCallback(CUstream hStream, CUstreamCallback callback, void *userData, unsigned int flags)
{
  static CUresult (*cuStreamAddCallback_orig)(CUstream, CUstreamCallback, void *, unsigned int) = NULL;
  if (!cuStreamAddCallback_orig)
  {
    cuStreamAddCallback_orig = dlsym(orig_handle, "cuStreamAddCallback");
  }

  return cuStreamAddCallback_orig(hStream, callback, userData, flags);
}


CUresult cuStreamBeginCapture_v2(CUstream hStream, CUstreamCaptureMode mode)
{
  static CUresult (*cuStreamBeginCapture_v2_orig)(CUstream, CUstreamCaptureMode) = NULL;
  if (!cuStreamBeginCapture_v2_orig)
  {
    cuStreamBeginCapture_v2_orig = dlsym(orig_handle, "cuStreamBeginCapture_v2");
  }

  return cuStreamBeginCapture_v2_orig(hStream, mode);
}


CUresult cuThreadExchangeStreamCaptureMode(CUstreamCaptureMode *mode)
{
  static CUresult (*cuThreadExchangeStreamCaptureMode_orig)(CUstreamCaptureMode *) = NULL;
  if (!cuThreadExchangeStreamCaptureMode_orig)
  {
    cuThreadExchangeStreamCaptureMode_orig = dlsym(orig_handle, "cuThreadExchangeStreamCaptureMode");
  }

  return cuThreadExchangeStreamCaptureMode_orig(mode);
}


CUresult cuStreamEndCapture(CUstream hStream, CUgraph *phGraph)
{
  static CUresult (*cuStreamEndCapture_orig)(CUstream, CUgraph *) = NULL;
  if (!cuStreamEndCapture_orig)
  {
    cuStreamEndCapture_orig = dlsym(orig_handle, "cuStreamEndCapture");
  }

  return cuStreamEndCapture_orig(hStream, phGraph);
}


CUresult cuStreamIsCapturing(CUstream hStream, CUstreamCaptureStatus *captureStatus)
{
  static CUresult (*cuStreamIsCapturing_orig)(CUstream, CUstreamCaptureStatus *) = NULL;
  if (!cuStreamIsCapturing_orig)
  {
    cuStreamIsCapturing_orig = dlsym(orig_handle, "cuStreamIsCapturing");
  }

  return cuStreamIsCapturing_orig(hStream, captureStatus);
}


CUresult cuStreamGetCaptureInfo(CUstream hStream, CUstreamCaptureStatus *captureStatus, cuuint64_t *id)
{
  static CUresult (*cuStreamGetCaptureInfo_orig)(CUstream, CUstreamCaptureStatus *, cuuint64_t *) = NULL;
  if (!cuStreamGetCaptureInfo_orig)
  {
    cuStreamGetCaptureInfo_orig = dlsym(orig_handle, "cuStreamGetCaptureInfo");
  }

  return cuStreamGetCaptureInfo_orig(hStream, captureStatus, id);
}


CUresult cuStreamAttachMemAsync(CUstream hStream, CUdeviceptr dptr, size_t length, unsigned int flags)
{
  static CUresult (*cuStreamAttachMemAsync_orig)(CUstream, CUdeviceptr, size_t, unsigned int) = NULL;
  if (!cuStreamAttachMemAsync_orig)
  {
    cuStreamAttachMemAsync_orig = dlsym(orig_handle, "cuStreamAttachMemAsync");
  }

  return cuStreamAttachMemAsync_orig(hStream, dptr, length, flags);
}


CUresult cuStreamQuery(CUstream hStream)
{
  static CUresult (*cuStreamQuery_orig)(CUstream) = NULL;
  if (!cuStreamQuery_orig)
  {
    cuStreamQuery_orig = dlsym(orig_handle, "cuStreamQuery");
  }

  return cuStreamQuery_orig(hStream);
}


CUresult cuStreamSynchronize(CUstream hStream)
{
  static CUresult (*cuStreamSynchronize_orig)(CUstream) = NULL;
  if (!cuStreamSynchronize_orig)
  {
    cuStreamSynchronize_orig = dlsym(orig_handle, "cuStreamSynchronize");
  }

  return cuStreamSynchronize_orig(hStream);
}


CUresult cuStreamDestroy_v2(CUstream hStream)
{
  static CUresult (*cuStreamDestroy_v2_orig)(CUstream) = NULL;
  if (!cuStreamDestroy_v2_orig)
  {
    cuStreamDestroy_v2_orig = dlsym(orig_handle, "cuStreamDestroy_v2");
  }

  return cuStreamDestroy_v2_orig(hStream);
}


CUresult cuEventCreate(CUevent *phEvent, unsigned int Flags)
{
  static CUresult (*cuEventCreate_orig)(CUevent *, unsigned int) = NULL;
  if (!cuEventCreate_orig)
  {
    cuEventCreate_orig = dlsym(orig_handle, "cuEventCreate");
  }

  return cuEventCreate_orig(phEvent, Flags);
}


CUresult cuEventRecord(CUevent hEvent, CUstream hStream)
{
  static CUresult (*cuEventRecord_orig)(CUevent, CUstream) = NULL;
  if (!cuEventRecord_orig)
  {
    cuEventRecord_orig = dlsym(orig_handle, "cuEventRecord");
  }

  return cuEventRecord_orig(hEvent, hStream);
}


CUresult cuEventQuery(CUevent hEvent)
{
  static CUresult (*cuEventQuery_orig)(CUevent) = NULL;
  if (!cuEventQuery_orig)
  {
    cuEventQuery_orig = dlsym(orig_handle, "cuEventQuery");
  }

  return cuEventQuery_orig(hEvent);
}


CUresult cuEventSynchronize(CUevent hEvent)
{
  static CUresult (*cuEventSynchronize_orig)(CUevent) = NULL;
  if (!cuEventSynchronize_orig)
  {
    cuEventSynchronize_orig = dlsym(orig_handle, "cuEventSynchronize");
  }

  return cuEventSynchronize_orig(hEvent);
}


CUresult cuEventDestroy_v2(CUevent hEvent)
{
  static CUresult (*cuEventDestroy_v2_orig)(CUevent) = NULL;
  if (!cuEventDestroy_v2_orig)
  {
    cuEventDestroy_v2_orig = dlsym(orig_handle, "cuEventDestroy_v2");
  }

  return cuEventDestroy_v2_orig(hEvent);
}


CUresult cuEventElapsedTime(float *pMilliseconds, CUevent hStart, CUevent hEnd)
{
  static CUresult (*cuEventElapsedTime_orig)(float *, CUevent, CUevent) = NULL;
  if (!cuEventElapsedTime_orig)
  {
    cuEventElapsedTime_orig = dlsym(orig_handle, "cuEventElapsedTime");
  }

  return cuEventElapsedTime_orig(pMilliseconds, hStart, hEnd);
}


CUresult cuImportExternalMemory(CUexternalMemory *extMem_out, const CUDA_EXTERNAL_MEMORY_HANDLE_DESC *memHandleDesc)
{
  static CUresult (*cuImportExternalMemory_orig)(CUexternalMemory *, const CUDA_EXTERNAL_MEMORY_HANDLE_DESC *) = NULL;
  if (!cuImportExternalMemory_orig)
  {
    cuImportExternalMemory_orig = dlsym(orig_handle, "cuImportExternalMemory");
  }

  return cuImportExternalMemory_orig(extMem_out, memHandleDesc);
}


CUresult cuExternalMemoryGetMappedBuffer(CUdeviceptr *devPtr, CUexternalMemory extMem, const CUDA_EXTERNAL_MEMORY_BUFFER_DESC *bufferDesc)
{
  static CUresult (*cuExternalMemoryGetMappedBuffer_orig)(CUdeviceptr *, CUexternalMemory, const CUDA_EXTERNAL_MEMORY_BUFFER_DESC *) = NULL;
  if (!cuExternalMemoryGetMappedBuffer_orig)
  {
    cuExternalMemoryGetMappedBuffer_orig = dlsym(orig_handle, "cuExternalMemoryGetMappedBuffer");
  }

  return cuExternalMemoryGetMappedBuffer_orig(devPtr, extMem, bufferDesc);
}


CUresult cuExternalMemoryGetMappedMipmappedArray(CUmipmappedArray *mipmap, CUexternalMemory extMem, const CUDA_EXTERNAL_MEMORY_MIPMAPPED_ARRAY_DESC *mipmapDesc)
{
  static CUresult (*cuExternalMemoryGetMappedMipmappedArray_orig)(CUmipmappedArray *, CUexternalMemory, const CUDA_EXTERNAL_MEMORY_MIPMAPPED_ARRAY_DESC *) = NULL;
  if (!cuExternalMemoryGetMappedMipmappedArray_orig)
  {
    cuExternalMemoryGetMappedMipmappedArray_orig = dlsym(orig_handle, "cuExternalMemoryGetMappedMipmappedArray");
  }

  return cuExternalMemoryGetMappedMipmappedArray_orig(mipmap, extMem, mipmapDesc);
}


CUresult cuDestroyExternalMemory(CUexternalMemory extMem)
{
  static CUresult (*cuDestroyExternalMemory_orig)(CUexternalMemory) = NULL;
  if (!cuDestroyExternalMemory_orig)
  {
    cuDestroyExternalMemory_orig = dlsym(orig_handle, "cuDestroyExternalMemory");
  }

  return cuDestroyExternalMemory_orig(extMem);
}


CUresult cuImportExternalSemaphore(CUexternalSemaphore *extSem_out, const CUDA_EXTERNAL_SEMAPHORE_HANDLE_DESC *semHandleDesc)
{
  static CUresult (*cuImportExternalSemaphore_orig)(CUexternalSemaphore *, const CUDA_EXTERNAL_SEMAPHORE_HANDLE_DESC *) = NULL;
  if (!cuImportExternalSemaphore_orig)
  {
    cuImportExternalSemaphore_orig = dlsym(orig_handle, "cuImportExternalSemaphore");
  }

  return cuImportExternalSemaphore_orig(extSem_out, semHandleDesc);
}


CUresult cuSignalExternalSemaphoresAsync(const CUexternalSemaphore *extSemArray, const CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS *paramsArray, unsigned int numExtSems, CUstream stream)
{
  static CUresult (*cuSignalExternalSemaphoresAsync_orig)(const CUexternalSemaphore *, const CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS *, unsigned int, CUstream) = NULL;
  if (!cuSignalExternalSemaphoresAsync_orig)
  {
    cuSignalExternalSemaphoresAsync_orig = dlsym(orig_handle, "cuSignalExternalSemaphoresAsync");
  }

  return cuSignalExternalSemaphoresAsync_orig(extSemArray, paramsArray, numExtSems, stream);
}


CUresult cuWaitExternalSemaphoresAsync(const CUexternalSemaphore *extSemArray, const CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS *paramsArray, unsigned int numExtSems, CUstream stream)
{
  static CUresult (*cuWaitExternalSemaphoresAsync_orig)(const CUexternalSemaphore *, const CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS *, unsigned int, CUstream) = NULL;
  if (!cuWaitExternalSemaphoresAsync_orig)
  {
    cuWaitExternalSemaphoresAsync_orig = dlsym(orig_handle, "cuWaitExternalSemaphoresAsync");
  }

  return cuWaitExternalSemaphoresAsync_orig(extSemArray, paramsArray, numExtSems, stream);
}


CUresult cuDestroyExternalSemaphore(CUexternalSemaphore extSem)
{
  static CUresult (*cuDestroyExternalSemaphore_orig)(CUexternalSemaphore) = NULL;
  if (!cuDestroyExternalSemaphore_orig)
  {
    cuDestroyExternalSemaphore_orig = dlsym(orig_handle, "cuDestroyExternalSemaphore");
  }

  return cuDestroyExternalSemaphore_orig(extSem);
}


CUresult cuStreamWaitValue32(CUstream stream, CUdeviceptr addr, cuuint32_t value, unsigned int flags)
{
  static CUresult (*cuStreamWaitValue32_orig)(CUstream, CUdeviceptr, cuuint32_t, unsigned int) = NULL;
  if (!cuStreamWaitValue32_orig)
  {
    cuStreamWaitValue32_orig = dlsym(orig_handle, "cuStreamWaitValue32");
  }

  return cuStreamWaitValue32_orig(stream, addr, value, flags);
}


CUresult cuStreamWaitValue64(CUstream stream, CUdeviceptr addr, cuuint64_t value, unsigned int flags)
{
  static CUresult (*cuStreamWaitValue64_orig)(CUstream, CUdeviceptr, cuuint64_t, unsigned int) = NULL;
  if (!cuStreamWaitValue64_orig)
  {
    cuStreamWaitValue64_orig = dlsym(orig_handle, "cuStreamWaitValue64");
  }

  return cuStreamWaitValue64_orig(stream, addr, value, flags);
}


CUresult cuStreamWriteValue32(CUstream stream, CUdeviceptr addr, cuuint32_t value, unsigned int flags)
{
  static CUresult (*cuStreamWriteValue32_orig)(CUstream, CUdeviceptr, cuuint32_t, unsigned int) = NULL;
  if (!cuStreamWriteValue32_orig)
  {
    cuStreamWriteValue32_orig = dlsym(orig_handle, "cuStreamWriteValue32");
  }

  return cuStreamWriteValue32_orig(stream, addr, value, flags);
}


CUresult cuStreamWriteValue64(CUstream stream, CUdeviceptr addr, cuuint64_t value, unsigned int flags)
{
  static CUresult (*cuStreamWriteValue64_orig)(CUstream, CUdeviceptr, cuuint64_t, unsigned int) = NULL;
  if (!cuStreamWriteValue64_orig)
  {
    cuStreamWriteValue64_orig = dlsym(orig_handle, "cuStreamWriteValue64");
  }

  return cuStreamWriteValue64_orig(stream, addr, value, flags);
}


CUresult cuStreamBatchMemOp(CUstream stream, unsigned int count, CUstreamBatchMemOpParams *paramArray, unsigned int flags)
{
  static CUresult (*cuStreamBatchMemOp_orig)(CUstream, unsigned int, CUstreamBatchMemOpParams *, unsigned int) = NULL;
  if (!cuStreamBatchMemOp_orig)
  {
    cuStreamBatchMemOp_orig = dlsym(orig_handle, "cuStreamBatchMemOp");
  }

  return cuStreamBatchMemOp_orig(stream, count, paramArray, flags);
}


CUresult cuFuncGetAttribute(int *pi, CUfunction_attribute attrib, CUfunction hfunc)
{
  static CUresult (*cuFuncGetAttribute_orig)(int *, CUfunction_attribute, CUfunction) = NULL;
  if (!cuFuncGetAttribute_orig)
  {
    cuFuncGetAttribute_orig = dlsym(orig_handle, "cuFuncGetAttribute");
  }

  return cuFuncGetAttribute_orig(pi, attrib, hfunc);
}


CUresult cuFuncSetAttribute(CUfunction hfunc, CUfunction_attribute attrib, int value)
{
  static CUresult (*cuFuncSetAttribute_orig)(CUfunction, CUfunction_attribute, int) = NULL;
  if (!cuFuncSetAttribute_orig)
  {
    cuFuncSetAttribute_orig = dlsym(orig_handle, "cuFuncSetAttribute");
  }

  return cuFuncSetAttribute_orig(hfunc, attrib, value);
}


CUresult cuFuncSetCacheConfig(CUfunction hfunc, CUfunc_cache config)
{
  static CUresult (*cuFuncSetCacheConfig_orig)(CUfunction, CUfunc_cache) = NULL;
  if (!cuFuncSetCacheConfig_orig)
  {
    cuFuncSetCacheConfig_orig = dlsym(orig_handle, "cuFuncSetCacheConfig");
  }

  return cuFuncSetCacheConfig_orig(hfunc, config);
}


CUresult cuFuncSetSharedMemConfig(CUfunction hfunc, CUsharedconfig config)
{
  static CUresult (*cuFuncSetSharedMemConfig_orig)(CUfunction, CUsharedconfig) = NULL;
  if (!cuFuncSetSharedMemConfig_orig)
  {
    cuFuncSetSharedMemConfig_orig = dlsym(orig_handle, "cuFuncSetSharedMemConfig");
  }

  return cuFuncSetSharedMemConfig_orig(hfunc, config);
}


CUresult cuLaunchKernel(CUfunction f, unsigned int gridDimX, unsigned int gridDimY, unsigned int gridDimZ, unsigned int blockDimX, unsigned int blockDimY, unsigned int blockDimZ, unsigned int sharedMemBytes, CUstream hStream, void **kernelParams, void **extra)
{
  static CUresult (*cuLaunchKernel_orig)(CUfunction, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, CUstream, void **, void **) = NULL;
  if (!cuLaunchKernel_orig)
  {
    cuLaunchKernel_orig = dlsym(orig_handle, "cuLaunchKernel");
  }

  return cuLaunchKernel_orig(f, gridDimX, gridDimY, gridDimZ, blockDimX, blockDimY, blockDimZ, sharedMemBytes, hStream, kernelParams, extra);
}


CUresult cuLaunchCooperativeKernel(CUfunction f, unsigned int gridDimX, unsigned int gridDimY, unsigned int gridDimZ, unsigned int blockDimX, unsigned int blockDimY, unsigned int blockDimZ, unsigned int sharedMemBytes, CUstream hStream, void **kernelParams)
{
  static CUresult (*cuLaunchCooperativeKernel_orig)(CUfunction, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, CUstream, void **) = NULL;
  if (!cuLaunchCooperativeKernel_orig)
  {
    cuLaunchCooperativeKernel_orig = dlsym(orig_handle, "cuLaunchCooperativeKernel");
  }

  return cuLaunchCooperativeKernel_orig(f, gridDimX, gridDimY, gridDimZ, blockDimX, blockDimY, blockDimZ, sharedMemBytes, hStream, kernelParams);
}


CUresult cuLaunchCooperativeKernelMultiDevice(CUDA_LAUNCH_PARAMS *launchParamsList, unsigned int numDevices, unsigned int flags)
{
  static CUresult (*cuLaunchCooperativeKernelMultiDevice_orig)(CUDA_LAUNCH_PARAMS *, unsigned int, unsigned int) = NULL;
  if (!cuLaunchCooperativeKernelMultiDevice_orig)
  {
    cuLaunchCooperativeKernelMultiDevice_orig = dlsym(orig_handle, "cuLaunchCooperativeKernelMultiDevice");
  }

  return cuLaunchCooperativeKernelMultiDevice_orig(launchParamsList, numDevices, flags);
}


CUresult cuLaunchHostFunc(CUstream hStream, CUhostFn fn, void *userData)
{
  static CUresult (*cuLaunchHostFunc_orig)(CUstream, CUhostFn, void *) = NULL;
  if (!cuLaunchHostFunc_orig)
  {
    cuLaunchHostFunc_orig = dlsym(orig_handle, "cuLaunchHostFunc");
  }

  return cuLaunchHostFunc_orig(hStream, fn, userData);
}


CUresult cuFuncSetBlockShape(CUfunction hfunc, int x, int y, int z)
{
  static CUresult (*cuFuncSetBlockShape_orig)(CUfunction, int, int, int) = NULL;
  if (!cuFuncSetBlockShape_orig)
  {
    cuFuncSetBlockShape_orig = dlsym(orig_handle, "cuFuncSetBlockShape");
  }

  return cuFuncSetBlockShape_orig(hfunc, x, y, z);
}


CUresult cuFuncSetSharedSize(CUfunction hfunc, unsigned int bytes)
{
  static CUresult (*cuFuncSetSharedSize_orig)(CUfunction, unsigned int) = NULL;
  if (!cuFuncSetSharedSize_orig)
  {
    cuFuncSetSharedSize_orig = dlsym(orig_handle, "cuFuncSetSharedSize");
  }

  return cuFuncSetSharedSize_orig(hfunc, bytes);
}


CUresult cuParamSetSize(CUfunction hfunc, unsigned int numbytes)
{
  static CUresult (*cuParamSetSize_orig)(CUfunction, unsigned int) = NULL;
  if (!cuParamSetSize_orig)
  {
    cuParamSetSize_orig = dlsym(orig_handle, "cuParamSetSize");
  }

  return cuParamSetSize_orig(hfunc, numbytes);
}


CUresult cuParamSeti(CUfunction hfunc, int offset, unsigned int value)
{
  static CUresult (*cuParamSeti_orig)(CUfunction, int, unsigned int) = NULL;
  if (!cuParamSeti_orig)
  {
    cuParamSeti_orig = dlsym(orig_handle, "cuParamSeti");
  }

  return cuParamSeti_orig(hfunc, offset, value);
}


CUresult cuParamSetf(CUfunction hfunc, int offset, float value)
{
  static CUresult (*cuParamSetf_orig)(CUfunction, int, float) = NULL;
  if (!cuParamSetf_orig)
  {
    cuParamSetf_orig = dlsym(orig_handle, "cuParamSetf");
  }

  return cuParamSetf_orig(hfunc, offset, value);
}


CUresult cuParamSetv(CUfunction hfunc, int offset, void *ptr, unsigned int numbytes)
{
  static CUresult (*cuParamSetv_orig)(CUfunction, int, void *, unsigned int) = NULL;
  if (!cuParamSetv_orig)
  {
    cuParamSetv_orig = dlsym(orig_handle, "cuParamSetv");
  }

  return cuParamSetv_orig(hfunc, offset, ptr, numbytes);
}


CUresult cuLaunch(CUfunction f)
{
  static CUresult (*cuLaunch_orig)(CUfunction) = NULL;
  if (!cuLaunch_orig)
  {
    cuLaunch_orig = dlsym(orig_handle, "cuLaunch");
  }

  return cuLaunch_orig(f);
}


CUresult cuLaunchGrid(CUfunction f, int grid_width, int grid_height)
{
  static CUresult (*cuLaunchGrid_orig)(CUfunction, int, int) = NULL;
  if (!cuLaunchGrid_orig)
  {
    cuLaunchGrid_orig = dlsym(orig_handle, "cuLaunchGrid");
  }

  return cuLaunchGrid_orig(f, grid_width, grid_height);
}


CUresult cuLaunchGridAsync(CUfunction f, int grid_width, int grid_height, CUstream hStream)
{
  static CUresult (*cuLaunchGridAsync_orig)(CUfunction, int, int, CUstream) = NULL;
  if (!cuLaunchGridAsync_orig)
  {
    cuLaunchGridAsync_orig = dlsym(orig_handle, "cuLaunchGridAsync");
  }

  return cuLaunchGridAsync_orig(f, grid_width, grid_height, hStream);
}


CUresult cuParamSetTexRef(CUfunction hfunc, int texunit, CUtexref hTexRef)
{
  static CUresult (*cuParamSetTexRef_orig)(CUfunction, int, CUtexref) = NULL;
  if (!cuParamSetTexRef_orig)
  {
    cuParamSetTexRef_orig = dlsym(orig_handle, "cuParamSetTexRef");
  }

  return cuParamSetTexRef_orig(hfunc, texunit, hTexRef);
}


CUresult cuGraphCreate(CUgraph *phGraph, unsigned int flags)
{
  static CUresult (*cuGraphCreate_orig)(CUgraph *, unsigned int) = NULL;
  if (!cuGraphCreate_orig)
  {
    cuGraphCreate_orig = dlsym(orig_handle, "cuGraphCreate");
  }

  return cuGraphCreate_orig(phGraph, flags);
}


CUresult cuGraphAddKernelNode(CUgraphNode *phGraphNode, CUgraph hGraph, const CUgraphNode *dependencies, size_t numDependencies, const CUDA_KERNEL_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphAddKernelNode_orig)(CUgraphNode *, CUgraph, const CUgraphNode *, size_t, const CUDA_KERNEL_NODE_PARAMS *) = NULL;
  if (!cuGraphAddKernelNode_orig)
  {
    cuGraphAddKernelNode_orig = dlsym(orig_handle, "cuGraphAddKernelNode");
  }

  return cuGraphAddKernelNode_orig(phGraphNode, hGraph, dependencies, numDependencies, nodeParams);
}


CUresult cuGraphKernelNodeGetParams(CUgraphNode hNode, CUDA_KERNEL_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphKernelNodeGetParams_orig)(CUgraphNode, CUDA_KERNEL_NODE_PARAMS *) = NULL;
  if (!cuGraphKernelNodeGetParams_orig)
  {
    cuGraphKernelNodeGetParams_orig = dlsym(orig_handle, "cuGraphKernelNodeGetParams");
  }

  return cuGraphKernelNodeGetParams_orig(hNode, nodeParams);
}


CUresult cuGraphKernelNodeSetParams(CUgraphNode hNode, const CUDA_KERNEL_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphKernelNodeSetParams_orig)(CUgraphNode, const CUDA_KERNEL_NODE_PARAMS *) = NULL;
  if (!cuGraphKernelNodeSetParams_orig)
  {
    cuGraphKernelNodeSetParams_orig = dlsym(orig_handle, "cuGraphKernelNodeSetParams");
  }

  return cuGraphKernelNodeSetParams_orig(hNode, nodeParams);
}


CUresult cuGraphAddMemcpyNode(CUgraphNode *phGraphNode, CUgraph hGraph, const CUgraphNode *dependencies, size_t numDependencies, const CUDA_MEMCPY3D *copyParams, CUcontext ctx)
{
  static CUresult (*cuGraphAddMemcpyNode_orig)(CUgraphNode *, CUgraph, const CUgraphNode *, size_t, const CUDA_MEMCPY3D *, CUcontext) = NULL;
  if (!cuGraphAddMemcpyNode_orig)
  {
    cuGraphAddMemcpyNode_orig = dlsym(orig_handle, "cuGraphAddMemcpyNode");
  }

  return cuGraphAddMemcpyNode_orig(phGraphNode, hGraph, dependencies, numDependencies, copyParams, ctx);
}


CUresult cuGraphMemcpyNodeGetParams(CUgraphNode hNode, CUDA_MEMCPY3D *nodeParams)
{
  static CUresult (*cuGraphMemcpyNodeGetParams_orig)(CUgraphNode, CUDA_MEMCPY3D *) = NULL;
  if (!cuGraphMemcpyNodeGetParams_orig)
  {
    cuGraphMemcpyNodeGetParams_orig = dlsym(orig_handle, "cuGraphMemcpyNodeGetParams");
  }

  return cuGraphMemcpyNodeGetParams_orig(hNode, nodeParams);
}


CUresult cuGraphMemcpyNodeSetParams(CUgraphNode hNode, const CUDA_MEMCPY3D *nodeParams)
{
  static CUresult (*cuGraphMemcpyNodeSetParams_orig)(CUgraphNode, const CUDA_MEMCPY3D *) = NULL;
  if (!cuGraphMemcpyNodeSetParams_orig)
  {
    cuGraphMemcpyNodeSetParams_orig = dlsym(orig_handle, "cuGraphMemcpyNodeSetParams");
  }

  return cuGraphMemcpyNodeSetParams_orig(hNode, nodeParams);
}


CUresult cuGraphAddMemsetNode(CUgraphNode *phGraphNode, CUgraph hGraph, const CUgraphNode *dependencies, size_t numDependencies, const CUDA_MEMSET_NODE_PARAMS *memsetParams, CUcontext ctx)
{
  static CUresult (*cuGraphAddMemsetNode_orig)(CUgraphNode *, CUgraph, const CUgraphNode *, size_t, const CUDA_MEMSET_NODE_PARAMS *, CUcontext) = NULL;
  if (!cuGraphAddMemsetNode_orig)
  {
    cuGraphAddMemsetNode_orig = dlsym(orig_handle, "cuGraphAddMemsetNode");
  }

  return cuGraphAddMemsetNode_orig(phGraphNode, hGraph, dependencies, numDependencies, memsetParams, ctx);
}


CUresult cuGraphMemsetNodeGetParams(CUgraphNode hNode, CUDA_MEMSET_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphMemsetNodeGetParams_orig)(CUgraphNode, CUDA_MEMSET_NODE_PARAMS *) = NULL;
  if (!cuGraphMemsetNodeGetParams_orig)
  {
    cuGraphMemsetNodeGetParams_orig = dlsym(orig_handle, "cuGraphMemsetNodeGetParams");
  }

  return cuGraphMemsetNodeGetParams_orig(hNode, nodeParams);
}


CUresult cuGraphMemsetNodeSetParams(CUgraphNode hNode, const CUDA_MEMSET_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphMemsetNodeSetParams_orig)(CUgraphNode, const CUDA_MEMSET_NODE_PARAMS *) = NULL;
  if (!cuGraphMemsetNodeSetParams_orig)
  {
    cuGraphMemsetNodeSetParams_orig = dlsym(orig_handle, "cuGraphMemsetNodeSetParams");
  }

  return cuGraphMemsetNodeSetParams_orig(hNode, nodeParams);
}


CUresult cuGraphAddHostNode(CUgraphNode *phGraphNode, CUgraph hGraph, const CUgraphNode *dependencies, size_t numDependencies, const CUDA_HOST_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphAddHostNode_orig)(CUgraphNode *, CUgraph, const CUgraphNode *, size_t, const CUDA_HOST_NODE_PARAMS *) = NULL;
  if (!cuGraphAddHostNode_orig)
  {
    cuGraphAddHostNode_orig = dlsym(orig_handle, "cuGraphAddHostNode");
  }

  return cuGraphAddHostNode_orig(phGraphNode, hGraph, dependencies, numDependencies, nodeParams);
}


CUresult cuGraphHostNodeGetParams(CUgraphNode hNode, CUDA_HOST_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphHostNodeGetParams_orig)(CUgraphNode, CUDA_HOST_NODE_PARAMS *) = NULL;
  if (!cuGraphHostNodeGetParams_orig)
  {
    cuGraphHostNodeGetParams_orig = dlsym(orig_handle, "cuGraphHostNodeGetParams");
  }

  return cuGraphHostNodeGetParams_orig(hNode, nodeParams);
}


CUresult cuGraphHostNodeSetParams(CUgraphNode hNode, const CUDA_HOST_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphHostNodeSetParams_orig)(CUgraphNode, const CUDA_HOST_NODE_PARAMS *) = NULL;
  if (!cuGraphHostNodeSetParams_orig)
  {
    cuGraphHostNodeSetParams_orig = dlsym(orig_handle, "cuGraphHostNodeSetParams");
  }

  return cuGraphHostNodeSetParams_orig(hNode, nodeParams);
}


CUresult cuGraphAddChildGraphNode(CUgraphNode *phGraphNode, CUgraph hGraph, const CUgraphNode *dependencies, size_t numDependencies, CUgraph childGraph)
{
  static CUresult (*cuGraphAddChildGraphNode_orig)(CUgraphNode *, CUgraph, const CUgraphNode *, size_t, CUgraph) = NULL;
  if (!cuGraphAddChildGraphNode_orig)
  {
    cuGraphAddChildGraphNode_orig = dlsym(orig_handle, "cuGraphAddChildGraphNode");
  }

  return cuGraphAddChildGraphNode_orig(phGraphNode, hGraph, dependencies, numDependencies, childGraph);
}


CUresult cuGraphChildGraphNodeGetGraph(CUgraphNode hNode, CUgraph *phGraph)
{
  static CUresult (*cuGraphChildGraphNodeGetGraph_orig)(CUgraphNode, CUgraph *) = NULL;
  if (!cuGraphChildGraphNodeGetGraph_orig)
  {
    cuGraphChildGraphNodeGetGraph_orig = dlsym(orig_handle, "cuGraphChildGraphNodeGetGraph");
  }

  return cuGraphChildGraphNodeGetGraph_orig(hNode, phGraph);
}


CUresult cuGraphAddEmptyNode(CUgraphNode *phGraphNode, CUgraph hGraph, const CUgraphNode *dependencies, size_t numDependencies)
{
  static CUresult (*cuGraphAddEmptyNode_orig)(CUgraphNode *, CUgraph, const CUgraphNode *, size_t) = NULL;
  if (!cuGraphAddEmptyNode_orig)
  {
    cuGraphAddEmptyNode_orig = dlsym(orig_handle, "cuGraphAddEmptyNode");
  }

  return cuGraphAddEmptyNode_orig(phGraphNode, hGraph, dependencies, numDependencies);
}


CUresult cuGraphClone(CUgraph *phGraphClone, CUgraph originalGraph)
{
  static CUresult (*cuGraphClone_orig)(CUgraph *, CUgraph) = NULL;
  if (!cuGraphClone_orig)
  {
    cuGraphClone_orig = dlsym(orig_handle, "cuGraphClone");
  }

  return cuGraphClone_orig(phGraphClone, originalGraph);
}


CUresult cuGraphNodeFindInClone(CUgraphNode *phNode, CUgraphNode hOriginalNode, CUgraph hClonedGraph)
{
  static CUresult (*cuGraphNodeFindInClone_orig)(CUgraphNode *, CUgraphNode, CUgraph) = NULL;
  if (!cuGraphNodeFindInClone_orig)
  {
    cuGraphNodeFindInClone_orig = dlsym(orig_handle, "cuGraphNodeFindInClone");
  }

  return cuGraphNodeFindInClone_orig(phNode, hOriginalNode, hClonedGraph);
}


CUresult cuGraphNodeGetType(CUgraphNode hNode, CUgraphNodeType *type)
{
  static CUresult (*cuGraphNodeGetType_orig)(CUgraphNode, CUgraphNodeType *) = NULL;
  if (!cuGraphNodeGetType_orig)
  {
    cuGraphNodeGetType_orig = dlsym(orig_handle, "cuGraphNodeGetType");
  }

  return cuGraphNodeGetType_orig(hNode, type);
}


CUresult cuGraphGetNodes(CUgraph hGraph, CUgraphNode *nodes, size_t *numNodes)
{
  static CUresult (*cuGraphGetNodes_orig)(CUgraph, CUgraphNode *, size_t *) = NULL;
  if (!cuGraphGetNodes_orig)
  {
    cuGraphGetNodes_orig = dlsym(orig_handle, "cuGraphGetNodes");
  }

  return cuGraphGetNodes_orig(hGraph, nodes, numNodes);
}


CUresult cuGraphGetRootNodes(CUgraph hGraph, CUgraphNode *rootNodes, size_t *numRootNodes)
{
  static CUresult (*cuGraphGetRootNodes_orig)(CUgraph, CUgraphNode *, size_t *) = NULL;
  if (!cuGraphGetRootNodes_orig)
  {
    cuGraphGetRootNodes_orig = dlsym(orig_handle, "cuGraphGetRootNodes");
  }

  return cuGraphGetRootNodes_orig(hGraph, rootNodes, numRootNodes);
}


CUresult cuGraphGetEdges(CUgraph hGraph, CUgraphNode *from, CUgraphNode *to, size_t *numEdges)
{
  static CUresult (*cuGraphGetEdges_orig)(CUgraph, CUgraphNode *, CUgraphNode *, size_t *) = NULL;
  if (!cuGraphGetEdges_orig)
  {
    cuGraphGetEdges_orig = dlsym(orig_handle, "cuGraphGetEdges");
  }

  return cuGraphGetEdges_orig(hGraph, from, to, numEdges);
}


CUresult cuGraphNodeGetDependencies(CUgraphNode hNode, CUgraphNode *dependencies, size_t *numDependencies)
{
  static CUresult (*cuGraphNodeGetDependencies_orig)(CUgraphNode, CUgraphNode *, size_t *) = NULL;
  if (!cuGraphNodeGetDependencies_orig)
  {
    cuGraphNodeGetDependencies_orig = dlsym(orig_handle, "cuGraphNodeGetDependencies");
  }

  return cuGraphNodeGetDependencies_orig(hNode, dependencies, numDependencies);
}


CUresult cuGraphNodeGetDependentNodes(CUgraphNode hNode, CUgraphNode *dependentNodes, size_t *numDependentNodes)
{
  static CUresult (*cuGraphNodeGetDependentNodes_orig)(CUgraphNode, CUgraphNode *, size_t *) = NULL;
  if (!cuGraphNodeGetDependentNodes_orig)
  {
    cuGraphNodeGetDependentNodes_orig = dlsym(orig_handle, "cuGraphNodeGetDependentNodes");
  }

  return cuGraphNodeGetDependentNodes_orig(hNode, dependentNodes, numDependentNodes);
}


CUresult cuGraphAddDependencies(CUgraph hGraph, const CUgraphNode *from, const CUgraphNode *to, size_t numDependencies)
{
  static CUresult (*cuGraphAddDependencies_orig)(CUgraph, const CUgraphNode *, const CUgraphNode *, size_t) = NULL;
  if (!cuGraphAddDependencies_orig)
  {
    cuGraphAddDependencies_orig = dlsym(orig_handle, "cuGraphAddDependencies");
  }

  return cuGraphAddDependencies_orig(hGraph, from, to, numDependencies);
}


CUresult cuGraphRemoveDependencies(CUgraph hGraph, const CUgraphNode *from, const CUgraphNode *to, size_t numDependencies)
{
  static CUresult (*cuGraphRemoveDependencies_orig)(CUgraph, const CUgraphNode *, const CUgraphNode *, size_t) = NULL;
  if (!cuGraphRemoveDependencies_orig)
  {
    cuGraphRemoveDependencies_orig = dlsym(orig_handle, "cuGraphRemoveDependencies");
  }

  return cuGraphRemoveDependencies_orig(hGraph, from, to, numDependencies);
}


CUresult cuGraphDestroyNode(CUgraphNode hNode)
{
  static CUresult (*cuGraphDestroyNode_orig)(CUgraphNode) = NULL;
  if (!cuGraphDestroyNode_orig)
  {
    cuGraphDestroyNode_orig = dlsym(orig_handle, "cuGraphDestroyNode");
  }

  return cuGraphDestroyNode_orig(hNode);
}


CUresult cuGraphInstantiate(CUgraphExec *phGraphExec, CUgraph hGraph, CUgraphNode *phErrorNode, char *logBuffer, size_t bufferSize)
{
  static CUresult (*cuGraphInstantiate_orig)(CUgraphExec *, CUgraph, CUgraphNode *, char *, size_t) = NULL;
  if (!cuGraphInstantiate_orig)
  {
    cuGraphInstantiate_orig = dlsym(orig_handle, "cuGraphInstantiate");
  }

  return cuGraphInstantiate_orig(phGraphExec, hGraph, phErrorNode, logBuffer, bufferSize);
}


CUresult cuGraphExecKernelNodeSetParams(CUgraphExec hGraphExec, CUgraphNode hNode, const CUDA_KERNEL_NODE_PARAMS *nodeParams)
{
  static CUresult (*cuGraphExecKernelNodeSetParams_orig)(CUgraphExec, CUgraphNode, const CUDA_KERNEL_NODE_PARAMS *) = NULL;
  if (!cuGraphExecKernelNodeSetParams_orig)
  {
    cuGraphExecKernelNodeSetParams_orig = dlsym(orig_handle, "cuGraphExecKernelNodeSetParams");
  }

  return cuGraphExecKernelNodeSetParams_orig(hGraphExec, hNode, nodeParams);
}


CUresult cuGraphLaunch(CUgraphExec hGraphExec, CUstream hStream)
{
  static CUresult (*cuGraphLaunch_orig)(CUgraphExec, CUstream) = NULL;
  if (!cuGraphLaunch_orig)
  {
    cuGraphLaunch_orig = dlsym(orig_handle, "cuGraphLaunch");
  }

  return cuGraphLaunch_orig(hGraphExec, hStream);
}


CUresult cuGraphExecDestroy(CUgraphExec hGraphExec)
{
  static CUresult (*cuGraphExecDestroy_orig)(CUgraphExec) = NULL;
  if (!cuGraphExecDestroy_orig)
  {
    cuGraphExecDestroy_orig = dlsym(orig_handle, "cuGraphExecDestroy");
  }

  return cuGraphExecDestroy_orig(hGraphExec);
}


CUresult cuGraphDestroy(CUgraph hGraph)
{
  static CUresult (*cuGraphDestroy_orig)(CUgraph) = NULL;
  if (!cuGraphDestroy_orig)
  {
    cuGraphDestroy_orig = dlsym(orig_handle, "cuGraphDestroy");
  }

  return cuGraphDestroy_orig(hGraph);
}


CUresult cuOccupancyMaxActiveBlocksPerMultiprocessor(int *numBlocks, CUfunction func, int blockSize, size_t dynamicSMemSize)
{
  static CUresult (*cuOccupancyMaxActiveBlocksPerMultiprocessor_orig)(int *, CUfunction, int, size_t) = NULL;
  if (!cuOccupancyMaxActiveBlocksPerMultiprocessor_orig)
  {
    cuOccupancyMaxActiveBlocksPerMultiprocessor_orig = dlsym(orig_handle, "cuOccupancyMaxActiveBlocksPerMultiprocessor");
  }

  return cuOccupancyMaxActiveBlocksPerMultiprocessor_orig(numBlocks, func, blockSize, dynamicSMemSize);
}


CUresult cuOccupancyMaxActiveBlocksPerMultiprocessorWithFlags(int *numBlocks, CUfunction func, int blockSize, size_t dynamicSMemSize, unsigned int flags)
{
  static CUresult (*cuOccupancyMaxActiveBlocksPerMultiprocessorWithFlags_orig)(int *, CUfunction, int, size_t, unsigned int) = NULL;
  if (!cuOccupancyMaxActiveBlocksPerMultiprocessorWithFlags_orig)
  {
    cuOccupancyMaxActiveBlocksPerMultiprocessorWithFlags_orig = dlsym(orig_handle, "cuOccupancyMaxActiveBlocksPerMultiprocessorWithFlags");
  }

  return cuOccupancyMaxActiveBlocksPerMultiprocessorWithFlags_orig(numBlocks, func, blockSize, dynamicSMemSize, flags);
}


CUresult cuOccupancyMaxPotentialBlockSize(int *minGridSize, int *blockSize, CUfunction func, CUoccupancyB2DSize blockSizeToDynamicSMemSize, size_t dynamicSMemSize, int blockSizeLimit)
{
  static CUresult (*cuOccupancyMaxPotentialBlockSize_orig)(int *, int *, CUfunction, CUoccupancyB2DSize, size_t, int) = NULL;
  if (!cuOccupancyMaxPotentialBlockSize_orig)
  {
    cuOccupancyMaxPotentialBlockSize_orig = dlsym(orig_handle, "cuOccupancyMaxPotentialBlockSize");
  }

  return cuOccupancyMaxPotentialBlockSize_orig(minGridSize, blockSize, func, blockSizeToDynamicSMemSize, dynamicSMemSize, blockSizeLimit);
}


CUresult cuOccupancyMaxPotentialBlockSizeWithFlags(int *minGridSize, int *blockSize, CUfunction func, CUoccupancyB2DSize blockSizeToDynamicSMemSize, size_t dynamicSMemSize, int blockSizeLimit, unsigned int flags)
{
  static CUresult (*cuOccupancyMaxPotentialBlockSizeWithFlags_orig)(int *, int *, CUfunction, CUoccupancyB2DSize, size_t, int, unsigned int) = NULL;
  if (!cuOccupancyMaxPotentialBlockSizeWithFlags_orig)
  {
    cuOccupancyMaxPotentialBlockSizeWithFlags_orig = dlsym(orig_handle, "cuOccupancyMaxPotentialBlockSizeWithFlags");
  }

  return cuOccupancyMaxPotentialBlockSizeWithFlags_orig(minGridSize, blockSize, func, blockSizeToDynamicSMemSize, dynamicSMemSize, blockSizeLimit, flags);
}


CUresult cuTexRefSetArray(CUtexref hTexRef, CUarray hArray, unsigned int Flags)
{
  static CUresult (*cuTexRefSetArray_orig)(CUtexref, CUarray, unsigned int) = NULL;
  if (!cuTexRefSetArray_orig)
  {
    cuTexRefSetArray_orig = dlsym(orig_handle, "cuTexRefSetArray");
  }

  return cuTexRefSetArray_orig(hTexRef, hArray, Flags);
}


CUresult cuTexRefSetMipmappedArray(CUtexref hTexRef, CUmipmappedArray hMipmappedArray, unsigned int Flags)
{
  static CUresult (*cuTexRefSetMipmappedArray_orig)(CUtexref, CUmipmappedArray, unsigned int) = NULL;
  if (!cuTexRefSetMipmappedArray_orig)
  {
    cuTexRefSetMipmappedArray_orig = dlsym(orig_handle, "cuTexRefSetMipmappedArray");
  }

  return cuTexRefSetMipmappedArray_orig(hTexRef, hMipmappedArray, Flags);
}


CUresult cuTexRefSetAddress_v2(size_t *ByteOffset, CUtexref hTexRef, CUdeviceptr dptr, size_t bytes)
{
  static CUresult (*cuTexRefSetAddress_v2_orig)(size_t *, CUtexref, CUdeviceptr, size_t) = NULL;
  if (!cuTexRefSetAddress_v2_orig)
  {
    cuTexRefSetAddress_v2_orig = dlsym(orig_handle, "cuTexRefSetAddress_v2");
  }

  return cuTexRefSetAddress_v2_orig(ByteOffset, hTexRef, dptr, bytes);
}


CUresult cuTexRefSetAddress2D_v3(CUtexref hTexRef, const CUDA_ARRAY_DESCRIPTOR *desc, CUdeviceptr dptr, size_t Pitch)
{
  static CUresult (*cuTexRefSetAddress2D_v3_orig)(CUtexref, const CUDA_ARRAY_DESCRIPTOR *, CUdeviceptr, size_t) = NULL;
  if (!cuTexRefSetAddress2D_v3_orig)
  {
    cuTexRefSetAddress2D_v3_orig = dlsym(orig_handle, "cuTexRefSetAddress2D_v3");
  }

  return cuTexRefSetAddress2D_v3_orig(hTexRef, desc, dptr, Pitch);
}


CUresult cuTexRefSetFormat(CUtexref hTexRef, CUarray_format fmt, int NumPackedComponents)
{
  static CUresult (*cuTexRefSetFormat_orig)(CUtexref, CUarray_format, int) = NULL;
  if (!cuTexRefSetFormat_orig)
  {
    cuTexRefSetFormat_orig = dlsym(orig_handle, "cuTexRefSetFormat");
  }

  return cuTexRefSetFormat_orig(hTexRef, fmt, NumPackedComponents);
}


CUresult cuTexRefSetAddressMode(CUtexref hTexRef, int dim, CUaddress_mode am)
{
  static CUresult (*cuTexRefSetAddressMode_orig)(CUtexref, int, CUaddress_mode) = NULL;
  if (!cuTexRefSetAddressMode_orig)
  {
    cuTexRefSetAddressMode_orig = dlsym(orig_handle, "cuTexRefSetAddressMode");
  }

  return cuTexRefSetAddressMode_orig(hTexRef, dim, am);
}


CUresult cuTexRefSetFilterMode(CUtexref hTexRef, CUfilter_mode fm)
{
  static CUresult (*cuTexRefSetFilterMode_orig)(CUtexref, CUfilter_mode) = NULL;
  if (!cuTexRefSetFilterMode_orig)
  {
    cuTexRefSetFilterMode_orig = dlsym(orig_handle, "cuTexRefSetFilterMode");
  }

  return cuTexRefSetFilterMode_orig(hTexRef, fm);
}


CUresult cuTexRefSetMipmapFilterMode(CUtexref hTexRef, CUfilter_mode fm)
{
  static CUresult (*cuTexRefSetMipmapFilterMode_orig)(CUtexref, CUfilter_mode) = NULL;
  if (!cuTexRefSetMipmapFilterMode_orig)
  {
    cuTexRefSetMipmapFilterMode_orig = dlsym(orig_handle, "cuTexRefSetMipmapFilterMode");
  }

  return cuTexRefSetMipmapFilterMode_orig(hTexRef, fm);
}


CUresult cuTexRefSetMipmapLevelBias(CUtexref hTexRef, float bias)
{
  static CUresult (*cuTexRefSetMipmapLevelBias_orig)(CUtexref, float) = NULL;
  if (!cuTexRefSetMipmapLevelBias_orig)
  {
    cuTexRefSetMipmapLevelBias_orig = dlsym(orig_handle, "cuTexRefSetMipmapLevelBias");
  }

  return cuTexRefSetMipmapLevelBias_orig(hTexRef, bias);
}


CUresult cuTexRefSetMipmapLevelClamp(CUtexref hTexRef, float minMipmapLevelClamp, float maxMipmapLevelClamp)
{
  static CUresult (*cuTexRefSetMipmapLevelClamp_orig)(CUtexref, float, float) = NULL;
  if (!cuTexRefSetMipmapLevelClamp_orig)
  {
    cuTexRefSetMipmapLevelClamp_orig = dlsym(orig_handle, "cuTexRefSetMipmapLevelClamp");
  }

  return cuTexRefSetMipmapLevelClamp_orig(hTexRef, minMipmapLevelClamp, maxMipmapLevelClamp);
}


CUresult cuTexRefSetMaxAnisotropy(CUtexref hTexRef, unsigned int maxAniso)
{
  static CUresult (*cuTexRefSetMaxAnisotropy_orig)(CUtexref, unsigned int) = NULL;
  if (!cuTexRefSetMaxAnisotropy_orig)
  {
    cuTexRefSetMaxAnisotropy_orig = dlsym(orig_handle, "cuTexRefSetMaxAnisotropy");
  }

  return cuTexRefSetMaxAnisotropy_orig(hTexRef, maxAniso);
}


CUresult cuTexRefSetBorderColor(CUtexref hTexRef, float *pBorderColor)
{
  static CUresult (*cuTexRefSetBorderColor_orig)(CUtexref, float *) = NULL;
  if (!cuTexRefSetBorderColor_orig)
  {
    cuTexRefSetBorderColor_orig = dlsym(orig_handle, "cuTexRefSetBorderColor");
  }

  return cuTexRefSetBorderColor_orig(hTexRef, pBorderColor);
}


CUresult cuTexRefSetFlags(CUtexref hTexRef, unsigned int Flags)
{
  static CUresult (*cuTexRefSetFlags_orig)(CUtexref, unsigned int) = NULL;
  if (!cuTexRefSetFlags_orig)
  {
    cuTexRefSetFlags_orig = dlsym(orig_handle, "cuTexRefSetFlags");
  }

  return cuTexRefSetFlags_orig(hTexRef, Flags);
}


CUresult cuTexRefGetAddress_v2(CUdeviceptr *pdptr, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetAddress_v2_orig)(CUdeviceptr *, CUtexref) = NULL;
  if (!cuTexRefGetAddress_v2_orig)
  {
    cuTexRefGetAddress_v2_orig = dlsym(orig_handle, "cuTexRefGetAddress_v2");
  }

  return cuTexRefGetAddress_v2_orig(pdptr, hTexRef);
}


CUresult cuTexRefGetArray(CUarray *phArray, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetArray_orig)(CUarray *, CUtexref) = NULL;
  if (!cuTexRefGetArray_orig)
  {
    cuTexRefGetArray_orig = dlsym(orig_handle, "cuTexRefGetArray");
  }

  return cuTexRefGetArray_orig(phArray, hTexRef);
}


CUresult cuTexRefGetMipmappedArray(CUmipmappedArray *phMipmappedArray, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetMipmappedArray_orig)(CUmipmappedArray *, CUtexref) = NULL;
  if (!cuTexRefGetMipmappedArray_orig)
  {
    cuTexRefGetMipmappedArray_orig = dlsym(orig_handle, "cuTexRefGetMipmappedArray");
  }

  return cuTexRefGetMipmappedArray_orig(phMipmappedArray, hTexRef);
}


CUresult cuTexRefGetAddressMode(CUaddress_mode *pam, CUtexref hTexRef, int dim)
{
  static CUresult (*cuTexRefGetAddressMode_orig)(CUaddress_mode *, CUtexref, int) = NULL;
  if (!cuTexRefGetAddressMode_orig)
  {
    cuTexRefGetAddressMode_orig = dlsym(orig_handle, "cuTexRefGetAddressMode");
  }

  return cuTexRefGetAddressMode_orig(pam, hTexRef, dim);
}


CUresult cuTexRefGetFilterMode(CUfilter_mode *pfm, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetFilterMode_orig)(CUfilter_mode *, CUtexref) = NULL;
  if (!cuTexRefGetFilterMode_orig)
  {
    cuTexRefGetFilterMode_orig = dlsym(orig_handle, "cuTexRefGetFilterMode");
  }

  return cuTexRefGetFilterMode_orig(pfm, hTexRef);
}


CUresult cuTexRefGetFormat(CUarray_format *pFormat, int *pNumChannels, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetFormat_orig)(CUarray_format *, int *, CUtexref) = NULL;
  if (!cuTexRefGetFormat_orig)
  {
    cuTexRefGetFormat_orig = dlsym(orig_handle, "cuTexRefGetFormat");
  }

  return cuTexRefGetFormat_orig(pFormat, pNumChannels, hTexRef);
}


CUresult cuTexRefGetMipmapFilterMode(CUfilter_mode *pfm, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetMipmapFilterMode_orig)(CUfilter_mode *, CUtexref) = NULL;
  if (!cuTexRefGetMipmapFilterMode_orig)
  {
    cuTexRefGetMipmapFilterMode_orig = dlsym(orig_handle, "cuTexRefGetMipmapFilterMode");
  }

  return cuTexRefGetMipmapFilterMode_orig(pfm, hTexRef);
}


CUresult cuTexRefGetMipmapLevelBias(float *pbias, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetMipmapLevelBias_orig)(float *, CUtexref) = NULL;
  if (!cuTexRefGetMipmapLevelBias_orig)
  {
    cuTexRefGetMipmapLevelBias_orig = dlsym(orig_handle, "cuTexRefGetMipmapLevelBias");
  }

  return cuTexRefGetMipmapLevelBias_orig(pbias, hTexRef);
}


CUresult cuTexRefGetMipmapLevelClamp(float *pminMipmapLevelClamp, float *pmaxMipmapLevelClamp, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetMipmapLevelClamp_orig)(float *, float *, CUtexref) = NULL;
  if (!cuTexRefGetMipmapLevelClamp_orig)
  {
    cuTexRefGetMipmapLevelClamp_orig = dlsym(orig_handle, "cuTexRefGetMipmapLevelClamp");
  }

  return cuTexRefGetMipmapLevelClamp_orig(pminMipmapLevelClamp, pmaxMipmapLevelClamp, hTexRef);
}


CUresult cuTexRefGetMaxAnisotropy(int *pmaxAniso, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetMaxAnisotropy_orig)(int *, CUtexref) = NULL;
  if (!cuTexRefGetMaxAnisotropy_orig)
  {
    cuTexRefGetMaxAnisotropy_orig = dlsym(orig_handle, "cuTexRefGetMaxAnisotropy");
  }

  return cuTexRefGetMaxAnisotropy_orig(pmaxAniso, hTexRef);
}


CUresult cuTexRefGetBorderColor(float *pBorderColor, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetBorderColor_orig)(float *, CUtexref) = NULL;
  if (!cuTexRefGetBorderColor_orig)
  {
    cuTexRefGetBorderColor_orig = dlsym(orig_handle, "cuTexRefGetBorderColor");
  }

  return cuTexRefGetBorderColor_orig(pBorderColor, hTexRef);
}


CUresult cuTexRefGetFlags(unsigned int *pFlags, CUtexref hTexRef)
{
  static CUresult (*cuTexRefGetFlags_orig)(unsigned int *, CUtexref) = NULL;
  if (!cuTexRefGetFlags_orig)
  {
    cuTexRefGetFlags_orig = dlsym(orig_handle, "cuTexRefGetFlags");
  }

  return cuTexRefGetFlags_orig(pFlags, hTexRef);
}


CUresult cuTexRefCreate(CUtexref *pTexRef)
{
  static CUresult (*cuTexRefCreate_orig)(CUtexref *) = NULL;
  if (!cuTexRefCreate_orig)
  {
    cuTexRefCreate_orig = dlsym(orig_handle, "cuTexRefCreate");
  }

  return cuTexRefCreate_orig(pTexRef);
}


CUresult cuTexRefDestroy(CUtexref hTexRef)
{
  static CUresult (*cuTexRefDestroy_orig)(CUtexref) = NULL;
  if (!cuTexRefDestroy_orig)
  {
    cuTexRefDestroy_orig = dlsym(orig_handle, "cuTexRefDestroy");
  }

  return cuTexRefDestroy_orig(hTexRef);
}


CUresult cuSurfRefSetArray(CUsurfref hSurfRef, CUarray hArray, unsigned int Flags)
{
  static CUresult (*cuSurfRefSetArray_orig)(CUsurfref, CUarray, unsigned int) = NULL;
  if (!cuSurfRefSetArray_orig)
  {
    cuSurfRefSetArray_orig = dlsym(orig_handle, "cuSurfRefSetArray");
  }

  return cuSurfRefSetArray_orig(hSurfRef, hArray, Flags);
}


CUresult cuSurfRefGetArray(CUarray *phArray, CUsurfref hSurfRef)
{
  static CUresult (*cuSurfRefGetArray_orig)(CUarray *, CUsurfref) = NULL;
  if (!cuSurfRefGetArray_orig)
  {
    cuSurfRefGetArray_orig = dlsym(orig_handle, "cuSurfRefGetArray");
  }

  return cuSurfRefGetArray_orig(phArray, hSurfRef);
}


CUresult cuTexObjectCreate(CUtexObject *pTexObject, const CUDA_RESOURCE_DESC *pResDesc, const CUDA_TEXTURE_DESC *pTexDesc, const CUDA_RESOURCE_VIEW_DESC *pResViewDesc)
{
  static CUresult (*cuTexObjectCreate_orig)(CUtexObject *, const CUDA_RESOURCE_DESC *, const CUDA_TEXTURE_DESC *, const CUDA_RESOURCE_VIEW_DESC *) = NULL;
  if (!cuTexObjectCreate_orig)
  {
    cuTexObjectCreate_orig = dlsym(orig_handle, "cuTexObjectCreate");
  }

  return cuTexObjectCreate_orig(pTexObject, pResDesc, pTexDesc, pResViewDesc);
}


CUresult cuTexObjectDestroy(CUtexObject texObject)
{
  static CUresult (*cuTexObjectDestroy_orig)(CUtexObject) = NULL;
  if (!cuTexObjectDestroy_orig)
  {
    cuTexObjectDestroy_orig = dlsym(orig_handle, "cuTexObjectDestroy");
  }

  return cuTexObjectDestroy_orig(texObject);
}


CUresult cuTexObjectGetResourceDesc(CUDA_RESOURCE_DESC *pResDesc, CUtexObject texObject)
{
  static CUresult (*cuTexObjectGetResourceDesc_orig)(CUDA_RESOURCE_DESC *, CUtexObject) = NULL;
  if (!cuTexObjectGetResourceDesc_orig)
  {
    cuTexObjectGetResourceDesc_orig = dlsym(orig_handle, "cuTexObjectGetResourceDesc");
  }

  return cuTexObjectGetResourceDesc_orig(pResDesc, texObject);
}


CUresult cuTexObjectGetTextureDesc(CUDA_TEXTURE_DESC *pTexDesc, CUtexObject texObject)
{
  static CUresult (*cuTexObjectGetTextureDesc_orig)(CUDA_TEXTURE_DESC *, CUtexObject) = NULL;
  if (!cuTexObjectGetTextureDesc_orig)
  {
    cuTexObjectGetTextureDesc_orig = dlsym(orig_handle, "cuTexObjectGetTextureDesc");
  }

  return cuTexObjectGetTextureDesc_orig(pTexDesc, texObject);
}


CUresult cuTexObjectGetResourceViewDesc(CUDA_RESOURCE_VIEW_DESC *pResViewDesc, CUtexObject texObject)
{
  static CUresult (*cuTexObjectGetResourceViewDesc_orig)(CUDA_RESOURCE_VIEW_DESC *, CUtexObject) = NULL;
  if (!cuTexObjectGetResourceViewDesc_orig)
  {
    cuTexObjectGetResourceViewDesc_orig = dlsym(orig_handle, "cuTexObjectGetResourceViewDesc");
  }

  return cuTexObjectGetResourceViewDesc_orig(pResViewDesc, texObject);
}


CUresult cuSurfObjectCreate(CUsurfObject *pSurfObject, const CUDA_RESOURCE_DESC *pResDesc)
{
  static CUresult (*cuSurfObjectCreate_orig)(CUsurfObject *, const CUDA_RESOURCE_DESC *) = NULL;
  if (!cuSurfObjectCreate_orig)
  {
    cuSurfObjectCreate_orig = dlsym(orig_handle, "cuSurfObjectCreate");
  }

  return cuSurfObjectCreate_orig(pSurfObject, pResDesc);
}


CUresult cuSurfObjectDestroy(CUsurfObject surfObject)
{
  static CUresult (*cuSurfObjectDestroy_orig)(CUsurfObject) = NULL;
  if (!cuSurfObjectDestroy_orig)
  {
    cuSurfObjectDestroy_orig = dlsym(orig_handle, "cuSurfObjectDestroy");
  }

  return cuSurfObjectDestroy_orig(surfObject);
}


CUresult cuSurfObjectGetResourceDesc(CUDA_RESOURCE_DESC *pResDesc, CUsurfObject surfObject)
{
  static CUresult (*cuSurfObjectGetResourceDesc_orig)(CUDA_RESOURCE_DESC *, CUsurfObject) = NULL;
  if (!cuSurfObjectGetResourceDesc_orig)
  {
    cuSurfObjectGetResourceDesc_orig = dlsym(orig_handle, "cuSurfObjectGetResourceDesc");
  }

  return cuSurfObjectGetResourceDesc_orig(pResDesc, surfObject);
}


CUresult cuDeviceCanAccessPeer(int *canAccessPeer, CUdevice dev, CUdevice peerDev)
{
  static CUresult (*cuDeviceCanAccessPeer_orig)(int *, CUdevice, CUdevice) = NULL;
  if (!cuDeviceCanAccessPeer_orig)
  {
    cuDeviceCanAccessPeer_orig = dlsym(orig_handle, "cuDeviceCanAccessPeer");
  }

  return cuDeviceCanAccessPeer_orig(canAccessPeer, dev, peerDev);
}


CUresult cuCtxEnablePeerAccess(CUcontext peerContext, unsigned int Flags)
{
  static CUresult (*cuCtxEnablePeerAccess_orig)(CUcontext, unsigned int) = NULL;
  if (!cuCtxEnablePeerAccess_orig)
  {
    cuCtxEnablePeerAccess_orig = dlsym(orig_handle, "cuCtxEnablePeerAccess");
  }

  return cuCtxEnablePeerAccess_orig(peerContext, Flags);
}


CUresult cuCtxDisablePeerAccess(CUcontext peerContext)
{
  static CUresult (*cuCtxDisablePeerAccess_orig)(CUcontext) = NULL;
  if (!cuCtxDisablePeerAccess_orig)
  {
    cuCtxDisablePeerAccess_orig = dlsym(orig_handle, "cuCtxDisablePeerAccess");
  }

  return cuCtxDisablePeerAccess_orig(peerContext);
}


CUresult cuDeviceGetP2PAttribute(int *value, CUdevice_P2PAttribute attrib, CUdevice srcDevice, CUdevice dstDevice)
{
  static CUresult (*cuDeviceGetP2PAttribute_orig)(int *, CUdevice_P2PAttribute, CUdevice, CUdevice) = NULL;
  if (!cuDeviceGetP2PAttribute_orig)
  {
    cuDeviceGetP2PAttribute_orig = dlsym(orig_handle, "cuDeviceGetP2PAttribute");
  }

  return cuDeviceGetP2PAttribute_orig(value, attrib, srcDevice, dstDevice);
}


CUresult cuGraphicsUnregisterResource(CUgraphicsResource resource)
{
  static CUresult (*cuGraphicsUnregisterResource_orig)(CUgraphicsResource) = NULL;
  if (!cuGraphicsUnregisterResource_orig)
  {
    cuGraphicsUnregisterResource_orig = dlsym(orig_handle, "cuGraphicsUnregisterResource");
  }

  return cuGraphicsUnregisterResource_orig(resource);
}


CUresult cuGraphicsSubResourceGetMappedArray(CUarray *pArray, CUgraphicsResource resource, unsigned int arrayIndex, unsigned int mipLevel)
{
  static CUresult (*cuGraphicsSubResourceGetMappedArray_orig)(CUarray *, CUgraphicsResource, unsigned int, unsigned int) = NULL;
  if (!cuGraphicsSubResourceGetMappedArray_orig)
  {
    cuGraphicsSubResourceGetMappedArray_orig = dlsym(orig_handle, "cuGraphicsSubResourceGetMappedArray");
  }

  return cuGraphicsSubResourceGetMappedArray_orig(pArray, resource, arrayIndex, mipLevel);
}


CUresult cuGraphicsResourceGetMappedMipmappedArray(CUmipmappedArray *pMipmappedArray, CUgraphicsResource resource)
{
  static CUresult (*cuGraphicsResourceGetMappedMipmappedArray_orig)(CUmipmappedArray *, CUgraphicsResource) = NULL;
  if (!cuGraphicsResourceGetMappedMipmappedArray_orig)
  {
    cuGraphicsResourceGetMappedMipmappedArray_orig = dlsym(orig_handle, "cuGraphicsResourceGetMappedMipmappedArray");
  }

  return cuGraphicsResourceGetMappedMipmappedArray_orig(pMipmappedArray, resource);
}


CUresult cuGraphicsResourceGetMappedPointer_v2(CUdeviceptr *pDevPtr, size_t *pSize, CUgraphicsResource resource)
{
  static CUresult (*cuGraphicsResourceGetMappedPointer_v2_orig)(CUdeviceptr *, size_t *, CUgraphicsResource) = NULL;
  if (!cuGraphicsResourceGetMappedPointer_v2_orig)
  {
    cuGraphicsResourceGetMappedPointer_v2_orig = dlsym(orig_handle, "cuGraphicsResourceGetMappedPointer_v2");
  }

  return cuGraphicsResourceGetMappedPointer_v2_orig(pDevPtr, pSize, resource);
}


CUresult cuGraphicsResourceSetMapFlags_v2(CUgraphicsResource resource, unsigned int flags)
{
  static CUresult (*cuGraphicsResourceSetMapFlags_v2_orig)(CUgraphicsResource, unsigned int) = NULL;
  if (!cuGraphicsResourceSetMapFlags_v2_orig)
  {
    cuGraphicsResourceSetMapFlags_v2_orig = dlsym(orig_handle, "cuGraphicsResourceSetMapFlags_v2");
  }

  return cuGraphicsResourceSetMapFlags_v2_orig(resource, flags);
}


CUresult cuGraphicsMapResources(unsigned int count, CUgraphicsResource *resources, CUstream hStream)
{
  static CUresult (*cuGraphicsMapResources_orig)(unsigned int, CUgraphicsResource *, CUstream) = NULL;
  if (!cuGraphicsMapResources_orig)
  {
    cuGraphicsMapResources_orig = dlsym(orig_handle, "cuGraphicsMapResources");
  }

  return cuGraphicsMapResources_orig(count, resources, hStream);
}


CUresult cuGraphicsUnmapResources(unsigned int count, CUgraphicsResource *resources, CUstream hStream)
{
  static CUresult (*cuGraphicsUnmapResources_orig)(unsigned int, CUgraphicsResource *, CUstream) = NULL;
  if (!cuGraphicsUnmapResources_orig)
  {
    cuGraphicsUnmapResources_orig = dlsym(orig_handle, "cuGraphicsUnmapResources");
  }

  return cuGraphicsUnmapResources_orig(count, resources, hStream);
}


CUresult cuGetExportTable(const void **ppExportTable, const CUuuid *pExportTableId)
{
  static CUresult (*cuGetExportTable_orig)(const void **, const CUuuid *) = NULL;
  if (!cuGetExportTable_orig)
  {
    cuGetExportTable_orig = dlsym(orig_handle, "cuGetExportTable");
  }

  return cuGetExportTable_orig(ppExportTable, pExportTableId);
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
