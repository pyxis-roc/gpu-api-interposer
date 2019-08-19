#pragma once

#include <arghelper.h>
#include <stdio.h>
#include <stdlib.h>

static struct param_table *pt;

static int get_arg_blob_extra(CUfunction f, void **extra, unsigned char *argblob) {
  return ah_construct_arg_blob_extra(pt, extra, argblob);
}

static int get_arg_blob(CUfunction f, void **kernelParams, unsigned char *argblob) {
  int symbol;

  if(!pt) return 0;
  
  symbol = ah_find_symbol_index_by_handle(pt, f);
  if(symbol == -1) {
	fprintf(stderr, "ERROR: Couldn't find symbol index for handle %p\n", f);
	return 0;
  }

  return ah_construct_arg_blob(pt, symbol, 0 /* TODO */, kernelParams, argblob);
}

static __attribute__((constructor)) void arghelper_init() {
  char *argsfile = getenv("ARGHELPER_FILE");

  if(argsfile == NULL) {
    fprintf(stderr, "WARNING: ARGHELPER_FILE is not set, arguments will not be saved.\n");
    return;
  }

  if(!ah_init_oob_param_table(argsfile, &pt)) {
	fprintf(stderr, "ERROR: ARGHELPER_FILE '%s' could not be read, arguments will not be saved.\n", argsfile);
	return;
  }

  /* ah_dump_param_table(pt); */
}

static __attribute__((destructor)) void arghelper_deinit() {
  if(pt) {
	ah_deinit_param_table(pt);
	pt = NULL;
  }
}
