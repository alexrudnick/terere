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

bible.es-qu: bible.es bible.qu
	./bitext_es_qu.sh

bible.en-es: bible.en bible.es
	./bitext_en_es.sh

bible.es-en: bible.es bible.en
	./bitext_es_en.sh


## extract bibles from their original formats
bible.es:
	./extract_es.sh

bible.gn:
	./extract_gn.sh

bible.en:
	./extract_en.sh

bible.qu:
	./extract_qu.sh
