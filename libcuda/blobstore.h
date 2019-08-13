#pragma once

typedef struct blobstore * blobstore;

int bs_initialize(const char *filename, blobstore *bs);
int bs_store(blobstore bs, int ctx, const char *name, void *blob, size_t blobsize);
int bs_close(blobstore bs);
