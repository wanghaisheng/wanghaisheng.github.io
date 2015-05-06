title: how to understand  Health Concern
date:   2014-3-24 14:43:12
updated	:
permalink:
tags:
- 医疗信息标准
- HIT
- 临床概念
categories:
- 医疗信息标准
- 临床概念

---



Health Concern的概念是我一直捉摸不透的，

为什么要有这样的一个概念 最近在FHIR 的mailing list上有一些探讨 收集以供自己了理解

![](http://image.sciencenet.cn/album/201403/24/1447599wulki5ndd4rpbrb.png)

The conundrum of the observation-concern-problem-diagnosis continuum in my view is a form of progressive alerting or risk communication. Additionally as we move from a traditional medical record to a health record to a care plan, we are entering new territory in terminology and users.



From the clinical perspective, a “Health Concern” is:

“a health related matter that is of interest, importance or worry to someone, who may be the patient, patient's family or patient's health care provider”

http://wiki.hl7.org/index.php?title=Health_Concern



A condition may or may not be considered a health concern, depending on whose perspective.

For example, anorexic nervosa – a patient will be adamant that this is definitely NOT a health concern from his/her perspective. But the patient’s family and a health provider will consider that as a health concern

The same applies to over-weight (or under-weight), smoking, alcohol use …..



Some condition when categorized as health concern, may or may not be actioned upon.

For example, a 98 yo patient recently diagnosed with breast cancer, the patient and family acknowledge that it is a health concern, but do not want any intervention beyond a passive watch.





From the technical perspective, the “Health Concern” is a tracker/tracking mechanism:

“contains no semantics beyond that need for tracking, excepting the link between related Conditions (as identified through ObservationEvent or ObservationRisk assessments conveying Event, Clinical Finding, Disorder assertions, etc).”

http://wiki.hl7.org/index.php?title=Health_Concern



The definition and examples on “Health Concern” from clinical perspectives have been approved by PCWG at the San Antonio meeting.

We are still working on the formal definition of “health concern” as tracker.





It is worth noting that once a condition is considered as a health concern, it may or may not get “removed” from the health concern tracking, even though that condition has been deemed clinically as “resolved” or “in remission”.

For example:

leukaemia (and other conditions such as gout) in remission, will not get removed from the health concern tracking. It will be tracked continuously.

Recurrent pyrogenic cholangitis when completely resolved after surgical intervention – antibiotic therapy, exploration of CBD to remove obstruction, cholecystectomy, etc. The condition may still get tracked as health concern  for potential problem such as changes in weight cycling, steatorrhoea, colonic cancer risk, etc



To require tracking of patient’s health concern(s) is not a fantasy at all. It goes to the heart of patient safety.
