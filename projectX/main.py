#!/usr/bin/python
import glob,sys,time
from argparse import (ArgumentParser, FileType)
import logging, os, sys, re, collections, operator, math, shutil, datetime
from collections import Counter
import pandas as pd
import copy, statistics
from multiprocessing import Pool
from projectX.constants import SAMPLE_FIELDS,SAMPLE_FIELDS_DATATYPES,ILLUMINA_ASSEMBLERS,NANOPORE_ASSEMBLERS

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
    parser.add_argument('--assembler', type=str, required=False,
                        help='Assembler to use default: skesa (illumina), flye (nanopore)')
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



def init_sample_obj():
    sampleObj = {}
    for i in range(0,len(SAMPLE_FIELDS)):
        field = SAMPLE_FIELDS[i]
        dataType = SAMPLE_FIELDS_DATATYPES[i]
        if dataType == 'int':
            sampleObj[field] = 0
        elif dataType == 'float':
            sampleObj[field] = 0.0
        elif dataType == 'str':
            sampleObj[field] = ''
        elif dataType == 'list':
            sampleObj[field] = []
        elif dataType == 'dict':
            sampleObj[field] = {}
    return sampleObj 



def main():
    cmd_args = parse_args()
    sample_id = cmd_args.prefix
    
    #init the sample object with the commandline parameters
    sampleObj = init_sample_obj()
    sampleObj['sample_id'] = sample_id
    for arg in cmd_args:
        sampleObj['params'][arg] = cmd_args.arg

    #Get sequencing tech
    sampleObj['seqTech'] = cmd_args.seqTech.lower()

    selected_assembler = cmd_args.assembler

    #determine initial assembler
    if sampleObj['seqTech'] == 'nanopore':
        if selected_assembler is not None:
            if not selected_assembler in NANOPORE_ASSEMBLERS:
                logger.error("Invalid assembler selected: {}, valid options are:{}".format(selected_assembler,NANOPORE_ASSEMBLERS))
                sys.exit()
        else:
            selected_assembler = NANOPORE_ASSEMBLERS[0]
    elif sampleObj['seqTech'] == 'illumina':
        if selected_assembler is not None:
            if not selected_assembler in ILLUMINA_ASSEMBLERS:
                logger.error("Invalid assembler selected: {}, valid options are:{}".format(selected_assembler,ILLUMINA_ASSEMBLERS))
                sys.exit()
        else:
            selected_assembler = ILLUMINA_ASSEMBLERS[0]

    sampleObj['assembler'] = selected_assembler

    #establish read layout
    if R1 is not None and R2 is not None:
        sampleObj['read_layout'] = 'single'
    else:
        sampleObj['read_layout'] = 'paired'





    return

if __name__ == '__main__':
    main()
