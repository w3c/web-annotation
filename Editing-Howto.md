## Editing and Building the Documents

### Model

Only edit the most recent working draft, currently `/model/wd2`.  Only edit `index-nametemplate.html` and then follow these steps to build the final HTML document:

* Run `python ./rename_names.py` — this adds the names to the use cases  
* Run `python ./extract_egs.py` — this checks and extracts the examples
* Load `index-respec.html` in a browser and use `respec` to save as HTML
* Move the resulting `index.html` into the directory
* In the directory, `git add -A *``

The final files for publication are:

* `index.html`
* `examples/`  
* `images/`
* `orcid_logo.png`

### Vocab

Only edit the most recent working draft, currently `/vocab/wd`.  Only edit `index-linktemplate.html` and then follow these steps to build the final HTML document:

* Run `python ./make_links.py` — this makes all of the vocab terms into links
* Run `python ./extract_egs.py` — this checks and extracts the examples
* Load `index-respec.html` in a browser and use `respec` to save as HTML
* Move the resulting `index.html` into the directory
* In the directory, `git add -A *``

The final files for publication are:

* `index.html`
* `examples/`
* `images/`
* `orcid_logo.png`

### Protocol

Only edit the most recent working draft, currently `/protocol/wd`.  Only edit `index-respec.html` and then follow these steps to build the final HTML document:

* Load `index-respec.html` in a browser and use `respec` to save as HTML
* Move the resulting `index.html` into the directory
* In the directory, `git add -A *``

The final files for publication are:

* `index.html`
* `orcid_logo.png`

(There are no scripts associated with the protocol document)

### HTML serialization note

Only edit the most recent working draft, currently `/serialization-html-note`.  Only edit `index-turtle-not-highligh.html` and the follow these steps build the final HTML document

* Run `python highlight-turtle.py` — this adds color highlighting to turtle examples
* Load `index-respec.html` in a browser and use `respec` to save as HTML
* Move the resulting `index.html` into the directory
* In the directory, `git add -A *`

The final files for publication are:

* `index.html`
* `images/`
* `orcid_logo.png`

### Selector note

Only edit the most recent working draft, currently `/selector-note`.  Only edit `index-turtle-not-highligh.html` and the follow these steps build the final HTML document

* Run `python highlight-turtle.py` — this adds color highlighting to turtle examples
* Load `index-respec.html` in a browser and use `respec` to save as HTML5
* Move the resulting `index.html` into the directory
* In the directory, `git add -A *`

The final files for publication are:

* `index.html`
* `images/`
* `orcid_logo.png`
