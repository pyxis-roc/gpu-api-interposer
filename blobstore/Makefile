CC=gcc
CFLAGS=-fPIC

all: blobstore.o

blobstore.o: blobstore.c blobstore.h
	$(CC) $(CFLAGS) -c -g -O $< -o $@
