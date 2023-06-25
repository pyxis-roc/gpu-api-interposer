# SPDX-FileCopyrightText: 2019,2023 University of Rochester
#
# SPDX-License-Identifier: MIT

CC=gcc
CFLAGS=-fPIC

all: blobstore.o

blobstore.o: blobstore.c blobstore.h
	$(CC) $(CFLAGS) -c -g -O $< -o $@
