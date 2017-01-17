
from lxml import etree
import re
import codecs

from pygments import highlight
from pygments.lexers import TurtleLexer
from pygments.formatters import HtmlFormatter

from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager

namespaces = {
	'oa'      : Namespace('http://www.w3.org/ns/oa#'),
	'dc'      : Namespace('http://purl.org/dc/elements/1.1/'),
	'dcterms' : Namespace('http://purl.org/dc/terms/'),
	'dctypes' : Namespace('http://purl.org/dc/dcmitype/'),
	'owl'     : Namespace('http://www.w3.org/2002/07/owl#'),
	'rdf'     : Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#'),
	'rdfs'    : Namespace('http://www.w3.org/2000/01/rdf-schema#'),
	'skos'    : Namespace('http://www.w3.org/2004/02/skos/core#'),
	'foaf'    : Namespace('http://xmlns.com/foaf/0.1/'),
	'xsd'     : Namespace('http://www.w3.org/2001/XMLSchema#'),
	'as'      : Namespace('http://www.w3.org/ns/activitystreams#'),
	'schema'  : Namespace('http://schema.org/')
}

pfxs = []

for (key,val) in namespaces.copy().iteritems():
	pfxs.append("@prefix %s: <%s> ." % (key, val))
pfxstr = '\n'.join(pfxs)

fh = codecs.open('index-turtle-not-highlight.html', 'r', 'utf-8')
data = fh.read()
fh.close()
data = data.replace('\r\n', '\n')
dom = etree.HTML(data)
egs = dom.xpath('//pre[@class="example nohighlight turtle"]')

ttl = TurtleLexer()
fmt = HtmlFormatter(cssclass="turtle")

css = fmt.get_style_defs('.turtle')
css = css.replace(".turtle  { background: #f8f8f8; }", "")
css = "<style>%s</style>" % css
data = data.replace("<style>", css + "<style>")

x=1

for eg in egs:
	# print "afas"
	egdata = eg.xpath('./text()')[0]
	egdata = egdata.strip()
	if not egdata:
		continue

	egdata = egdata.replace("&lt;", "<")
	egdata = egdata.replace("&gt;", ">")

	g = Graph()
	gdata = pfxstr + "\n\n" + egdata
	try:
		g.parse(data=gdata, format="turtle")
		# fh = codecs.open("examples/correct/anno%s.ttl" % x, 'w', 'utf-8')
		# fh.write(data)
		# fh.close()
	except:
		print "Busted: " + eg.xpath('@title')[0]
		print egdata
		print "\n\n"
		raise
	x += 1

	# Now syntax highlight for turtle
	eghtml = highlight(egdata, ttl, fmt)
	eghtml = eghtml.replace("<pre>", '')
	eghtml = eghtml.replace("</pre>", '')
	eghtml = eghtml.replace('<div class="turtle">', '')
	eghtml = eghtml.replace('</div>','')
	egdata = egdata.replace("<", "&lt;")
	egdata = egdata.replace(">", "&gt;")
	eghtml = eghtml.strip()
	data = data.replace(egdata, eghtml, 1)

# Write out the final result
fh = codecs.open("index-respec.html", 'w', 'utf-8')
fh.write(data)
fh.close()
