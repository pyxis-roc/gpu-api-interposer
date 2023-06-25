#!/bin/bash

# SPDX-FileCopyrightText: 2021 University of Rochester
#
# SPDX-License-Identifier: MIT

P=`dirname $0`
if [ -z "$VIRTUAL_ENV" ]; then
    echo "No VIRTUAL_ENV detected. Set VIRTUAL_ENV to /usr/local if you want a system-wide install."
    exit 1;
fi;

bindir=$VIRTUAL_ENV/bin
libdir=$VIRTUAL_ENV/lib

ln -vsr $P/run_ptxvm.sh $bindir/
ln -vsr $P/build/libcudart_intercept.so $libdir/
ln -vsr $P/build/libcudart.so* $libdir/
