default: oa.rdf oa.jsonld oa.rdfa.html tmp/oa.html index.html

index-respec.html: index-linktemplate.html
	python make_links.py

index.html: index-respec.html
	echo "\n\nindex.html is out of date.\n Open index-respec.html in browser, then\n click ReSpec and Save Snapshot as HTML to index.html\n"
	sleep 2
	gnome-open index-respec.html || open index-respec.html || start index-respec.html


oa.rdf: oa.ttl bin/jena
	echo '<?xml version="1.0" encoding="UTF-8"?>' > oa.rdf
	echo '<!--' >> oa.rdf
	# Copy license header
	grep "^### " oa.ttl | sed 's/###//' >> oa.rdf
	echo '-->' >> oa.rdf
	bin/jena/bin/riot --output=rdfxml oa.ttl >> oa.rdf

oa.jsonld: oa.ttl bin/jena
	echo -n '{ "__header": "' > oa.jsonld
	grep "^### " oa.ttl | sed 's/###//' | tr '\n' ' ' >> oa.jsonld
	echo '",' >> oa.jsonld
	bin/jena/bin/riot --output=jsonld oa.ttl | grep -v "^{" >> oa.jsonld

oa.rdfa.html: oa.ttl
	curl --data-urlencode content@oa.ttl http://rdf-translator.appspot.com/convert/n3/rdfa/content > oa.rdfa.html

tmp/oa.html: bin/widoco.jar oa.ttl widoco.properties
	mkdir -p tmp
	java -jar bin/widoco.jar -ontFile oa.ttl  -outFolder tmp -confFile widoco.properties -rewriteAll
	mv tmp/index-en.html tmp/oa.html
	cp widoco/* tmp/sections/

bin:  bin/jena bin/widoco.jar



# http://jena.apache.org/
bin/jena:
	mkdir -p bin
	rm -rf bin/jena
	curl -L http://archive.apache.org/dist/jena/binaries/apache-jena-3.0.0.tar.gz -o bin/jena.tar.gz
	echo 0563da22020560ea2b08cc011bebf878c10515ce jena.tar.gz > bin/jena.tar.gz.sha1
	cd bin ; sha1sum -c jena.tar.gz.sha1
	cd bin ; tar xzf jena.tar.gz && mv apache-jena* jena
	rm bin/jena.tar.gz*

# See https://github.com/dgarijo/Widoco
bin/widoco.jar:
	mkdir -p bin
	curl -L https://github.com/dgarijo/Widoco/blob/v0.0.1/JAR/widoco-0.0.1-jar-with-dependencies.jar?raw=true -o bin/widoco.tmp
	echo add2bb94a4d8aac1a30152d63077df51b644d0c3 widoco.tmp > bin/widoco.jar.sha1
	cd bin ; sha1sum -c widoco.jar.sha1
	mv bin/widoco.tmp bin/widoco.jar

clean:
	rm -rf tmp oa.rdf oa.jsonld oa.rdfa.html index-respec.html index.html

all: bin clean default
