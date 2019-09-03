#!/usr/bin/env python3

from collections import namedtuple

MemoryRegion = namedtuple('MemoryRegion', 'start end')

#TODO: Make this a faster, using binary search
#Note: memory regions do not overlap
class MemoryRegions(object):
    def __init__(self):
        self.regions = []

    def add(self, n):
        if self.overlap(n) is None:
            i = -1
            for i, r in enumerate(self.regions):
                if r.start >= n.end:
                    break

            self.regions.insert(i, n)
            return n
        else:
            return None

    def remove(self, n):
        self.regions.remove(n)

    def at(self, point):
        for r in self.regions:
            if point >= r.start and point <= r.end:
                return r

        return None

    def overlap(self, region):
        for r in self.regions:
            if r.start < region.start:
                A = r
                B = region
            else:
                A = region
                B = r

            if B.start >= A.start and B.start <= A.end:
                return MemoryRegion(start=B.start, end=min(B.end, A.end))

        return None

if __name__ == "__main__":
    x = MemoryRegions()
    print(x.add(MemoryRegion(8, 8+4)))
    print(x.add(MemoryRegion(0, 4)))
    print(x.add(MemoryRegion(9, 10)))

    print(x.regions)

    y = x.at(8)
    print(y)
    x.remove(y)
