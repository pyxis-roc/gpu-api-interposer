#!/usr/bin/env python3

import argparse
import sys
import yaml

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Identify API functions that are not instrumented.")
    p.add_argument("trace", help="File generated by libx_trace")
    p.add_argument("filteryaml", help="Filter YAML")
    
    args = p.parse_args()
    
    with open(args.trace, "r") as f:
        tracefns = set([x.strip() for x in f.readlines()])

    with open(args.filteryaml, "r") as f:
        filtered = yaml.safe_load(f)
        filtered = set(filtered.get('pre_and_post', [])) | set(filtered.get('post', [])) | set(filtered.get('pre', []))

        missing = tracefns - filtered
        if missing:
            for fn in missing:
                print(fn)

        sys.exit(1 if len(missing) else 0)