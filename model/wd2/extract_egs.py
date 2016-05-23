from lxml import etree
import json
from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager

namespaces = {
              'oa' : Namespace('http://www.w3.org/ns/oa#'),
              'dc' : Namespace('http://purl.org/dc/elements/1.1/'),
              'dcterms' : Namespace('http://purl.org/dc/terms/'),
              'dctypes' : Namespace('http://purl.org/dc/dcmitype/'),
              'owl' : Namespace('http://www.w3.org/2002/07/owl#'),
              'rdf' : Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#'),
              'rdfs' : Namespace('http://www.w3.org/2000/01/rdf-schema#'),
              'skos' : Namespace('http://www.w3.org/2004/02/skos/core#'),
              'foaf' : Namespace('http://xmlns.com/foaf/0.1/'),
              'prov' : Namespace('http://www.w3.org/ns/prov#'),
              'xsd' : Namespace('http://www.w3.org/2001/XMLSchema#'),
              'sioc' : Namespace("http://rdfs.org/sioc/ns#")}

pfxs = []

for (key,val) in namespaces.copy().iteritems():
	pfxs.append("@prefix %s: <%s> ." % (key, val))
pfxstr = '\n'.join(pfxs)

fh = file('index-respec.html')
data = fh.read()
fh.close()

dom = etree.HTML(data)
egs = dom.xpath('//pre[@class="example highlight"]')

x = 0

# NB this is a string to ensure ordering of the keys
collection = """
{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "id": "http://example.org/collection1",
  "type": "AnnotationCollection",
  "creator": "http://www.w3.org/",
  "label": "Annotation Examples",
  "total": %i,
  "first": {
    "id": "http://example.org/collection1/page1",
    "type": "AnnotationPage",
    "startIndex": 0,
    "items": [
"""

end = """
    ]
  }
}
"""


fh = file('../../jsonld/anno.jsonld')
ctxt = fh.read()
fh.close()
ctxtjs = json.loads(ctxt)
ctxtjs = ctxtjs['@context']
for (k,v) in ctxtjs.items():
	if type(v) == str and v.startswith('http://'):
		del ctxtjs[k]

annos = []

def check_keys(what):
	for (k,v) in what.items():
		# @context isn't in the context...
		if k == "@context":
			continue
		# schema is our go to extension example
		if k.startswith('schema:'):
			continue
		if not k in ctxtjs:
			raise ValueError("Unknown key: {0}".format(k))
		if type(v) == dict:
			check_keys(v)
		elif type(v) == list:
			for i in v:
				if type(i) == dict:
					check_keys(i)

for eg in egs:
	egdata = eg.xpath('./text()')[0]
	if egdata.strip()[0] == '{':
		# JSON-LD
		try:
			myjs = json.loads(egdata)
			if myjs['type'] != "Annotation":
				continue

			# Run some simple checks
			# Recursively check that every key of every object is in the context
			# In the future, run all validations!
			check_keys(myjs)

			x += 1  # Only do this once per example!
			egdata = egdata.strip()
			fh = file("examples/correct/anno%s.json" % x, 'w')
			fh.write(egdata)
			fh.close()
			eglines = egdata.split('\n')
			eglines = ["      " + y for y in eglines]
			egl2 = [eglines[0]]
			egl2.extend(eglines[2:])
			egd = '\n'.join(egl2)
			annos.append(egd)
		except Exception, e:
			print "Busted: " + eg.xpath('@title')[0]
			print e
			print egdata

	else:	
		print "Busted: " + eg.xpath('@title')[0]
		print egdata
		print "\n\n"

fh = file("examples/correct/collection1.json", 'w')
fh.write(collection % len(annos))
for a in annos:
	fh.write(a)
	if a != annos[-1]:
		fh.write(',\n')
fh.write(end)
fh.close()
