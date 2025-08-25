#!/bin/bash
#SBATCH --job-name=gpt_dev1
#SBATCH --output=./logs/output.log
#SBATCH --error=./logs/error.log
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --mem=32G

echo "Date"
date

module load cuda/12.3

time_s=$(date +%s)

python gpt-dev1.py

time_e=$(date +%s)

echo "Elapsed time: $((time_e-time_s))"
