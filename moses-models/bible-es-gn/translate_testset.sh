#!/bin/bash

echo "TRANSLATING THE BAD TEST SET"

"$HOME"/mosesdecoder/bin/moses \
  --config mert-work/moses.ini \
  --threads 1 \
  < bad-testset.source \
  > OUTPUT

## Requires sacrebleu, which you can get by going:
## sudo pip3 install sacrebleu
## https://github.com/awslabs/sockeye/tree/master/contrib/sacrebleu
echo "CALCULATING THE BAD BLEU SCORE"
sacrebleu ./bad-testset.target < OUTPUT
