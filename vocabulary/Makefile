
default: out/oa.rdf out/oa.jsonld out/oa.ttl out/doc

clean:
	rm -rf out 

deepclean: clean
	rm -rf bin

all: bin clean default

	

out/oa.ttl: oa.ttl
	cp oa.ttl out/oa.ttl

out/oa.rdf: oa.ttl bin/jena out
	bin/jena/bin/riot --output=rdfxml oa.ttl > out/oa.rdf

out/oa.jsonld: oa.ttl bin/jena out
	bin/jena/bin/riot --output=jsonld oa.ttl > out/oa.jsonld

out/doc: bin/widoco.jar
	mkdir -p out/doc
	java -jar bin/widoco.jar -ontFile oa.ttl  -outFolder out/doc -confFile widoco.properties -rewriteAll


bin: 
	mkdir -p bin

out:
	mkdir -p out

# http://jena.apache.org/
bin/jena: bin
	rm -rf bin/jena
	curl http://www.us.apache.org/dist/jena/binaries/apache-jena-3.0.0.tar.gz > bin/jena.tar.gz
	echo 0563da22020560ea2b08cc011bebf878c10515ce jena.tar.gz > bin/jena.tar.gz.sha1
	cd bin ; sha1sum -c jena.tar.gz.sha1 
	cd bin ; tar xzf jena.tar.gz && mv apache-jena* jena
	rm bin/jena.tar.gz*

# See https://github.com/dgarijo/Widoco
bin/widoco.jar: bin
	curl https://github.com/dgarijo/Widoco/blob/6601579c9a2dd825cb1800aefc872939727e1ed6/JAR/widoco-0.0.1-jar-with-dependencies.jar?raw=true > bin/widoco.tmp
	echo 4f00237ac28115d5301751c5312029f9b5c31558 widoco.tmp > bin/widoco.jar.sha1
	cd bin ; sha1sum -c widoco.jar.sha1
	mv bin/widoco.tmp bin/widoco.jar
