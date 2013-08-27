#!/bin/bash

## requires langid.py
## script based on https://github.com/saffsd/langid.py#training-a-model

LANGIDPY=/home/alex/checkouts/langid.py/langid
TRAIN=$LANGIDPY/train

CORPUS=/home/alex/trylangid/corpus
MODEL=`pwd`/corpus.model

cd $TRAIN
python index.py $CORPUS -m $MODEL
python tokenize.py $MODEL
python DFfeatureselect.py $MODEL
python IGweight.py -d $MODEL
python IGweight.py -lb $MODEL
python LDfeatureselect.py $MODEL
python scanner.py $MODEL
python NBtrain.py -j 1 $MODEL 
