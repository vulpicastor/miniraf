import astropy.io.fits as fits
import numpy as np
import sys

METHOD_MAP = {"median": lambda x: np.median(x, axis=0, overwrite_input=True),
              "average": lambda x: np.average(x, axis=0),
              "sum": lambda x: np.sum(x, axis=0)}

def stack_fits_data(filenames):
    fits_files = []
    filesdict = {}
    for f in filenames:
        if f not in filesdict:
            filesdict[f] = fits.open(f)
        fits_files.append(filesdict[f])
    stack = np.stack((f[0].data for f in fits_files), axis=0)
    for _, v in filesdict.items():
        v.close()
    return stack

def create_parser(subparsers):
    parser_combine = subparsers.add_parser("combine", help="combine help")
    parser_combine.add_argument("-m", "--method", choices=["median", "average", "sum"], required=True)
    parser_combine.add_argument("-o", "--output", metavar="OUTFILE", default=sys.stdout.buffer)
    parser_combine.add_argument("file", nargs="+")
    parser_combine.set_defaults(func=main)

def main(args):
    image_stack = stack_fits_data(args.file)
    result = METHOD_MAP[args.method](image_stack)
    hdu = fits.PrimaryHDU(result)
    hdu.writeto(args.output)
