## makefile to build all the bibles and run alignment on them

all: bible.es-en bible.es-gn bible.es-qu bible.en-es

## Spanish-English
bible.es-en: bible.es bible.en
	./bitext_es_en.sh
	~/cdec/corpus/filter-length.pl -80 output/bible.es-en.unfiltered > output/bible.es-en.surface
	## having done the length filtering, we can take the source side of the
	## surface bitext and produce the annotated version.
	~/cdec/corpus/cut-corpus.pl 1 \
		< output/bible.es-en.surface \
		> output/bible.es-en.surface.source
	analyze -f freeling-config/es.cfg < output/bible.es-en.surface.source > output/bible.es-en.source.tagged
	~/cdec/corpus/cut-corpus.pl 2 \
		< output/bible.es-en.surface \
		> output/bible.es-en.surface.target
	analyze -f freeling-config/en.cfg < output/bible.es-en.surface.target > output/bible.es-en.target.tagged
	python3 freeling_to_annotated.py \
	    --freeling output/bible.es-en.source.tagged \
	    --lemma_out output/bible.es-en.source.lemmas \
	    --annotated output/bible.es-en.source.annotated
	python3 freeling_to_annotated.py \
	    --freeling output/bible.es-en.target.tagged \
	    --lemma_out output/bible.es-en.target.lemmas \
	    --annotated output/bible.es-en.target.annotated
	~/cdec/corpus/paste-files.pl \
	    output/bible.es-en.source.lemmas \
	    output/bible.es-en.target.lemmas \
	    > output/bible.es-en
	~/cdec/word-aligner/fast_align -i ./output/bible.es-en -d -v -o > output/bible.es-en.align

## English-Spanish (very similar to es-en)
bible.en-es: bible.en bible.es
	./bitext_en_es.sh
	~/cdec/corpus/filter-length.pl -80 output/bible.en-es.unfiltered > output/bible.en-es.surface
	## having done the length filtering, we can take the source side of the
	## surface bitext and produce the annotated version.
	~/cdec/corpus/cut-corpus.pl 1 \
		< output/bible.en-es.surface \
		> output/bible.en-es.surface.source
	analyze -f freeling-config/en.cfg < output/bible.en-es.surface.source > output/bible.en-es.source.tagged
	~/cdec/corpus/cut-corpus.pl 2 \
		< output/bible.en-es.surface \
		> output/bible.en-es.surface.target
	analyze -f freeling-config/es.cfg < output/bible.en-es.surface.target > output/bible.en-es.target.tagged
	python3 freeling_to_annotated.py \
	    --freeling output/bible.en-es.source.tagged \
	    --lemma_out output/bible.en-es.source.lemmas \
	    --annotated output/bible.en-es.source.annotated
	python3 freeling_to_annotated.py \
	    --freeling output/bible.en-es.target.tagged \
	    --lemma_out output/bible.en-es.target.lemmas \
	    --annotated output/bible.en-es.target.annotated
	~/cdec/corpus/paste-files.pl \
	    output/bible.en-es.source.lemmas \
	    output/bible.en-es.target.lemmas \
	    > output/bible.en-es
	~/cdec/word-aligner/fast_align -i ./output/bible.en-es -d -v -o > output/bible.en-es.align

## Spanish-Guarani
bible.es-gn: bible.es bible.gn
	./bitext_es_gn.sh
	~/cdec/corpus/filter-length.pl -80 output/bible.es-gn.unfiltered > output/bible.es-gn.surface
	## having done the length filtering, we can take the source side of the
	## surface bitext and produce the annotated version.
	~/cdec/corpus/cut-corpus.pl 1 \
		< output/bible.es-gn.surface \
		> output/bible.es-gn.surface.source
	analyze -f freeling-config/es.cfg < output/bible.es-gn.surface.source > output/bible.es-gn.source.tagged
	python3 freeling_to_annotated.py \
	    --freeling output/bible.es-gn.source.tagged \
	    --lemma_out output/bible.es-gn.source.lemmas \
	    --annotated output/bible.es-gn.source.annotated
	~/cdec/corpus/cut-corpus.pl 2 \
		< output/bible.es-gn.surface \
		> output/bible.es-gn.surface.target
	### run gn side through cdec's lowercasing and tokenization.
	cat output/bible.es-gn.surface.target \
		| ~/cdec/corpus/lowercase.pl \
		| ~/cdec/corpus/tokenize-anything.sh \
		> output/bible.es-gn.surface.target.tokenized
	## now get the gn lemmas
	python3 lemmatize_text.py gn output/bible.es-gn.surface.target.tokenized output/bible.es-gn.target.lemmas
	~/cdec/corpus/paste-files.pl \
	    output/bible.es-gn.source.lemmas \
	    output/bible.es-gn.target.lemmas \
	    > output/bible.es-gn
	~/cdec/word-aligner/fast_align -i ./output/bible.es-gn -d -v -o > output/bible.es-gn.align

## Spanish-Quechua
bible.es-qu: bible.es bible.qu
	./bitext_es_qu.sh
	~/cdec/corpus/filter-length.pl -80 output/bible.es-qu.unfiltered > output/bible.es-qu.surface
	## having done the length filtering, we can take the source side of the
	## surface bitext and produce the annotated version.
	~/cdec/corpus/cut-corpus.pl 1 \
		< output/bible.es-qu.surface \
		> output/bible.es-qu.surface.source
	analyze -f freeling-config/es.cfg < output/bible.es-qu.surface.source > output/bible.es-qu.source.tagged
	python3 freeling_to_annotated.py \
	    --freeling output/bible.es-qu.source.tagged \
	    --lemma_out output/bible.es-qu.source.lemmas \
	    --annotated output/bible.es-qu.source.annotated
	~/cdec/corpus/cut-corpus.pl 2 \
		< output/bible.es-qu.surface \
		> output/bible.es-qu.surface.target
	### run qu side through cdec's lowercasing and tokenization.
	cat output/bible.es-qu.surface.target \
		| ~/cdec/corpus/lowercase.pl \
		| ~/cdec/corpus/tokenize-anything.sh \
		> output/bible.es-qu.surface.target.tokenized
	## now get the qu lemmas
	python3 lemmatize_text.py qu output/bible.es-qu.surface.target.tokenized output/bible.es-qu.target.lemmas
	~/cdec/corpus/paste-files.pl \
	    output/bible.es-qu.source.lemmas \
	    output/bible.es-qu.target.lemmas \
	    > output/bible.es-qu
	~/cdec/word-aligner/fast_align -i ./output/bible.es-qu -d -v -o > output/bible.es-qu.align

## extract bibles from their original formats
bible.es:
	./extract_es.sh

bible.gn:
	./extract_gn.sh

bible.en:
	./extract_en.sh

bible.qu:
	./extract_qu.sh

bible.de:
	./extract_de.sh

bible.fr:
	./extract_fr.sh

bible.it:
	./extract_it.sh

bible.nl:
	./extract_nl.sh
