#!/bin/bash

python3 print_bitext.py \
  --source bible.es \
  --target bible.qu \
  --lowercase \
  --tokenize \
  --out bible.es-qu.unfiltered \