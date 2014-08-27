#!/bin/bash

python3 print_bitext.py \
  --source es.bible \
  --target en.bible \
  --lowercase \
  --tokenize \
  --lemmatize  \
  --out bible.es-en \
