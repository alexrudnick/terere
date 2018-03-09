#!/bin/bash

python3 parse_bible_corpus_xml.py \
  ~/checkouts/bible-corpus/bibles/German.xml \
  > output/bible.de \
  2> /dev/null
