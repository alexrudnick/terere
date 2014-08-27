#!/bin/bash

python3 print_bitext.py \
  --source bible.en \
  --target bible.es \
  --lowercase \
  --tokenize \
  --lemmatize  \
  --out bible.en-es \
