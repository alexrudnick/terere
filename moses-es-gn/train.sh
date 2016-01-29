#!/bin/bash

mkdir -p corpus

cat ~/terere/bibletools/output/bible.es-gn \
  | ~/cdec/corpus/cut-corpus.pl 1 \
  | ~/space/mosesdecoder/scripts/tokenizer/escape-special-chars.perl \
  > corpus/bible.es

cat ~/terere/bibletools/output/bible.es-gn \
  | ~/cdec/corpus/cut-corpus.pl 2 \
  | ~/space/mosesdecoder/scripts/tokenizer/escape-special-chars.perl \
  > corpus/bible.gn

~/space/mosesdecoder/scripts/training/train-model.perl \
  --cores 8 \
  --external-bin-dir /space/mosesdecoder/tools \
  --corpus ./corpus/bible \
  --f gn \
  --e es \
  --alignment grow-diag-final-and \
  --lm 0:3:/space/terere/moses-es-gn/nc.klm
