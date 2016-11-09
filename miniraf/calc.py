from astropy.io import fits
import sys

from .util import load_fits_data

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

def main(args):
    a, b = load_fits_data(args.file1), load_fits_data(args.file2)
    result = OP_MAP[args.op](a, b)
    hdu = fits.PrimaryHDU(result)
    hdu.writeto(args.output)
