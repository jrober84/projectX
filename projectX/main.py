#!/usr/bin/python
import glob
import time
from argparse import (ArgumentParser, FileType)
import logging, os, sys, re, collections, operator, math, shutil, datetime
from collections import Counter
import pandas as pd
import copy, statistics
from multiprocessing import Pool

def parse_args():
    "Parse the input arguments, use '-h' for help"
    parser = ArgumentParser(description='ProjectX')
    parser.add_argument('--database_dir', type=str, required=True,
                        help='ProjectX compatible database directory')
    parser.add_argument('--se', type=str, required=False,
                        help='single-end fastq read')
    parser.add_argument('--R1', type=str, required=False,
                        help='paired-end fwd fastq read')
    parser.add_argument('--R2', type=str, required=False,
                        help='paired-end rev fastq read')
    parser.add_argument('--outdir', type=str, required=True,
                        help='output directory')
    parser.add_argument('--prefix', type=str, required=False,
                        help='output file prefix', default='projectX')
    parser.add_argument('--type', type=str, required=True,
                        help='Treat data as single or multi source')
    parser.add_argument('--seqTech', type=str, required=True,
                        help='Explicit sequencing technology: Illumina or Nanopore')
    parser.add_argument('--correct', required=False,
                        help='Perform read correction',action='store_true')
    parser.add_argument('--trim', required=False,
                        help='Perform read trimming',action='store_true')
    parser.add_argument('--dedup', required=False,
                        help='Perform read deduplication',action='store_true')
    parser.add_argument('--min_read_len', type=int, required=False,
                        help='Filter reads shorter than this limit',
                        default=0)
    parser.add_argument('--min_genome_size', type=int, required=False,
                        help='Flag genomes which are too small',
                        default=0)
    parser.add_argument('--max_genome_size', type=int, required=False,
                        help='Flag genomes which are too large',
                        default=-1)
    parser.add_argument('--min_genome_cov_depth', type=int, required=False,
                        help='Flag samples where the raw sequencing depth is too low',
                        default=40)
    parser.add_argument('--max_genome_cov_depth', type=int, required=False,
                        help='Downsample reads if coverage depth exceeds threshold range ( 1 - n) default off',
                        default=-1)
    parser.add_argument('--min_mash_ident', type=float, required=False,
                        help='Min mash identity for screening', default=0.05)
    parser.add_argument('--min_mash_pvalue', type=float, required=False,
                        help='Min mash identity for screening', default=0.05)
    parser.add_argument('--n_threads', type=str, required=False,
                        help='output directory', default=1)
    parser.add_argument('--cleanup', required=False,
                        help='Delete all interim files and processed reads',action='store_true')
    parser.add_argument('--no_plots', required=False,
                        help='suppress making plots',action='store_true')


    return parser.parse_args()


def main():
    return

if __name__ == '__main__':
    main()
