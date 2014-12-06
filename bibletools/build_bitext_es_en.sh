#!/bin/bash

./bitext_es_en.sh
~/cdec/corpus/filter-length.pl -80 bible.es-en.unfiltered > bible.es-en.surface

## having done the length filtering, we can take the source side of the
## surface bitext and produce the annotated version.
~/cdec/corpus/cut-corpus.pl 1 < bible.es-en.surface \
    | analyze -f freeling-config/es.cfg \
    > bible.es-en.source.freeling

python3 freeling_to_annotated.py \
    --freeling bible.es-en.source.freeling \
    --lemma_out bible.es-en.lemmas \
    --annotated bible.es-en

## really we just want to lemmatize the target side...
#python3 lemmatize_text.py bible.es-en.surface bible.es-en
#~/cdec/word-aligner/fast_align -i ./bible.es-en -d -v -o > bible.es-en.align
