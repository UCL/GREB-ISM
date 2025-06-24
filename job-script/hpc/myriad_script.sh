#!/bin/bash -l
#$ -pe smp 4
#$ -l mem=4G
#$ -l h_rt=1:00:00
#$ -wd /home/ucakahb/Scratch/GREB-ISM
#$ -j y
#$ -o /home/ucakahb/Scratch/job_$JOB_ID.out

cd /home/ucakahb/GREB-ISM/job-script/
./run_icesheet.csh
