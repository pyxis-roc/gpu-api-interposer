@0xde9279214e9f7175;

struct GetInterface {
  iface @0 : Tag;
  enum Tag {
	rebaseableMemory @0;
  }
}

interface RebaseableMemory {
  initialize @0 (byteSize :UInt64);
  allocMemory @1 ();
  rebase @2 (newBase: UInt64);
  copyTo @3 (addr: UInt64, data :Data);
  copyFrom @4 (addr: UInt64, byteCount: UInt64) -> (data: Data);
}
