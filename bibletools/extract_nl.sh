#!/bin/bash

python3 parse_bible_corpus_xml.py \
  ~/checkouts/bible-corpus/bibles/Dutch.xml \
  > output/bible.nl \
  2> /dev/null
