---
title: "显示特定的标签值"
meta_title: ""
description: "this is meta description"
date: 2012-4-30T17:14:12Z
image: "/images/image-placeholder.png"
categories: ["工作"]
author: "haisheng"
tags:  ["医疗信息标准", "XSLT","HIT"]
draft: false
---


From looking at your XSLT and expected results, it looks like that for each a element in your XML, you want to output infomation on the following c elements present, if any occur before the next a element present.

For this, you could use an xsl:key to look up c elements for a given a element
```
<xsl:key name="lookup" match="c" use="generate-id(preceding-sibling::a[1])" />
```
i.e. Group together all c elements by the first preceding a element.

Then, you can firstly select a elements for which there are such c elements like so:
```
<xsl:apply-templates select="a[key('lookup', generate-id())]" />
```
Then, within this template, you can select the cc elements for output, like so:
```
<xsl:apply-templates select="key('lookup', generate-id())" />
```
So, given the following XSLT

```
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:output method="text" indent="yes"/>

   <xsl:key name="lookup" match="c" use="generate-id(preceding-sibling::a[1])" />

   <xsl:template match="/root">
      <xsl:apply-templates select="a[key('lookup', generate-id())]" />
   </xsl:template>

   <xsl:template match="a">
      <xsl:value-of select="concat(@id, ':&#13;', '&#13;')" />
      <xsl:apply-templates select="key('lookup', generate-id())" />
   </xsl:template>

   <xsl:template match="c">
      <xsl:apply-templates select="@*" />
      <xsl:value-of select="'&#13;'" />
   </xsl:template>

   <xsl:template match="c/@*">
      <xsl:value-of select="concat(local-name(), ':', ., ':&#13;')" />
   </xsl:template>
</xsl:stylesheet>
```
When applied to the following XML
```
<root>
   <a id="a1" name="a1"/>
   <b text="b1"/>
   <d test="test0" location="L0" text="c0"/>
   <a id="a2" name="a2"/>
   <b text="b2"/>
   <c test="test1" location="L1" text="c1"/>
   <c test="test2" location="L2" text="c2"/>
   <a id="a3" name="a3"/>
   <b text="b3"/>
   <c test="test3" location="L3" text="c3"/>
   <c test="test4" location="L4" text="c4"/>
   <c test="test5" location="L5" text="c5"/>
</root>
```
The following is output
```
a2:

test:test1:
location:L1:
text:c1:

test:test2:
location:L2:
text:c2:

a3:

test:test3:
location:L3:
text:c3:

test:test4:
location:L4:
text:c4:

test:test5:
location:L5:
text:c5:
```
Note that I am output the attributes on the c element in the order they appear in the XML document.
