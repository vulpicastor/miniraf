import argparse

from . import calc
from . import combine
from . import map as mmap
from . import stats

from .util import *

def _make_argparser():
    argparser = argparse.ArgumentParser()
    subparsers = argparser.add_subparsers(help="sub-command help")
    calc.create_parser(subparsers)
    combine.create_parser(subparsers)
    mmap.create_parser(subparsers)
    stats.create_parser(subparsers)
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
