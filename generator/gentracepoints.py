#!/usr/bin/env python3

import argparse
import sys


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Generate a tracepoint template for a header file")
    p.add_argument("header", help="C header file")
    p.add_argument("tp_recipe.yaml", help="Tracepoint recipe")
    p.add_argument("-o", "--output", help="Output template file")

    args = p.parse_args()

    
