#! /bin/bash

export nnodes=`cat nnodes`
export nreps=`cat nreps`

# eqS = time (in ns) to be used as equilibration run
# S = total number of runs 
# N = number of duplicates

export i=52
export eqS=5
export S=40
export N=5

./postprocess.sh &>> $S-5_result.log
