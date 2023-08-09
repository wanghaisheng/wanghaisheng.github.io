---
title: "译自Implementing IHE SVS Over the Trifolia Consolidated CDA by  Keith Boone"
meta_title: ""
description: "this is meta description"
date: 2012-3-15T15:27:12Z
image: "/images/image-placeholder.png"
categories: ["工作"]
author: "haisheng"
tags: ["医疗信息标准", "译文","HIT","Keith Boone"]
draft: false
---

Friday, March 9, 2012 BY Keith Boone
Implementing IHE SVS Over the Trifolia Consolidated CDA Database  

这个32行的程序是为了让JSP页面能够根据Trifolia Workbench database 构建一个 IHE SVS Value Set 的实现。它完全没有处理任何错误，如果变量匹配的话 就得到 valueset, valuesetmember and dictionarycodesystem表中的数据。
```
<?xml version="1.0" encoding="ISO-8859-1" ?>
<svs:RetrieveValueSetResponse xmlns:svs="urn:ihe:iti:svs:2008" xmlns:html="http://www.w3.org/1999/xhtml"><%@
 taglib uri="http://java.sun.com/jsp/jstl/sql" prefix="sql" %><%@
 taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %><%@
 taglib uri="http://java.sun.com/jsp/jstl/xml" prefix="x"
%><sql:setDataSource var="snapshot" driver="com.mysql.jdbc.Driver"
 url="jdbc:mysql://localhost:3306/templatedb"
 user="user"  password="password"
/><sql:query dataSource="${snapshot}" var="valueset"
>SELECT valueSetName, description, ID from valueset WHERE OID = ?;
   <sql:param>${param.id}</sql:param>
</sql:query>
<svs:ValueSet version="" displayName="valueset.rowsByIndex[0][0]"id="{param.id}">
<svs:ConceptList xml:lang="en-US">
<sql:query dataSource="${snapshot}" var="members"
>SELECT m.code code, m.displayName displayname, m.codeSystemOID codeSystemOID, cs.codeSystemName codeSystemName
FROM valuesetmember m
LEFT JOIN dictionarycodesystem cs
ON m.codeSystemOID = cs.OID
WHERE m.valueSetOId = ?;
   <sql:param>${param.id}</sql:param>
</sql:query
>
<c:forEach var="row" items="${members.rows}">
<svs:Concept code="row.code"displayName="{row.displayName}" codeSystem="row.codeSystemOID"codeSystemName="{row.codeSystemName}" />
</c:forEach>
</svs:ConceptList>
</svs:ValueSet>
</svs:RetrieveValueSetResponse>
```
如何使用
1 安装MySQL Community Edition and JDBC Drivers
2.安装Trifolia Workbench (zip)
3.安装JSTL Libraries and MySQL JDBC Drivers into your Web Application
4.将上面的源码复制到RetrieveValueSet.jsp
5.根据MySQL的安装 更改用户名和密码
6.在WEB-INF文件夹下的web.xml中添加如下行
```
<servlet>
  <description>A Servlet conforming to the IHE SVS Profile</description>
  <display-name>IHE SVS Servlet</display-name>
  <servlet-name>RetrieveValueSet</servlet-name>
  <jsp-file>/RetrieveValueSet.jsp</jsp-file>
 </servlet>
 <servlet-mapping>
  <servlet-name>RetrieveValueSet</servlet-name>
  <url-pattern>/RetrieveValueSet</url-pattern>
 </servlet-mapping>
```
