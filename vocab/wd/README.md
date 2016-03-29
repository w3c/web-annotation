# W3C Web Annotation vocabulary

* Contact: [Web Annotation Working Group](http://www.w3.org/annotation/)

The vocabulary/ontology for the [W3C Web Annotation Data
Model](http://www.w3.org/TR/annotation-model/), describing the
http://www.w3.org/ns/oa# namespace.

This is *work in progress* - feel free to raise any
[issues](https://github.com/w3c/web-annotation/issues) or
[suggest changes](https://github.com/w3c/web-annotation/pulls).

Discuss this on the 
[public-annotation mailing list](https://lists.w3.org/Archives/Public/public-annotation/).


* [index.html](index.html) -- Web Annotation Vocabulary HTML (This is for publishing - don't edit directly)
* [index-respec.html](index-respec.html) -- [ReSpec](https://www.w3.org/respec/) source for index.html
* [index-linktemplate.html](index-linktemplate.html)  -- not sure!
* [oa.ttl](oa.ttl) -- Web Annotation vocabulary as RDFS/OWL in [RDF Turtle](https://www.w3.org/TR/turtle/) format - not yet fully up to date with  `index.html`



## Converting oa.ttl

To convert [oa.ttl](oa.ttl) to `oa.rdf` and `oa.jsonld`, and 
you are on Linux or OS X, and have Java 7 or later installed, then try:

	make

This will populate the `tmp` folder using [Apache Jena](http://jena.apache.org/).
Do not check in the tmp/ folder to git.

For inspection this will also render `oa.ttl` as `tmp/oa.html` using
[Widoco](https://github.com/dgarijo/Widoco)
and open that in the browser, but note that this
HTML file should NOT be published, as the HTML-version of the
vocabulary is defined in [index.html](index.html) by hand.


The software required is downloaded on demand to the `bin/` folder.

