#!/bin/bash

file_name="file"

for i in `echo $file_name`; do

#    vmd -dispdev text -e wat_exchng_counter.tcl -f ./${i} > ${i}_vmd.out

    python ./wat_exchng_counter.py ${i}_vmd.out > ${i}_wat_exchng.out

done
