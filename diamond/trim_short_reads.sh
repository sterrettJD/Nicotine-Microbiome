#!/bin/bash

# This removes reads of a below a certain length from paired read files in fastq format (e.g., R1 and R2 from the same library)
# Usage: $ bash trim_short_reads [input fastqR1] [minimum read length to keep]

#1. Start with inputs
fq=$1
minlen=$2

#2. Find all entries with read length less than minimum length and print line numbers
awk -v min=$minlen '{if(NR%4==2) if(length($0)<min) print NR"\n"NR-1"\n"NR+1"\n"NR+2}' $fq > temp.lines

#3. Remove the line numbers recorded in "lines" from both fastqs
awk 'NR==FNR{l[$0];next;} !(FNR in l)' temp.lines $fq > $fq.$minlen

#4. Conclude
echo "Pairs shorter than $minlen bases removed from $fq"