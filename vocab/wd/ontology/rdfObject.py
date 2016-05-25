
from rdflib import ConjunctiveGraph, URIRef, BNode, Literal, Namespace

try:
    from rdflib import StringInputSource
    RDF_VER=2.4
except:
    import StringIO
    from rdflib import plugin, query

    RDF_VER=3.0
    # rdflib_sparql seems broken with initNs?

    try:
        plugin.register('sparql', query.Processor,
                       'rdfextras.sparql.processor', 'Processor')
        plugin.register('sparql', query.Result,
                       'rdfextras.sparql.query', 'SPARQLQueryResult')
    except:
        pass


try:
    import rdfextras
    rdfextras.registerplugins()
except:
    pass

import uuid
import time

def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

def gen_uuid():
    return "urn:uuid:%s" % uuid.uuid4()

namespaces = {'ore' : Namespace('http://www.openarchives.org/ore/terms/'),
              'oa' : Namespace('http://www.w3.org/ns/oa#'),
              'cnt' : Namespace('http://www.w3.org/2011/content#'),
              'exif' : Namespace('http://www.w3.org/2003/12/exif/ns#'),
              'dc' : Namespace('http://purl.org/dc/elements/1.1/'),
              'dcterms' : Namespace('http://purl.org/dc/terms/'),
              'dctypes' : Namespace('http://purl.org/dc/dcmitype/'),
              'owl' : Namespace('http://www.w3.org/2002/07/owl#'),
              'rdf' : Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#'),
              'rdfs' : Namespace('http://www.w3.org/2000/01/rdf-schema#'),
              'trig' : Namespace('http://www.w3.org/2004/03/trix/rdfg-1/'),
              'skos' : Namespace('http://www.w3.org/2004/02/skos/core#'),
              'foaf' : Namespace('http://xmlns.com/foaf/0.1/'),
              'prov' : Namespace('http://www.w3.org/ns/prov#'),
              'xsd' : Namespace('http://www.w3.org/2001/XMLSchema#'),
              'gr' : Namespace('http://purl.org/goodrelations/v1#'),
              'geo' : Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#'),
              'sioc' : Namespace("http://rdfs.org/sioc/ns#"),
              'time' : Namespace("http://www.w3.org/2006/time#"),
              'bibo' : Namespace('http://purl.org/ontology/bibo/'),
              'sc' : Namespace('http://iiif.io/api/presentation/2#'),
              'iiif' : Namespace('http://iiif.io/api/image/2#'),
              'svcs' : Namespace('http://rdfs.org/sioc/services#'),
              'iana' : Namespace('http://www.iana.org/assignments/relation/'),
              'ldp' : Namespace('http://www.w3.org/ns/ldp#'),
              'pcdm' : Namespace('http://pcdm.org/models#'),
              'acl' : Namespace('http://www.w3.org/ns/auth/acl#'),
              'as' : Namespace('http://www.w3.org/ns/activitystreams#')              
              }

### Elements commonly used
### If an element is in this list, you can do object.predicate,
### rather than object._namespace.predicate
### (Not complete for most namespaces, just common terms)
elements = {
    'ore' : ['describes', 'isDescribedBy', 'aggregates', 'isAggregatedBy', 'similarTo', 'proxyFor', 
             'proxyIn', 'lineage'],  
    'dc' : ['coverage', 'date', 'description', 'format', 'identifier', 'language', 'publisher', 
            'relation', 'rights', 'source', 'subject', 'title'],  # no creator, contributor
    'dcterms': ['abstract', 'accessRights', 'accrualMethod', 'accrualPeriodicity', 'accrualPolicy', 'alternative', 'audience', 'available', 'bibliographicCitation', 'conformsTo', 'contributor', 'created', 'creator', 'dateAccepted', 'dateCopyrighted', 'dateSubmitted', 'educationLevel', 'extent', 'hasFormat', 'hasPart', 'hasVersion', 'instructionalMethod', 'isFormatOf', 'isPartOf', 'isReferencedBy', 'isReplacedBy', 'isRequiredBy', 'issued', 'isVersionOf', 'license', 'mediator', 'medium', 'modified', 'provenance', 'references', 'replaces', 'requires', 'rights', 'rightsHolder', 'spatial', 'tableOfContents', 'temporal', 'valid'],  # also rights
    'cnt' : ['chars', 'characterEncoding'],
    'foaf' : ['accountName', 'aimChatID', 'birthday', 'depiction', 'depicts', 'family_name', 'firstName', 'gender', 'givenname', 'homepage', 'icqChatID', 'img', 'interest', 'jabberID', 'knows', 'logo', 'made', 'maker', 'mbox', 'member', 'msnChatID', 'name', 'nick', 'openid', 'page', 'phone', 'surname', 'thumbnail', 'weblog', 'yahooChatID'],
    'prov' : ['actedOnBehalfOf', 'endedAtTime', 'startedAtTime', 'used', 'wasAssociatedWith', 'wasAttributedTo', 'wasDerivedFrom', 'wasGeneratedBy', 'wasInformedBy'],
    'owl' : ['sameAs'],
    'rdf' : ['type', 'first', 'rest', 'value'],
    'rdfs' : ['seeAlso', 'label', 'isDefinedBy', 'range', 'domain', 'comment', 'subClassOf', 'subPropertyOf'],
    'oa' : [ 'hasBody', 'hasTarget', 'hasSource', 'hasSelector', 'hasScope', 'styledBy', 'styleClass', 'hasState', 'equivalentTo', 'annotatedBy', 'annotatedAt', 
             'serializedBy', 'serializedAt', 'when', 'cachedSource', 'start', 'end', 'exact', 'prefix', 'suffix', 'motivatedBy'],
    'skos' : ['prefLabel', 'inScheme', 'broader', 'narrower', 'related', 'changeNote', 'editorialNote', 'broadMatch', 'closeMatch', 'exactMatch'],
    'iana' : ['alternate', 'current' ,'enclosure', 'edit', 'edit-media', 'first', 'last',  'next', 'next-archive', 'previous', 'payment', 'prev-archive', 'related', 'replies', 'service', 'via'],  # -self, -license
    'bibo' : ['pageStart', 'pageEnd', 'volume'],
    'exif' : ['height', 'width', 'imageHeight', 'imageWidth', 'bitsPerSample']
    }

### The order in which to search the above hash
namespaceSearchOrder = ['ore', 'oa', 'cnt', 'dc', 'dcterms', 'foaf', 'rdf', 'rdfs', 'prov', 'exif', 'owl', 'skos', 'iana', 'bibo']

mimetypeHash = {'rdfa' : 'application/xhtml+xml',
                'xml' : 'application/rdf+xml',
                'nt' : 'text/plain',
                'n3' : 'text/rdf+n3',
                'turtle' : 'application/turtle',
                'pretty-xml' : 'application/rdf+xml',
                'json-ld' : 'application/ld+json'               
                }

formatHash = {'application/xhtml+xml' : 'rdfa',
              'application/x-turtle' : 'turtle',
              'text/plain' : 'nt',
              'text/rdf+n3' : 'n3'}

unconnectedAction = 'ignore'
        

# --- Object Class Definitions ---

# More Black Magic -- Dynamically create classes
# XXX Supercool would be to parse ontology file to auto-generate superClasses. 
# XXX This would map python Multiple Inheritance to rdf MI

class TypeFactory(object):    
    def __init__(self, ns, defaultUUID=False):
        self.namespace = ns
        # Preconstructed classes
        self._override = {}
        # Should we default to using a UUID?
        self._defaultUUID = defaultUUID
        # Class for *parent* of new class
        self._overrideParent = {}
        # Multiple rdf type statements to add
        self._multiSubClassOf = {}
        self._ontology = None
        
    def __getattr__(self, what):

        if self._override.has_key(what):
            return self._override[what]
        else:
            nso = self.namespace[what]
            prnt = self._overrideParent.get(what, RdfObject)
            extraClasses = self._multiSubClassOf.get(what, [])
            
            if self._defaultUUID:
                def fnc(this, uri='uuid', **kw):
                    prnt.__init__(this, uri)
                    this._rdf.type = nso
                    for c in extraClasses:
                        this._rdf.type = c
                    for (k,v) in kw.items():
                        setattr(this,k,v)              
            else:                    
                def fnc(this, uri=None, **kw):
                    prnt.__init__(this, uri)
                    this._rdf.type = nso 
                    for c in extraClasses:
                        this._rdf.type = c
                    for (k,v) in kw.items():
                        setattr(this,k,v)    
                        
            o = type(what, (prnt,), {'__init__' : fnc})
            # Cache our new class
            self._override[what] = o
            return o

types = {}
typesNS = {}
for (nm,ns) in namespaces.copy().items():
    types[nm] = TypeFactory(ns)
    typesNS[ns] = types[nm]

class Graph(ConjunctiveGraph):
    def __init__(self, store=None, id=None):
        if store != None and id != None:
            ConjunctiveGraph.__init__(self, store, id)
        else:
            ConjunctiveGraph.__init__(self)
        self.bindall()
    
    def bindall(self):
        for (key,val) in namespaces.copy().iteritems():
            self.bind(key, val)

    def find_namespace(self, name):
        # find best namespace
        for k in namespaceSearchOrder:
            v = elements[k]
            if name in v:
                return namespaces[k]
        return None

    def split_uri(self, uri):
        # given namespaced uri, find base property name
        slsplit = uri.split('/')
        hsplit = slsplit[-1].split('#')
        return (uri[:0-len(hsplit[-1])], hsplit[-1])
        

class RdfObject(object):
    graph = None
    uri = ""
    currNs = ""
    objects = {}

    def __init__(self, uri=None):
        graph = Graph()
        self._graph_ = graph
        if isinstance(uri, URIRef) or isinstance(uri, BNode):
            self._uri_ = uri
        elif uri == None:
            self._uri_ = BNode()
        elif type(uri) in [str, unicode]:
            if uri == 'uuid':
                # magic uuid uri
                self._uri_ = URIRef(gen_uuid())
            else:
                self._uri_ = URIRef(uri)
        else:
            raise ValueError("URI for object must be string, unicode, URIRef, BNode, or None")

        self._currNs_ = ''
        self._objects_ = {}

    def __str__(self):
        return str(self.uri)

    def __getattr__(self, name):
        # fetch value from graph
        cns = self.currNs
        if name[0] == "_" and name[-1] == "_":
            return getattr(self, name[1:-1])
        elif name[0] == "_" and namespaces.has_key(name[1:]):
            # we're looking for self.namespace.property
            self._currNs_ = name[1:]
            return self
        elif cns:
            val = self.get_value(name, cns)
            self._currNs_ = ''
        else:
            val = self.get_value(name)
        return val

    def __setattr__(self, name, value):
        if name[0] == "_" and name[-1] == "_":            
            return object.__setattr__(self, name[1:-1], value)
        elif name[0] == "_" and namespaces.has_key(name[1:]):
            # we're looking for self.namespace.property
            object.__setattr__(self, 'currNs', name[1:])
            return self
        elif self.currNs:
            val = self.set_value(name, value, self.currNs)        
        else:
            val = self.set_value(name, value)
        object.__setattr__(self, 'currNs', '')
        return val

    def __iter__(self):
        l = [x for x in self._graph_]
        return l.__iter__()

    def __len__(self):
        return len(self._graph_)

    def set_value(self, name, value, ns=None):
        if ns:
            nsobj = namespaces[ns]
        else:
            nsobj = self.graph.find_namespace(name)
   
        if value == []:
            for val in self.graph.objects(self.uri, nsobj[name]):
                self.graph.remove((self.uri, nsobj[name], val))
        else:
            if isinstance(value, RdfObject):
                self.add_object(value)
                value = value._uri_
            if not isinstance(value, URIRef) and not isinstance(value, BNode):
                value = Literal(value)
            try:
                self.graph.add((self.uri, nsobj[name], value))
            except:
                print type(nsobj)
                print "Trying to add: %s %s [%s] %s" % (self.uri, nsobj, name, value)
                raise
        return 1

    def get_value(self, name, ns=None):        
        if ns:
            nsobj = namespaces[ns]
        else:
            nsobj = self.graph.find_namespace(name)
        l = []
        for obj in self.graph.objects(self.uri, nsobj[name]):
            l.append(obj)
        return l

    def add_object(self, what):
        self._objects_[what._uri_] = what

    def remove_object(self, what):
        del self._objects_[what._uri_]

    def predicates(self):
        return list(self.graph.predicates())

    def serialize(self, format="", uri=None, mimeType="", **kw):
        if not format and not mimeType:
            format = 'pretty-xml'
        if not format and mimeType:
            try:
                format = formatHash[mimeType]
            except:
                raise ValueError("Unknown mimeType: %s" % mimeType)
        elif not mimeType :
            try:
                mimeType = mimetypeHash[format]
            except:
                raise ValueError("Unknown format: %s" % format)

        g = self.merge_graphs()
        g.bindall()
        
        data = g.serialize(format=format, **kw)
                
        rd = GraphSerialization(data, uri=uri, format=format, mimeType=mimeType)
        return rd

    def merge_graphs(self):
        g = Graph()
        stack = [self]
        done = []
        while stack:
            what = stack.pop(0)
            if what == None or what in done:
                continue
            done.append(what)            
            g += what._graph_
            for at in what._objects_.values():
                stack.append(at)
            
        g = self.connected_graph(g)
        return g

    def connected_graph(self, graph):
        if unconnectedAction == 'ignore':
            return graph

        g = Graph()
        all_nodes = list(graph.all_nodes())
        all_nodes = filter(lambda y: not isinstance(y, Literal), all_nodes)
        discovered = {}
        visiting = [uri]
        while visiting:
            x = visiting.pop()
            if not discovered.has_key(x):
                discovered[x] = 1
            for (p, new_x) in graph.predicate_objects(subject=x):
                g.add((x,p,new_x))
                if (isinstance(new_x, URIRef) or isinstance(new_x, BNode)) and not discovered.has_key(new_x) and not new_x in visiting:
                    visiting.append(new_x)
            for (new_x, p) in graph.subject_predicates(object=x):
                g.add((new_x,p,x))
                if (isinstance(new_x, URIRef) or isinstance(new_x, BNode)) and not discovered.has_key(new_x) and not new_x in visiting:
                    visiting.append(new_x)
        if len(discovered) != len(all_nodes):
            if unconnectedAction == 'warn':
                print "Warning: Graph is unconnected, some nodes being dropped"
            elif unconnectedAction == 'raise':
                raise ValueError('Graph to be serialized is unconnected')
            elif unconnectedAction != 'drop':
                raise ValueError('Unknown unconnectedAction setting: %s' % unconnectedAction)
        return g

    def do_sparql(self, sparql):
        # first merge graphs
        g = self.merge_graphs()
        # now do sparql query on merged graph
        sparql = sparql.replace('??self', '<%s>' % str(self.uri))

        if RDF_VER == 3.0:
            return g.query(sparql)
        else:
            return g.query(sparql, initNs=namespaces.copy())

    
class GraphSerialization(object):
    def __init__(self, data=None, uri=None, format="", mimeType=""):
        self.data = data
        self.uri = uri
        self.format = format
        self.mimeType = mimeType

    def parse(self):
        # parse to find graph
        graph =  Graph()

        if self.data:
            if RDF_VER >= 3.0:
                data = StringIO.StringIO(self.data)
            else:
                data = StringInputSource(self.data)
        elif self.uri:
            data = self.uri
        else:
            raise ValueError("No data to parse available")
        if self.format and self.format != 'pretty-xml':
            graph.parse(data, format=self.format)
        else:
            graph.parse(data)
        return self.process_graph(graph)

    def process_graph(self, graph):
        # make one object per subject
        objs = {}
        refs = {}

        # Urgh. Hopefully dealing with small graphs!

        # first find all the type assertions
        typuri = URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')
        mytypes = {}
        for (s,p,o) in graph:
            if p == typuri:
                try:
                    mytypes[s].append(o)
                except:
                    mytypes[s] = [o]

        for (s,p,o) in graph:
            try:
                obj = objs[s]
            except KeyError:
                if mytypes.has_key(s):
                    # find a type object
                    obj = None
                    for typ in mytypes[s]:
                        splt = graph.split_uri(typ)
                        tgt = splt[0]
                        factory = typesNS[Namespace(tgt)]
                        cnstr = getattr(factory, splt[1]) 
                        obj = cnstr(s)
                        break
                    if obj == None:
                        obj = RdfObject(s)
                else:
                    obj = RdfObject(s)
                objs[s] = obj
            obj.graph.add((s,p,o))
            if isinstance(o, URIRef) or isinstance(o, BNode):
                try:
                    refs[obj].append(o)
                except KeyError:
                    refs[obj] = [o]
        # now join up
        for (k, v) in refs.items():
            for targ in v:
                try:
                    k.add_object(objs[targ])
                except:
                    pass
        return objs
                    
if __name__ == '__main__':        
    
    book = types['bibo'].Book('http://example.org/book1')
    book.title = "Title"
    book.subject = "Some Subject"
    book._dc.subject = "Some Other Subject"
    book.extent = 1

    who = types['foaf'].Agent('http://example.org/bob')
    who.name = "Bob Smith"
    book.creator = who

    rd = book.serialize('json-ld', indent=4)
    print rd.data

