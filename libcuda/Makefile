GENINTERPOSER=../generator/geninterposer.py
GENTRACEPOINTS=../generator/gentracepoints.py
GENRECORDER=../generator/genrecorder.py
FAKE_C_HEADERS=~/extsrc/pycparser/utils/fake_libc_include/
CUDA_INC=$(CUDA_LIB)/../include
CUDA_H=$(CUDA_INC)/cuda.h
SONAME=libcuda.so.1
OBJS=libcuda_passthru.so libcuda_trace.so libcuda_record.so

all: $(OBJS)

%.so: %.c
	gcc -g -fPIC -shared -Wl,--soname='$(SONAME)' $< -o $@ -ldl -I$(CUDA_INC)

libcuda_record.so: libcuda_record.c libcuda_record_instr.c libcuda_record_tp.o
	gcc -g -fPIC -shared -Wl,--soname='$(SONAME)' $^ -o $@ -llttng-ust -ldl -I$(CUDA_INC)

libcuda_passthru.c:
	$(GENINTERPOSER) --dlopen --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) -o $@

libcuda_trace.c:
	$(GENINTERPOSER) --dlopen --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) --trace -o $@

libcuda_record.c: 
	$(GENINTERPOSER) --dlopen --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) --ctx --pre-instrument --post-instrument --tpargs --filter libcuda_record_filter.yaml --oprefix libcuda_record -o $@

libcuda_record_tp.o: libcuda_record_tp.yaml libcuda_record_tpargs.yaml
	$(GENTRACEPOINTS) --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) $< -o $(@:.o=.tp) --tpargs libcuda_record_tpargs.yaml --tpinfo libcuda_record_tpinfo.yaml
	CFLAGS="-fPIC -I$(CUDA_INC)" lttng-gen-tp -v $(@:.o=.tp)

libcuda_record_instr.c: libcuda_record_tp.o libcuda_record_tpinfo.yaml libcuda_record.c libcuda_record_pre_instr.h libcuda_record_post_instr.h
	$(GENRECORDER) --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args libcuda_record_tpinfo.yaml libcuda_record_pre_instr.h libcuda_record_post_instr.h -I$(CUDA_INC) -o $@

.phony: clean

clean:	
	rm -f $(OBJS) 
