#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>
#include "arghelper.h"

int ah_init_oob_param_table(const char *filename, struct param_table **ppt) {
  struct stat sb;
  struct param_table *pt;
  
  pt = (struct param_table *) calloc(1, sizeof(struct param_table));

  pt->fd = open(filename, O_RDONLY);
  if(pt->fd == -1) {
	fprintf(stderr, "ERROR: Unable to open OOB parameter table '%s' (%d: %s)\n", filename, errno, strerror(errno));

	free(pt);
	return 0;
  }

  if(fstat(pt->fd, &sb) == -1) {
	fprintf(stderr, "ERROR: Unable to fstat '%s' (%d: %s)\n", filename, errno, strerror(errno));
	goto err_pre_mmap;
  }
  pt->length = sb.st_size;
  
  if((pt->oob = mmap(NULL, pt->length, PROT_READ, MAP_PRIVATE, pt->fd, 0)) == MAP_FAILED) {
	fprintf(stderr, "ERROR: Unable to mmap '%s' (%d: %s)\n", filename, errno, strerror(errno));
	goto err_pre_mmap;
  }

  // this will cause issues if stored in network byte order...
  pt->version = *((unsigned int *) pt->oob);
  
  if(pt->version != 1) {
	fprintf(stderr, "ERROR: Unrecognized version %d, only recognize 1\n", pt->version);
	goto err_post_mmap;
  }

  pt->nsymbols = ((unsigned int *) pt->oob)[1];
  pt->symbolnames = (unsigned char **) calloc(pt->nsymbols, sizeof(unsigned char *));
  if(!pt->symbolnames) {
	fprintf(stderr, "ERROR: Unable to allocate memory for symbol names (%d: %s)\n", errno, strerror(errno));
	goto err_post_mmap;
  }


  pt->handles = (intptr_t *) calloc(pt->nsymbols, sizeof(intptr_t *));
  if(!pt->handles) {
	fprintf(stderr, "ERROR: Unable to allocate memory for handles (%d: %s)\n", errno, strerror(errno));
	goto err_post_alloc;
  }
  
  unsigned int strtablen = ((unsigned int *) pt->oob)[2];
  unsigned char *name = pt->oob + 12;
  
  int i;
  for(i = 0; i < pt->nsymbols; i++) {
	pt->symbolnames[i] = name;

	while(*name++ != '\0')
	  ;
  }

  pt->offsets = (unsigned int *) (pt->oob + 12 + strtablen);
  pt->params = pt->oob + 12 + strtablen + pt->nsymbols * sizeof(pt->offsets[0]);

  *ppt = pt;
  
  return 1;

 err_post_alloc:
  if(pt->symbolnames) free(pt->symbolnames);
 err_post_mmap:
  munmap(pt->oob, pt->length);
 err_pre_mmap:
  close(pt->fd);
  free(pt);
  return 0;
}

void ah_read_param_info_next(struct param_data *pd) {
  pd->arch = *pd->offset++;
  pd->nparams = *pd->offset++;
  if(pd->nparams > 0) {
	pd->param_sz = pd->offset;
	pd->param_off = pd->param_sz + pd->nparams;
  }
  pd->offset += pd->nparams * 2;
}

void ah_read_param_info_init(struct param_table *pt, int symbol, struct param_data *pd) {

  pd->offset = pt->params + pt->offsets[symbol];
  pd->narch = *pd->offset++;
  pd->nparams = 0;
  
  for(int i = 0; i < pd->narch && i < 1; i++) {
	ah_read_param_info_next(pd);
  }
}

void ah_dump_param_table(struct param_table *pt) {
  int i;
  struct param_data pd;
  
  printf("%d entries\n", pt->nsymbols);
  for(int i = 0; i < pt->nsymbols; i++) {
	printf("%d: %s\n", i, pt->symbolnames[i]);

	ah_read_param_info_init(pt, i, &pd);

	printf("  narch: %d\n", pd.narch);

	for(int k = 0; k < pd.narch; k++) {
	  printf("    arch: %d, nparams: %d\n", pd.arch, pd.nparams);
		
	  for(int j = 0; j < pd.nparams; j++) {
		printf("\t%d (off: %d)\n", pd.param_sz[j], pd.param_off[j]);
	  }
	  printf("\n");
	  ah_read_param_info_next(&pd);
	}
  }
}

int ah_find_symbol_index(struct param_table *pt, const char *symbol) {
  int low, high, mid;
  int c;
  
  low = 0;
  high = pt->nsymbols - 1;

  while(low <= high) {
	mid = (low + high) / 2;

	c = strcmp(symbol, pt->symbolnames[mid]) ;
	if(c == 0)
	  return mid;

	if(c > 0) {
	  low = mid + 1;
	} else {
	  high = mid - 1;
	}
  }

  return -1;
}

int ah_find_symbol_index_by_handle(struct param_table *pt, const void *handle) {
  /* unfortunately, this is linear search :(, possibly switch to a hash table */
  for(int i = 0; i < pt->nsymbols; i++) {
	if(pt->handles[i] == (intptr_t) handle) return i;
  }
  
  return -1;
}


int ah_register_handle_for_symbol(struct param_table *pt, const void *handle, const char *symbol) {
  int sndx;
  
  if((sndx = ah_find_symbol_index(pt, symbol)) != -1) {
	pt->handles[sndx] = (intptr_t) handle;
  } else {
	fprintf(stderr, "WARNING:arghelper: Unable to find symbol '%s' to register handle\n", symbol);
  }
}

int ah_deinit_param_table(struct param_table *pt) {
  free(pt->symbolnames);
  munmap(pt->oob, pt->length);
  close(pt->fd);
  free(pt);
  return 1;
}

#ifdef MAIN
int main(int argc, char *argv[]) {
  if(argc == 1) {
	fprintf(stderr, "Usage: %s argfile\n", argv[0]);
	exit(1);
  }

  struct param_table *pt;
  
  if(ah_init_oob_param_table(argv[1], &pt)) {
	ah_dump_param_table(pt);

	assert(ah_find_symbol_index(pt, "") == -1);
	
	for(int i = 0; i < pt->nsymbols; i++) {
	  int j;
	  j = ah_find_symbol_index(pt, pt->symbolnames[i]);
	  assert(i == j);
	}
	
	ah_deinit_param_table(pt);
  }
}
#endif
