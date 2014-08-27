#!/bin/bash

python3 parse_youversion.py \
  ~/bibles/spider-bible.com/*.gdc \
  2> nonstandardverseids \
  > gn.bible
