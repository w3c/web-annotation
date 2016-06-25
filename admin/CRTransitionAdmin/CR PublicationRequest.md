[to be sent to the webmaster, comm team, coralie, xueyuan, WG chairs and editors, Doug, on the 25th of July 2016]

(Coralie, Xueyuan, this is for information only; I will send you the HPN and AC mail drafts at the time of the publication)

Denis,

This is an official publication request for the publication of three Web Annotation WG documents as Candidate Recommendations. The publication date is the 5th of July, 2016. The transition request for CR has been issued in:

	https://lists.w3.org/Archives/Member/chairs/2016AprJun/0086.html

the Director's approval is in:

	https://www.w3.org/2016/06/24-wacr-minutes.html

with a small caveat: there is a pending issue that has to be dealt with the Tag. We hope to have that settled by the time of the publication; it may happen, however, that the third document below (Web Annotation Protocol) has to be pulled from the current transition for a later date. Hopefully, that will not happen. In any case, I will keep you posted.

The documents are as follows
----------------------------

Web Annotation Data Model
http://www.w3.org/TR/2016/CR-annotation-model-20160705/

Web Annotation Vocabulary
http://www.w3.org/TR/2016/CR-annotation-vocab-20160705/

Web Annotation Protocol
http://www.w3.org/TR/2016/CR-annotation-protocol-20160705/

Abstract and Status Sections
----------------------------

See the previous URL-s

The documents are already in place and pass the new pubrules' checker (ie, specberus). (There are some warnings but those are subjects of specberus discussions or tiny bugs, we have discussed those separately.)

The link checker has a number of problems with the Web Annotation Vocabulary document; however, those are problems with the checker and not the document itself. Indeed, there are a number of errors reported on RDF term URL-s, in the RDF, RDF Schema, or Activity Stream namespaces. Those are valid RDF URI-s, although they are not dereferencable (they are not part of HTML document), which messes up the link checker. These namespaces are:

http://www.w3.org/1999/02/22-rdf-syntax-ns
http://www.w3.org/ns/activitystreams
http://www.w3.org/2000/01/rdf-schema

There are also a number of error reports related to http://purl.org/dc/; these are all dereferencable when done via a browser.

Thanks!

Ivan
