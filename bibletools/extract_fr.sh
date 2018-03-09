#!/bin/bash

python3 parse_bible_corpus_xml.py \
  ~/checkouts/bible-corpus/bibles/French.xml \
  > output/bible.fr \
  2> /dev/null
