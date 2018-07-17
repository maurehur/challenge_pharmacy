#! /bin/bash
set -e

MYPWD=${PWD}

#run
echo 'processing data...'
run_text=$(python $MYPWD/src/pharmacy_counting.py
)

echo $run_text
echo 'Done!'
