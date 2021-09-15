GENINTERPOSER=../generator/geninterposer.py
GENTRACEPOINTS=../generator/gentracepoints.py
GENRECORDER=../generator/genrecorder.py
FAKE_C_HEADERS ?= /usr/share/python3-pycparser/fake_libc_include

#~/extsrc/pycparser/utils/fake_libc_include/
CUDA_HOME ?= /usr/local/cuda
CUDA_INC=$(CUDA_HOME)/include
CUDA_H=$(CUDA_INC)/cuda_runtime_api.h
BLOBSTORE=../blobstore
ARGHELPER=../arghelper
SO=libcudart.so.11.0

ifeq ($(shell test -f $(SO) || echo 'doesnotexist'),doesnotexist)
$(error SO=$(SO) does not exist, specify a valid path to libcudart.so)
endif

SONAME=$(shell objdump -p $(SO) | grep SONAME | awk '{print $$2}')
# do not include trailing / in BUILD_DIR
BUILD_DIR=build
OBJS=$(BUILD_DIR)/libcudart_passthru.so $(BUILD_DIR)/libcudart_trace.so $(BUILD_DIR)/libcudart_intercept.so $(BUILD_DIR)/$(SONAME)


all: $(OBJS)

%.so: %.c
	gcc -g -fPIC -shared -Wl,--soname='$(SONAME)' $< -o $@ -I$(CUDA_INC) -I$(COMPAT_INC) $(COMPAT_LIBS) -ldl

$(BUILD_DIR)/completed: $(COMPAT_INC)/ptxvm_compatrt.h
	grep --only-matching 'ptxvm_.*(' $< | sed 's/(//g' > $@

$(BUILD_DIR)/$(SONAME): $(BUILD_DIR)/libcudart_intercept.so
	ln -s $< $@
	ln -sf $< $(BUILD_DIR)/libcudart.so

$(BUILD_DIR)/libcudart_passthru.c: undocumented.h
	$(GENINTERPOSER) --undocumented undocumented.h --dlopen --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) -o $@

$(BUILD_DIR)/libcudart_trace.c: undocumented.h
	$(GENINTERPOSER) --undocumented undocumented.h --dlopen --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) --trace -o $@

$(BUILD_DIR)/libcudart_intercept.c: undocumented.h intercept.yaml $(BUILD_DIR)/completed
	$(GENINTERPOSER) --undocumented undocumented.h --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) --intercept intercept.yaml -o $@ --oprefix $(BUILD_DIR)/cuda_runtime_api --completed $(BUILD_DIR)/completed

.phony: clean

clean:
	rm -f $(OBJS)
