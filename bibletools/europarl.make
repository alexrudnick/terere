## makefile just for the Europarl bitext

all: europarl.en-es europarl.es-en europarl.es-fr

# English-Spanish
europarl.en-es:
	~/cdec/corpus/paste-files.pl /space/europarl-parallel/europarl-v7.es-en.en /space/europarl-parallel/europarl-v7.es-en.es > output/europarl.en-es.unfiltered
	~/cdec/corpus/filter-length.pl -80 output/europarl.en-es.unfiltered > output/europarl.en-es.surface
	## having done the length filtering, we can take the source side of the
	## surface bitext and produce the annotated version.
	~/cdec/corpus/cut-corpus.pl 1 \
		< output/europarl.en-es.surface \
		> output/europarl.en-es.surface.source
	analyze -f freeling-config/en.cfg < output/europarl.en-es.surface.source > output/europarl.en-es.source.tagged
	~/cdec/corpus/cut-corpus.pl 2 \
		< output/europarl.en-es.surface \
		> output/europarl.en-es.surface.target
	analyze -f freeling-config/es.cfg < output/europarl.en-es.surface.target > output/europarl.en-es.target.tagged
	python3 freeling_to_annotated.py \
	    --freeling output/europarl.en-es.source.tagged \
	    --lemma_out output/europarl.en-es.source.lemmas \
	    --annotated output/europarl.en-es.source.annotated
	python3 freeling_to_annotated.py \
	    --freeling output/europarl.en-es.target.tagged \
	    --lemma_out output/europarl.en-es.target.lemmas \
	    --annotated output/europarl.en-es.target.annotated
	~/cdec/corpus/paste-files.pl \
	    output/europarl.en-es.source.lemmas \
	    output/europarl.en-es.target.lemmas \
	    > output/europarl.en-es
	~/cdec/word-aligner/fast_align -i ./output/europarl.en-es -d -v -o > output/europarl.en-es.align

europarl.es-en:
	~/cdec/corpus/paste-files.pl /space/europarl-parallel/europarl-v7.es-en.es /space/europarl-parallel/europarl-v7.es-en.en > output/europarl.es-en.unfiltered
	~/cdec/corpus/filter-length.pl -80 output/europarl.es-en.unfiltered > output/europarl.es-en.surface
	## having done the length filtering, we can take the source side of the
	## surface bitext and produce the annotated version.
	~/cdec/corpus/cut-corpus.pl 1 \
		< output/europarl.es-en.surface \
		> output/europarl.es-en.surface.source
	analyze -f freeling-config/es.cfg < output/europarl.es-en.surface.source > output/europarl.es-en.source.tagged
	~/cdec/corpus/cut-corpus.pl 2 \
		< output/europarl.es-en.surface \
		> output/europarl.es-en.surface.target
	analyze -f freeling-config/en.cfg < output/europarl.es-en.surface.target > output/europarl.es-en.target.tagged
	python3 freeling_to_annotated.py \
	    --freeling output/europarl.es-en.source.tagged \
	    --lemma_out output/europarl.es-en.source.lemmas \
	    --annotated output/europarl.es-en.source.annotated
	python3 freeling_to_annotated.py \
	    --freeling output/europarl.es-en.target.tagged \
	    --lemma_out output/europarl.es-en.target.lemmas \
	    --annotated output/europarl.es-en.target.annotated
	~/cdec/corpus/paste-files.pl \
	    output/europarl.es-en.source.lemmas \
	    output/europarl.es-en.target.lemmas \
	    > output/europarl.es-en
	~/cdec/word-aligner/fast_align -i ./output/europarl.es-en -d -v -o > output/europarl.es-en.align

europarl.es-fr:
	~/cdec/corpus/paste-files.pl /space/europarl/aligned/es-fr/es.txt /space/europarl/aligned/es-fr/fr.txt > output/europarl.es-fr.unfiltered
	~/cdec/corpus/filter-length.pl -80 output/europarl.es-fr.unfiltered > output/europarl.es-fr.surface
	## having done the length filtering, we can take the source side of the
	## surface bitext and produce the annotated version.
	~/cdec/corpus/cut-corpus.pl 1 \
		< output/europarl.es-fr.surface \
		> output/europarl.es-fr.surface.source
	analyze -f freeling-config/es.cfg < output/europarl.es-fr.surface.source > output/europarl.es-fr.source.tagged
	~/cdec/corpus/cut-corpus.pl 2 \
		< output/europarl.es-fr.surface \
		> output/europarl.es-fr.surface.target
	analyze -f freeling-config/fr.cfg < output/europarl.es-fr.surface.target > output/europarl.es-fr.target.tagged
	python3 freeling_to_annotated.py \
	    --freeling output/europarl.es-fr.source.tagged \
	    --lemma_out output/europarl.es-fr.source.lemmas \
	    --annotated output/europarl.es-fr.source.annotated
	python3 freeling_to_annotated.py \
	    --freeling output/europarl.es-fr.target.tagged \
	    --lemma_out output/europarl.es-fr.target.lemmas \
	    --annotated output/europarl.es-fr.target.annotated
	~/cdec/corpus/paste-files.pl \
	    output/europarl.es-fr.source.lemmas \
	    output/europarl.es-fr.target.lemmas \
	    > output/europarl.es-fr
	~/cdec/word-aligner/fast_align -i ./output/europarl.es-fr -d -v -o > output/europarl.es-fr.align

100keuroparl.es-fr:
	~/cdec/corpus/paste-files.pl /space/europarl/aligned/es-fr/es.txt /space/europarl/aligned/es-fr/fr.txt > output/europarl.es-fr.unfiltered
	~/cdec/corpus/filter-length.pl -80 output/europarl.es-fr.unfiltered > output/europarl.es-fr.surface
	head -n 100000 output/europarl.es-fr.surface > output/100keuroparl.es-fr.surface
	## having done the length filtering, we can take the source side of the
	## surface bitext and produce the annotated version.
	~/cdec/corpus/cut-corpus.pl 1 \
		< output/100keuroparl.es-fr.surface \
		> output/100keuroparl.es-fr.surface.source
	analyze -f freeling-config/es.cfg < output/100keuroparl.es-fr.surface.source > output/100keuroparl.es-fr.source.tagged
	~/cdec/corpus/cut-corpus.pl 2 \
		< output/100keuroparl.es-fr.surface \
		> output/100keuroparl.es-fr.surface.target
	analyze -f freeling-config/fr.cfg < output/100keuroparl.es-fr.surface.target > output/100keuroparl.es-fr.target.tagged
	python3 freeling_to_annotated.py \
	    --freeling output/100keuroparl.es-fr.source.tagged \
	    --lemma_out output/100keuroparl.es-fr.source.lemmas \
	    --annotated output/100keuroparl.es-fr.source.annotated
	python3 freeling_to_annotated.py \
	    --freeling output/100keuroparl.es-fr.target.tagged \
	    --lemma_out output/100keuroparl.es-fr.target.lemmas \
	    --annotated output/100keuroparl.es-fr.target.annotated
	~/cdec/corpus/paste-files.pl \
	    output/100keuroparl.es-fr.source.lemmas \
	    output/100keuroparl.es-fr.target.lemmas \
	    > output/100keuroparl.es-fr
	~/cdec/word-aligner/fast_align -i ./output/100keuroparl.es-fr -d -v -o > output/100keuroparl.es-fr.align

europarl.es-de:
	~/cdec/corpus/paste-files.pl /space/europarl/aligned/es-de/es.txt /space/europarl/aligned/es-de/de.txt > output/europarl.es-de.unfiltered
	~/cdec/corpus/filter-length.pl -80 output/europarl.es-de.unfiltered > output/europarl.es-de.surface
	## having done the length filtering, we can take the source side of the
	## surface bitext and produce the annotated version.
	~/cdec/corpus/cut-corpus.pl 1 \
		< output/europarl.es-de.surface \
		> output/europarl.es-de.surface.source
	analyze -f freeling-config/es.cfg < output/europarl.es-de.surface.source > output/europarl.es-de.source.tagged
	~/cdec/corpus/cut-corpus.pl 2 \
		< output/europarl.es-de.surface \
		> output/europarl.es-de.surface.target
	analyze -f freeling-config/de.cfg < output/europarl.es-de.surface.target > output/europarl.es-de.target.tagged
	python3 freeling_to_annotated.py \
	    --freeling output/europarl.es-de.source.tagged \
	    --lemma_out output/europarl.es-de.source.lemmas \
	    --annotated output/europarl.es-de.source.annotated
	python3 freeling_to_annotated.py \
	    --freeling output/europarl.es-de.target.tagged \
	    --lemma_out output/europarl.es-de.target.lemmas \
	    --annotated output/europarl.es-de.target.annotated
	~/cdec/corpus/paste-files.pl \
	    output/europarl.es-de.source.lemmas \
	    output/europarl.es-de.target.lemmas \
	    > output/europarl.es-de
	~/cdec/word-aligner/fast_align -i ./output/europarl.es-de -d -v -o > output/europarl.es-de.align
