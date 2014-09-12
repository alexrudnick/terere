#!/bin/bash

python3 print_bitext.py \
  --source bible.en \
  --target bible.es \
  --lowercase \
  --tokenize \
  --out bible.en-es.unfiltered \
