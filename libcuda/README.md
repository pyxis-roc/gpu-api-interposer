This directory contains interposers for the CUDA Device API.

# Pre-requisites

You'll need the following Python3 packages:

  - pycparser (== 2.21)
  - pyelftools
  - sqlite3

If you're going to use `libcuda_record.so` to generate a trace of the
CUDA device API, you'll also need:

  - babeltrace (== 2.0)
  - lttng

In addition to the `lttng-tools` and `liblttng-ust` packages.

[note to pyx users: these are already installed]

# Install the harmonv package

If you haven't already, make sure you install the `harmonv` package.

```
cd ../harmonv
python3 setup.py develop
```

The commands above setup the harmonv package for development, but you
can also install it.


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

    $BUILD_DIR/record_cuda.sh cuda_binary arg1 arg2 ...

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

    /path/to/libcuda-replay/libcuda_replay.py /path/to/lttng-trace /path/to/bs.db /path/to/binary /path/to/argfiles.yaml

## Adding new APIs to record in the trace

The `libcuda_record` tracing library uses
[lttng-ust](https://lttng.org/man/3/lttng-ust/v2.7/) to record the
trace. If you're not familiar with `lttng-ust`, it is highly
recommended you read the [lttng
documentation](https://lttng.org/docs/v2.10/), especially the part on
[tracing user applications with
lttng-ust](https://lttng.org/docs/v2.10/#doc-tracing-your-own-user-application)

Each API call is given at most two tracepoints: one suffixed `_pre`,
before the API call is executed, and one suffixed `_post`, that
captures data after the API call is executed, including the return
value.

You will need to complete at least 2 steps to add a new API call:

  1. Add the API function name to `libcuda_record_filter.yaml` in the
    `pre` section (to generate a `_pre` tracepoint), in the `_post`
    section (to generate a `_post` tracepoint). There is a
    `pre_and_post` section that will generate both tracepoints.

  2. Add fields and types for the tracepoint to record arguments to
     the API call in `libcuda_record_tp.yaml`. This specifies how to
     translate C types (like `CUdevice`) to a [CTF
     macro](https://lttng.org/docs/v2.10/#doc-lttng-modules-tp-fields)
     (like `ctf_integer`). It also allows you to record expressions.

Once you've done the two steps above, you will be able to record
traces with the new API calls.

### Writing a field specific in `libcuda_record_tp.yaml`

The `libcuda_record_tp.yaml` is a specification of a `lttng-ust`
tracepoint. The `gentracepoints.py` tool converts this to the `.tp`
file expected by lttng-ust.

The contents of this file specify the `TP_FIELDS` part for each
tracepoint. The `TP_ARGS` part is automatically generated from the
headers.

To add fields for a new API, you must add the appropriately-suffixed
(`_pre`, `_post` or both) to the `tracepoint_events`
dictionary. Assume we want to add fields for the `post` version of a
new API `cuExampleAPI(int arg1, int *arg2)`. We would write this as
the following entry in `tracepoint_events`:

```
   cuExampleAPI_post:
      fields:
         - arg1:
	     type: ctf_integer
	     type_args:
	        int_type: int
	 - arg2:
	     type: ctf_integer
	     type_args:
                int_type: int
		expr: "*arg2"
	 - *retval_field
         - *ctx_field
```

The entry is given the name of the tracepoint, here
`cuExampleAPI_post`. It contains a `fields` list that lists an entry
for each argument and corresponds to an entry in the `TP_FIELDS`
macro. Here we have two API arguments `arg1` and `arg2`, and two
additional fields. These are the standard fields `ctx_field` (which
assigns identifiers to individual API calls to make correlations
easier), and the standard `retval_field` which records the return
value of the API call for a `_post` tracepoint.

For each entry in `fields`, we need to specify the macro type used in
`TP_FIELDS`. For both arguments here, we use `ctf_integer`. We then
specify the arguments to `ctf_integer` in the `type_args`
dictionary. We use the [same
names](https://lttng.org/man/3/lttng-ust/v2.10/) for arguments to
`ctf_integer`. For `ctf_integer`, these are `int_type`, `field_name`
and `expr`. You can omit `field_name` and `expr`, as we have done for
`arg1` here. They will simply be set to `arg1`.

For `arg2`, we elect not to store the value of the pointer, but rather
its contents, hence `expr` is `"*int2"`. The quotes are necessary
because "`*`" is the indirection operator in YAML.

NOTE: Not all type macros are currently supported.

### Recording large amounts of data in the blobstore

TODO.

For now, look at the definition of `cuMemcpyHtoD_v2_pre` to see how
the blobstore can be used.

### The `optional` section in `libcuda_record_filter.yaml`

The `optional` section in `libcuda_record_filter.yaml` denotes API
calls that are not present in all versions. It suppresses error
messages about missing API calls.


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

# Copyright

SPDX-FileCopyrightText: 2019,2021,2023 University of Rochester

SPDX-License-Identifier: MIT


