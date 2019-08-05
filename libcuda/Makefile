GENINTERPOSER=../generator/geninterposer.py
FAKE_C_HEADERS=~/extsrc/pycparser/utils/fake_libc_include/
CUDA_H=/usr/local/cuda/include/cuda.h
SONAME=libcuda.so.1

all: libcuda_passthru.so libcuda_trace.so

%.so: %.c
	gcc -g -fPIC -shared -Wl,--soname='$(SONAME)' $< -o $@ -ldl -I/usr/local/cuda/include

libcuda_passthru.c:
	$(GENINTERPOSER) --dlopen --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) -o $@

libcuda_trace.c:
	$(GENINTERPOSER) --dlopen --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) --trace -o $@
