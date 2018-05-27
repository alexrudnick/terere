#!/bin/bash

python WikiExtractor.py < gnwiki-latest-pages-articles.xml 

# cat all the output wiki pages together and remove any remaining tags.
cat AA/wiki_* \
  | sed s/\<.*\>//g \
  > plaintext.txt
