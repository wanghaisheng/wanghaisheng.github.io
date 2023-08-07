---
title: "译Introducing NHIN Direct NHIN Direct的介绍 by Keith Boone"
meta_title: ""
description: "this is meta description"
date: 2010-12-13T16:52:23Z
image: "/images/image-placeholder.png"
categories: ["医疗信息标准", "译文"]
author: "John Doe"
tags: ["医疗信息标准", "译文","HIT","Keith Boone"]
draft: false
---


[原文链接](http://geekdoctor.blogspot.com/2010/03/introducing-nhin-direct.html)

之所以关注这篇文章的作者是因为之前一直在看Keith Boone的Blog,从他的首页上看到了几个人的Blog的外链,Keith这么胸猛,他推荐的人自然不会逊色。他们也将成为我在茫茫Healthcare Standards的知识海洋中学习的几盏明灯。

这篇文章简介了NHIN Direct的一些基本知识，希望大家都能够有所了解。

译文如下：

在过去的5年里,我同很多有天赋的标准开发人员、实作指导书(IG)撰写人员和软件开发工程师一起工作。我们已经制作了use case,选定了标准,统一了差距/冗余，撰写了互操作规范。



我很高兴看到我们在内容和词汇标准上取得的成就。我们有足够的动力和大量的应用。



传输仍然是一个需要努力的领域。FHA Connect是一个很好的开始,但是对于拥有很多use case的小的提供者来说, -支持有意义的从提供者到提供者，从提供者到付款方以及从提供者到公共卫生的医疗数据的推动(the push of healthcare data) 是一个挑战。很多SDO标准开发组织已经通过组合使用现有标准撰写了传输的互操作性规范和标准。对于拥有有限的可用资源的小型组织来说这些文档仍然不是最简单的。



当我问到构建一些更加简单的方法时,他们告诉我利用现有的标准来说明use case的话，这些指导guide书最好的。



这就显得很矛-假如我们一开始撰写互操作性标准和规范时基于的标准是不适合给资源有限的小型机构构建简单、易用、基于网络的数据传输的规范和标准的话？

答案是-我们需要一种新的、更简单的利用REST、简单的SOAP和SMTP的方法来传输数据。我认为NHIN Direct就是这种方法。





以下是从NHIN Direct FAQ网页上截取的亮点



What is NHIN Direct?

NHIN Direct是一系列使得授权的医护提供者之间健康信息安全、简单传递的标准、政策和服务,。NHIN Direct使得基于标准的健康信息的交换支持有意义方法的核心层1(core Stage 1 Meaningful Use measures ),包括支持CCD和medication reconciliation的护理记录摘要、转院摘要、出院摘要和其他临床文档的交换以及不同提供者之间实验室结果的交换。



Why NHIN Direct?

有必要通过一个支持core Meaningful Use outcomes and measures有意义的核心结果指标的简单的、基于标准的、广泛部署和良好支持的方法来做供应商之间使用Internet安全的传输健康信息扩展NHIN来支持更广范围的参与者和供应商



What is the relationship between NHIN Direct and the currently described NHIN Architecture?

目前所描述的NHIN架构描述了一种在National Health Information Organizations,国家健康信息机构之间病人查询、文档搜索以及交换的方法。包括联邦供应商比如Veterans Health Administration, Department of Defense Military Health System, RHIOs, 和 大型的IDNs.NHIN Direct支持不同的供应商、医院、实验室和其他医疗卫生机构间的交互的场景(cases of pushed communication)

目前NHIN委员会的成员将能够支持NHID Direct模型,供应商并且NHIN Direct的推动组织将扩展以支持发现和交换用例。两种模型都需要并且对同一个参与者同时使用，这取决于信息交换的需要。



Does NHIN Direct replace the current NHIN model? Or is NHIN Direct the current NHIN model on “training wheels”?

不会。NHIN Direct和目前的NHIN模型支持不同的用例usecase，二者在一个健全的国家级医疗信息交换系统中是并存的。

How will the specifications and standards for NHIN Direct be developed?

标准和规范将会在一种快速、开放的过程中来开发，旨在吸引代表公共和私人供应商和技术实现者的不同的利益相关者。



What NHIN Direct doesn’t solve

为了快速的构建它,我们刻意的将NHIN Direct限制在解决一个具有良好定义的问题点的标准和规范上。除非需要特殊的功能来支持核心的用例,我们会推后或者暂时忽略它。这样做的话,我们并非低估任何健康信息交换领域或者需要,不过是仅仅定义一个可以同时推进全国信息交换和短期内可以实现的范围。



How can I or my organization participate?

1.     从三月到年末NHIN Direct的利益相关者的一个核心小组将会一同迭代地开发核心的规范和服务描述以及在示范和现实世界的实施环境中编码来测试这些规范。为了密切合作,核心小组将由承诺积极参与的5-8个相关者参与,代码开发和贡献，最重要的是在现实世界中实现最终的规范和服务,来示范这些核心用例。

2.     NHIN Direct工作会直接以公开的方式,提供充分参与的机会。我们欢迎对一些开源的参考实现和运用不同技术的标准实现的评论和反馈,开发代码以及代码的贡献,

3.     Technology enablers可能会被动的参与标准的开发工作,通过检测工作和产生的规范,实作指导书(IG)以及参考的技术实现,然后积极参与到2010年下半年和2011年的构建NHIN Direct核心服务到EHR和HIE中去,和其他卫生技术实现。



NHIN Direct的奋斗理念表述在设计规则中

The golden standards rule of "rough consensus, working code" will be applied to this effort.



Discuss disagreements in terms of goals and outcomes, not in terms of specific technical implementations.



The NHIN Direct project will adhere to the following design principles agreed to by the HIT Standards Committee from the feedback provided to the Implementation Workgroup



Keep it simple; think big, but start small; recommend standards as minimal as possible to support the business goal and then build as you go.



Don’t let “perfect” be the enemy of “good enough”; go for the 80% that everyone can agree on; get everyone to send the basics (medications, problem list, allergies, labs) before focusing on the more obscure.



Keep the implementation cost as low as possible; eliminate any royalties or other expenses associated with the use of standards.



Design for the little guy so that all participants can adopt the standard and not just the best resourced.



Do not try to create a one size fits all standard, it will be too heavy for the simple use cases.



Separate content standards from transmission standards; i.e., if CCD is the html, what is the https?



Create publicly available controlled vocabularies & code sets that are easily accessible / downloadable



Leverage the web for transport whenever possible to decrease complexity & the implementers’ learning curve (“health internet”).



Create Implementation Guides that are human readable, have working examples, and include testing tools.



我很期待NHIN Direct的努力,一如既往的,新兴技术我总是想成为早期的运用者、测试员并做出积极的贡献。



RF:

FHA Connect说明:来源于FHA connect官方网站

“FHA Connection is an interactive application that gives our business partners secure interaction with HUD mainframe systems to do research and update our files. Through FHA Connection our business partners can send information to and receive information from our systems.



FHA Connection transactions include: requesting and updating a case number, recording appraisal and mortgagor insurance information, reassigning appraisers, changing borrower, requesting duplicate Mortgage Insurance Certificate; provides lenders a low-cost, on-line option for submitting delinquent data, to retrieve title approval information, to view the status of receipt of the mortgage insurance premiums.”
