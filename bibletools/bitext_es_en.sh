#!/bin/bash

python3 print_bitext.py \
  --source output/bible.es \
  --target output/bible.en \
  --lowercase \
  --tokenize \
  --out output/bible.es-en.unfiltered \
