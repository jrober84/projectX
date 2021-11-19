NANOPORE_ASSEMBLERS = [
    'flye', 'canu'
]
ILLUMINA_ASSEMBLERS = [
    'spades', 'skesa', 'megahit'
]

POLISHERS = [ 'meddaka','pilon']

SEQTECH = ['illumina','nanopore','pacbio']

TYPING_TOOLS = [
    'mlst','sistr','ectyper'
]

READ_ALIGNERS = [ 'bwa', 'kma']

TYPING_TOOL_TAXA = {
    'mlst': {'mlst': []},
    'serotype':{'sistr': ['Salmonella'],'ectyper': ['Escherichia','Shigella']}
}

READ_CLASSIFIERS = ['centrifuge']

WORKFLOW_STAGES = ['correction',
                   'preprocessing',
                   'screening',
                   'assembly',
                   'polishing',
                   'assemblyMetrics'
                   'classification',
                   'detection',
                   ]

SAMPLE_FIELDS = [
    'sample_id',
    'sample_type',
    'analysis_date',
    'seqTech',
    'read_layout',
    'raw_seq_files',
    'total_reads_pre',
    'total_reads_post',
    'total_bases_pre',
    'total_bases_post',
    'read_mean_len_pre',
    'read_mean_len_post',
    'read_gc_pre',
    'read_gc_post',
    'read_insert_size_peak',
    'read_duplication_rate',
    'est_genome_size',
    'est_genome_cov',
    'est_hetero',
    'processed_seqFiles',
    'screening_db',
    'screening_db_version',
    'identified_taxa',
    'reported_sample_type',
    'detected_sample_type',
    'assembler',
    'polisher',
    'num_contigs_gt0',
    'num_contigs_gt500',
    'n50_contigs_gt500',
    'mash_dist_ReadsVsAssembly',
    'gene_db',
    'gene_db_version',
    'detect_assembly_genes',
    'detect_mapping_genes',
    'qa_messages',
    'run_params'
]

SAMPLE_FIELDS_DATATYPES = [
    'str',
    'str',
    'date',
    'str',
    'str',
    'list',
    'int',
    'int',
    'int',
    'int',
    'float',
    'float',
    'float',
    'float',
    'float',
    'float',
    'float',
    'float',
    'float',
    'list',
    'str',
    'str',
    'list',
    'str',
    'str',
    'str',
    'str',
    'int',
    'int',
    'int',
    'float',
    'str',
    'str',
    'dict',
    'dict',
    'list',
    'dict'
]