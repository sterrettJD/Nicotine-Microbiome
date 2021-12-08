# Nicotine-Microbiome
IQ Biology Rotation Project 

## Abstract
**Nicotine Metabolism Genes in the Oral Microbiomes of Nicotine Users and Non-Users**

John Sterrett 1,2, Noah Fierer 3,4
1. Department of Integrative Physiology, University of Colorado, Boulder, CO
2. Interdisciplinary Quantitative Biology, University of Colorado, Boulder, CO
3. Department of Ecology and Evolutionary Biology, University of Colorado, Boulder, CO
4. Cooperative Institute for Research in Environmental Sciences, Boulder, CO

Individuals who smoke cigarettes or use e-cigarettes inhale nicotine (among other compounds) frequently throughout the day, and such drug use increases risks of cancer, lung disease, and cardiovascular disease. Many studies have investigated the metabolism of nicotine within human cells and tissues, which occurs at a rate that is largely genetically determined, with this rate affecting the likelihood of successful smoking cessation. What has not been investigated is whether those bacteria living in the oral cavity are also capable of nicotine metabolism. Given that bacteria capable of nicotine metabolism have been found in other environments and given the well-characterized impacts of nicotine use on the taxonomic structure of oral microbiomes, it is possible that frequent nicotine use could select for nicotine-metabolizing bacteria in the oral microbiome. However, no research has specifically investigated whether genes for nicotine degradation are even present in the oral microbiome and, if so, whether the oral microbiomes of smokers and e-cigarette users have higher relative abundances of genes involved in nicotine catabolism. 

To address this knowledge gap, I compiled a database of sequences for all known bacterial genes involved in nicotine degradation. I then analyzed a publicly available oral microbiome shotgun metagenomic dataset from a study of smokers, e-cigarette users, and non-users. The raw reads were quality filtered and merged, and bacterial nicotine degradation genes were identified. Nicotine gene counts were then normalized based on the number of single-copy bacterial marker genes per metagenome. I was able to detect genes encoding 16 of the 27 enzymes in the pyridine and pyrrolidine pathways for nicotine degradation, demonstrating that genes for nicotine degradation are indeed present in the oral microbiome. However, there were no significant increases in the relative abundances of nicotine degradation genes in smokers or e-cigarette users compared to non-users. The dataset, though, was limited by large variation in sequencing depth, and our analysis was constrained to relative abundances of such genes. The detection of nicotine degradation genes supports the application of our pipeline to other existing metagenomic datasets or the development of qPCR assays to quantify absolute abundances of these genes. Furthermore, the constructed database and pipeline could be used with reference genome databases to more identify which bacterial taxa, beyond those already described, are likely capable of nicotine catabolism. This work was supported in part by the Interdisciplinary Quantitative Biology (IQ Biology) program at the BioFrontiers Institute, University of Colorado, Boulder.

## Goal

- Assess number of nicotine-degrading genes in the oral microbiomes of smokers/vapers vs non-smokers/vapers

## Main files of interest
- diamond/ contains the Snakefile for the Snakemake pipeline
- diamond_analysis/ contains the Jupyter notebook used to analyze the Diamond output
- database-building/ contains diamond formatted databases for nicotine-degrading genes as well as the raw .fasta files for the database (used uniprot-fastas/uniprot-nicotine.fasta for the fasta)

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
- Merge reads using PEAR
- Filter short reads using 
- Use Diamond to find nicotine-degrading genes in the oral microbiomes
- Assess difference in nicotine-degrading genes in the oral microbiomes of smokes/vapers vs controls
- Normalize based on total reads and bacterial single-copy marker genes (DIAMOND as well) from [here](https://data.gtdb.ecogenomic.org/releases/release202/202.0/genomic_files_reps/bac120_marker_genes_reps_r202.tar.gz)

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
- tested diamond with `diamond blastx -q PRJNA548383/SRR9641933/SRR9641933_1.fastq -d database-building/uniprot-nicotine-db.dmnd -o test.tsv `
  - Got a couple hundred hits

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
