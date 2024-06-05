#!/bin/bash
#SBATCH --account=bar
#SBATCH --time=04:00:00
#SBATCH --nodes=2
#SBATCH --job-name=iea22m
#SBATCH --mail-user pbortolo@nrel.gov
#SBATCH --mail-type BEGIN,END,FAIL
######SBATCH --partition=debug
#SBATCH --qos=high
######SBATCH --mem=1000GB      # RAM in MB
#SBATCH --output=job_log.%j.out  # %j will be replaced with the job ID


# Load and activate your conda environment

source activate weis-env
 
mpirun -np 72 python driver.py

 
