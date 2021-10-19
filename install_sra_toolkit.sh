#!/bin/bash

#download the sra toolkit
wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-mac64.tar.gz

#unzip it
tar -vxzf sratoolkit.current-mac64.tar.gz

#For convenience (and to show you where the binaries are) append the path to the binaries to your PATH environment variable
export PATH=$PATH:$PWD/sratoolkit.current-mac64/bin

#should print out a path
which fastq-dump
