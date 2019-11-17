@0xde9279214e9f7175;

struct GetInterface {
  iface @0 : Tag;
  ordinal @1 : UInt32;

  enum Tag {
	rebaseableMemory @0;
	cudaGPU @1;
  }
}

interface RebaseableMemory {
  initialize @0 (byteSize :UInt64); # TODO: deprecated
  allocMemory @1 ();
  rebase @2 (newBase: UInt64);
  copyTo @3 (addr: UInt64, data :Data);
  copyFrom @4 (addr: UInt64, byteCount: UInt64) -> (data: Data);
}

interface CUDAGPU {
  initialize @0 (ordinal :UInt32);
  initMemory @6 ();
  setName @1 (name :Text);
  setTotalMemory @2 (sizeInBytes  :UInt64);
  setAttribute @3 (attribute :UInt32, value :Int32);
  setUuid @4 (uuid :Data);  # data for now, maybe list(octets)
  launchKernel @5 (f :Data,
				   gridDimX :UInt32, gridDimY :UInt32, gridDimZ :UInt32,
				   blockDimX :UInt32, blockDimY :UInt32, blockDimZ :UInt32,
				   sharedMemBytes :UInt64,
				   stream :UInt32,  # TODO 
				   kernelParams :List(Data));
}
