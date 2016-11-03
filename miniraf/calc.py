import argparse
from astropy.io import fits
import sys

OP_MAP = {"+": lambda x, y: x + y,
          "-": lambda x, y: x - y,
          "*": lambda x, y: x * y,
          "/": lambda x, y: x / y}

def create_parser(subparsers):
    parser_calc = subparsers.add_parser("calc", help="calc help")
    parser_calc.add_argument("-o", "--output", metavar="OUTFILE", default=sys.stdout.buffer)
    parser_calc.add_argument("file1")
    parser_calc.add_argument("op", choices=["+", "-", "*", "/"])
    parser_calc.add_argument("file2")
    parser_calc.set_defaults(func=main)

def load_fits_data(filename):
    with fits.open(filename) as f:
        data = f[0].data
    return data

def main(args):
    a, b = load_fits_data(args.file1), load_fits_data(args.file2)
    result = OP_MAP[args.op](a, b)
    hdu = fits.PrimaryHDU(result)
    hdu.writeto(args.output)
