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

## Spanish-French
bible.es-fr: bible.es bible.fr
	./bitext_es_fr.sh
	~/cdec/corpus/filter-length.pl -80 output/bible.es-fr.unfiltered > output/bible.es-fr.surface
	## having done the length filtering, we can take the source side of the
	## surface bitext and produce the annotated version.
	~/cdec/corpus/cut-corpus.pl 1 \
		< output/bible.es-fr.surface \
		> output/bible.es-fr.surface.source
	analyze -f freeling-config/es.cfg < output/bible.es-fr.surface.source > output/bible.es-fr.source.tagged
	~/cdec/corpus/cut-corpus.pl 2 \
		< output/bible.es-fr.surface \
		> output/bible.es-fr.surface.target
	analyze -f freeling-config/fr.cfg < output/bible.es-fr.surface.target > output/bible.es-fr.target.tagged
	python3 freeling_to_annotated.py \
	    --freeling output/bible.es-fr.source.tagged \
	    --lemma_out output/bible.es-fr.source.lemmas \
	    --annotated output/bible.es-fr.source.annotated
	python3 freeling_to_annotated.py \
	    --freeling output/bible.es-fr.target.tagged \
	    --lemma_out output/bible.es-fr.target.lemmas \
	    --annotated output/bible.es-fr.target.annotated
	~/cdec/corpus/paste-files.pl \
	    output/bible.es-fr.source.lemmas \
	    output/bible.es-fr.target.lemmas \
	    > output/bible.es-fr
	~/cdec/word-aligner/fast_align -i ./output/bible.es-fr -d -v -o > output/bible.es-fr.align

## Spanish-German
bible.es-de: bible.es bible.de
	./bitext_es_de.sh
	~/cdec/corpus/filter-length.pl -80 output/bible.es-de.unfiltered > output/bible.es-de.surface
	## having done the length filtering, we can take the source side of the
	## surface bitext and produce the annotated version.
	~/cdec/corpus/cut-corpus.pl 1 \
		< output/bible.es-de.surface \
		> output/bible.es-de.surface.source
	analyze -f freeling-config/es.cfg < output/bible.es-de.surface.source > output/bible.es-de.source.tagged
	~/cdec/corpus/cut-corpus.pl 2 \
		< output/bible.es-de.surface \
		> output/bible.es-de.surface.target
	analyze -f freeling-config/de.cfg < output/bible.es-de.surface.target > output/bible.es-de.target.tagged
	python3 freeling_to_annotated.py \
	    --freeling output/bible.es-de.source.tagged \
	    --lemma_out output/bible.es-de.source.lemmas \
	    --annotated output/bible.es-de.source.annotated
	python3 freeling_to_annotated.py \
	    --freeling output/bible.es-de.target.tagged \
	    --lemma_out output/bible.es-de.target.lemmas \
	    --annotated output/bible.es-de.target.annotated
	~/cdec/corpus/paste-files.pl \
	    output/bible.es-de.source.lemmas \
	    output/bible.es-de.target.lemmas \
	    > output/bible.es-de
	~/cdec/word-aligner/fast_align -i ./output/bible.es-de -d -v -o > output/bible.es-de.align

## Spanish-Italian
bible.es-it: bible.es bible.it
	./bitext_es_it.sh
	~/cdec/corpus/filter-length.pl -80 output/bible.es-it.unfiltered > output/bible.es-it.surface
	## having done the length filtering, we can take the source side of the
	## surface bitext and produce the annotated version.
	~/cdec/corpus/cut-corpus.pl 1 \
		< output/bible.es-it.surface \
		> output/bible.es-it.surface.source
	analyze -f freeling-config/es.cfg < output/bible.es-it.surface.source > output/bible.es-it.source.tagged
	~/cdec/corpus/cut-corpus.pl 2 \
		< output/bible.es-it.surface \
		> output/bible.es-it.surface.target
	analyze -f freeling-config/it.cfg < output/bible.es-it.surface.target > output/bible.es-it.target.tagged
	python3 freeling_to_annotated.py \
	    --freeling output/bible.es-it.source.tagged \
	    --lemma_out output/bible.es-it.source.lemmas \
	    --annotated output/bible.es-it.source.annotated
	python3 freeling_to_annotated.py \
	    --freeling output/bible.es-it.target.tagged \
	    --lemma_out output/bible.es-it.target.lemmas \
	    --annotated output/bible.es-it.target.annotated
	~/cdec/corpus/paste-files.pl \
	    output/bible.es-it.source.lemmas \
	    output/bible.es-it.target.lemmas \
	    > output/bible.es-it
	~/cdec/word-aligner/fast_align -i ./output/bible.es-it -d -v -o > output/bible.es-it.align

## Spanish-Dutch
bible.es-nl: bible.es bible.nl
	./bitext_es_nl.sh
	~/cdec/corpus/filter-length.pl -80 output/bible.es-nl.unfiltered > output/bible.es-nl.surface
	## having done the length filtering, we can take the source side of the
	## surface bitext and produce the annotated version.
	~/cdec/corpus/cut-corpus.pl 1 \
		< output/bible.es-nl.surface \
		> output/bible.es-nl.surface.source
	analyze -f freeling-config/es.cfg < output/bible.es-nl.surface.source > output/bible.es-nl.source.tagged
	python3 freeling_to_annotated.py \
	    --freeling output/bible.es-nl.source.tagged \
	    --lemma_out output/bible.es-nl.source.lemmas \
	    --annotated output/bible.es-nl.source.annotated
	~/cdec/corpus/cut-corpus.pl 2 \
		< output/bible.es-nl.surface \
		> output/bible.es-nl.surface.target
	~/lamachine/bin/frog -n < output/bible.es-nl.surface.target > output/bible.es-nl.target.frog
	python3 frog_to_lemmas.py \
	    --frog output/bible.es-nl.target.frog \
	    --lemma_out output/bible.es-nl.target.lemmas
	~/cdec/corpus/paste-files.pl \
	    output/bible.es-nl.source.lemmas \
	    output/bible.es-nl.target.lemmas \
	    > output/bible.es-nl
	~/cdec/word-aligner/fast_align -i ./output/bible.es-nl -d -v -o > output/bible.es-nl.align

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
