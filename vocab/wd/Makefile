default: tmp

tmp/oa.ttl: oa.ttl
	mkdir -p tmp
	cp oa.ttl tmp/oa.ttl

tmp/oa.rdf: oa.ttl bin/jena
	mkdir -p tmp
	echo '<?xml version="1.0" encoding="UTF-8"?>' > tmp/oa.rdf
	echo '<!--' >> tmp/oa.rdf
	# Copy license header
	grep "^## " oa.ttl | sed 's/##//' >> tmp/oa.rdf
	echo '-->' >> tmp/oa.rdf
	bin/jena/bin/riot --output=rdfxml oa.ttl >> tmp/oa.rdf

tmp/oa.jsonld: oa.ttl bin/jena
	mkdir -p tmp
	echo -n '{ "__header": "' > tmp/oa.jsonld
	grep "^## " oa.ttl | sed 's/##//' | tr '\n' ' ' >> tmp/oa.jsonld
	echo '",' >> tmp/oa.jsonld
	bin/jena/bin/riot --output=jsonld oa.ttl | grep -v "^{" >> tmp/oa.jsonld

tmp/oa.html: bin/widoco.jar oa.ttl widoco.properties
	mkdir -p tmp
	java -jar bin/widoco.jar -ontFile oa.ttl  -outFolder tmp -confFile widoco.properties -rewriteAll
	mv tmp/index-en.html tmp/index.html
	cp tmp/index.html tmp/oa.html
	gnome-open tmp/oa.html || open tmp/oa.html || start tmp\\oa.html

bin:  bin/jena bin/widoco.jar

tmp: tmp/oa.ttl tmp/oa.rdf tmp/oa.jsonld tmp/oa.html


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
	rm -rf tmp

all: bin clean default
