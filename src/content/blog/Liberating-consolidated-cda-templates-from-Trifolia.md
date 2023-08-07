title:  译自Liberating Consolidated CDA Templates from the Trifolia  Keith Boone
date:  2012-3-15 14:48:12
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

Tuesday, March 6, 2012 By Keith Boone
Liberating Consolidated CDA Templates from the Trifolia Workbench Data
CDA Consolidation project的目标之一是从模板的模型驱动数据中自动化的构建验证和开发工具。我曾期望与MDHT项目有更加紧密的合作，我希望最终能够实现。几个星期以前，HL7和Lantana发布了包含CDA Consolidation data的Trifolia Workbench。Trifolia Workbench是以Eclipse Public License开源形式发布的，其源码，目前也就是数据库表结构，和一个Microsoft Access前端，同时从CDAConsolidation guide中将数据载入MySQL数据库的工具。 就此工具而言，它只是开了个头，我想要的更多。我的开发人员需要CDA Consolidation Guide的schematron文件。我想要数据以一种我可以与源材料进行比较以完成与HITSP C32的差距分析。因此，过去的俩天里我想把数据整成一种我能用的XML的格式，从这种格式中得到schematron文件。第一部分的工作已经完成了，你可以在下面的标题中下载。第二部分仍在进行当中。
要从数据库中得到数据，整成XML的格式，我使用了如下三种工具：
* Oxygen XML Editor (my current favorite among XML Editors)
* Xalan XSLT Engine (the only XSL Transformer I want to use)
* MySQL JDBC Drivers
* An XSL Stylesheet which is really the subject of this post
 Oxygen中包含了Xalan，也包含了一个SQL Extensions library,这意味着我可以完成对Trifolia Workbench表中数据的查询。
我写了一个两步转换。第一步先把表分开，第二步构建合适的XML结构。Trifolia template database共有5个主要的表：

* Templates (template)
* Constraints (template_constraint)
* Code Systems (dictionarycodesystem)
* Value Sets (valueset)
* Value Set Members (valuesetmember)

前2个主要的表对于验证而言是最重要的。剩下的三个是为了维护值集。也有很多不同目的的包含了人可读术语的编码表：

* Vocabulary Binding Types (vocbinding_type) [STATIC, DYNAMIC]
* Contexts (dictionarycontext)
* Conformance Types (conformance_type) [SHALL, SHALL NOT, SHOULD, SHOULD NOT, MAY]
* Template Types (template_type) [document, section, entry, subentry, unspecified]

我没有处理implementation guide表(implementationguide或associationtemplateimplementationguide)，或者是用户列表(tdb_users)，但你要知道 有这些表的存在
第一步，将这些表的内容复制到<templates>, <constraints>, <codeSystems>, <valueSets>, and <members> elements  <tdb> element元素内。数据复制是直接了当的。第一步就是对一些表格进行查询，用Left JOIN操作来分解code表中的术语。
我写了一个处理结果的模板，然后根据列名得到每行中的每个单元的属性或元素。如下；
```
  <xsl:template name="SQLtoXML">
    <!-- resultXML is the rowset returned by the query -->
    <xsl:param name="resultXML" select="."/>
    <xsl:param name="result" select="exslt:node-set($resultXML)"/>
    <!-- map is a string containing either an a or an e for each cell
         indicating whether it should be output as an attribute or an
         element
    -->
    <xsl:param name="map"/>
    <xsl:param name="meta" select="$result/sql/metadata"/>

    <!-- name is the element name to use for each row, and defaults
         to the table name -->
    <xsl:param name="name" select="$meta/column-header[1]/@table-name"/>

    <!-- for each row in the result set -->
    <xsl:for-each select="$result/sql/row-set/row">
      <!-- generate an element for the row -->
      <xsl:element name="{$name}">
        <!-- for each column in the result set -->
        <xsl:for-each select="col">
          <xsl:variable name="pos" select="position()"/>
          <!-- if there is an a in the map position for the cell -->
          <xsl:if
            test="substring(map,pos, 1) = 'a' and string(.) != ''">
            <!-- generate an attribute for it -->
            <xsl:attribute name="{@column-label}">
              <xsl:value-of select="."/>
            </xsl:attribute>
          </xsl:if>
        </xsl:for-each>
        <!-- And again for each column in the result set -->
        <xsl:for-each select="col">
          <xsl:variable name="pos" select="position()"/>
          <!-- if there is an e in the map position for the cell -->
          <xsl:if
            test="substring(map,pos, 1) != 'a' and string(.) != ''">
            <!-- generate an element for it -->
            <xsl:element name="{@column-label}">
              <xsl:value-of select="."/>
            </xsl:element>
          </xsl:if>
        </xsl:for-each>
      </xsl:element>
    </xsl:for-each>
  </xsl:template>
```  
第一步中提取数据成XML的片段，但是还没有合适的容器。这些片段在第二步中重构。这一步中每个constraint元素根据parentConstraintID 和templateID 属性的值 置于合适的 <template> or <constraint>，每个 <member>根据它的valueSetOID 属性值插入到合适的 <valueSet>元素中。

下载
你可以从google code中下载得到Stylesheet文件，它能够将 Trifolia Workbench database中的数据提取成XML格式。这种格式的文档 后面我会写。
指导
1.安装Trifolia Database 需要MySQL Community Edition)
注意：如果已经安装了MySQL 请在运行源码前执行命令 set charset latin1
2.安装JDBC Driver for MySQL.将jar文件复制到合适的lib文件夹下。
3.修改stylesheet顶端的 <xsl:param>元素 插入你的用户名和密码。
4.运行stylesheet。它会输出一个包含模板数据库内容的文件。
问题
有任何问题可以留言
备注
stylesheet修正了Trifolia Workbench数据的很多问题。workbench中数据的语境并没有限制namespace，因此你不能直接在stylesheets or Schematron中使用。
同时，请注意template_constraint中valueSetOID是直接实际的ID 而不是它的OID。
