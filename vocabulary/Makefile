default: out

out/oa.ttl: oa.ttl
	mkdir -p out
	cp oa.ttl out/oa.ttl

out/oa.rdf: oa.ttl bin/jena
	mkdir -p out
	bin/jena/bin/riot --output=rdfxml oa.ttl > out/oa.rdf

out/oa.jsonld: oa.ttl bin/jena
	mkdir -p out
	bin/jena/bin/riot --output=jsonld oa.ttl > out/oa.jsonld

out/oa: bin/widoco.jar oa.ttl widoco.properties
	mkdir -p out/oa
	java -jar bin/widoco.jar -ontFile oa.ttl  -outFolder out/oa -confFile widoco.properties -rewriteAll

bin:  bin/jena bin/widoco.jar

out: out/oa.ttl out/oa.rdf out/oa.jsonld out/oa


# http://jena.apache.org/
bin/jena:
	mkdir -p bin
	rm -rf bin/jena
	curl -L http://www.us.apache.org/dist/jena/binaries/apache-jena-3.0.0.tar.gz > bin/jena.tar.gz
	echo 0563da22020560ea2b08cc011bebf878c10515ce jena.tar.gz > bin/jena.tar.gz.sha1
	cd bin ; sha1sum -c jena.tar.gz.sha1 
	cd bin ; tar xzf jena.tar.gz && mv apache-jena* jena
	rm bin/jena.tar.gz*

# See https://github.com/dgarijo/Widoco
bin/widoco.jar:
	mkdir -p bin
	curl -L https://github.com/dgarijo/Widoco/blob/6601579c9a2dd825cb1800aefc872939727e1ed6/JAR/widoco-0.0.1-jar-with-dependencies.jar?raw=true > bin/widoco.tmp
	echo c146d8f2683e08143fc236c062c7b99995179505 widoco.tmp > bin/widoco.jar.sha1
	cd bin ; sha1sum -c widoco.jar.sha1
	mv bin/widoco.tmp bin/widoco.jar

clean:
	rm -rf out 

all: bin clean default
