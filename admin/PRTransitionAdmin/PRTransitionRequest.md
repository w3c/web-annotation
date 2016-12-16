(To be sent to: Philippe le Hégaret <plh@w3.org>, Ralph Swick <ralph@w3.org>, Tim Berners-Lee <timbl@w3.org>, w3t-comm@w3.org, chairs@w3.org. CC to Ivan and the editors of the documents)


Philippe, Ralph,

The Web Annotation Working Group requests transition to PR status for three specifications on Web Annotation. The publication is planned for the 17 January of 2017; the documents are follows:

-	Web Annotation Data Model
-	Web Annotation Vocabulary
-	Web Annotation Protocol

Document title, URIs, Abstract and Status
=========================================

Web Annotation Data Model
-------------------------

-	Editors' Draft: http://w3c.github.io/web-annotation/model/wd2/index.html
-	Final /TR URI when it gets published: https://www.w3.org/TR/2016/PR-annotation-model-20170117/

Abstract: http://w3c.github.io/web-annotation/protocol/wd/index.html#h-abstract
Status:   http://w3c.github.io/web-annotation/model/wd2/index.html#h-sotd

Web Annotation Vocabulary
-------------------------


-	Editors' Draft: http://w3c.github.io/web-annotation/vocab/wd/index.html
-	Final /TR URI when it gets published: https://www.w3.org/TR/2016/PR-annotation-vocab-20170117/

Abstract: http://w3c.github.io/web-annotation/vocab/wd/index.html#h-abstract
Status:   http://w3c.github.io/web-annotation/vocab/wd/index.html#h-sotd

Web Annotation Protocol
-----------------------

-	Version ready to be published: http://w3c.github.io/web-annotation/protocol/wd/index.html
-	Final /TR URI when it gets published: https://www.w3.org/TR/2016/PR-annotation-protocol-20170117/

Abstract: http://w3c.github.io/web-annotation/protocol/wd/index.html#h-abstract
Status:   http://w3c.github.io/web-annotation/protocol/wd/index.html#h-sotd

Proposed publication date:
==========================

January 17, 2017

Records of the decision to request the transition:
==================================================

- https://www.w3.org/2016/12/16-annotation-minutes.html#resolution03

Evidence That Documentation Satisfies Group's Requirements
==========================================================

See the CR Transition request for the details (nothing has changed since that date):

-	https://lists.w3.org/Archives/Member/chairs/2016AprJun/0086.html

Disposition of Comments and Changes Since CR
============================================

The disposition of all the comments received during the Candidate Recommendation phase are part of the github issues' list:

-	Closed issues for this milestone: https://github.com/w3c/web-annotation/milestone/3?closed=1
-	Open issues for this milestone:   https://github.com/w3c/web-annotation/milestone/3

All resulting changes are editorial (e.g., explanatory text, change of formal references, etc.), and are listed in the respective documents.

For the records, the list of open issues that are not labelled as 'postponed' or only relevant to a possible WG note are:

http://bit.ly/2hIBtkz

One editorial change will be necessary for the PR: during the last CR round a feature ("string body") was *copied* by mistake into an informative appendix as if it was to become an optional feature:

- https://www.w3.org/TR/annotation-model/#string-body-1

This was, however, an editorial oversight, the feature *did* remain normative in the main text because there *are* 2 required implementations for it. That appendix will be removed from the PR version of the document.


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

The are no features at risk, see:

https://www.w3.org/TR/2016/CR-annotation-model-20161122/

Vocabulary document
-------------------

There was one feature at risk, see

https://www.w3.org/TR/2016/CR-annotation-vocab-20161122/

> "The use of the ActivityStreams terms are considered to be at-risk, pending [activitystreams-vocabulary] reaching Candidate Recommendation and, eventually, Recommendation. If this fails, the (few) terms used in the current document will be replaced by terms with a similar names and similar semantics, but in the namespace defined by this document."

The vocabulary in question is now in (2nd) CR:

https://www.w3.org/TR/2016/CR-activitystreams-vocabulary-20161215/

The Social Web WG has also passed a resolution recently:

> "We consider the 12 AS2 terms used by WebAnnotations to be stable and will not substantively change their definitions from those in our 06 September 2016 CR. We expect to go to PR in Jan 2017 and see no likely impediments, given our plan to drop any vocabulary terms lacking 2 impls. We currently lack 2 impls of as:startIndex, but assume Anno can provide them.""

 (see https://www.w3.org/wiki/Socialwg/2016-12-06-minutes#resolution03)

Based on this resolution, the WG's decision is to simply remove the 'at risk' label and publish the document unchanged with a reference to the CR version of the activity stream vocabulary. It is expected that the two documents will get into sync by the time of the possible publication of the Recommendations.

Resolution: https://www.w3.org/2016/12/16-annotation-minutes.html#resolution02

Protocol document
-----------------

The are no features at risk, see:

https://www.w3.org/TR/2016/CR-annotation-protocol-20161122/


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

The implementation reports show that the exit criteria are fulfilled for all three documents. The details are as below.

Note that the tests and the implementation reports include both required and optional features. Although, from the point of view of the CR Exit Criteria only the required features are relevant, the Working Group thought that providing test cases and a report on the optional features, too, would be useful for the community beyond the CR transition, too.

Model
-----

For the model, we have 12 implementations, see details and implementation reports at:

-	https://github.com/w3c/test-results/blob/gh-pages/annotation-model/README.md
-	https://w3c.github.io/test-results/annotation-model/all.html

The second document also includes some description on how to “read” the implementation report in terms of exit criteria and the optional vs. required features.

Vocabulary
----------

For the vocabulary, we have 2 implementations, see details and implementation reports at:

-	https://github.com/w3c/test-results/blob/gh-pages/annotation-vocab/README.md
-	http://w3c.github.io/test-results/annotation-vocab/all.html

Note that the exit criteria of the vocabulary as a separate entity means, essentially, proving the consistency of the vocabulary and its consistency with JSON-LD. Hence a relatively small report.

Protocol
--------

For the protocol, we have 3 implementations, see details and implementation reports at:

-	https://github.com/w3c/test-results/blob/gh-pages/annotation-protocol/README.md
-	https://w3c.github.io/test-results/annotation-protocol/all.html


Plans for "life after Rec"
==========================

The plans of the Working group are:

-	The github repository will be maintained, albeit reducing the persons who have write/modify access to WG co-chairs and document editors.
-	An errata mechanism has been set up which allows for the community to submit errata via the github issues list: https://www.w3.org/annotation/errata/
-	The already existing Open Annotation Community Group, which was also at the origin of this work, will keep the the discussion open with the community, will check the validity of reported errata, and *may* put forward new features that could lead to a possible next version of the Web Annotation Recommendation.

Thanks

-	Rob Sanderson and Tim Cole, Working Group Chairs
-	Ivan Herman, W3C Team Contact
