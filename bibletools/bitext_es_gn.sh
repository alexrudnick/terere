#!/bin/bash

python3 print_bitext.py \
  --source es.bible \
  --target gn.bible \
  --lowercase \
  --tokenize \
  --lemmatize  \
  --out bible.es-gn \
