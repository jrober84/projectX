#!/usr/bin/env python3
import os
from distutils.core import setup
from setuptools import find_packages

author = 'James Robertson'

classifiers = """
Development Status :: 3 - Alpha
Environment :: Console
License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
Intended Audience :: Science/Research
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Bio-Informatics
Programming Language :: Python
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: Implementation :: CPython
Operating System :: POSIX :: Linux
""".strip().split('\n')


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


exec(open('projectX/version.py').read())

setup(
    name='projectX',
    include_package_data=True,
    version='0.0.1',
    python_requires='>=3.8.0,<4',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    packages=find_packages(exclude=['tests']),
    url='https://github.com/jrober84/parsityper',
    license='GPLv3',
    author='James Robertson',
    author_email='james.robertson@canada.ca',
    description=(
        'Generic pathogen analysis pipeline'),
    keywords='assembly, pathogens, subtyping',
    classifiers=classifiers,
    package_dir={'projectX': 'projectX'},
    package_data={
        "": ["*.txt", "*.fasta","*.html","*.gb"],
    },

    install_requires=[
        'numpy',
        'pandas',
        'biopython',
        'scipy',
        'six',
        'matplotlib',
        'argparse',
        'statistics',
        'plotly'

    ],

    entry_points={
        'console_scripts': [
            'projectX=projectX:main',
        ],
    },
)