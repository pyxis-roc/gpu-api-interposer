#!/bin/bash

P=`dirname $0`

if [ $# -lt 1 ]; then
    echo "Usage: $0 command..."
    exit 1;
fi;

# attempt to locate libcuda.so.1
for x in "$DLOPEN_LIBRARY" /usr/lib64/libcuda.so.1 /usr/lib/x86_64-linux-gnu/libcuda.so.1; do
    if [ -f "$x" ]; then
	DLOPEN_LIBRARY=$x
	break;
    fi;
done;

if [ ! -f "$DLOPEN_LIBRARY" ]; then
    echo "Could not locate libcuda.so.1 in the usual places, set DLOPEN_LIBRARY to point to libcuda.so.1"
    exit 1;
fi;

TS=`date +%Y%m%d-%H%M%S` # use lttng-like format
LD_PRELOAD=${LD_PRELOAD:-$P/libcuda_record.so}
BLOBSTORE_PATH=`mktemp cuda-record-bs-$TS-XXXXXX.db`

if [ -z "$DEBUG" ]; then
    ARGHELPER_FILE=${ARGHELPER_FILE:-${1}.arg}
else
    # assume $1 is gdb
    ARGHELPER_FILE=${ARGHELPER_FILE:-${2}.arg}
    unset BLOBSTORE_PATH
fi;

if [ ! -f "$ARGHELPER_FILE" ]; then
    # attempt to create argfile if one does not exist
    if ! "$P/nvparams.py" "$1" "$ARGHELPER_FILE"; then
	echo "Couldn't create/access '$ARGHELPER_FILE'"
	exit 1;
    fi;
fi;

echo "DLOPEN_LIBRARY=$DLOPEN_LIBRARY"
echo "BLOBSTORE_PATH=$BLOBSTORE_PATH"
echo "ARGHELPER_FILE=$ARGHELPER_FILE"

lttng create cuda-record || exit 1;
lttng enable-event --userspace "libcuda_interposer:*" || exit 1;
lttng add-context --userspace -t vtid || exit 1;
lttng start || exit 1;

export DLOPEN_LIBRARY
export LD_PRELOAD
[ -z "$DEBUG" ] && export BLOBSTORE_PATH
export ARGHELPER_FILE
"$@"
unset ARGHELPER_FILE
unset BLOBSTORE_PATH
unset DLOPEN_LIBRARY
unset LD_PRELOAD

lttng stop || exit 1;
lttng destroy || exit 1;
