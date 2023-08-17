This repository contains a collection of related software for the
interception of CUDA API calls.  For the moment, it also contains
`harmonv`, a set of tools for manipulation of NVIDIA fat binaries
among other things.

# Library Interposer generation tools

The `generator` directory contains a set of utilities for the
automatic generation of library interposers from header files. These
can then be used through the `LD_PRELOAD` mechanism to intercept API
calls to shared libraries.

The `libcuda` and `libcuda-rt` contain examples of how the generator
tools are used to generate interposers for the CUDA Device API and the
CUDA Runtime API respectively.

The `blobstore` directory contains a library that can be used by
interposers to store large blobs of binary data in a SQLite3 database.

The `arghelper` directory contains a utility to parse arguments passed
to CUDA kernels when they are launched, converting them to blobs that
can then be stored in the trace.

# harmonv

The `harmonv` directory is not directly linked to the interposition
generation tools, but is often used by them.

Its primary purpose is to provide substitutions for tools like
NVIDIA's `cuobjdump`, but through a Python library interface.






