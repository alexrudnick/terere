#!/bin/bash

python3 print_bitext.py \
  --source bible.es \
  --target bible.en \
  --lowercase \
  --tokenize \
  --out bible.es-en.unfiltered \
