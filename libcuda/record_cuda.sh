#!/bin/bash

P=`dirname $0`

DLOPEN_LIBRARY=${DLOPEN_LIBRARY:-/usr/lib64/libcuda.so.1}
LD_PRELOAD=${LD_PRELOAD:-$P/libcuda_record.so}

lttng create cuda-record || exit 1;
lttng enable-event --userspace "libcuda_interposer:*" || exit 1;
lttng start || exit 1;

export DLOPEN_LIBRARY
export LD_PRELOAD
"$@"
unset DLOPEN_LIBRARY
unset LD_PRELOAD

lttng stop || exit 1;
lttng destroy || exit 1;
