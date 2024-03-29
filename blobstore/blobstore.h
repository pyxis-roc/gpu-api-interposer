/*
   blobstore.h

   Instrumentation helper to store blobs too large for traces in sqlite3 databases.

   Author: Sreepathi Pai

   Copyright (C) 2019,2023 The University of Rochester

   SPDX-FileCopyrightText: 2019,2023 University of Rochester

   SPDX-License-Identifier: MIT
*/

#pragma once

typedef struct blobstore * blobstore;

int bs_create(const char *filename, blobstore *bs);
int bs_store(blobstore bs, int ctx, const char *name, const void *blob, size_t blobsize);
int bs_close(blobstore bs);
