The `harmonv` package aims to provide tools and utilities for working
with NVIDIA's closed-source toolchain.

The name `harmonv` is meant to invoke ``harmony", and is inspired from
previous harmony projects. Hopefully, we'll also retire this project
someday.

Obviously, this is unaffiliated with NVIDIA.

# Pre-requisites

You'll need the following Python3 packages

  - pyelftools
  - lz4

# Installation

You can install this package by running:

     python3 setup.py develop

Which will setup the package for development.

# Components

## nvfatbin.py

This library contains tools for working with NVIDIA Fat Binaries and
CUBIN files.

## fbextractor.py

This extracts PTX and ELF files from NVIDIA Fat Binaries. It requires
`cuobjdump` or the `lz4` library to decompress sections.

## hcuobjdump

A primitive version of `cuobjdump` intended as a demonstration.

## gen_xlat_metadata.py

A utility to extract all information from a CUDA binary that is
necessary for translation into a JSON file.

# Copyright

SPDX-FileCopyrightText: 2019,2021 University of Rochester

SPDX-License-Identifier: MIT

