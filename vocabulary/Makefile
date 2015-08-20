
default: bin out out/oa.rdf out/oa.jsonld

# http://jena.apache.org/
bin/jena:
	mkdir -p bin 
	rm -rf bin/jena
	curl http://www.us.apache.org/dist/jena/binaries/apache-jena-3.0.0.tar.gz > bin/jena.tar.gz
	echo 0563da22020560ea2b08cc011bebf878c10515ce jena.tar.gz > bin/jena.tar.gz.sha1
	cd bin ; sha1sum -c jena.tar.gz.sha1 
	cd bin ; tar xzf jena.tar.gz && mv apache-jena* jena
	rm bin/jena.tar.gz*

# See https://github.com/dgarijo/Widoco
bin/widoco.jar:
	mkdir -p bin
	curl https://github.com/dgarijo/Widoco/blob/6601579c9a2dd825cb1800aefc872939727e1ed6/JAR/widoco-0.0.1-jar-with-dependencies.jar?raw=true > bin/widoco.tmp
	echo 4f00237ac28115d5301751c5312029f9b5c31558 widoco.tmp > bin/widoco.jar.sha1
	cd bin ; sha1sum -c widoco.jar.sha1
	mv bin/widoco.tmp bin/widoco.jar

	

bin: bin/jena bin/widoco.jar

out: oa.ttl
	mkdir -p out
	cp oa.ttl out/oa.ttl
	java -jar bin/widoco.jar -ontFile oa.ttl  -outFolder out -confFile widoco.properties -rewriteAll

out/oa.rdf: oa.ttl
	mkdir -p out
	bin/jena/bin/riot --output=rdfxml oa.ttl > out/oa.rdf

out/oa.jsonld: oa.ttl bin/jena
	mkdir -p out
	bin/jena/bin/riot --output=jsonld oa.ttl > out/oa.jsonld

clean:
	rm -rf out 

all: clean default
