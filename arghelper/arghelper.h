#pragma once
#include <stdint.h>

struct param_table {
  int fd;
  size_t length;
  unsigned char *oob;
  unsigned int version;
  unsigned int nsymbols;
  unsigned char **symbolnames;
  unsigned int *offsets;
  unsigned char *params;
  intptr_t *handles;
};

struct param_data {
  int narch;
  int nparams;
  unsigned char arch;
  unsigned char *param_sz;
  unsigned char *param_off;

  unsigned char *offset;
};


int ah_init_oob_param_table(const char *filename, struct param_table **ppt);
void ah_read_param_info_next(struct param_data *pd);
void ah_read_param_info_init(struct param_table *pt, int symbol, struct param_data *pd);
void ah_dump_param_table(struct param_table *pt);
int ah_find_symbol_index(struct param_table *pt, const char *symbol);
int ah_deinit_param_table(struct param_table *pt);
int ah_construct_arg_blob(struct param_table *pt, int symbol, int arch,
						  void **args, unsigned char *argblob);
int ah_find_symbol_index_by_handle(struct param_table *pt, const void *handle);
