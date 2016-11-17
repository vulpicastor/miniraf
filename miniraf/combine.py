import astropy.io.fits as fits
import numpy as np
import sys

from .util import stack_fits_data

METHOD_MAP = {"median": lambda x: np.median(x, axis=0, overwrite_input=True),
              "average": lambda x: np.mean(x, axis=0),
              "sum": lambda x: np.sum(x, axis=0)}

SCALE_MAP = {"median": lambda a: a / np.median(a),
             "average": lambda a: a / np.mean(a),
            }

def create_parser(subparsers):
    parser_combine = subparsers.add_parser("combine", help="combine help")
    parser_combine.add_argument("-m", "--method", choices=["median", "average", "sum"], required=True)
    parser_combine.add_argument("-s", "--scale", choices=["median", "average"])
    parser_combine.add_argument("-o", "--output", metavar="OUTFILE", default=sys.stdout.buffer)
    parser_combine.add_argument("file", nargs="+")
    parser_combine.set_defaults(func=main)

def main(args):
    if args.scale is None:
        image_stack = stack_fits_data(args.file)
    else:
        image_stack = stack_fits_data(args.file, SCALE_MAP[args.scale])
    result = METHOD_MAP[args.method](image_stack)
    hdu = fits.PrimaryHDU(result)
    hdu.writeto(args.output)
