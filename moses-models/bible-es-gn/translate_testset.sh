#!/bin/bash

echo "TRANSLATING THE BAD TEST SET"

"$HOME"/mosesdecoder/bin/moses \
  --config model/moses.ini \
  --threads 1 \
  < testset_100.source \
  > OUTPUT

echo "CALCULATING THE BAD BLEU SCORE"
~/mosesdecoder/scripts/generic/multi-bleu.perl ./testset_100.target \
  < OUTPUT
