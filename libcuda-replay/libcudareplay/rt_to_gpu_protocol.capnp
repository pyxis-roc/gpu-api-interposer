@0xde9279214e9f7175;

struct GPUProperties {
  ordinal @0  :UInt32;
  totalMemory @1 :UInt64;
}

struct GetInterface {
  iface @0 : Tag;
  ordinal @1 : UInt32;

  enum Tag {
	rebaseableMemory @0;
	gpuEmulator @1;
  }
}

interface RebaseableMemory {
  initialize @0 (byteSize :UInt64); # TODO: deprecated
  allocMemory @1 ();
  rebase @2 (newBase: UInt64);
  copyTo @3 (addr: UInt64, data :Data);
  copyFrom @4 (addr: UInt64, byteCount: UInt64) -> (data: Data);
}

interface GPUEmulator {
  initialize @0 (gpu_props :GPUProperties);
  loadImage @1 (imgId :UInt64, image :Data);
  launchKernel @2 (imgId: UInt64,
  	           entry :Data,
                   gridDimX :UInt32, gridDimY :UInt32, gridDimZ :UInt32,
                   blockDimX :UInt32, blockDimY :UInt32, blockDimZ :UInt32,
                   sharedMemBytes :UInt64,
                   queue :UInt32,
		   kernelParams :List(Data));
}