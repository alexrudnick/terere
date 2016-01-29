BITEXT=~/terere/bibletools/output/bible.es-gn

## XXX: need to sensibly extract dev and test sets from the bitext
head -n 100 $BITEXT > dev.lc-tok.es-gn
head -n 200 $BITEXT | tail -n 100 > devtest.lc-tok.es-gn

~/cdec/extractor/extract -c extract.ini -g dev.grammars --max_nonterminals 0 -t 2 < dev.lc-tok.es-gn > dev.lc-tok.es-gn.sgm
~/cdec/extractor/extract -c extract.ini -g devtest.grammars --max_nonterminals 0 -t 2 < devtest.lc-tok.es-gn > devtest.lc-tok.es-gn.sgm

## turn grammars into phrase-based phrase tables
sed -i "s/^\[X\] ||| //g" dev.grammars/*
sed -i "s/^\[X\] ||| //g" devtest.grammars/*
