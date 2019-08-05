#!/usr/bin/env python3

import sys
import argparse
import pycparser
import subprocess
import tempfile
import os
import logging

def preprocess(infile, cpp_args_file = None):
    h, fn = tempfile.mkstemp(suffix = ".h")
    
    args = [infile, "-o", fn]
    
    if cpp_args_file is not None:
        with open(cpp_args_file, "r") as f:
            args = [s.strip() for s in f.readlines() if s[0] != "#"] + args

    cmd = ["cpp"] + args
    logging.info("Running " + " ".join(cmd))

    try:
        p = subprocess.run(cmd, check=True)
    except:
        raise

    os.close(h)
    return fn

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Generate a interceptor")
    p.add_argument("hfile", help="Include file")
    p.add_argument("--cppargsfile", help="File that contains C preprocessor arguments, one per line")

    args = p.parse_args()

    preprocessed = preprocess(args.hfile, args.cppargsfile)
    print(preprocessed)
    
