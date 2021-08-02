#!/usr/bin/env python3

import argparse
import tarfile
import os
import sys
import configparser
import io
import stat
import time

def add_metadata(output, root, members):
    cfg = configparser.ConfigParser()
    cfg[root] = {'name': root}
    cfg[root].update(members)

    data = ""
    with io.StringIO() as f:
        cfg.write(f)
        f.seek(0)

        data = f.getvalue()

    n = root + '.cfg'
    ti = tarfile.TarInfo(name=os.path.join(root, n))
    ti.size = len(data)
    ti.mtime = time.time()

    with io.BytesIO(data.encode('utf-8')) as f:
        output.addfile(ti, fileobj=f)

def fixperms(t):
    t.mode = t.mode | stat.S_IRGRP | stat.S_IROTH
    if t.mode & stat.S_IFDIR:
        t.mode = t.mode | stat.S_IXGRP | stat.S_IXOTH
    return t

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

    if args.root:
        root = args.root
    else:
        root = os.path.basename(args.archive)
        root = root[0:root.index(".")]

    members_to_add = [('trace', td),
                      ('blobstore', args.blobstore),
                      ('binary', args.binary),
                      ('args_binary', args.binary + ".arg"),
                      ('args_yaml', args.binary + ".arg.yaml")]

    with tarfile.open(args.archive, f'w:{args.compression}') as output:
        members = {}
        for n, m in members_to_add:
            arcname = os.path.join(root, os.path.basename(m))
            print(f"Adding {n} file {m} as {arcname}")
            output.add(m, arcname, filter=fixperms)

            members[n] = arcname[len(root)+1:]
            members["orig_" + n] = os.path.abspath(m)

        add_metadata(output, root, members)
