BITEXT=~/terere/bibletools/output/bible.es-gn

~/cdec/word-aligner/fast_align -i $BITEXT -d -v -o > training.es-gn.fwd_align
~/cdec/word-aligner/fast_align -i $BITEXT -d -v -o -r > training.es-gn.rev_align
~/cdec/utils/atools -i training.es-gn.fwd_align -j training.es-gn.rev_align -c grow-diag-final-and > training.gdfa

~/cdec/extractor/sacompile -b $BITEXT -a training.gdfa -c extract.ini -o training.sa
