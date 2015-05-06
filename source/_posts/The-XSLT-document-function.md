title:    译自The XSLT document() function  by  Keith Boone
date:  2012-3-17 13:10:12
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

Thursday, January 26, 2012  BY Keith Boone
[The XSLT document() function](http://motorcycleguy.blogspot.com/2012/01/using-xslt-document-function-to-look-up.html)
有人在Structured Document 工作组邮件列表中问了一个如何将code转换成display name的问题。
在XSLT中，我一直在使用一种技术，它能够让我不用在XSLT stylesheet中嵌入转换逻辑，轻松地访问要查询的表。
在描述这种技术之前，我想先说说它的多种用途：
1.code转换
常常你需要将一种编码系统下的code转换为另一种code system下的code。我常使用这种技术实现本地code到标准词汇的转换 例如
从ANSI+到UCUM的单位转换
从问题严重程度的本地码到HITSP C32中要求的severity 的SNOMED CT code的转换
从问题状态的本地码到问题状态的SNOMED CT 码的转换
从问题类型的本地码到问题类型的SNOMED CT码的转换
从生命体征的本地码到生命体征的SNOMED CT码的转换
2.display name的查询 和code转换差不多，我们常常有的是标准的code，而没有与之相关的display name。利用此技术可实现比较小(不超过1000个code)的值集中display name的查询
3.标识符到web服务 end point的对应
从家庭社区的ID到XCA web服务地址
从DICOM AE标题到WADOweb服务endpoint
4.动态变化规则的验证，比如验证一个code是否符合词汇或值集的当前版本

此技术最基本的就是构建一个你要在stylesheet中使用的XML文档资源，为了声明此资源 你要：
<xsl:variable name="myDocument" select="document('mydocument.xml')"/>
它能够构建一个变量，此变量在你随后的XML中使用的XPath表达式中会用到。对于开篇提到的问题，我们所要做的就是如何根据一个语言code 也就是病人优先选用的语言，获取相应的display name。此code的值位于patient/languageCommunication/languageCode/@code
下面的XSLT片段展示了一个通过查询XML文档来获取病人语言的display name的模板
```
<xsl:variable name="langs" select="document('lang.xml')"/>
   ...
<xsl:template name='patientLanguage'>
  <!-- get the code -->
  <xsl:variable name='lang'
    select='//patient/languageCommunication/languageCode/@code'/>
  <xsl:variable name='mappedLang' select='langs//language[@code=lang]'/>
  <xsl:choose>
    <xsl:when test='$mappedLang'>
      <xsl:value-of select='$mappedLang/@displayName'/>
    </xsl:when>
    <xsl:otherwise>Unknown</xsl:otherwise>
  </xsl:choose>
</xsl:template>
```
此技术也可用在访问由RESTFUL web服务器endpoint所动态构建的resource中。在Values Sets and Query Health博文中我进行了演示

此技术的另外一个用途就是在schematron 规则中核对值集的一致性。如果你要求code/@code的值必须来自某一特殊的值集，你可以写一个访问web资源的规则，如下
```
<rule context='*/cda:templateId[@root = templateIdentifier]'>
  ...
  <let name='code' value='cda:code/@code'/>
  <let name='valueSetDoc' value='document("https://example.com/RetrieveValueSet?id=1.2.840.10008.6.1.308")'/>
  <assert test='valueSetDoc//ihe:Concept[@code=code]'>
    The code/@code element must come from the XXX Value Set (OID: 1.2.840.10008.6.1.308)
  </assert>
</rule>
```
能够使用外部的XML数据文件是XSLT的一大优势。能够与web服务动态构建的XML资源结合起来使之功能更加强大。
