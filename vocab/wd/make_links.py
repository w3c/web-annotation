
from lxml import etree
import re

usre = re.compile("^_(.+)_:(.+)$")

namespaces = {
    "dc":      "http://purl.org/dc/elements/1.1/",
    "dcterms": "http://purl.org/dc/terms/",
    "dctypes": "http://purl.org/dc/dcmitype/",
    "foaf":    "http://xmlns.com/foaf/0.1/",
    "rdf":     "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs":    "http://www.w3.org/2000/01/rdf-schema#",
    "skos":    "http://www.w3.org/2004/02/skos/core#",
    "xsd":     "http://www.w3.org/2001/XMLSchema#",
    "ldp":     "http://www.w3.org/ns/ldp#",
    "iana":    "http://www.iana.org/assignments/relation/",
    "owl":     "http://www.w3.org/2002/07/owl#",
    "prov":    "http://www.w3.org/ns/prov#",
    "cnt":     "http://www.w3.org/2011/content#",    
    "as":      "http://www.w3.org/ns/activitystreams#"
}

fh = file('index-linktemplate.html')
data = fh.read()
fh.close()
dom = etree.HTML(data)

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
		newtoc.append('<a href="#%s">%s</a>' % (ti.lower(), ti))
	newstr = " | ".join(newtoc)
	data = data.replace(toc, newstr)


# link , separated entries in div @class=tech/ul/li
techs = dom.xpath('//div[@class="tech"]/ul/li/strong')
for tech in techs:
	t = tech.tail.strip()
	if tech.text != "URI:":
		ts = t.split(',')
		newt = []
		for ti in ts:
			ti = ti.strip()
			if ti.startswith("xsd:"):
				# Don't try to link xsd:string/integer/datetime, etc
				newt.append(ti)
			else:
				link = ti.lower()
				if link.startswith('oa:'):
					link = link[3:]
				else:
					link = link.replace(":", "-", 1)
				newt.append('<a href="#%s">%s</a>' % (link, ti))
		newstr = ", ".join(newt)
		print "In: %s\nReplace: %s" % (t, newstr)
		data = data.replace("</strong> %s" % t, "</strong> %s" % newstr, 1)
	else:
		m = usre.match(t)
		if m:
			bits = m.groups()
			uri = "%s%s" % (namespaces[bits[0]], bits[1])
			data = data.replace(t, '<a href="%s">%s</a>' % (uri, uri), 1)


# Write out the result
fh = file("index-respec.html", 'w')
fh.write(data)
fh.close()

