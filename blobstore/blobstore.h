#pragma once

typedef struct blobstore * blobstore;

int bs_create(const char *filename, blobstore *bs);
int bs_store(blobstore bs, int ctx, const char *name, const void *blob, size_t blobsize);
int bs_close(blobstore bs);
