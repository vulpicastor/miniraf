import argparse
import astropy.io.fits as fits
import numpy as np

import calc
import combine

if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    subparsers = argparser.add_subparsers(help="sub-command help")
    calc.create_parser(subparsers)
    combine.create_parser(subparsers)
    args = argparser.parse_args()
    print(args)
    args.func(args)

