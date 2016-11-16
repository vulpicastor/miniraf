import numpy as np
import matplotlib.pyplot as plt

from .util import load_fits_data, median_if_sorted

OUTPUT_TEMPLATE = """Stats for {filename}
Image size: {x} x {y}
Min:        {min}
Max:        {max}
Median:     {median}
Mean:       {average}
Std dev:    {stddev}"""

def create_parser(subparsers):
    parser_stats = subparsers.add_parser("stats", help="Display statistics and histograms")
    parser_stats.add_argument("-H", "--histogram", action="store_true", help="Show histogram")
    parser_stats.add_argument("file", nargs="+")
    parser_stats.set_defaults(func=main)

def _calc_hist_bins(bin_size, stats):
    low = int(stats["min"])
    high = int(stats["max"])
    high += bin_size - (high - low) % bin_size
    bins = (high - low) // bin_size
    kwargs = {}
    kwargs["range"] = (low, high)
    kwargs["bins"] = bins
    return kwargs

def _add_histogram(i, title, data, *args, **kwargs):
    plt.figure(i)
    plt.hist(data, **kwargs)
    plt.xlabel("Data number")
    plt.ylabel("Frequency")
    plt.title(title)

def main(args):
    for i, f in enumerate(args.file):
        data = load_fits_data(f)
        # TODO: check that data is 2-dimensional
        # FITS data is column-major
        y, x = data.shape
        data = data.reshape(-1, order="A")
        data.sort()
        stats = {
            "filename": f,
            "min": data[0],
            "max": data[-1],
            "median": median_if_sorted(data),
            "average": data.mean(),
            "stddev": data.std(),
            "x": x,
            "y": y,
        }
        print(OUTPUT_TEMPLATE.format(**stats))
        if args.histogram:
            kwargs = _calc_hist_bins(2, stats)
            _add_histogram(i, f, data, normed=True, **kwargs)
    plt.show()
