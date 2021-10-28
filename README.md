# Nicotine-Microbiome
IQ Biology Rotation Project with Noah Fierer

## Goal

- Assess number of nicotine-degrading genes in the oral microbiomes of smokers/vapers vs non-smokers/vapers

## Methods

- Pull shotgun metagenomic data from [this paper](https://www.science.org/doi/10.1126/sciadv.aaz0108?utm_campaign=SciMag&utm_medium=Twitter&utm_source=JHubbard)
  - Project IDs: PRJNA548383, PRJNA544061, and PRJNA508385
- Create database of sequences for genes involved in nicotine degradation, based on [Mu et al., 2020](https://www.sciencedirect.com/science/article/pii/S001393512030150X)
  - MetaCyc degradation pathways tsvs added
  - Pull fastas from GenBank
    - `conda install -y -c conda-forge -c bioconda -c defaults entrez-direct`
    - `esearch -db protein -query 'Protein name' | efetch -format fasta`
    - But some of the genes only have names, not accession IDs, so they return sequences for unwanted genes...
  - Start with a few key genes to get the pipeline running
  - Pull from [UniProt](https://www.uniprot.org/) and/or [GenBank](https://www.ncbi.nlm.nih.gov/guide/howto/find-transcript-gene/)
    - UniProt [API querying](https://www.uniprot.org/help/api_queries)
  - Then add others once things are working
  - Check for these genes in their hosts in [IMG](https://img.jgi.doe.gov/) as a sanity check
- Use Diamond to find nicotine-degrading genes in the oral microbiolmes
- Assess difference in nicotine-degrading genes in the oral microbiomes of smokes/vapers vs controls
- Look at MAGs if time?

## Database

- Get MetaCyc gene details
- Search E.C. IDs in UniProt
- Download fastas for all matching sequences
  - For `3.5.1.3`, filtered only bacteria because lots of human and mouse sequences were coming up
  - Skipped `1.3.99.-` and `1.5.99.-` because too many unrelated genes were coming up
  - E.C. for nctB was sourced from Uniprot info on (S)-6-hydroxynicotine oxidase
  - Skipped `1.5.8.M1` because it wasn't pulling up any results, and searching the name pulled up kdhA/B/C, which I already had

## Diamond
- Please cite http://dx.doi.org/10.1038/s41592-021-01101-x Nature Methods (2021)

## Files/details

1. `setup_scripts` contains scripts with code to install sra toolkit. I haven't tried these in script format (since I only needed to install it once), 
but I imagine I will need this code later if using fastq-dump on fiji.
  - If having issues see the [documentation](https://github.com/ncbi/sra-tools/wiki/02.-Installing-SRA-Toolkit) 
or [config guidelines](https://github.com/ncbi/sra-tools/wiki/03.-Quick-Toolkit-Configuration). 
  - Note for future John can try the following instead of `vdb-config -i`:
    - `vdb-config --restore-defaults`
    - `vdb-config -s "/repository/user/main/public/root=."`
    - `vdb-config -s "cache-enabled=true"`
    - `vdb-config --report-cloud-identity yes`

2. `get_data.sh` is a script to loop through the SRA accession values for the projects and download the fastq files in directories named by their run IDs.
  - If having issues with this, consider something similar to the following: 
> while read line; do \
> wget http://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?cmd=dload&run_list=${line}&format=fastq; \
> done<list_of_ids
