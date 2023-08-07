title: 医疗信息标准的开源实现
date: 2010-11-29 15:41:17
updated	:
permalink:
tags:
- 医疗信息标准
- 译文
categories:
- 医疗信息标准
- 译文

---


Cross Enterprise Document Sharing 跨机构文档共享



IheOS http://sourceforge.net/projects/iheos/

IheOS源自NIST本来做原始的XDS规范测试的(现在不做这个了)的参考实现的工作。Bill Majurski是XDS的创始人，并且不止是XDS规范的核心人员之一，也是这个开源项目的核心之一，也是很多由IHE开发的用于XDS和其他规范测试的工具的核心之一。



O3-XDS http://sourceforge.net/projects/o3-xds/

O3-XDS代表” Open Three (O3) - Cross Enterprise Document Sharing”，O3-XDS是一个开源的、符合IHEXDS注册和存储库，可以在source forge找到。



Open eHealth Integration Platform http://repo.openehealth.org/confluence/display/ipf2

Open eHealth Integration Platform包括支持大量的IHE规范，包括XDS,PIX,PDQ(包括PIX/PDQ V3)，ATNA,XCA,XCPD.根据参考网站它在大量的不同的项目中被使用。

参考网站的地址:

http://repo.openehealth.org/confluence/display/ipf2/IPF+project+and+product+references

微软开发了XDS.b的一种实现，你可以在CodePlex网站上找到

http://ihe.codeplex.com/



HIEOS http://kenai.com/projects/hieos

HIEOS是一个IHE XDS.b (Integrating the Healthcare Enterprise (IHE) Cross Enterprise Document Sharing (XDS.b))和XCA(the Cross Community Access (XCA))集成规范的开源实现。主要是Vangent开发的。(http://www.marketwire.com/press-release/Vangent-Releases-HIEOS-Health-Information-Exchange-Open-Source-Software-1061437.htm)



IHE Profiles Charter Project

在open Health Tools中IHE规范Charter项目是一个重点关注IHE互操作规范的开源项目。这个工具支持一下IHE规范：

1)         ATNA: Audit Trail and Node Authentication审计跟踪和节点认证

2)         MPQ: Multi Patient Query多病人查询

3)         PAM: Patient Demographics Source病人的人口统计学资料来源

4)         PIX: Patient Identifier Cross-Referencing病人标识交叉索引

5)         PDQ: Patient Demographics Query病人人口统计学资料查询

6)         SVS: Shared Value Sets共享值集

7)         XCA: Cross Community Access跨社区访问

8)         XDS: Cross-Enterprise Document Sharing跨机构文档共享

9)         XUA: Cross-Enterprise User Assertion跨机构用户声明

这个项目相关的一些子项目：

1)         OpenXDS:服务器端IHE XDS.b的实现包括XDS存储库和注册角色。https://openxds.projects.openhealthtools.org/

2)         OpenATNA:服务器端IHE ANTA实现带有审计报告存储库https://openatna.projects.openhealthtools.org/

3)         OpenPIXPDQ:服务器端IHE PIX/PDQ规范的实现https://openpixpdq.projects.openhealthtools.org/



OHT

OHT工作来源于Eclipse Open Healthcare Framework，现在已经过渡成OHT项目的开发工作。

http://www.eclipse.org/ohf/components/ihe/

IBM在项目的初期付出了很多。



MOSS Misys Open Source Solutions

MOSS包括项目Braid( http://sourceforge.net/projects/braid)，它支持连接XDS..PIX/PDQ,ATNA的客户端，也有一个CCD生成器。服务器端组件来自于以上提到的Open Health Tools项目。



CONNECT http://www.connectopensource.org/

CONNECT是一个开源的软件和社区项目，是由美国政府的联邦卫生机构发起的。CONNECT支持基于IHE规范，其中包括XCA,ANTA,XDR的HITSP标准，在CONNECT网站上很难找到特定的文档显示它是支持IHE的，但是的确是支持的。它被超过23个组织的产品中被使用。



Xebra http://sourceforge.net/projects/xebra

Xebra项目是由HxTI发布的,是一个跨平台的、开源、瘦客户端和服务器端的基于web分布和医学图像结果的临床摘要的项目。Xebra基于最新的开源工业标准，包括JPEG2000,WADO和XDS-I规范。



Clinical Document Architecture and CCD



Misys Open Source Solutions (MOSS)

 http://www.misysoss.com/technical/open-source-solutions

MOSS包含一个CCD生成器



Mirth

Mirth有构建CDA文档的api

http://www.mirthcorp.com/community/wiki/display/MR/CDAPI+User+Guide



Model Driven Health Tools

https://www.projects.openhealthtools.org/sf/projects/mdht/

MDHT有一些很优秀的工具来生成CDA实作指导书,构建模型和生成CDA内容的工具。IHE、HL7、HITSP标准的CDA工具指南也是很有用的。



Eclipse CDA Editor

http://www.hl7book.net/index.php?title=Eclipse_Instance_Editor

Eclipse CDA Editor是一个CDA的实例验证和编辑器，它支持基于MIF的CDA内容的验证。



HL7 Version 2





HAPI

http://hl7api.sourceforge.net/

HAPI是一个开源的HL7 V2.X消息解析器, 是由加拿大的多伦多University Health Network(http://www.uhn.ca/) 发起的。



NHAPI

http://nhapi.sourceforge.net/home.php

NHAPI是给微软开发人员的HAPI项目的.net的接口。它源自于Colorado HIE: COHIE的开发。



MIRTH

http://www.mirthcorp.com/community/overview

Mirth是一个开源的集成引擎，它支持HL7,X12N,NCPDP消息标准。



HL7 Version 3



大多XDS的开源实现都包含HL7V3支持，包括Open eHealth Integration Platform(http://repo.openehealth.org/confluence/display/ipf2)
