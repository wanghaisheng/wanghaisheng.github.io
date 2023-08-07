---
title: "FHIR概览"
meta_title: ""
description: "this is meta description"
date: 2012-6-10T20:08:12Z
image: "/images/image-placeholder.png"
categories: ["医疗信息标准", "FHIR"]
author: "John Doe"
tags: ["医疗信息标准", "信息交换","FHIR"]
draft: false
---

自去年Grahame Grieve引出v3 has failed的讨论之后，RFH的出现似乎给HL7带来了一些生机。从RFH到FHIR 自是经过一番努力。越来越多的人对此表示出极大的兴趣，菜鸟我也不例外。故拟在后面的一些篇章中对目前所有的一些的资料进行一些简单的介绍和试译。 来到Grahame Grieve自己维护的博客主站（链接）上，在右侧links处即可看到一些相关信息，点击Fast Health Interoperability Resources即可进入，本文中将尝试对此主页上的内容做简要介绍。
20120814更新
Warning: FHIR is a draft specification that is still undergoing development prior to balloting as a full HL7 standard
作者2次强调了这一点  FHIR仍然处于开发之中 并不是一个完整的HL7的投票版标准
首先是一些外链。
Infrastructure基本架构
简介Introduction
资源格式Resource Format
数据类型Data Types
编码与术语Codes & Terminologies
扩展性Extensibility
资源规范Profiling Resources
Exchange交换

    实现Implementation
    组合Aggregations
    RESTREST (HTTP)
    消息Messaging
    文档Documents
    一致性声明Conformance Statement
    hData整合hData Integration
    Administrative Resources管理性资源
        人Person
        动物Animal
        组织Organization
        代理Agent
        病患Patient
        诊所Clinics
        入院Admissions
        预约Appointments
        感兴趣InterestOfCare
        转诊Transfers
        Clinical Components临床组件/医学组件
            生命体征等Vitals etc
            实验室报告Lab Report
            评估水平Assessment Scale
            影像Imaging
            警告Alert
            手术/操作Procedure
            会诊Consultation
            问题Problem
            饮食Diet
            植入物Implant
        Medications药物
            处方Prescription
            声明Statement
            分发Dispense
            用药Administration
            过敏Immunization



Welcome to FHIR欢迎来到FHIR/faiə/

Fast Healthcare Interoperability Resources 定义了一个医疗卫生资源的集合。这些资源所表达的是一个个模块化的医学概念，在医疗保健及相关流程中通过交换实现快速高效地解决问题。这些资源涵盖了医疗卫生的基本元素-病人、入院、诊断报告、药物和问题列表以及其中的一些参与者，同时也支持更加丰富和复杂的临床模型。资源的简单的直接的定义是基于充分的需求收集、正规分析以及与其他标准的交叉对应而来。

Useful Links有用的链接

    FHIR规范The FHIR specification
    chm格式的规范The specification as a Windows Help File (.chm)
    单个html格式的规范The specification in a single book
    zip格式的完整规范A Zip of the whole specification for offline use
    FHIR的schemaFHIR Schemas
    参考实现Reference Implementations
    FHIR的维基FHIR wiki - home for FHIR development team
    Version 0.02, Last Version, May 28, 2012. (Diff with current)
    Version 0.01, First Archived Version (During Vancouver WGM), May 14, 2012. (Diff with current)
    公开的测试服务器Publicly Available Test ServersFHIR License
    FHIR属于HL7所有，维护也归HL7。
    你可以重新发布FHIR
    你可以构建衍生规范或者是产品以及服务的实现
    你不能因你的规范中使用了FHIR的内容从而声称HL7或其中任一成员认可你的衍生规范
    任意HL7或者此规范的参与人员对你对FHIR的使用不负任何责任
    注意：为什么不使用开源的标准许可证？我们想使用 Creative Commons或者 a license listed here其中之一，但都不是用最朴实的英语来描述的。尽管专利是个问题，我们仍渴望能够满足开源项目的这些需求these requirements from the Open Source Initiative。

    然而我们解决了长期许可证的问题，我们应用如下许可证，它是根据OMG的改编而成：

    Subject to all of the terms and conditions below, HL7 hereby grants you a fully-paid up, non-exclusive, nontransferable, perpetual, worldwide license (without the right to sublicense), to use this specification to create and distribute software and special purpose specifications that are based upon this specification, and to use, copy, and distribute this specification as provided under the United States Copyright Act; provided that:
        both the copyright notice identified above and this permission notice appear on any copies of this specification;
        the use of the specifications is for informational purposes and will not be resold or transferred for commercial purposes;
        no modifications are made to this specification.

    This limited permission automatically terminates without notice if you breach any of these terms or conditions. Upon termination, you will destroy immediately any copies of the specifications in your possession or control.
    GENERAL USE RESTRICTIONS

    Any unauthorized use of this specification may violate copyright laws, trademark laws, and communications regulations and statutes. This document contains information which is protected by copyright. All Rights Reserved. No part of this work covered by copyright herein may be reproduced or used in any form or by any means--graphic, electronic, or mechanical, including photocopying, recording, taping, or information storage and retrieval systems--without permission of the copyright owner.
    DISCLAIMER OF WARRANTY

    WHILE THIS PUBLICATION IS BELIEVED TO BE ACCURATE, IT IS PROVIDED "AS IS" AND MAY CONTAIN ERRORS OR MISPRINTS. HL7 MAKES NO WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, WITH REGARD TO THIS PUBLICATION, INCLUDING BUT NOT LIMITED TO ANY WARRANTY OF TITLE OR OWNERSHIP, IMPLIED WARRANTY OF MERCHANTABILITY OR WARRANTY OF FITNESS FOR A PARTICULAR PURPOSE OR USE. IN NO EVENT SHALL HL7 BE LIABLE FOR ERRORS CONTAINED HEREIN OR FOR DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, RELIANCE OR COVER DAMAGES, INCLUDING LOSS OF PROFITS, REVENUE, DATA OR USE, INCURRED BY ANY USER OR ANY THIRD PARTY IN CONNECTION WITH THE FURNISHING, PERFORMANCE, OR USE OF THIS MATERIAL, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

    The entire risk as to the quality and performance of software developed using this specification is borne by you. This disclaimer of warranty constitutes an essential part of the license granted to you to use this specification.
    CONFORMANCEHL7 is and shall at all times be the sole entity that may authorize developers, suppliers and sellers of computer software or specifications to use certification marks, trademarks or other special designations to indicate compliance with with FHIR. Software developed under the terms of this license may claim compliance or conformance with FHIR if and only if the software compliance is of a nature fully matching the applicable conformance points as stated in the FHIR specification. Software developed only partially matching the applicable compliance points may claim only that the software was based on FHIR, but may not claim compliance or conformance with this specification. In the event that testing suites or processes are implemented or approved by HL7, Inc., software developed using this specification may claim compliance or conformance with the FHIR specification only if the software satisfactorily completes the testing suites.
    FHIR的存档版本Archived Versions of FHIR
    这里的存档只保存了重要的历史版本，也只有单个html的格式，仅用在html diff工具中。
        Version 0.04, 投票前的最终版 / Connectathon stable source (compare with this to see what has changed during the freeze). (Diff with current)
        Version 0.03, June 6, 2012. (Diff with current)
        Version 0.02, Last Version, May 28, 2012. (Diff with current)
        Version 0.01, First Archived Version (During Vancouver WGM), May 14, 2012. (Diff with current)
