#!/bin/bash

python3 print_bitext.py \
  --source en.bible \
  --target es.bible \
  --lowercase \
  --tokenize \
  --lemmatize  \
  --out bible.en-es \
