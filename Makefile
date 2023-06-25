# SPDX-FileCopyrightText: 2021,2023 University of Rochester
#
# SPDX-License-Identifier: MIT

LIBCUDA_BUILD_DIR ?= build

all:

.PHONY: libcuda

libcuda:
	mkdir -p libcuda/$(LIBCUDA_BUILD_DIR)
	$(MAKE) -C libcuda BUILD_DIR=$(LIBCUDA_BUILD_DIR)
