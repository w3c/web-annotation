(mail sent: https://lists.w3.org/Archives/Member/chairs/2016AprJun/0086.html)

Philippe, Ralph,

The Web Annotation Working Group requests transition to CR status for four specifications on Web Annotation. The publication is planned for the 5 of July; the documents are follows:

 * Web Annotation Data Model
 * Web Annotation Vocabulary
 * Web Annotation Protocol


(1) Document title, URIs, Abstract and Status
=============================================

Web Annotation Data Model
-------------------------

- Version ready to be published
	http://w3c.github.io/web-annotation/admin/TR/annotation-model/Overview.html
- Final /TR URI when it gets published
	http://www.w3.org/TR/2016/CR-annotation-model-20160705/

Abstract:

Annotations are typically used to convey information about a resource or associations between resources. Simple examples include a comment or tag on a single web page or image, or a blog post about a news article.

The Web Annotation Data Model specification describes a structured model and format to enable annotations to be shared and reused across different hardware and software platforms. Common use cases can be modeled in a manner that is simple and convenient, while at the same time enabling more complex requirements, including linking arbitrary content to a particular data point or to segments of timed multimedia resources.

The specification provides a specific JSON format for ease of creation and consumption of annotations based on the conceptual model that accommodates these use cases, and the vocabulary of terms that represents it.

Status:
	http://w3c.github.io/web-annotation/admin/TR/annotation-model/Overview.html#h-sotd

Web Annotation Vocabulary
-------------------------

- Version ready to be published
	http://w3c.github.io/web-annotation/admin/TR/annotation-vocab/Overview.html
- Final /TR URI when it gets published
	http://www.w3.org/TR/2016/CR-annotation-vocab-20160705/

Abstract:

The Web Annotation Vocabulary specifies the set of RDF classes, predicates and named entities that are used by the Web Annotation Data Model [annotation-model]. It also lists recommended terms from other ontologies that are used in the model, and provides the JSON-LD Context and profile definitions needed to use the Web Annotation JSON serialization in a Linked Data context.

Status:
	http://w3c.github.io/web-annotation/admin/TR/annotation-vocab/Overview.html#h-sotd

Web Annotation Protocol
-----------------------

- Version ready to be published
	http://w3c.github.io/web-annotation/admin/TR/annotation-protocol/Overview.html
- Final /TR URI when it gets published
	http://www.w3.org/TR/2016/CR-annotation-protocol-20160705/

Abstract:

Annotations are typically used to convey information about a resource or associations between resources. Simple examples include a comment or tag on a single web page or image, or a blog post about a news article.

The Web Annotation Protocol describes the transport mechanisms for creating and managing annotations in a method that is consistent with the Web Architecture and REST best practices.

Status:
	http://w3c.github.io/web-annotation/admin/TR/annotation-protocol/Overview.html#h-sotd


(2)  Record of the decision to request the transition
=====================================================

	https://www.w3.org/2016/06/10-annotation-minutes.html#resolution01


(3) Record of Changes
=====================

The separate sections of each document record the noteworthy changes.


(4) Evidence that the document satisfies group's requirements
===============================================================

The main input to this Working Group was the Open Annotation Data Model:

	http://www.openannotation.org/spec/core/

developed by a separate Community Group:

	http://www.w3.org/community/openannotation/

which is widely deployed (and most implementations are now converting to the output of this Working Group) and which had its own "guiding principles":

	https://www.w3.org/community/openannotation/open-annotation-guiding-principles/

An additional requirement document was the

	Digital Publishing Annotation Use Cases
	https://www.w3.org/TR/dpub-annotation-uc/

Finally, the group collected a few additional requirements itself:

	https://www.w3.org/annotation/wiki/Annotation_System_Requirements

The final output of the Working Group takes into account these requirements in the way the Open Annotation Vocabulary has been reused; the changes, compared to the Open Annotation Data Model, are documented at:

	http://w3c.github.io/web-annotation/admin/TR/annotation-model/#changes-from-previous-draft

In particular, reflecting the terms in the charter

	https://www.w3.org/annotation/charter/

the list of the deliverables in the charter are fulfilled by the deliverables as follows:

1. "Abstract Data Model": the "Web Annotation Data Model" defines this data model
2. "Vocabulary": the "Web Annotation Vocabulary" defines the protocol as an RDF/OWL vocabulary; the Working Group also provides the formal vocabulary specification at the http://www.w3.org/ns/oa URL.
3. "Serializations": The "Web Annotation Data Model" is defined in terms of JSON-LD; the RDF vocabulary has natural serializations in terms of the standard RDF serializations (Turtle, RDF/XML, etc). The Working Group also plans to publish a Working Group Note on the HTML+RDFa serialization.
4. "HTTP API": is defined by the "Web Annotation Protocol"
5. "Client-side API": the Working Group has _not_ fulfilled this requirement due to a lack of interest and necessary expertise.
6. "Robust Link Anchoring": _part_ of this deliverable is part of the "Web Annotation Data Model", more specifically via Selectors like the Text Quote or CSS selectors. The Working Group also initiated a work on "FindText API", which was planned to be published as a joined deliverable with the Web Platform Working Group but, due to the lack of interest by browser vendors, this work has been abandoned.


(5) Evidence that the document has received wide review and that issues have  been formally addressed
=====================================================================================================

The group has received and recorded a number of issues; additionally, when the Group issued a Working Draft on the 31 march 2016, it also explicitly asked for a wide review (declaring that version as some sort of a virtual LC). All the comments coming up to this transition have been addressed and resolved satisfactorily:

All issues (removing admin, postponed, testing, etc. issues):

	https://github.com/w3c/web-annotation/issues?utf8=%E2%9C%93&q=is%3Aissue

All open issues currently:
	- https://github.com/w3c/web-annotation/issues

All open issues, minus on those on non rec-track notes, testing, administrative, or postponed issues:

	https://github.com/w3c/web-annotation/issues?utf8=%E2%9C%93&q=is%3Aissue+-label%3Aadmin+-label%3Apostpone+-label%3Atesting+-label%3Aselector_note+-label%3Aserialization+
	(http://bit.ly/1X6xqMn)

(Some issues have been postponed to a next version.)

The WG explicitly asked review from Internationalization, Accessibility, Privacy, and Security. It has received, and handled comments from:

	I18n: https://github.com/w3c/web-annotation/issues?q=is%3Aissue+label%3Ai18n-review
	Privacy: https://github.com/w3c/web-annotation/issues?q=is%3Aissue+label%3Apriv-review

Furthermore, although the group has not received explicit Accessibility review, it has decided to take over the Accessibility issues that have been added to the Open Annotation Vocabulary in its adaptation to EPUB:

	http://www.idpf.org/epub/oa/

See:

	https://github.com/w3c/web-annotation/issues/231

Decisions on the issues, answers to, and responses from commenter are all registered in the issue threads, with pointers to the IRC logs where the resolutions were passed on the calls.


(6) Objections
==============

There were no formal objections.


(7) Features marked as "at risk"
================================

There are two.

For the model and the vocabulary, see:

	http://w3c.github.io/web-annotation/admin/TR/annotation-model/#sets-of-bodies-and-targets

The issue is really a matter of understanding whether the grouping, with particular semantics, of several annotation bodies or targets leads to major implementation issues.

For the vocabulary, the extra risk is based on the dependency on Activity Streams; they should be in Rec before this document goes to Rec. As an emergency measure, the (few) classes should be defined in the Annotation namespace in case the Activity Stream document does not make it (with identical semantics).


(8) Patent disclosures
======================

No patent disclosures for these documents at the moment

	https://www.w3.org/2004/01/pp-impl/73180/exclude


(9)  Implementation information and testing
===========================================

The working group intends to  issue a call for implementations to demonstrate the validity of the specification.

The description of how tests are to be run is here:

   https://github.com/w3c/web-annotation-tests/blob/master/README.md

which refers to

   https://github.com/Spec-Ops/web-platform-tests/blob/master/annotation-model/README.md

for the testing of the model & vocabulary, and to

   https://github.com/Spec-Ops/web-platform-tests/blob/annotation-protocol/annotation-protocol/README.md

for the protocol testing. Both, although different, rely on the general W3C testing environment.

The Working Group maintains a separate Wiki page for ongoing or pledged implementations:

	https://www.w3.org/annotation/wiki/Implementations

Note that many of those implementations already exist but are based on the Open Annotation Model (ie, the predecessor of the Web Annotation Model). They have pledged to upgrade their implementations to use the latest model, although the exact dates are not necessarily known.

Note also that the Web Annotation Vocabulary and the Open Annotation Vocabulary are very close; most of the vocabulary items are identical or have been only marginally changed. The wide deployment of the OA vocabulary proves that the vocabulary _usage_ of those terms can already been considered as widely adopted for the WA documents as well.

Thanks

Rob Sanderson and Tim Cole, Working Group Chairs
Ivan Herman and Doug Schepers, W3C Team Contacts
