
import sys, os, re
import commands
import time

from rdflib import Namespace
from rdfsObj import Class, Property, Ontology, ontologies, ontologyNamespaces
from rdfObject import namespaces as NS, types, URIRef

from lxml import etree

now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


onto = Ontology(str(NS['oa']))
onto._owl.versionInfo = now
onto.modified = now
onto.title = "Web Annotation Ontology"
onto.creator = "Robert Sanderson"
onto.creator = "Benjamin Young"
onto.creator = "Paolo Ciccarese"
onto.comment = "The Web Annotation ontology defines the terms of the Web Annotation vocabulary"
onto.seeAlso = URIRef("http://www.w3.org/TR/annotation-vocab/")
onto._owl.previousVersionURI = URIRef("http://www.openannotation.org/spec/core/20130208/oa.owl")
ontologies['oa'] = onto
ontologyNamespaces[NS['oa']] = onto


fh = file('../index-linktemplate.html')
data = fh.read()
fh.close()

dom = etree.HTML(data)

odom = dom.xpath('//section[./h2/text()="Web Annotation Ontology"]')[0]
classes = odom.xpath('.//section[./h3/text()="Classes"]/section[@class="term"]')
props = odom.xpath('.//section[./h3/text()="Properties"]/section[@class="term"]')
instances = odom.xpath('.//section[./h3/text()="Named Individuals"]/section[@class="term"]')

names = {}
subclasses = {}

for c in classes:
	name = c.xpath('./h4/text()')[0]
	comment = ' '.join(c.xpath('./p//text()')).replace('\r', '')
	comment = comment.replace("[[!", "").replace("]]", "")
	info = c.xpath('./div/ul')[0]
	subclass = info.xpath('./li[./strong/text()="Sub Class Of:"]/text()')
	if subclass:
		subclass = subclass[0].strip()
		subclass = subclass.replace('oa:', '')
		subclass = subclass.replace('|', '')
		cidx = subclass.find(':')
		if cidx > -1:
			# autocreate a subclass
			names[subclass] = NS[subclass[:cidx]][subclass[cidx+1:]]
	else:
		subclass = None

	cl = Class(NS['oa'][name])
	cl.label = name
	cl.comment = comment
	names[name] = cl
	subclasses[cl] = subclass
	cl.isDefinedBy = onto

for (k,v) in subclasses.items():
	if v:
		subcl = names[v]
		k.subClassOf = subcl


for p in props:
	name = p.xpath('./h4/text()')[0]
	comment = ' '.join(p.xpath('./p//text()')).replace('\r', '')
	comment = comment.replace("[[!", "").replace("]]", "")	
	info = p.xpath('./div/ul')[0]
	domain = info.xpath('./li[./strong/text()="Domain:"]/text()')	
	rng = info.xpath('./li[./strong/text()="Range:"]/text()')
	if domain:
		domain = domain[0].strip()
		domain = domain.replace("oa:", '')
	else:
		domain = None
	if rng:
		rng = rng[0].strip()
		rng = rng.replace("oa:", '')
		rng = rng.replace("|", '')
		cidx = rng.find(':')
		if cidx > -1:
			# autocreate a subclass
			names[rng] = NS[rng[:cidx]][rng[cidx+1:]]		
	else:
		rng = None

	prop = Property(NS['oa'][name])
	prop.label = name
	prop.comment = comment
	prop.isDefinedBy = onto
	if domain:
		prop.domain = names[domain]
	if rng:
		prop.range = names[rng]

### Instances

for i in instances:
	name = i.xpath('./h4/text()')[0]
	comment = ' '.join(i.xpath('./p//text()')).replace('\r', '')
	comment = comment.replace("[[!", "").replace("]]", "")	
	info = i.xpath('./div/ul')[0]	
	iof = info.xpath('./li[./strong/text()="Instance Of:"]/text()')[0]
	iof = iof.strip()
	iof = iof.replace('oa:', '')
	iofclass = names[iof]

	factory = types['oa']
	parent = getattr(factory, iof)
	inst = parent(NS['oa'][name])
	inst.comment = comment
	inst.label = name
	inst.isDefinedBy = onto
	onto.add_object(inst)


srlz = onto.serialize('pretty-xml')
fh = file('index.xml', 'w')
fh.write(srlz.data)
fh.close()

srlz = onto.serialize('turtle')
fh = file('index.ttl', 'w')
fh.write(srlz.data)
fh.close()
