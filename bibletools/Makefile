## makefile to build all the bibles

all: bible.es-en bible.es-gn bible.es-qu bible.en-es

bible.es-gn: bible.es bible.gn
	./bitext_es_gn.sh

bible.es-qu: bible.es bible.qu
	./bitext_es_qu.sh

bible.en-es: bible.en bible.es
	./bitext_en_es.sh

bible.es-en: bible.es bible.en
	./bitext_es_en.sh

bible.es:
	./extract_es.sh

bible.gn:
	./extract_gn.sh

bible.en:
	./extract_en.sh

bible.qu:
	./extract_qu.sh
