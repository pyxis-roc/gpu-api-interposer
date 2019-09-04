GENINTERPOSER=../generator/geninterposer.py
GENTRACEPOINTS=../generator/gentracepoints.py
GENRECORDER=../generator/genrecorder.py
FAKE_C_HEADERS=/usr/share/python3-pycparser/fake_libc_include
#~/extsrc/pycparser/utils/fake_libc_include/
CUDA_INC=$(CUDA_LIB)/../include
CUDA_H=$(CUDA_INC)/cuda.h
BLOBSTORE=../blobstore
ARGHELPER=../arghelper
SONAME=libcuda.so.1
# do not include trailing / in BUILD_DIR
BUILD_DIR=build
OBJS=$(BUILD_DIR)/libcuda_passthru.so $(BUILD_DIR)/libcuda_trace.so $(BUILD_DIR)/libcuda_record.so $(BUILD_DIR)/record_cuda.sh


all: $(OBJS)

%.so: %.c
	gcc -g -fPIC -shared -Wl,--soname='$(SONAME)' $< -o $@ -ldl -I$(CUDA_INC)

$(BUILD_DIR)/libcuda_record.so: $(BUILD_DIR)/libcuda_record.c $(BUILD_DIR)/libcuda_record_instr.c $(BUILD_DIR)/libcuda_record_tp.o $(BLOBSTORE)/blobstore.o $(ARGHELPER)/arghelper.o
	gcc -g -fPIC -shared -Wl,--soname='$(SONAME)' $^ -o $@ -llttng-ust -ldl -lsqlite3 -I$(CUDA_INC) -I$(BLOBSTORE) -I$(ARGHELPER)

$(BUILD_DIR)/libcuda_passthru.c:
	$(GENINTERPOSER) --dlopen --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) -o $@

$(BUILD_DIR)/libcuda_trace.c:
	$(GENINTERPOSER) --dlopen --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) --trace -o $@

$(BUILD_DIR)/libcuda_record.c: libcuda_record_filter.yaml
	$(GENINTERPOSER) --dlopen --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) --ctx --pre-instrument --post-instrument --tpargs --filter $< --oprefix $(BUILD_DIR)/libcuda_record -o $@

$(BUILD_DIR)/libcuda_record_tp.o: libcuda_record_tp.yaml $(BUILD_DIR)/libcuda_record.c
	$(GENTRACEPOINTS) --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args $(CUDA_H) $< -o $(@:.o=.tp) --tpargs $(BUILD_DIR)/libcuda_record_tpargs.yaml --tpinfo $(BUILD_DIR)/libcuda_record_tpinfo.yaml
	CFLAGS="-fPIC -I$(CUDA_INC)" lttng-gen-tp -v $(@:.o=.tp)

ifneq ($(BUILD_DIR), .)
$(BUILD_DIR)/kernelparams.h: kernelparams.h
	cp $< $@

$(BUILD_DIR)/record_cuda.sh: record_cuda.sh
	cp $< $@
endif

$(BUILD_DIR)/libcuda_record_instr.c: $(BUILD_DIR)/libcuda_record_tp.o $(BUILD_DIR)/libcuda_record_tpinfo.yaml $(BUILD_DIR)/libcuda_record.c $(BUILD_DIR)/libcuda_record_pre_instr.h $(BUILD_DIR)/libcuda_record_post_instr.h $(BUILD_DIR)/kernelparams.h
	$(GENRECORDER) --fake-c-headers $(FAKE_C_HEADERS) --cppargsfile cuda_h_cpp_args --blobstore $(BUILD_DIR)/libcuda_record_tpinfo.yaml $(BUILD_DIR)/libcuda_record_pre_instr.h $(BUILD_DIR)/libcuda_record_post_instr.h -I$(CUDA_INC) -I$(BUILD_DIR) --include-local 'kernelparams.h' -o $@

$(BLOBSTORE)/blobstore.o:
	$(MAKE) -C $(BLOBSTORE)

$(ARGHELPER)/arghelper.o:
	$(MAKE) -C $(ARGHELPER)

.phony: clean

clean:
	rm -f $(OBJS)
