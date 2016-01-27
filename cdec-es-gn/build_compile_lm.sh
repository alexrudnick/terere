cat ~/terere/bibletools/output/bible.es-gn.target.lemmas | ~/cdec/klm/lm/builder/lmplz --order 3 > nc.lm

~/cdec/klm/lm/build_binary nc.lm nc.klm
