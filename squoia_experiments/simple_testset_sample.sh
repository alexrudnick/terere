#!/bin/bash

# Bad testset sampling.

shuf ~/terere/bibletools/output/bible.es-qu.surface > corpus-together.shuffled

head -n 100 corpus-together.shuffled \
  | ~/cdec/corpus/cut-corpus.pl 1 \
  | ~/cdec/corpus/tokenize-anything.sh \
  > bad-testset.source

head -n 100 corpus-together.shuffled \
  | ~/cdec/corpus/cut-corpus.pl 2 \
  | ~/cdec/corpus/tokenize-anything.sh \
  > bad-testset.target
