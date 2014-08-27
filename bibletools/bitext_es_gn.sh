#!/bin/bash

python3 print_bitext.py \
  --source bible.es \
  --target bible.gn \
  --lowercase \
  --tokenize \
  --lemmatize  \
  --out bible.es-gn \
