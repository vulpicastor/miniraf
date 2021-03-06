import astropy.io.fits as fits
import numpy as np

def stack_fits_data(filenames, scalefunc=None):
    fits_files = []
    filesdict = {}
    for f in filenames:
        if f not in filesdict:
            filesdict[f] = fits.open(f)
        fits_files.append(filesdict[f])
    if scalefunc is None:
        stack = np.stack((f[0].data for f in fits_files), axis=0)
    else:
        stack = np.stack((scalefunc(f[0].data) for f in fits_files), axis=0)
    for _, v in filesdict.items():
        v.close()
    return stack

def load_fits_data(filename):
    with fits.open(filename) as f:
        data = f[0].data
    return data

def median_if_sorted(a):
    n = len(a)
    if n % 2 != 0:
        return a[n//2]
    return (a[n//2-1] + a[n//2]) / 2
