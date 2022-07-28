#!/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=4
#SBATCH --nodes=1
#SBATCH --time=30-00:00:00
#SBATCH --ntasks-per-node=1


cd /projects/bgmp/ano/Bi622/Demultiplex/Assignment-the-first 
dir=/projects/bgmp/shared/2017_sequencing/

conda activate bgmp_py310
/usr/bin/time -v ./demux_A1.py -f $dir/1294_S1_L008_R2_001.fastq.gz -r 8 -o R2_A1_graph