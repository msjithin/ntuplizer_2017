#!/bin/bash

source /cvmfs/cms.cern.ch/crab3/crab.sh 
for jobDir in `ls ${1}`; do
   
#echo "${jobDir}"
#crab resubmit -d ${1}/${jobDir}
crab status -d ${1}/${jobDir}
   
done
