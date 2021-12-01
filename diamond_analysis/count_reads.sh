#!/bin/bash
# NOTE : Quote it else use array to avoid problems #

FILES="../data/*"

for f in $FILES
do
  echo "Processing $f"
  # take action on each file.
  name=$(basename $f)
  lines=$(cat $f/$name.assembled.75.fastq|wc -l)
  reads=$(($lines/4))
  echo "$f \t $reads" >> num_reads.txt
done
