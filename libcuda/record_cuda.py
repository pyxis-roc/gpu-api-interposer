#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2021,2022,2023 University of Rochester
#
# SPDX-License-Identifier: MIT

# Author:       Benjamin Valpey

import os
import shutil
import subprocess
import sys
import tempfile
import datetime
import atexit
from libcudareplay import pack_api_trace


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--DLOPEN_LIBRARY", help="Path to libcuda.so.1")
    p.add_argument("--BLOBSTORE_PATH", help="Path to where blobstore will be saved")
    p.add_argument(
        "--ARGHELPER_FILE",
        help="Path to where arghelper file will be saved (or read from if it exists and is newer than the binary)",
    )
    p.add_argument("--LD_PRELOAD", help="Path to libcuda_record.so")
    p.add_argument("--archive", help="Archive output file")
    p.add_argument(
        "-c",
        "--compression",
        choices=["bz2", "xz"],
        help="Compression format",
        default="bz2",
    )
    p.add_argument(
        "-r",
        "--root",
        help="Root of tar file (default: name of archive before first .)",
    )
    p.add_argument(
        "cmd",
        nargs="+",
        help="The command to execute, along with its normal command line args",
    )
    p.add_argument("-d", help="Turn on debug mode (prints output)", action="store_true")
    args = p.parse_args()

    new_env = os.environ.copy()

    safety_cleanup = []
    for x in [
        os.environ.get("DLOPEN_LIBRARY", args.DLOPEN_LIBRARY),
        "/usr/lib64/libcuda.so.1",
        "/usr/lib/x86_64-linux-gnu/libcuda.so.1",
    ]:
        if x is None:
            continue
        if os.path.isfile(x):
            new_env["DLOPEN_LIBRARY"] = x
            break
    else:
        print(
            "Could not locate libcuda.so.1 in the usual places, set DLOPEN_LIBRARY to point to libcuda.so.1"
        )
        sys.exit(1)

    TS = f"{datetime.datetime.now():%Y%m%d-%H%M%S}"

    if args.ARGHELPER_FILE is None:
        new_env["ARGHELPER_FILE"] = args.cmd[0] + ".arg"
    else:
        new_env["ARGHELPER_FILE"] = args.ARGHELPER_FILE

    if args.LD_PRELOAD is None:
        new_env["LD_PRELOAD"] = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "libcuda_record.so"
        )
    else:
        new_env["LD_PRELOAD"] = args.LD_PRELOAD

    if args.BLOBSTORE_PATH is None:
        f, BLOBSTORE_PATH = tempfile.mkstemp(
            prefix=f"cuda-record-bs-{TS}-", suffix=".db"
        )
        new_env["BLOBSTORE_PATH"] = BLOBSTORE_PATH
        os.close(f)
    else:
        BLOBSTORE_PATH = args.BLOBSTORE_PATH
        new_env["BLOBSTORE_PATH"] = BLOBSTORE_PATH

    if not os.path.isfile(new_env["ARGHELPER_FILE"]) or (
        os.path.getctime(new_env["ARGHELPER_FILE"]) < os.path.getctime(args.cmd[0])
    ):
        sys.path.append(os.path.dirname(os.path.realpath(__file__)))
        import nvparams

        ka = nvparams.get_kernel_arguments(args.cmd[0])
        if len(ka) > 0:
            import yaml

            d, b = nvparams.create_arg_recorder_helper(
                ka, new_env["ARGHELPER_FILE"], True
            )
            with open(new_env["ARGHELPER_FILE"] + ".yaml", "w") as f:
                f.write(yaml.dump(d))
        else:
            print(
                "ERROR: No kernel argument information found. Does the binary contain ELF sections?",
                sys.stderr,
            )
            sys.exit(1)

    try:
        # make a temporary directory where the trace will be stored
        tracedir = tempfile.mkdtemp()
        res = subprocess.run(
            ["lttng", "create", "cuda-record", "-o", tracedir],
            check=True,
            capture_output=True,
        )

        if args.d:
            print(res.stdout.decode("utf-8"))
            print("=" * 50)
            print(res.stderr.decode("utf-8"))

        def exit_safely():
            subprocess.run(["lttng", "destroy"])
            shutil.rmtree(tracedir)
            for f in safety_cleanup:
                if os.path.isfile(f):
                    os.remove(f)
                if os.path.isfile(f + ".yaml"):
                    os.remove(f + ".yaml")

        atexit.register(exit_safely)

        subprocess.run(
            ["lttng", "enable-event", "--userspace", "libcuda_interposer:*"],
            check=True,
            capture_output=True,
        )

        subprocess.run(
            ["lttng", "add-context", "--userspace", "-t", "vtid"],
            check=True,
            capture_output=True,
        )
        subprocess.run(["lttng", "start"], check=True, capture_output=True)

        subprocess.run(args.cmd, stdout=sys.stdout, stderr=sys.stderr, env=new_env)

        subprocess.run(["lttng", "stop"], capture_output=True, check=True)
    except subprocess.CalledProcessError as e:
        print(e.stderr, file=sys.stderr)
        sys.exit(1)

    # Assume the binary is the first element of cmd
    if args.archive is None:
        args.archive = args.cmd[0] + ".tar." + args.compression

    root = os.path.basename(args.cmd[0]).split(".")[0]
    members_to_add = [
        ("trace", tracedir),
        ("blobstore", BLOBSTORE_PATH),
        ("binary", args.cmd[0]),
        ("args_binary", new_env["ARGHELPER_FILE"]),
        ("args_yaml", new_env["ARGHELPER_FILE"] + ".yaml"),
    ]
    safety_cleanup.append(new_env["ARGHELPER_FILE"])
    pack_api_trace.pack_trace(args.archive, args.compression, root, members_to_add)

    # Only remove arghelper file if it was not specified via command line
    if args.ARGHELPER_FILE is not None:
        try:
            os.remove(new_env["ARGHELPER_FILE"])
            os.remove(new_env["ARGHELPER_FILE"] + ".yaml")
        except OSError:
            pass
    try:
        os.remove(new_env["BLOBSTORE_PATH"])
    except OSError:
        print("Warning: could not remove BLOBSTORE.", file=sys.stderr)
