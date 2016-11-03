import argparse

import calc
import combine

from combine import stack_fits_data
from calc import load_fits_data

def _argparse():
    argparser = argparse.ArgumentParser()
    subparsers = argparser.add_subparsers(help="sub-command help")
    calc.create_parser(subparsers)
    combine.create_parser(subparsers)
    return argparser.parse_args()

def main():
    args = _argparse()
    args.func(args)

if __name__=="__main__":
    main()
