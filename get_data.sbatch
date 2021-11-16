#!/bin/bash
#SBATCH -p short # Partition or queue. In this case, short!
#SBATCH --job-name=download_nicotine_data # Job name
#SBATCH --mail-type=ALL # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=jost9358@colorado.edu
#SBATCH --nodes=1 # Only use a single node
#SBATCH --ntasks=1 # Run on a single CPU
#SBATCH --mem=100gb # Memory limit
#SBATCH --time=04:00:00 # Time limit hrs:min:sec
#SBATCH --output=/Users/jost9358/Nicotine-Microbiome_%j.out # Standard output and error log
#SBATCH --error=/Users/jost9358/Nicotine-Microbiome_%j.err # %j inserts job number


for filename in PRJNA508385_Acc_List.txt  PRJNA544061_Acc_List.txt  PRJNA548383_Acc_List.txt ; do

    while read line; do
    # for read each line
        if [ -e ~/Nicotine-Micobiome/PRJNA548383/$line ]; then
            echo "File exists"
    
        else
            prefetch $line --output-directory PRJNA548383/$line
            fasterq-dump $line --outdir PRJNA548383/$line --progress
        fi
    
    done < Accession_lists/$filename

done
