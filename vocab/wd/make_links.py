
from lxml import etree
import re

usre = re.compile("^_(.+)_:(.+)$")
includere = re.compile("[%][%]include/([^ ]+)[%][%]")

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
    "cnt":     "http://www.w3.org/2011/content#",    
    "as":      "http://www.w3.org/ns/activitystreams#",
    "schema":  "http://schema.org/"
}

fh = file('index-linktemplate.html')
data = fh.read()
fh.close()
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
	if tech.text == "URI:":
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





# Write out the result
fh = file("index-respec.html", 'w')
fh.write(data)
fh.close()

