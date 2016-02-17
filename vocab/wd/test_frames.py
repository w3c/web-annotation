from pyld import jsonld
from pyld.jsonld import compact, expand, frame
import json
import os

contextUri = "http://www.w3.org/ns/anno.jsonld"
contextmap = {
	contextUri: "../../jsonld/anno.jsonld"
}

# Stop code from looking up the contexts online EVERY TIME
def load_document_local(url):
    doc = {
        'contextUrl': None,
        'documentUrl': None,
        'document': ''
    }

    fn = contextmap.get(url, "")
    if fn:
	    fh = file(fn)
	    data = fh.read()
	    fh.close()
	    doc['document'] = data;
    return doc

jsonld.set_document_loader(load_document_local)

fh = file('../../jsonld/annotation_frame.jsonld')
data = fh.read()
fh.close()
annoframe = json.loads(data)

# read in examples and reframe

egdir = '../../model/wd2/examples/correct/'
examples = os.listdir(egdir)
for eg in examples:
	if eg.endswith('.json'):
		print eg
		fh = file(os.path.join(egdir, eg))
		data = fh.read()
		fh.close()
		anno = json.loads(data)
		anno['@context'] = contextUri
		framed = frame(anno, annoframe)
		out = compact(framed, contextUri)
		print json.dumps(out, sort_keys=True, indent=2)
