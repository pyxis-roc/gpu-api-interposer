#!/usr/bin/env python3

# Author:       Benjamin Valpey

import os
import shutil
import subprocess
import sys
import tempfile
import datetime
import atexit
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import nvparams




if __name__ == '__main__':
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--DLOPEN_LIBRARY", help="Path to libcuda.so.1")
    p.add_argument("--BLOBSTORE_PATH", help="Path to where blobstore will be saved")
    p.add_argument("--ARGHELPER_FILE", help="Path to where arghelper file will be saved (or read from if it exists and is newer than the binary)")
    p.add_argument("--LD_PRELOAD", help="Path to libcuda_record.so")
    p.add_argument("--archive", help="Archive output file")
    p.add_argument("-c", "--compression", choices=['bz2', 'xz'], help="Compression format", default="bz2")
    p.add_argument("-r", "--root", help="Root of tar file (default: name of archive before first .)")
    p.add_argument("cmd", nargs="+", help="The command to execute, along with its normal command line args")
    args = p.parse_args()

    new_env = os.environ.copy()


    for x in [os.environ.get('DLOPEN_LIBRARY', args.DLOPEN_LIBRARY), "/usr/lib64/libcuda.so.1", "/usr/lib/x86_64-linux-gnu/libcuda.so.1"]:
        if x is None:
            continue
        if os.path.isfile(x):
            new_env['DLOPEN_LIBRARY'] = x
            break
    else:
        print("Could not locate libcuda.so.1 in the usual places, set DLOPEN_LIBRARY to point to libcuda.so.1")
        exit(1)

    TS = f'{datetime.datetime.now():%Y%m%d-%H%M%S}'


    if args.ARGHELPER_FILE is None:
        new_env['ARGHELPER_FILE'] = args.cmd[0] + ".arg"
    else:
        new_env['ARGHELPER_FILE'] = args.ARGHELPER_FILE

    if args.LD_PRELOAD is None:
        new_env['LD_PRELOAD'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'libcuda_record.so')
    else:
        new_env['LD_PRELOAD'] = args.LD_PRELOAD

    
    if args.BLOBSTORE_PATH is None:
        f, BLOBSTORE_PATH = tempfile.mkstemp(prefix=f"cuda-record-bs-{TS}-", suffix=".db")
        new_env['BLOBSTORE_PATH'] = BLOBSTORE_PATH
        os.close(f)
    else:
        BLOBSTORE_PATH = args.BLOBSTORE_PATH
        new_env['BLOBSTORE_PATH'] = BLOBSTORE_PATH


    
    try:
        # make a temporary directory where the trace will be stored
        tracedir = tempfile.mkdtemp()
        subprocess.run(["lttng", "create", "cuda-record", "-o", tracedir],
                        check=True,
                        capture_output=True)

        def exit_safely():
            subprocess.run(["lttng", "destroy"])
            shutil.rmtree(tracedir)
        atexit.register(exit_safely)

        subprocess.run(["lttng", "enable-event", '--userspace', 'libcuda_interposer:*'],
                    check=True,
                    capture_output=True)

        subprocess.run(["lttng", "add-context", "--userspace", "-t", "vtid"],
                check=True,
                capture_output=True)
        subprocess.run(["lttng", "start"], check=True, capture_output=True)

        subprocess.run(args.cmd, stdout=sys.stdout, stderr=sys.stderr, env=new_env)

        subprocess.run(["lttng", "stop"], capture_output=True, check=True)
    except subprocess.CalledProcessError as e:
        print(e.stderr, file=sys.stderr)
        exit(1)
    
    # now call record_cuda.py

    # A hack to get the path to the module, so we can execute it
    import libcudareplay.pack_api_trace as pack_api_trace
    pack_api_path = os.path.abspath(pack_api_trace.__file__)

    # Assume the binary is the first element of cmd
    if args.archive is None:
        args.archive = args.cmd[0] + '.tar.' + args.compression

    # pack_api_trace.py assumes that the ARGFILE is in the same location as the binary
    # This will be fixed and patched in a future update
    subprocess.run([pack_api_path, tracedir, BLOBSTORE_PATH, args.cmd[0], args.archive])

    os.remove(new_env['BLOBSTORE_PATH'])

    # Only remove arghelper file if it was not specified via command line
    if args.ARGHELPER_FILE is not None:
        shutil.rmtree(new_env['ARGHELPER_FILE'])
