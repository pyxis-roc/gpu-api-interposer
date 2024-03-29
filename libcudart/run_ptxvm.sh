#!/bin/bash

# SPDX-FileCopyrightText: 2021 University of Rochester
#
# SPDX-License-Identifier: MIT

function usage() {
    echo Usage: $0 [-l rtlibrary] ptx_module binary [args...]
}

if [ $# -lt 2 ]; then
    usage
    exit 0
fi;

while getopts "hl:" arg; do
    case $arg in
        h)
            usage
            exit 0
            ;;
        l)
            LIBRARY=$OPTARG
            ;;
        ?)
        usage
        exit 1
        ;;
    esac
done

shift $((OPTIND-1))

if [ $# -lt 2 ]; then
   usage
   exit 1
fi;

if [ -z "$LIBRARY" ]; then
    LIBRARY=`dirname $0`/../lib/libcudart_intercept.so
fi;

LIBRARY_DIR=`dirname $LIBRARY`

if [ ! -f "$LIBRARY" ]; then
    echo "CUDA interception library not found. $LIBRARY does not exist. Specify the path using -l"
    exit 1;
fi;

if [ ! "$1" == "no" ]; then
    #PTX_MODULE=`realpath "$1"`
    PTX_MODULE=$1
    # echo "PTX_MODULE is set to $PTX_MODULE"
else
    PTX_MODULE=$1
fi;
shift;

LD_LIBRARY_PATH=$LIBRARY_DIR:$LD_LIBRARY_PATH LD_PRELOAD=$LIBRARY PTX_MODULE=$PTX_MODULE "$@"
