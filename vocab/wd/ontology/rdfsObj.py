#!/home/cheshire/install/bin/python -i

from rdfObject import RdfObject, TypeFactory, types, namespaces
from rdflib import Namespace

try:
    # 3.0
    from rdflib.collection import Collection
except:
    # 2.4
    from rdflib.Collection import Collection


# Flatten recursive lists: rdf= [1,[2,[3,[4,[5,6]]]]]
def objstolist(t):
    l = []
    r = 1
    while r:
        try:
            r = t.rest[0]
        except:
            break
        l.append(t.first[0])        
        try:
            t = t._objects_[r]
        except:
            break
    return l

rdfs = types['rdfs']
rdf = types['rdf']
owl = types['owl']

Ontology = owl.Ontology


ontologies = {}
ontologyNamespaces = {}
for (k,v) in namespaces.items():
    o = Ontology(str(v))
    ontologies[k] = o
    ontologyNamespaces[v] = o
    types[k]._ontology = o

class ClassOrProperty(RdfObject):
    def __init__(self, uri):
        RdfObject.__init__(self, uri)
        # now split URI for isDefinedBy and label
        (onto, label) = self.graph.split_uri(uri)
        onto = Namespace(onto)
        if ontologyNamespaces.has_key(onto):
            ontobj = ontologyNamespaces[onto]
        else:
            ontobj = owl.Ontology(onto)
            ontologyNamespaces[onto] = ontobj
        self.isDefinedBy = ontobj
        ontobj.add_object(self)
        self.label = label

class Class(ClassOrProperty):
    def __init__(self, uri):
        ClassOrProperty.__init__(self, uri)
        self.type = namespaces['rdfs']['Class']

class Property(ClassOrProperty):
    def __init__(self, uri):
        ClassOrProperty.__init__(self, uri)
        self.type = namespaces['rdf']['Property']        
        
rdfs._overrideParent['Class'] = Class
rdf._overrideParent['Property'] = Property
