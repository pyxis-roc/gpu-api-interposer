#!/usr/bin/env python3

import argparse
import tarfile
import os
import sys

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Pack trace and ancillary files into an archive")
    p.add_argument("tracedir", help="LTTNG trace directory")
    p.add_argument("blobstore", help="Blobstore file")
    p.add_argument("binary", help="Binary file")
    p.add_argument("archive", help="Archive output file")
    p.add_argument("-c", "--compression", choices=['bz2', 'xz'], help="Compression format", default="bz2")
    p.add_argument("-r", "--root", help="Root of tar file (default: name of archive before first .)")

    args = p.parse_args()

    td = args.tracedir if os.path.basename(args.tracedir) != '' else os.path.dirname(args.tracedir)

    if not os.path.isdir(td):
        print(f"ERROR: Trace directory {td} must be a directory.")
        sys.exit(1)

    if not os.path.isfile(args.blobstore):
        print(f"ERROR: Blob store {args.blobstore} must be a file.")
        sys.exit(1)

    if not os.path.isfile(args.binary):
        print(f"ERROR: Binary {args.binary} must be a file.")
        sys.exit(1)

    if not os.path.isfile(args.binary + ".arg"):
        print(f"ERROR: Binary {args.binary} must have an args file {args.binary}.arg")
        sys.exit(1)

    if not os.path.isfile(args.binary + ".arg.yaml"):
        print(f"ERROR: Binary {args.binary} must have an args file {args.binary}.arg.yaml")
        sys.exit(1)

    root = args.archive[0:args.archive.index(".")]

    members_to_add = [td, args.blobstore, args.binary,
                      args.binary + ".arg",
                      args.binary + ".arg.yaml"]

    with tarfile.open(args.archive, f'w:{args.compression}') as output:
        for m in members_to_add:
            print(f"Adding {m}")
            output.add(m, os.path.join(root, os.path.basename(m)))
