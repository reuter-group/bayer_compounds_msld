#!/bin/bash

CHARMMEXEC=/net/orinoco/pga043/CHARMM_47a2/charmm_47a2/build_opls/charmm

#================= Analysis ==================================
# Get ith combination from combinations.txt
END=`wc -l combinations.txt | awk '{print $1}'`
for((i=1;i<=END;i++))
do
comb=`sed "${i}q;d" combinations.txt`
comb=($comb)

## Define substituents for each site
sub1=${comb[0]}

echo $sub1

#change "dtype" for different systems.
#Also, modify the stream file in cg2og_energies.inp according to the system chosen
#for, dtype = water and prot, stream file = *crn2ff_qpert.str
#for, dtype = cg2ogwater & cg2ogprot, stream file = *ff2crn_qpert.str

# post-processing trajectory containing original force field-charges

$CHARMMEXEC build=prot_prep dtype=crn2ffprot sys=prot box=71.750945 nbond=prot sub1=$sub1 -i postprocess_ff.inp #> junk_crn2ffprot_s1s"$sub1".log &

#grep 'GPU error' junk*.log

## **************************************************
## post-processing trajectory containing renormalized charges

$CHARMMEXEC build=prot_prep dtype=prot box=71.750945 nbond=prot sub1=$sub1 -i postprocess_renormal.inp #> junk_prot_s1s"$sub1".log &

done

#===============================================

