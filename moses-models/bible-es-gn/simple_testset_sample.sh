#!/bin/bash

# Bad testset sampling.

~/cdec/corpus/paste-files.pl corpus/bible.es corpus/bible.gn \
  > corpus-together.tmp

shuf corpus-together.tmp > corpus-together.shuffled

head -n 100 corpus-together.shuffled \
  | ~/cdec/corpus/cut-corpus.pl 1 \
  > bad-testset.source

head -n 100 corpus-together.shuffled \
  | ~/cdec/corpus/cut-corpus.pl 2 \
  > bad-testset.target
