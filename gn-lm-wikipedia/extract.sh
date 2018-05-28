#!/bin/bash

python2 WikiExtractor.py < gnwiki-latest-pages-articles.xml 

# cat all the output wiki pages together and remove any remaining tags.
cat AA/wiki_* \
  | sed s/\<.*\>//g \
  > gnwiki-text.txt

python3 one_sentence_per_line.py \
  --infn gnwiki-text.txt \
  --outfn gnwiki-text-sentences.txt

python3 ../bibletools/lemmatize_text.py gn \
  gnwiki-text-sentences.txt \
  gnwiki-text-sentences-lemmatized.txt
