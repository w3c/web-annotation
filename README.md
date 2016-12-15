Web-Annotation
==========

Documents produced by the [Web Annotation Working Group](http://www.w3.org/annotation/) of the W3C.

Current in-progress drafts:
  * Model: http://w3c.github.io/web-annotation/model/wd2/
    * [Test Results](https://github.com/w3c/test-results/tree/gh-pages/annotation-model#annotation-model-test-results) & [Process](https://github.com/w3c/test-results/tree/gh-pages/annotation-model#adding-new-results)
  * Vocab: http://w3c.github.io/web-annotation/vocab/wd/
    * [Test Results](https://github.com/w3c/test-results/tree/gh-pages/annotation-vocab#annotation-vocabulary-test-results)
  * Protocol: http://w3c.github.io/web-annotation/protocol/wd/
    * [Test Results](https://github.com/w3c/test-results/tree/gh-pages/annotation-protocol#annotation-protocol-test-results) & [Process](https://github.com/w3c/test-results/tree/gh-pages/annotation-protocol#adding-new-results)
  * Selector note: http://w3c.github.io/web-annotation/selector-note/

See also a [paged view](http://w3c.github.io/web-annotation/) of the documents served in HTML.

If you are member of the interest group, and you wish to contribute to the content of this repo, please contact Ivan Herman (<ivan@w3.org>), giving him your github login.


## Editing and Building the Documents

### Model

Only edit the most recent working draft, currently /model/wd2.  Only edit index-nametemplate.html and then follow these steps to build the final HTML document:

* Run `python ./rename_names.py` -- this adds the names to the use cases  
* Run `python ./extract_egs.py` -- this checks and extracts the examples
* Load `index-respec.html` in a browser and use respec to save as HTML5
* Move the resulting `index.html` into the directory
* In the directory, git add -A *

The final files for publication are:

* index.html
* examples/  
* images/

### Vocab

Only edit the most recent working draft, currently /vocab/wd.  Only edit index-linktemplate.html and then follow these steps to build the final HTML document:

* Run `python ./make_links.py` -- this makes all of the vocab terms into links
* Run `python ./extract_egs.py` -- this checks and extracts the examples
* Load `index-respec.html` in a browser and use respec to save as HTML5
* Move the resulting `index.html` into the directory
* In the directory, git add -A *

The final files for publication are:

* index.html
* examples/
* images/

### Protocol

Only edit the most recent working draft, currently /protocol/wd.  Only edit index-respec.html and then follow these steps to build the final HTML document:

* Load `index-respec.html` in a browser and use respec to save as HTML5
* Move the resulting `index.html` into the directory
* In the directory, git add -A *

The final files for publication are:

* index.html

(There are no scripts associated with the protocol document)

### Selector note

Only edit the most recent working draft, currently /selector-note.  Only edit index-respec.html and then follow these steps to build the final HTML document:

* Load `index-respec.html` in a browser and use respec to save as HTML5
* Move the resulting `index.html` into the directory
* In the directory, git add -A *

(There are no scripts associated with the Selector note)
