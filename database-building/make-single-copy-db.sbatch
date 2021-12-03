#!/bin/bash
#SBATCH -p short # Partition or queue. In this case, short!
#SBATCH --job-name=make_single_copy_db # Job name
#SBATCH --mail-type=ALL # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=jost9358@colorado.edu
#SBATCH --nodes=1 # Only use a single node
#SBATCH --ntasks=1 # Run on a single CPU
#SBATCH --mem=10gb # Memory limit
#SBATCH --time=01:00:00 # Time limit hrs:min:sec
#SBATCH --output=/Users/jost9358/Nicotine-Microbiome/make_single_copy_db_%j.out # Standard output and error log
#SBATCH --error=/Users/jost9358/Nicotine-Microbiome/make_single_copy_db_%j.err # %j inserts job number

# download the db
wget https://data.gtdb.ecogenomic.org/releases/release202/202.0/genomic_files_reps/bac120_marker_genes_reps_r202.tar.gz --no-check-certificate

# unzip it
tar -xf bac120_marker_genes_reps_r202.tar.gz

# concat all of the .faa into one file
cat bac120_marker_genes_reps_r202/faa/* > bac120_marker_genes_reps_r202/bac120_marker_genes_reps_r202.faa

# make the db
diamond makedb -in bac120_marker_genes_reps_r202/bac120_marker_genes_reps_r202.faa -o marker_gene_db.dmnd
