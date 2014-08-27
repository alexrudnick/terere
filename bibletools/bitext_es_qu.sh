#!/bin/bash

python3 print_bitext.py \
  --source es.bible \
  --target qu.bible \
  --lowercase \
  --tokenize \
  --lemmatize  \
  --out bible.es-qu \
