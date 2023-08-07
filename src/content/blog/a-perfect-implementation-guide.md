---
title: "译《A Perfect Implementation Guide》by Keith Boone"
meta_title: ""
description: "this is meta description"
date: 2012-2-23T17:40:12Z
image: "/images/image-placeholder.png"
categories: ["医疗信息标准", "译文"]
author: "John Doe"
tags: ["医疗信息标准", "译文","HIT","Keith Boone"]
draft: false
---


Tuesday, February 1, 2011
# A Perfect Implementation Guide

[英文原文链接](http://motorcycleguy.blogspot.com/2011/02/perfect-implementation-guide.html)
在上周HL7/IHE/ONC Consolidation Project的电话会议上，其中两个人同意新增一个独立的工作组来讨论publication format的问题。这篇也是我在这个工作组中的第一份答卷。
我代表HL7, IHE, and HITSP参与了CDA Implementation Guides的工作，也看到了很多来自CMS 法国 epSOS 德国和日本的IG。我也正在写一本关于CDA的书，预计年底就完成了。我列出了一些perfect guide的要求：
1.为了裁决问题，必须有单一的“normative”publication format，也是正式的规范
2.必须要有一种使得实施人员能够快速定位所需信息的丰富的、可搜索的多媒体格式
3.包含所有内容，包含一个页码的内容表格的一种可打印的格式，能够让实施人员获取到这种可打印的格式
4.必须包括范例文件、一致性数据、schema、shcematron、UML model等的补充材料来进一步支持实现
5.补充材料必须是标准化的格式，才能使用现成的工具。比如XSD Schematron或者XMI文件
6.表格化数据必须是CSV或者XML的格式，这样易于导入到现成的产品当中。
7.使用XML格式表示表格数据时需要良好的文档，更好的标准格式，必须在现成工具中易于使用。MIF不算
8.Publication format必须能够完整下载而无需外部的web服务或者网络连接。
9.IG必须含有确保一致性的可测试的一致性标准。注意：可测试的并不意味所有的测试都是自动化的。
10.一致性标准必须用可计算机化的格式来表示，以数据/模型的形式，使得其他系统能够以创新的方式来使用
11.一致性标准必须分为2部分，schema验证和功能性验证
12.schema验证标准无需了解输入就能确定交换的文档是否有效。不符合schema的文档就不是一个符合IG的。
13.功能性验证标准确定一些特殊的需求或和文档创建人员和接收人员所要求的功能(IHE中称之为content creator和consumer actor)
14.一致性标准主要以交换时文档中信息出现的顺序来组织，为的是易于获取。
15.一致性规则在于解释要求的目的来帮助实施人员理解规则想要完成的东西。
16.一致性规则必须提供一致性结果的例子，应该提供不一致的例子来辅助实现
17.IG使用容易理解的术语和方法，或者当使用领域术语或者方法时，解释这些内容以使得不熟悉该领域的实现人员理解它所讲的内容
18.IG提供多种形式的必要信息：一致性内容的UML模型，英语表达的一致性声明、可能的话，通过多种学习风格易于获取的表格形式，以及一致性内容的实例
19.只有一种格式的表现形式是规范化的，其他的都是提供信息来确保表现形式间的冲突可以解决
20.使用自动化的方案来产生多种表现形式以确保IG中信息的一致性。
