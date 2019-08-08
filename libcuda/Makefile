GENINTERPOSER=../generator/geninterposer.py
GENTRACEPOINTS=../generator/gentracepoints.py
FAKE_C_HEADERS=~/extsrc/pycparser/utils/fake_libc_include/
CUDA_INC=$(CUDA_LIB)/../include
CUDA_H=$(CUDA_INC)/cuda.h
SONAME=libcuda.so.1
OBJS=libcuda_passthru.so libcuda_trace.so libcuda_record.c

all: $(OBJS)

%.so: %.c
	gcc -g -fPIC -shared -Wl,--soname='$(SONAME)' $< -o $@ -ldl -I/usr/local/cuda/include

libcuda_record.so: libcuda_record.c libcuda_record_instr.c libcuda_record-tracepoints.o
	gcc -g -fPIC -shared -Wl,--soname='$(SONAME)' $^ -o $@ -ldl -I/usr/local/cuda/include

libcuda_passthru.c:
	$(GENINTERPOSER) --dlopen --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) -o $@

libcuda_trace.c:
	$(GENINTERPOSER) --dlopen --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) --trace -o $@

libcuda_record.c: libcuda.tp
	$(GENINTERPOSER) --dlopen --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) --pre-instrument --post-instrument --filter libcuda_record_filter.yaml --oprefix libcuda_record -o $@

libcuda_record-tracepoints.o: libcuda_record_tp.yaml
	$(GENTRACEPOINTS) --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) $< -o $(@:.o=.tp) --oprobes libcuda_record_probes.yaml
	CFLAGS="-fPIC -I$(CUDA_INC)" lttng-gen-tp -v $(@:.o=.tp)

.phony: clean

clean:	
	rm -f $(OBJS) 
