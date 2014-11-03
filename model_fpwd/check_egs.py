from lxml import etree
import json

fh = file('index.html')
data = fh.read()
fh.close()

dom = etree.XML(data)
egs = dom.xpath('//pre[@class="example highlight"]')

for eg in egs:
    egdata = eg.xpath('./text()')[0]
    try:
        json.loads(egdata)
    except:
        print "Busted: " + eg.xpath('@title')[0]
        print egdata
