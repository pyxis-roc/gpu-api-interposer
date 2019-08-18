#!/bin/bash

P=`dirname $0`

if [ $# -lt 1 ]; then
    echo "Usage: $0 command..."
    exit 1;
fi;

DLOPEN_LIBRARY=${DLOPEN_LIBRARY:-/usr/lib64/libcuda.so.1}
LD_PRELOAD=${LD_PRELOAD:-$P/libcuda_record.so}
BLOBSTORE_PATH=`mktemp cuda-record-bs-XXXXXX.db`

if [ -f "${1}.arg" ]; then
	ARGHELPER_FILE="${1}.arg"
fi;

echo "BLOBSTORE_PATH=$BLOBSTORE_PATH"
echo "ARGHELPER_FILE=$ARGHELPER_FILE"
lttng create cuda-record || exit 1;
lttng enable-event --userspace "libcuda_interposer:*" || exit 1;
lttng start || exit 1;

export DLOPEN_LIBRARY
export LD_PRELOAD
export BLOBSTORE_PATH
export ARGHELPER_FILE
"$@"
unset ARGHELPER_FILE
unset BLOBSTORE_PATH
unset DLOPEN_LIBRARY
unset LD_PRELOAD

lttng stop || exit 1;
lttng destroy || exit 1;
