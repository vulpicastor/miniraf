from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='miniraf',
    version='0.0a0.dev0',
    description='A minimal image reduction and analysis facility for FITS images',
    long_description=long_description,
    url="https://github.com/vulpicastor/miniraf/",
    author="Lizhou Sha",
    author_email="slz@mit.edu",
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        #'Development Status :: 3 - Alpha',
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='iraf fits pyraf astropy',
    packages=["miniraf"],
    install_requires=["numpy", "astropy"],
    extras_require={
#        'dev': ['check-manifest'],
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'miniraf=miniraf:main',
        ],
    },
)
