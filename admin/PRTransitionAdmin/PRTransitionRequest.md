Philippe, Ralph,

The Web Annotation Working Group requests transition to PR status for three specifications on Web Annotation. The publication is planned for the @@@@ of @@@@; the documents are follows:

-	Web Annotation Data Model
-	Web Annotation Vocabulary
-	Web Annotation Protocol

Document title, URIs, Abstract and Status
=========================================

Web Annotation Data Model
-------------------------

-	Editors' Draft: http://w3c.github.io/web-annotation/model/wd2/index.html
-	Final /TR URI when it gets published: http://www.w3.org/TR/2016/PR-annotation-model-2016@@@@/

Abstract:

Annotations are typically used to convey information about a resource or associations between resources. Simple examples include a comment or tag on a single web page or image, or a blog post about a news article.

The Web Annotation Data Model specification describes a structured model and format to enable annotations to be shared and reused across different hardware and software platforms. Common use cases can be modeled in a manner that is simple and convenient, while at the same time enabling more complex requirements, including linking arbitrary content to a particular data point or to segments of timed multimedia resources.

The specification provides a specific JSON format for ease of creation and consumption of annotations based on the conceptual model that accommodates these use cases, and the vocabulary of terms that represents it.

Status: http://w3c.github.io/web-annotation/model/wd2/index.html#h-sotd

Web Annotation Vocabulary
-------------------------

-	Editors' Draft: http://w3c.github.io/web-annotation/vocab/wd/index.html
-	Final /TR URI when it gets published: http://www.w3.org/TR/2016/PR-annotation-vocab-2016@@@@/

Abstract:

The Web Annotation Vocabulary specifies the set of RDF classes, predicates and named entities that are used by the Web Annotation Data Model [annotation-model]. It also lists recommended terms from other ontologies that are used in the model, and provides the JSON-LD Context and profile definitions needed to use the Web Annotation JSON serialization in a Linked Data context.

Status: http://w3c.github.io/web-annotation/vocab/wd/index.html#h-sotd

Web Annotation Protocol
-----------------------

-	Version ready to be published: http://w3c.github.io/web-annotation/protocol/wd/index.html
-	Final /TR URI when it gets published: http://www.w3.org/TR/2016/PR-annotation-protocol-2016@@@@/

Abstract:

Annotations are typically used to convey information about a resource or associations between resources. Simple examples include a comment or tag on a single web page or image, or a blog post about a news article.

The Web Annotation Protocol describes the transport mechanisms for creating and managing annotations in a method that is consistent with the Web Architecture and REST best practices.

Status: http://w3c.github.io/web-annotation/protocol/wd/index.html#h-sotd

Proposed publication date:
==========================

@@@@ @@, 2016

Records of the decision to request the transition:
==================================================

@@@@ LINK OF THE TO THE RESOLUTION @@@@

Evidence That Documentation Satisfies Group's Requirements
==========================================================

See the CR Transition request for the details (nothing has changed since that date):

-	https://lists.w3.org/Archives/Member/chairs/2016AprJun/0086.html

Dispostion of Comments and Changes Since CR
===========================================

The disposion of all the comments received during the Candidate Recommendation phase are part of the gihub issues' list:

-	Closed issues: https://github.com/w3c/web-annotation/milestone/3?closed=1
-	Open issues: https://github.com/w3c/web-annotation/milestone/3

All resulting changes are editorial, and are listed in the respective documents.

Evidence that the document has received wide review and that issues have been formally addressed
================================================================================================

Beyond the issues/comments since CR (see above), nothing has changed since the CR transition request. See that transition request for details:

-	https://lists.w3.org/Archives/Member/chairs/2016AprJun/0086.html

Objections
==========

There were no formal objections.

Features marked as "at risk"
============================

Model & Vocabulary documents
----------------------------

The Composite, List, and independents classes were marked at risk, pending implementation experience.

Resolution: @@@@@@

Vocabulary document
-------------------

Some terms come from the ActivityStreams vocabulary, and it was not clear what the course of that document would be. The Activity Vocabulary went to CR on the 6th of September. The current status is @@@@@

Resolution: @@@@@@

Patent disclosures
==================

No patent disclosures for these documents at the moment:

-	https://www.w3.org/2004/01/pp-impl/73180/exclude

Implementation information
==========================

The CR exit criteria are listed in the respective documents:

-	https://www.w3.org/TR/annotation-model/#candidate-recommendation-exit-criteria
-	https://www.w3.org/TR/annotation-vocab/#candidate-recommendation-exit-criteria
-	https://www.w3.org/TR/annotation-protocol/#candidate-recommendation-exit-criteria

The respective implementation reports are at:

-	https://w3c.github.io/test-results/annotation-model/all.html
-	http://w3c.github.io/test-results/annotation-vocab/all.html
-	https://w3c.github.io/test-results/annotation-protocol/all.html

Note that, for the purpose of this transition, only the first "block" of results is relevant, which lists the required features. The second "block" or results refer to the optional features; although these are not relevant for the transition, the WG included those in the test suite to help implementers in general.

The implementation reports show that the exit criteria are fulfilled for all three documents.

Plans for "life after Rec"
==========================

The plans of the Working group are:

-	The github repository will be maintained, albeit reducing the persons who have write/modify access to it to WG co-chairs and document editors.
-	An errata mechanism has already been set up which allows for the community to submit errata via the github issues list: https://www.w3.org/annotation/errata/
-	The already existing Open Annotation Community Group, which was also at the origin of this work, will keep the the discussion open with the community, will check the validity of reported errata, and *may* put forward new features that could lead to a possible next version of the Web Annotation Recommendation.

Thanks

-	Rob Sanderson and Tim Cole, Working Group Chairs
-	Ivan Herman, W3C Team Contacts
