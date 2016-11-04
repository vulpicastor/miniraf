from astropy.io import fits
import sys

def parse_expression(expr):
    pass

def create_parser(subparsers):
    parser_map = subparsers.add_parser("map", help="map help")
    parser_map.add_argument("-o", "--output", metavar="OUTFILE", default=sys.stdout.buffer)
    parser_map.add_argument("-m", "--map-function", required=True, metavar="EXPR")
    parser_map.add_argument("file", nargs="+")
    parser_map.set_defaults(func=main)

def main(args):
    pass
