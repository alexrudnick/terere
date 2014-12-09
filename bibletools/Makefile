## makefile to build all the bibles and run alignment on them

all: bible.es-en
#bible.es-gn bible.es-qu 
## bible.en-es

## run alignment

## bitext extraction
bible.es-gn: bible.es bible.gn
	./bitext_es_gn.sh
	~/cdec/corpus/filter-length.pl -80 bible.es-gn.unfiltered > bible.es-gn.surface
	python3 lemmatize_bitext.py bible.es-gn.surface bible.es-gn
	~/cdec/word-aligner/fast_align -i ./bible.es-gn -d -v -o > bible.es-gn.align

bible.es-qu: bible.es bible.qu
	./bitext_es_qu.sh
	~/cdec/corpus/filter-length.pl -80 bible.es-qu.unfiltered > bible.es-qu.surface
	python3 lemmatize_bitext.py bible.es-qu.surface bible.es-qu
	~/cdec/word-aligner/fast_align -i ./bible.es-qu -d -v -o > bible.es-qu.align

## OK, so in any case where the source language is Spanish, we want to run
## freeling on it. Let's think about the English case later.
bible.es-en: bible.es bible.en
	./bitext_es_en.sh
	~/cdec/corpus/filter-length.pl -80 output/bible.es-en.unfiltered > output/bible.es-en.surface
	## having done the length filtering, we can take the source side of the
	## surface bitext and produce the annotated version.
	~/cdec/corpus/cut-corpus.pl 1 \
		< output/bible.es-en.surface \
		| python3 freeling_splitted.py \
		> output/bible.es-en.surface.source.splitted
	analyze -f freeling-config/es.cfg < output/bible.es-en.surface.source.splitted > output/bible.es-en.source.tagged
	~/cdec/corpus/cut-corpus.pl 2 \
		< output/bible.es-en.surface \
		| python3 freeling_splitted.py \
		> output/bible.es-en.surface.target.splitted
	analyze -f freeling-config/es.cfg < output/bible.es-en.surface.target.splitted > output/bible.es-en-target.tagged
	##python3 lemmatize_bitext.py bible.es-en.surface bible.es-en
	##~/cdec/word-aligner/fast_align -i ./bible.es-en -d -v -o > bible.es-en.align

bible.en-es: bible.en bible.es
	./bitext_en_es.sh
	~/cdec/corpus/filter-length.pl -80 bible.en-es.unfiltered > bible.en-es.surface
	python3 lemmatize_bitext.py bible.en-es.surface bible.en-es
	~/cdec/word-aligner/fast_align -i ./bible.en-es -d -v -o > bible.en-es.align

## extract bibles from their original formats
bible.es:
	./extract_es.sh

bible.gn:
	./extract_gn.sh

bible.en:
	./extract_en.sh

bible.qu:
	./extract_qu.sh
