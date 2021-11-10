from projectX.ext_tools import run_command

def run_canu_correct(reads,prefix,out_dir,genome_size,min_length=1000,minOverlapLength=500,corOutCoverage=1000,n_threads=1):
    cmd_args = {'-p ':n_threads,
                '-p ':prefix,
                'stopOnLowCoverage=':'False',
                'genomeSize=':genome_size,
                'minReadLength=':min_length,
                'minOverlapLength':minOverlapLength,
                'corOutCoverage':corOutCoverage,
                '-d ':out_dir,
                '-nanopore ':reads}
    cmd = "canu -correct useGrid=False {}".format((" ".join(f'{k}{v}' for k,v in cmd_args.items())))
    (stdout, stderr) = run_command(cmd)
    is_valid = False
    #TODO create data structure with the path to the corrected reads
    return {'data': None, 'stderr': stderr, 'stdout': stdout,'is_vald':is_valid,'cmd':cmd}

def get_canu_version():
    return