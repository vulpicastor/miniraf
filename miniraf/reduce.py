import numpy as np
import sys

from .util import load_fits_data

def create_parser(subparsers):
    parser_reduce = subparsers.add_parser("reduce", help="reduce images")
    parser_reduce.add_argument("-o", "--output", metavar="PATH", default="")
    parser_reduce.add_argument("-s", "--scale-dark", metavar="SCALE", type=float, default=1.)
    parser_reduce.add_argument("-d", "--dark", metavar="DARK", required=True)
    parser_reduce.add_argument("-b", "--bias", metavar="BIAS")
    parser_reduce.add_argument("-f", "--flat", metavar="FLAT")
    parser_reduce.add_argument("file", nargs="+")
    parser_reduce.set_defaults(func=main)

def _output_filename(filename, suffix="_out"):
    name, _ = filename.rsplit(".", maxsplit=1)
    return name + suffix + ".fits"

def main(args):
    subtractor = load_fits_data(args.dark)
    if args.scale_dark <= 0:
        raise ValueError("Dark scaling factor must be positive")
    elif args.scale_dark != 1:
        if "bias" not in args:
            raise ValueError("Wish to scale bias-subtracted dark, but no bias file given")
        bias = load_fits_data(args.bias)
        subtractor = (subtractor - bias) * args.scale_dark + bias
    for f in args.file:
        pass
