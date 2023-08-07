---
title: "译自Value Sets and QueryHealth  by  Keith Boone"
meta_title: ""
description: "this is meta description"
date: 2012-3-17T13:31:12Z
image: "/images/image-placeholder.png"
categories: ["医疗信息标准", "译文"]
author: "John Doe"
tags: ["医疗信息标准", "译文","HIT","Keith Boone"]
draft: false
---


Tuesday, November 1, 2011 By Keith Boone
[Value Sets and QueryHealth](http://motorcycleguy.blogspot.com/2011/11/value-sets-and-queryhealth.html)

[Query Health]()的一大难题就是一个特殊的measure就可能引用大量的编码值。在HL7中它们称之为值集。比如 [TCNY Quality Measures](http://wiki.siframework.org/file/view/TCNY%20Quality%20Measures%20Report%20v%20Q4%202009%20091028.pdf)中在Query Health "Query and Data Analysis"就引用了大量的code
下面是一个例子
```
Eligible encounters (CPT codes)
99201; 99202; 99203; 99204; 99205; 99211; 99212; 99213; 99214; 99215; 99241; 99242;
 99243; 99244; 99245; 99354; 99355; 99385; 99386; 99387; 99395; 99396; 99397; 99401;
 99402; 99403; 99404; 99406; 99407
```
那么，我们就希望能够访问这些code。有很多种方法可以在query中对此值集进行编码
在HQMF中，可以写成由OR组成的单独encounter的条件
```
<sourceOf typeCode="PRCN">
  <conjunctionCode code="OR"/>
  <encounter>
    ...
    <code code='99201' codeSystem='2.16.840.1.113883.6.12'/>
  </encounter>
</sourceOf>
<sourceOf typeCode="PRCN">

  <conjunctionCode code="OR"/>
  <encounter>
    ...
    <code code='99202' codeSystem='2.16.840.1.113883.6.12'/>
  </encounter>
</sourceOf>
```
这看起来并不是很美观，或者重用性很好。本质上讲，你使用确定value set的某个code system中的一个code。
另一种方法是在code中使用valueSet属性。HQMF并不推荐这样的原因在于M&M工作组的一些人认为这不是个好主意。 如果要用的话，会是如下的样子
```
<sourceOf typeCode="PRCN">
  <encounter>
    ...
    <code valueSet='2.16.840.1.113883.19.1091'/>
  </encounter>
</sourceOf>
```
这种方法的问题在于你只是引用了value set，系统需要处理query的话就必须解决如何解引用的问题。
至少有2种方法来处理。一就是使用HL7定义的 Common Terminology Service specification。另一种就是用 IHE Sharing Value Sets (SVS) profile .该规范同时支持HTTP和SOAP两种绑定方法。
下面是一个检索value set的URL示例
https://example.com/RetrieveValueSet?id=1.2.840.10008.6.1.308
下面是它所能返回的示例
```
<RetrieveValueSetResponse xmlns="urn:ihe:iti:svs:2008" cacheExpirationHint="2008-08-15T00:00:00-05:00">
  <ValueSet id="1.2.840.10008.6.1.308"
    displayName="Common Anatomic Regions Context ID 4031" version="20061023">
    <ConceptList xml:lang="en-US">
      <Concept code="T-D4000" displayName="Abdomen"
        codeSystem="2.16.840.1.113883.6.5"/>
      <Concept code="R-FAB57" displayName="Abdomen and Pelvis"
        codeSystem="2.16.840.1.113883.6.5"/>
      <Concept code="T-15420" displayName="Acromioclavicular joint"
        codeSystem="2.16.840.1.113883.6.5"/>
      <Concept code="T-15750" displayName="Ankle joint"
        codeSystem="2.16.840.1.113883.6.5"/>
      <Concept code="T-280A0" displayName="Apex of Lung"
        codeSystem="2.16.840.1.113883.6.5"/>
      <Concept code="T-D8200" displayName="Arm"
        codeSystem="2.16.840.1.113883.6.5"/>
      <Concept code="T-60610" displayName="Bile Duct"
        codeSystem="2.16.840.1.113883.6.5"/>
      <Concept code="T-74000" displayName="Bladder"
        codeSystem="2.16.840.1.113883.6.5"/>
      <Concept code="T-04000" displayName="Breast"
        codeSystem="2.16.840.1.113883.6.5"/>
      <Concept code="T-26000" displayName="Bronchus"
        codeSystem="2.16.840.1.113883.6.5"/>
      <Concept code="T-12770" displayName="Calcaneus"
        codeSystem="2.16.840.1.113883.6.5"/>
      <Concept code="T-11501" displayName="Cervical spine"
        codeSystem="2.16.840.1.113883.6.5"/>
      </ConceptList>
  </ValueSet>
</RetrieveValueSetResponse>
```
对value set使用SVS有一些很好的特点。如果你想将value set放到SQL表中，你可以用XSLT来转换
```
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    xmlns:svs="urn:ihe:iti:svs:2008"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="text"/>
    <xsl:template match="/">
        <xsl:apply-templates select=".//svs:ConceptList"/>
    </xsl:template>
    <xsl:template match="svs:ConceptList">
        <xsl:text>INSERT INTO VALUESETMEMBERS (VALUESETID, CODE, CODESYSTEMID, DISPLAYNAME)&#x0A;</xsl:text>
        <xsl:apply-templates select="svs:Concept"></xsl:apply-templates>
    </xsl:template>
    <xsl:template match="svs:Concept">
        <xsl:text>VALUES ('</xsl:text>
        <xsl:value-of select="../../@id"/>
        <xsl:text>', '</xsl:text>
        <xsl:value-of select="@code"/>
        <xsl:text>', '</xsl:text>
        <xsl:value-of select="@codeSystem"/>
        <xsl:text>', '</xsl:text>
        <xsl:value-of select="@displayName"/>
        <xsl:text>')&#x0A;</xsl:text>
    </xsl:template>
</xsl:stylesheet>
````
另外你可以构建一些包含value set内容的JSON 对象
你也可以用XPath document功能来访问value set
```
document("https://example.com/RetrieveValueSet?id=1.2.840.10008.6.1.308")
```
