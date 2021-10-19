# Nicotine-Microbiome
IQ Biology Rotation Project with Noah Fierer

## Goal

- Assess number of nicotine-degrading genes in the oral microbiomes of smokers/vapers vs non-smokers/vapers

## Methods

- Pull shotgun metagenomic data from [this paper](https://www.science.org/doi/10.1126/sciadv.aaz0108?utm_campaign=SciMag&utm_medium=Twitter&utm_source=JHubbard)
  - Project IDs: PRJNA548383, PRJNA544061, and PRJNA508385
- Train Hidden Markov Model on nicotine-degrading genes
- Assess difference in nicotine-degrading genes in the oral microbiomes of smokes/vapers vs controls

## Files/details

1. `setup_scripts` contains scripts with code to install sra toolkit. I haven't tried these in script format (since I only needed to install it once), 
but I imagine I will need this code later if using fastq-dump on fiji.
  - If having issues see the [documentation](https://github.com/ncbi/sra-tools/wiki/02.-Installing-SRA-Toolkit) 
or [config guidelines](https://github.com/ncbi/sra-tools/wiki/03.-Quick-Toolkit-Configuration). 
  - Note for future John can try the following instead of `vdb-config -i`:
    - `vdb-config --restore-defaults`
    - `vdb-config -s "/repository/user/main/public/root=."`
    - `vdb-config -s "cache-enabled=true"`
    - vdb-config --report-cloud-identity yes

2. `get_data.sh` is a script to loop through the SRA accession values for the projects and download the fastq files in directories named by their run IDs.
