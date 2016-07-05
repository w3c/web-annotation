Dear Advisory Committee Representative,
Chairs,

I am pleased to announce that the following documents are now W3C Candidate Recommendations:

Web Annotation Data Model
http://www.w3.org/TR/2016/CR-annotation-model-20160705/

Web Annotation Vocabulary
http://www.w3.org/TR/2016/CR-annotation-vocab-20160705/

The approval and publication are in response to this transition request:
https://lists.w3.org/Archives/Member/chairs/2016AprJun/0086.html

The disposition of comments since the last Working Draft is available at:
https://github.com/w3c/web-annotation/issues?page=3&q=is%3Aissue+-label%3Apostpone+-label%3Atesting&utf8=%E2%9C%93

The group welcomes feedback by email to its public mailing list <public-annotation@w3.org>, or as issues raised in:
https://github.com/w3c/web-annotation/issues

A document with test cases, how to test, etc. is at:
https://github.com/w3c/web-annotation-tests/blob/master/README.md

Patent disclosures relevant to these specifications may be found on the Web Annotation Working Group's patent disclosure page in conformance with W3C policy:
https://www.w3.org/2004/01/pp-impl/73180/status

The Web Annotation Working Group expects to satisfy its implementation criteria by 30 September 2016.

This Call for Implementations follows section 6.4 “Candidate Recommendation" of the W3C Process Document:
https://www.w3.org/2015/Process-20150901/#candidate-rec

Thank you,

For Tim Berners-Lee, Director, and
Ralph Swick, Information and Knowledge Domain Lead;
Xueyuan Jia, W3C Marketing & Communications

==============================================
Quoting from
-----------------------------------------------------------------
Web Annotation Data Model
W3C Candidate Recommendation 05 July 2016
-----------------------------------------------------------------

This version:
           http://www.w3.org/TR/2016/CR-annotation-model-20160705/
Latest published version:
           http://www.w3.org/TR/annotation-model/

Abstract:
Annotations are typically used to convey information about a resource or associations between resources. Simple examples include a comment or tag on a single web page or image, or a blog post about a news article.

The Web Annotation Data Model specification describes a structured model and format to enable annotations to be shared and reused across different hardware and software platforms. Common use cases can be modeled in a manner that is simple and convenient, while at the same time enabling more complex requirements, including linking arbitrary content to a particular data point or to segments of timed multimedia resources.

The specification provides a specific JSON format for ease of creation and consumption of annotations based on the conceptual model that accommodates these use cases, and the vocabulary of terms that represents it.

Status of This Document:
This section describes the status of this document at the time of its publication. Other documents may supersede this document. A list of current W3C publications and the latest revision of this technical report can be found in the W3C technical reports index at http://www.w3.org/TR/.

This specification was derived from the Open Annotation Community Group's outcomes, and details of the differences between the two are maintained in the Acknowledgment appendix.

ISSUE 1
The Composite, List and Independents classes are marked At Risk, pending implementation experience.

This document was published by the Web Annotation Working Group as a Candidate Recommendation. This document is intended to become a W3C Recommendation. If you wish to make comments regarding this document, please send them to public-annotation@w3.org (subscribe, archives). W3C publishes a Candidate Recommendation to indicate that the document is believed to be stable and to encourage implementation by the developer community. This Candidate Recommendation is expected to advance to Proposed Recommendation no earlier than 30 September 2016. All comments are welcome.

Please see the Working Group's implementation report.

Publication as a Candidate Recommendation does not imply endorsement by the W3C Membership. This is a draft document and may be updated, replaced or obsoleted by other documents at any time. It is inappropriate to cite this document as other than work in progress.

This document was produced by a group operating under the 5 February 2004 W3C Patent Policy. W3C maintains a public list of any patent disclosures made in connection with the deliverables of the group; that page also includes instructions for disclosing a patent. An individual who has actual knowledge of a patent which the individual believes contains Essential Claim(s) must disclose the information in accordance with section 6 of the W3C Patent Policy.

This document is governed by the 1 September 2015 W3C Process Document.

-----------------------------------------------------------------
Web Annotation Vocabulary
W3C Candidate Recommendation 05 July 2016
-----------------------------------------------------------------

This version:
           http://www.w3.org/TR/2016/CR-annotation-vocab-20160705/
Latest published version:
           http://www.w3.org/TR/annotation-vocab/

Abstract:
The Web Annotation Vocabulary specifies the set of RDF classes, predicates and named entities that are used by the Web Annotation Data Model [annotation-model]. It also lists recommended terms from other ontologies that are used in the model, and provides the JSON-LD Context and profile definitions needed to use the Web Annotation JSON serialization in a Linked Data context.

Status of This Document:
This section describes the status of this document at the time of its publication. Other documents may supersede this document. A list of current W3C publications and the latest revision of this technical report can be found in the W3C technical reports index at http://www.w3.org/TR/.

ISSUE 1
The use of the ActivityStreams terms are considered to be at-risk, pending [activitystreams-vocabulary] reaching Candidate Recommendation and, eventually, Recommendation. If this fails, the (few) terms used in the current document will be replaced by terms with a similar names and similar semantics, but in the namespace defined by this document.

ISSUE 2
The Composite, List and Independents classes are marked At Risk, pending implementation experience.

This document was published by the Web Annotation Working Group as a Candidate Recommendation. This document is intended to become a W3C Recommendation. If you wish to make comments regarding this document, please send them to public-annotation@w3.org (subscribe, archives). W3C publishes a Candidate Recommendation to indicate that the document is believed to be stable and to encourage implementation by the developer community. This Candidate Recommendation is expected to advance to Proposed Recommendation no earlier than 30 September 2016. All comments are welcome.

Please see the Working Group's implementation report.

Publication as a Candidate Recommendation does not imply endorsement by the W3C Membership. This is a draft document and may be updated, replaced or obsoleted by other documents at any time. It is inappropriate to cite this document as other than work in progress.

This document was produced by a group operating under the 5 February 2004 W3C Patent Policy. W3C maintains a public list of any patent disclosures made in connection with the deliverables of the group; that page also includes instructions for disclosing a patent. An individual who has actual knowledge of a patent which the individual believes contains Essential Claim(s) must disclose the information in accordance with section 6 of the W3C Patent Policy.

This document is governed by the 1 September 2015 W3C Process Document.
