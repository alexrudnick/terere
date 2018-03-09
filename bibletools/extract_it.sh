#!/bin/bash

python3 parse_bible_corpus_xml.py \
  ~/checkouts/bible-corpus/bibles/Italian.xml \
  > output/bible.it \
  2> /dev/null
