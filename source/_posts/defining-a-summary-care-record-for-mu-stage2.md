title:  译自Defining a Summary Care Record for MeaningfulUse Stage2 by Keith Boone
date:  2012-3-15 14:20:12
updated	:
permalink:
tags:
- 医疗信息标准
- 译文
- HIT
- Keith Boone
categories:
- 医疗信息标准
- 译文
---
Wednesday, March 14, 2012 By Keith Boone
# Defining a Summary Care Record for MeaningfulUse Stage2

作者在文中提到“他在昨天的post中 描述了Meaningful Use Stage 2 rules中所存在的对于Summary Care Record的描述的混乱之处。今天他将进一步来简化它们。下面总共有2个表格。第一个表格只是对结果的总结。第二个表格详细描述了第一个表格。
Name, Gender, Race, Ethnicity, Preferred Language, and Date of Birth 姓名、性别、民族、宗教、语言、出生日期是所有摘要文档都有的，通常出现在CDA文档的Header的patient元素下面。
Provider information也常常出现在header部分，也是所有摘要文档所通用的。
Smoking Status, Vital Signs, Medications, Allergies, Problems, Procedures, Lab Tests and Results, and Care Plan
吸烟状态、体征、用药、过敏、问题、操作、实验室检查和结果、诊疗计划也是所有摘要文档共有的，在 consolidated guide的中也能找到对应的section。也有一些特例 ，为了满足MU标准你必须在一些文档中添加一些它所不包含的section。
Patient Instructions 可以出现在Care plan诊疗计划章节，或者出现在摘要的任何手写的文本中，但在CDA Consolidation中，直接有一个Instruction section可以用，可能用在任意一个所产生的摘要文档中，也可能是care plan章节的一个子章节。
任意文档中The date and location of the visit or stay 都位于<enconpassingEncounter>中，incentives rule中并没有对它们做出要求，但在standards rule中所有摘要文档却都要有。
The reason for visit 可以有多种方式：admission diagnosis, chief complaint, or reason for visit入院诊断、主诉、reason for visit，对于它们也有合适的section。同样，在incentives rule中也没有对它们做出要求。
Section 170.314(e)(2) stands out as the biggest odd-ball in the lot.  It includes medications and immunizations administered, patient decision aids, scheduled tests and visits and referrals.  The medications and immunizations administered should probably be recorded in the respective sections.  Patient Decision aids should be included in patient instructions.  The last three (future plans) should be included in the care plan.   That would normalize it nicely into the other groups.

 Growth charts also stand out.  These are not summaries, rather, they are assessments over time that can be crafted from data in multiple summaries.

 Care Team members don't show up in Clinical Summaries provided to patients.  Why wouldn't they be present when available?

 It isn't clear why diagnoses wouldn't be incorporated when available, or be viewable by the patient.

 It isn't clear why immunizations are reported in an ambulatory setting, but not in the inpatient setting (it's fairly common for some kinds of immunizations to be given during inpatient stays).

 Rationalizing these data elements across the summaries could easily get us to one or two definitions for summaries.

 A spreadsheet containing this content is available.
”
