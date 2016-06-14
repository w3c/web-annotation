
from lxml import etree
import re
import codecs

from pygments import highlight
from pygments.lexers import TurtleLexer
from pygments.formatters import HtmlFormatter

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
           	  'xsd' : Namespace('http://www.w3.org/2001/XMLSchema#'),
           	  'as' : Namespace('http://www.w3.org/ns/activitystreams#'),
           	  'schema' : Namespace('http://schema.org/')
              }

pfxs = []

for (key,val) in namespaces.copy().iteritems():
	pfxs.append("@prefix %s: <%s> ." % (key, val))
pfxstr = '\n'.join(pfxs)


usre = re.compile("^_(.+)_:(.+)$")
includere = re.compile("[%][%]include/([^ ]+)[%][%]")

fh = codecs.open('index-linktemplate.html', 'r', 'utf-8')
data = fh.read()
fh.close()
data = data.replace('\r\n', '\n')
dom = etree.HTML(data)

# Replace %%include/file%% with contents of file.
m = includere.search(data)
while m:
	fn = m.groups()[0]
	fh = file('../../%s' % fn)
	fstr = fh.read()
	fh.close()
	data = includere.sub(fstr, data, count=1)
	m = includere.search(data)

# Number all of the examples sequentially
x = 0
while data.find("%%anno%%") > -1:
	x += 1
	data = data.replace("%%anno%%", str(x), 1)

# link | separated entries in div @class=termtoc
tocs = dom.xpath('//div[@class="termtoc"]/text()')
for toc in tocs:
	toc = toc.strip()
	tis = toc.split(' | ')
	newtoc = []
	for ti in tis:
		ti = ti.strip()
		lnk = ti.replace(':', '-').lower()
		newtoc.append('<a href="#%s">%s</a>' % (lnk, ti))
	newstr = " | ".join(newtoc)
	data = data.replace(toc, newstr)


# link , separated entries in div @class=tech/ul/li
techs = dom.xpath('//div[@class="tech"]/ul/li/strong')
for tech in techs:
	t = tech.tail.strip()
	if tech.text == "IRI:":
		m = usre.match(t)
		if m:
			bits = m.groups()
			uri = "%s%s" % (namespaces[bits[0]], bits[1])
			if uri:
				data = data.replace(t, '<a href="%s">%s</a>' % (uri, uri), 1)
	elif tech.text.strip().startswith("Equivalent"):
		ts = t.split(',')
		newt = []
		for ti in ts:
			ti = ti.strip()
			if ti:
				(ns, term) = ti.split(':')
				uri = "%s%s" % (namespaces[ns], term)
				newt.append('<a href="%s">%s</a>' % (uri, ti))
		if newt:
			newstr = ', '.join(newt)
			data = data.replace("</strong> %s" % t, "</strong> %s" % newstr, 1)
	else:
		ts = t.split(',')
		if ts and ts[0]:
			newt = []
			for ti in ts:
				ti = ti.strip()
				if ti.startswith("xsd:"):
					# Don't try to link xsd:string/integer/datetime, etc
					newt.append(ti)
				elif ti.startswith("|"):
					ti = ti[1:]
					(ns, term) = ti.split(':')
					uri = "%s%s" % (namespaces[ns], term)
					newt.append('<a href="%s">%s</a>' % (uri, ti))
				else:
					link = ti.lower()
					if link.startswith('oa:'):
						link = link[3:]
					else:
						link = link.replace(":", "-", 1)
					newt.append('<a href="#%s">%s</a>' % (link, ti))
			newstr = ", ".join(newt)
			data = data.replace("</strong> %s" % t, "</strong> %s" % newstr, 1)

# Reparse to get all of the changes above...
dom = etree.HTML(data)
egs = dom.xpath('//pre[@class="turtle example nohighlight"]')

ttl = TurtleLexer()
fmt = HtmlFormatter(cssclass="turtle")

css = fmt.get_style_defs('.turtle')
css = css.replace(".turtle  { background: #f8f8f8; }", "")
css = "<style>%s</style>" % css
data = data.replace("<style>", css + "<style>")

slug = re.compile("/([^/]+?)> ")

for eg in egs:
	egdata = eg.xpath('./text()')[0]
	egdata = egdata.strip()
	if not egdata:
		continue
	if egdata.startswith("GET "):
		continue

	g = Graph()
	gdata = pfxstr + "\n\n" + egdata
	try:
		# Find name from data, rather than guess
		m = slug.search(egdata)
		if m:
			name = m.groups()[0]
			print "Found name: %s" % name
		else:
			print "Busted name!"
			raise ValueError

		if name != "diagram.jpg":
			g.parse(data=gdata, format="turtle")
			fh = codecs.open("examples/correct/%s.ttl" % name, 'w', 'utf-8')
			fh.write(gdata)
			fh.close()
	except:
		print "Busted: " + eg.xpath('@title')[0]
		print egdata
		print "\n\n"
		raise


	# Now syntax highlight for turtle
	eghtml = highlight(egdata, ttl, fmt)
	# eghtml = eghtml.replace("<pre>", '<pre class="nohighlight">')
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
