#!/bin/bash

mkdir -p corpus

cat ~/terere/bibletools/output/bible.es-en \
  | ~/cdec/corpus/cut-corpus.pl 1 \
  | "$HOME"/mosesdecoder/scripts/tokenizer/escape-special-chars.perl \
  > corpus/bible.es

cat ~/terere/bibletools/output/bible.es-en \
  | ~/cdec/corpus/cut-corpus.pl 2 \
  | "$HOME"/mosesdecoder/scripts/tokenizer/escape-special-chars.perl \
  > corpus/bible.en

"$HOME"/mosesdecoder/scripts/training/train-model.perl \
  --cores 8 \
  --external-bin-dir "$HOME"/mosesdecoder/tools \
  --corpus ./corpus/bible \
  --f es \
  --e en \
  --alignment srctotgt \
  --lm 0:3:"$HOME"/terere/moses-models/bible-es-en/nc.klm
