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


* [index-linktemplate.html](index-linktemplate.html)  -- Edit this
* [index-respec.html](index-respec.html) -- Made by `python make_links.py`
* [index.html](index.html) -- Saved from `index-respec.html` in a browser
* [oa.ttl](oa.ttl) -- Web Annotation vocabulary as RDFS/OWL in [RDF Turtle](https://www.w3.org/TR/turtle/) format - not yet fully up to date with  `index.html`



## Building


If you are on Linux or OS X, and have Python and 
Java 7 or later installed, then try:

	make

This will generate `index-respec.html` and open it in a browser. 
You will then have to save this to `index.html` in the GUI.

Additionally this will convert `oa.ttl` to `oa.rdf` and `oa.jsonld`
using [Apache Jena](http://jena.apache.org/).

For inspection this will also render `oa.ttl` as `tmp/oa.html` using
[Widoco](https://github.com/dgarijo/Widoco)
and open that in the browser, but note that this
HTML file should NOT be checked in or published, as the HTML-version of the
vocabulary is defined in [index.html](index.html) by hand.


The software required is downloaded on demand to the `bin/` folder.

