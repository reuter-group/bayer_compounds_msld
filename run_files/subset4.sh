#!/bin/bash

export nnodes=`cat nnodes`
export nreps=`cat nreps`
export nitt=1

END=40
for ((run=1;run<=END;run++))
do	

export run=$run	

for p in a b c d e

do

export ini=52
export i=$ini$p


./runset4.sh >> $END-5_jobs.log

done

done
