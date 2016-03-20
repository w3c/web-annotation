default: wd

wd/oa.ttl: oa.ttl
	mkdir -p wd
	cp oa.ttl wd/oa.ttl

wd/oa.rdf: oa.ttl bin/jena
	mkdir -p wd
	bin/jena/bin/riot --output=rdfxml oa.ttl > wd/oa.rdf

wd/oa.jsonld: oa.ttl bin/jena
	mkdir -p wd
	bin/jena/bin/riot --output=jsonld oa.ttl > wd/oa.jsonld

wd/oa.html: bin/widoco.jar oa.ttl widoco.properties
	mkdir -p wd
	java -jar bin/widoco.jar -ontFile oa.ttl  -outFolder wd -confFile widoco.properties -rewriteAll
	mv wd/index-en.html wd/index.html
	cp wd/index.html wd/oa.html

bin:  bin/jena bin/widoco.jar

wd: wd/oa.ttl wd/oa.rdf wd/oa.jsonld wd/oa.html


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
	rm -rf wd

all: bin clean default
