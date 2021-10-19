#!/bin/bash

filename='PRJNA548383_Acc_List.txt'

while read line;
do
# for read each line

prefetch $line --output-directory PRJNA548383/$line
fasterq-dump $line --outdir PRJNA548383/$line --progress

done < $filename
