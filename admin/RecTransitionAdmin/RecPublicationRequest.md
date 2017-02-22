[to be sent to the webmaster, comm team, coralie, xueyuan, WG chairs and editors]

(Coralie, Xueyuan, I will send you the HPN and AC mail drafts at the time of the publication)

Denis,

This is an official publication request for the publication of three Web Annotation WG documents as Recommendations, as well as two Working Group Notes as first public publication. The publication date is the 23rd of February, 2017.

The transition request for Rec has been issued in:

	https://lists.w3.org/Archives/Team/team-project/2017Feb/0023.html

the Director's approval is in:

	http://www.w3.org/mid/05b65168-5eb9-ee4f-4a60-7cba3d3d9ad5@w3.org

As for the two WG Notes, the approval request is in:

	https://lists.w3.org/Archives/Public/public-annotation/2017Feb/0014.html

Philippe's approval is in:

	https://lists.w3.org/Archives/Public/public-annotation/2017Feb/0017.html


The documents are as follows
----------------------------

Web Annotation Data Model
http://www.w3.org/TR/2017/REC-annotation-model-20170223/

Web Annotation Vocabulary
http://www.w3.org/TR/2017/REC-annotation-vocab-20170223/

Web Annotation Protocol
http://www.w3.org/TR/2017/REC-annotation-protocol-20170223/

Selectors and States
https://www.w3.org/TR/2017/NOTE-selectors-states-20170223/

Embedding Web Annotations in HTML
https://www.w3.org/TR/2017/NOTE-annotation-html-20170223/


Abstract and Status Sections
----------------------------

See the previous URL-s

I plan to put the documents in place on the 22nd of February, properly checked. I will notify you then if I hit any problems.

However, based on earlier experiences, I know that the link checker has a number of problems with the Web Annotation Vocabulary document, but, those are problems with the checker and not the document itself. Indeed, there are a number of errors reported on RDF term URL-s, in the RDF or RDF Schema namespaces. Those are valid RDF URI-s, although they are not dereferencable (they are not part of HTML document), which messes up the link checker. These namespaces are:

http://www.w3.org/1999/02/22-rdf-syntax-ns
http://www.w3.org/2000/01/rdf-schema

There is also an error (at this time) on a missing activitystream#Organization link; this is a bug in the namespace document maintained by the Social Web WG; a corresponding pull request has already been filed.

There are also a number of error reports related to http://purl.org/dc/; these are all dereferencable when done via a browser.

Thanks!

Ivan
