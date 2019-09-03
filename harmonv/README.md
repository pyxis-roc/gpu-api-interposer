The `harmonv` package aims to provide tools and utilities for working
with NVIDIA's closed-source toolchain.

The name `harmonv` is meant to invoke ``harmony", and is inspired from
previous harmony projects. Hopefully, we'll also retire this project
someday.

Obviously, this is unaffiliated with NVIDIA.

# Pre-requisites

You'll need the following Python3 packages

  - pyelftools

# Installation

You can install this package by running:

     python3 setup.py develop

Which will setup the package for development.

# Components

## nvfatbin.py

This contains tools for working with NVIDIA Fat Binaries and CUBIN files.

## ptxextract.py

This extracts compressed PTX files from NVIDIA Fat Binaries. It
currently requires `cuobjdump` to decompress the files.