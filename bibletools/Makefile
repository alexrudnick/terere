## makefile to build all the bibles and run alignment on them

all: bible.es-en bible.es-gn bible.es-qu bible.en-es \
     bible.es-en.align bible.es-gn.align bible.es-qu.align bible.en-es.align

## run alignment
bible.es-gn.align: bible.es-gn
	~/cdec/word-aligner/fast_align -i ./bible.es-gn -d -v -o > bible.es-gn.align

bible.es-qu.align: bible.es-qu
	~/cdec/word-aligner/fast_align -i ./bible.es-qu -d -v -o > bible.es-qu.align

bible.en-es.align: bible.en-es
	~/cdec/word-aligner/fast_align -i ./bible.en-es -d -v -o > bible.en-es.align

bible.es-en.align: bible.es-en
	~/cdec/word-aligner/fast_align -i ./bible.es-en -d -v -o > bible.es-en.align

## bitext extraction
bible.es-gn: bible.es bible.gn
	./bitext_es_gn.sh
	~/cdec/corpus/filter-length.pl -80 bible.es-gn.unfiltered > bible.es-gn.surface
	python3 lemmatize_bitext.py bible.es-gn.surface > bible.es-gn

bible.es-qu: bible.es bible.qu
	./bitext_es_qu.sh
	~/cdec/corpus/filter-length.pl -80 bible.es-qu.unfiltered > bible.es-qu.surface
	python3 lemmatize_bitext.py bible.es-qu.surface > bible.es-qu

bible.es-en: bible.es bible.en
	./bitext_es_en.sh
	~/cdec/corpus/filter-length.pl -80 bible.es-en.unfiltered > bible.es-en.surface
	python3 lemmatize_bitext.py bible.es-en.surface > bible.es-en

bible.en-es: bible.en bible.es
	./bitext_en_es.sh
	~/cdec/corpus/filter-length.pl -80 bible.en-es.unfiltered > bible.en-es.surface
	python3 lemmatize_bitext.py bible.en-es.surface > bible.en-es

## extract bibles from their original formats
bible.es:
	./extract_es.sh

bible.gn:
	./extract_gn.sh

bible.en:
	./extract_en.sh

bible.qu:
	./extract_qu.sh
