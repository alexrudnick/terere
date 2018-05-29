#!/bin/bash

cat ~/terere/bibletools/output/bible.es-gn.target.lemmas \
  ~/terere/gn-lm-wikipedia/gnwiki-text-sentences.tok.lemmas \
  | ~/cdec/klm/lm/builder/lmplz --order 3 > nc.lm

~/cdec/klm/lm/build_binary nc.lm nc.klm
