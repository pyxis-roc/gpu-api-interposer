#include <sqlite3.h>
#include <stdio.h>
#include <stdlib.h>
#include "blobstore.h"

struct blobstore {
  sqlite3 *db;
  sqlite3_stmt *insert_stmt;
  size_t max_blob_size;
};

typedef struct blobstore * blobstore;

int bs_create(const char *filename, blobstore *pbs) {
  int err;
  char *errmsg = NULL;
  blobstore bs;

  *pbs = (blobstore) malloc(sizeof(struct blobstore));
  bs = *pbs;
  bs->max_blob_size = 768*1048576; // 768MB, but really ask SQLite what this is...

  if((err = sqlite3_open(filename, &(bs->db))) != SQLITE_OK) {
    fprintf(stderr, "ERROR:bs_initialize: Could not open '%s': %s\n", filename, 
	    sqlite3_errstr(err));

    free(bs);
    bs = NULL;

    return 0;
  }

  if(sqlite3_exec(bs->db, 
		  "CREATE TABLE blobstore (ctx INTEGER, content_part INTEGER, name TEXT NOT NULL, contents BLOB, PRIMARY KEY (ctx, content_part));",
		  NULL,
		  NULL,
		  &errmsg) != SQLITE_OK) {
    
    fprintf(stderr, "ERROR:bs_initialize: Could not create table: %s\n", errmsg);
    sqlite3_free(errmsg);
    sqlite3_close(bs->db);

    bs->db = NULL;
    free(bs);
    bs = NULL;

    return 0;
  }

  if(sqlite3_prepare_v2(bs->db, 
			"INSERT INTO blobstore(ctx, content_part, name, contents) VALUES (?,?,?,?);",
			-1, /* zero terminated */
			&(bs->insert_stmt),
			NULL) != SQLITE_OK) {

    fprintf(stderr, "ERROR:bs_initialize: Could not prepare statement: %s\n", sqlite3_errmsg(bs->db));

    sqlite3_close(bs->db);
    bs->db = NULL;
    free(bs);
    bs = NULL;    
  } 

  
  return 1;
}

int bs_store(blobstore bs, int ctx, const char *name, const void *blob, size_t blobsize) {
  int err;
  int retval = 1;

  if(blobsize > bs->max_blob_size) {
    fprintf(stderr, "WARNING: Do not support blob size %lu (i.e. multipart blobs) yet!\n", blobsize);
    return 0;
  }
  
  if((err = sqlite3_bind_int(bs->insert_stmt, 1, ctx)) != SQLITE_OK) {
    fprintf(stderr, "ERROR:bs_store: Failed to bind ctx value: %s\n", sqlite3_errstr(err));
    return 0;
  }
  
  if((err = sqlite3_bind_text(bs->insert_stmt, 3, name, -1, SQLITE_TRANSIENT)) != SQLITE_OK) {
      fprintf(stderr, "ERROR:bs_store: Failed to bind name value: %s\n", sqlite3_errstr(err));
      return 0;
  }

  if((err = sqlite3_bind_int(bs->insert_stmt, 2, 1)) != SQLITE_OK) {  /* part */
    fprintf(stderr, "ERROR:bs_store: Failed to bind part value : %s\n", sqlite3_errstr(err));
    return 0;
  }

  if(blob == NULL || blobsize == 0) {
    err = sqlite3_bind_null(bs->insert_stmt, 4);
  } else {
    err = sqlite3_bind_blob(bs->insert_stmt, 4, blob, blobsize, SQLITE_TRANSIENT);
  }

  if(err != SQLITE_OK) {
    fprintf(stderr, "ERROR:bs_store: Failed to bind blob value: %s\n", sqlite3_errstr(err));
    return 0;
  }

  if((err = sqlite3_step(bs->insert_stmt)) != SQLITE_DONE) {
    fprintf(stderr, "ERROR:bs_store: Failed to store blob!: %s\n", sqlite3_errstr(err));

    retval = 0;
  }

  if((err = sqlite3_reset(bs->insert_stmt)) != SQLITE_OK) {
    fprintf(stderr, "ERROR:bs_store: Failed to reset: %s\n", sqlite3_errstr(err));

    retval = 0;
  }

  /* not sure if this returns SQLITE_OK */
  if((err = sqlite3_clear_bindings(bs->insert_stmt)) != SQLITE_OK) {
    fprintf(stderr, "ERROR:bs_store: Failed to clear bindings: %s\n", sqlite3_errstr(err));

    retval = 0;
  }

  return retval;
}

int bs_close(blobstore bs) {
  int err;

  if((err = sqlite3_finalize(bs->insert_stmt)) != SQLITE_OK) {
    fprintf(stderr, "ERROR:bs_close: Failed to finalize statement: %s\n", sqlite3_errstr(err));
    /* okay to ignore, causes leak though */
  } 

  if(sqlite3_close(bs->db) != SQLITE_OK) {
    fprintf(stderr, "ERROR:bs_close: Could not close database: %s\n", 
	    sqlite3_errmsg(bs->db));
    return 0;
  }

  bs->db = NULL;
  free(bs);

  return 1;
}

#ifdef IS_MAIN
int main(void) {
  blobstore bs;
  int *x;
  int i;

  if(bs_create("test.db", &bs)) {
    bs_store(bs, 1, "test", NULL, 0);

    x = (int *) malloc(1024*sizeof(int));
    for(i = 0; i < 1024; i++) x[i] = i;

    bs_store(bs, 2, "test", x, sizeof(int) * 1024);    

    bs_close(bs);
  }
}
#endif
