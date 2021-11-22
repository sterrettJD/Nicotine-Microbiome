#!/bin/bash

# make a big string with the cluster params
# I split it up into multiple lines here for reability's sake
cluster="\"sbatch --account jost9358 "
cluster+="--partition short "
cluster+="--job-name pear_diamond_nico_snakemake "
cluster+="--mail-type ALL "
cluster+="--mail-user jost9358@colorado.edu "
cluster+="--time 10:00:00 "
cluster+="--nodes 1 "
cluster+="--ntasks-per-node 20 " 
cluster+="--mem 260gb "
cluster+="--wait 60" 
cluster+="--output /Users/jost9358/Nicotine-Microbiome/run_diamond_out/%j.out "
cluster+="--error /Users/jost9358/Nicotine-Microbiome/run_diamond_out/%j.err"
cluster+="\""

snakemake --cluster $cluster -j 20 --latency-wait 60

#echo $cluster
