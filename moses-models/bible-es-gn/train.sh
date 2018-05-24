#!/bin/bash

mkdir -p corpus

# pull out the Spanish surface forms
python3 ../../bibletools/freeling_to_surface.py \
  --freeling ../../bibletools/output/bible.es-gn.source.tagged \
  > corpus/bible.es

# ... and Guarani lemmas
cat ~/terere/bibletools/output/bible.es-gn \
  | ~/cdec/corpus/cut-corpus.pl 2 \
  | "$HOME"/mosesdecoder/scripts/tokenizer/escape-special-chars.perl \
  > corpus/bible.gn

"$HOME"/mosesdecoder/scripts/training/train-model.perl \
  --cores 8 \
  --external-bin-dir "$HOME"/mosesdecoder/tools \
  --corpus ./corpus/bible \
  --f es \
  --e gn \
  --alignment srctotgt \
  --lm 0:3:"$HOME"/terere/moses-models/bible-es-gn/nc.klm
