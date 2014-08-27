#!/bin/bash

python3 parse_youversion.py \
  ~/spider-bible.com/*.gdc \
  2> nonstandardverseids \
  > gn.bible
