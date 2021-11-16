#!/bin/bash



for filename in PRJNA508385_Acc_List.txt  PRJNA544061_Acc_List.txt  PRJNA548383_Acc_List.txt ; do

    while read line;
    do
    # for read each line

    prefetch $line --output-directory PRJNA548383/$line
    fasterq-dump $line --outdir PRJNA548383/$line --progress

    done < Accession_lists/$filename

done
