
from lxml import etree

fh = file('index-respec.html')
data = fh.read()
fh.close()

dom = etree.HTML(data)

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
	if tech.text != "URI:":
		t = tech.tail.strip()
		ts = t.split(',')
		newt = []
		for ti in ts:
			ti = ti.strip()
			link = ti.lower()
			if link.startswith('oa:'):
				link = link[3:]
			newt.append('<a href="#%s">%s</a>' % (link, ti))
		newstr = ", ".join(newt)
		print "In: %s\nReplace: %s" % (t, newstr)
		data = data.replace("</strong> %s" % t, "</strong> %s" % newstr, 1)

fh = file("index-linked.html", 'w')
fh.write(data)
fh.close()

