This directory contains interposers for the CUDA Device API.

# Pre-requisites

You'll need the following Python3 packages:

  - pycparser
  - pyelftools
  - sqlite3

If you're going to use `libcuda_record.so` to generate a trace of the
CUDA device API, you'll also need:

  - babeltrace (< 2.0)
  - lttng

In addition to the `lttng-tools` and `liblttng-ust` packages.

[note to pyx users: these are already installed]

# Compiling

To compile, make sure you have the correct CUDA version loaded (if you
have multiple CUDA versions). Set the environment variable `CUDA_LIB`
to point to the correct CUDA library location (this is usually
`/usr/local/cuda/lib64`).

NOTE: If your fake C headers (from pycparser) are not in
`/usr/share/python3-pycparser/fake_libc_include`, you should pass the
correct directory as:

    make FAKE_C_HEADERS=/path/to/fake_libc_include ...

Create the default build directory:

    mkdir build

You can change the build directory by editing the Makefile or passing
the `BUILD_DIR` variable to make:

    make BUILD_DIR=/path/to/some/other/directory ...

First try to compile `libcuda_passthru.so`:

    make libcuda_passthru.so

If that works, try `libcuda_trace.so`:

    make libcuda_trace.so

Finally, compile `libcuda_record.so`, which records the CUDA API:

    make libcuda_record.so

See the instructions below on how to use these libraries.


# libcuda_passthru.so

This is a simple passthrough interposer that simply calls the
underlying CUDA Device API.

To use this:

    DLOPEN_LIBRARY=/path/to/actual/libcuda.so.1 LD_PRELOAD=/path/to/libcuda_passthru.so gpu-program-and-its-arguments...

The `gpu-program-and-its-args` is any program that uses CUDA and its
arguments. If it executed successfully, everything worked.

# libcuda_trace.so

This is a tracing interposer that will eventually record all the CUDA
Device API calls. For now, it only outputs the name of the API being
called.

To use this:

    TRACE_OUTPUT=trace.txt DLOPEN_LIBRARY=/path/to/actual/libcuda.so.1 LD_PRELOAD=/path/to/libcuda_trace.so gpu-program-and-its-arguments...

You should get a list of all CUDA device API functions called, using
this command:

    sort -u trace.txt

# libcuda_record.so

This is a complicated library that will eventually store a complete
CUDA Device API trace, so it is accompanied by a runner script.

The command:

    /path/to/libcuda/record_cuda.sh cuda_binary arg1 arg2 ...

will setup the correct environment variables and run the `cuda_binary`
executable with the specified arguments.

The output will be a lttng-ust trace prefixed with `cuda-record` in
the default lttng traces directory (usually `~/lttng-traces`) [the
path is echoed by the `record_cuda.sh` script], and a
`cuda-record-bs-timestamp-random.db` file in the *current* directory
that contains all the binary blobs.

You can use `babeltrace` to see the trace:

    babeltrace /path/to/lttng-trace

You can also use `libcuda-replay.py` to rerun the trace:

    /path/to/libcuda-replay/libcuda_replay.py /path/to/lttng-trace /path/to/bs.db /path/to/argfiles.yaml

## Advanced Usage

### Different locations for arg files

The `record_cuda.sh` script will create a `cuda_binary.args` and
`cuda_binary.args.yaml` file in the directory that contains the binary
if the files do not exist. If you don't want this, run:

    /path/to/libcuda/nvparams.py /path/to/cuda_binary /some/other/path/to/cuda_binary.arg

and set `ARGHELPER_FILE=/some/other/path/to/cuda_binary.arg`.

### Debugging libcuda_record.so

Run `record_cuda.sh` like this:

    DEBUG=anyvalue /path/to/record_cuda.sh gdb cudabinary 10 20

Note the `gdb` before `cudabinary`.

Currently, running in debug mode also disables blobstore, since GDB
seems to run the constructors twice.

