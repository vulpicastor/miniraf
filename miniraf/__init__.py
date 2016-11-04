import argparse

import calc
import combine
import map as mmap

from combine import stack_fits_data
from calc import load_fits_data

def _make_argparser():
    argparser = argparse.ArgumentParser()
    subparsers = argparser.add_subparsers(help="sub-command help")
    calc.create_parser(subparsers)
    combine.create_parser(subparsers)
    mmap.create_parser(subparsers)
    return argparser

def main():
    argparser = _make_argparser()
    args = argparser.parse_args()
    if "func" in args:
        args.func(args)
    else:
        raise NotImplementedError("REPL mode not implemented. Pass -h for help.")

if __name__=="__main__":
    main()
