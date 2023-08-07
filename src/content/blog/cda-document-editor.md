title: CDA文档编辑器
date: 2012-03-16 12:42:14
updated	:
permalink:
tags:
- 医疗信息标准
- CDA
categories:
- 医疗信息标准

---



CDA文档均为XML文件，故我们采用一些市面上常用的XML编辑软件。列举如下：
1.Oxygen XML Editor
它是一款基于Java的XML编辑器，支持XML, XSL, TXT, XSD, DTD文档，能自行校验XML, XSL, XSD代码，提示脚本错误。Oxygen能自动完成结束标签，代码高亮现实，支持Unicode。

Oxygen XML Editor是一款简洁并且功能一流的集XML察看和编辑等功能为一体的软件。由于它提供了对XML编辑特性的完整覆盖，因此，无论在企业界还是学术界，该软件的应用都很普及。它能工作在XML Schemas/ DTDs/Relax NG schemas和NRL Schemas.强大的转换支持让你不仅能编辑XSLT和XSL-FO文档,也能把它们转换成为你想要的如HTML/PS/PDF等文件。
个人感觉比较美观 易用性较高  
2.Altova XMLSpy©
在网上可以找到2006 2011的破解版本，易用性最高 我最喜欢和熟悉

```
XMLSpy的主要功能


XMLSpy 2005是一个用于XML工程开发的集成开发环境（Integrated Development Environment，简称IDE）。XMLSpy 2005可连同其他工具一起进行各种XML及文本文档的编辑和处理、进行XML文档（比如与数据库之间）的导入导出、在某些类型的XML文档与其他文档类型间作相互转换、关联工程中的不同类型的XML文档、利用内置的XSLT 1.0/2.0处理器和XQuery 1.0处理器进行文档处理，甚至能够根据XML文档生成代码。

XMLSpy 2005还提供了一中XML文档的图形化编辑视图——Authentic视图（直观视图），它使得用户可以像使用字处理软件那样对XML文档进行数据录入。Authentic视图在下列场合特别有用：



· 不熟悉XML的人被要求把数据录入XML文档

· 多个用户需要浏览或将数据录入位于某个服务器或共享资源上的单个文档。



本节我们仅对XMLSpy 2005的主要功能作简要的概述。这些功能在后面介绍各个视图（Text视图、Schema/WSDL视图、Authentic视图等）的章节和用户参考手册中还会被详细描述。请注意，本节没有完全列出XMLSpy 2005的所有功能。本节的目的只是给您提供一个XMLSpy 2005所支持功能的大致印象。


在多种编辑格式下编辑XML文档
您可以将XML文档作为普通文本来编辑（Text视图）、也可以在一个具有层次结构的表中进行编辑（增强型Grid视图），还可以在图形化的所见即所得（WYSIWYG）视图中编辑（Authentic视图）。对于XML Schema和WSDL文档，您还可以使用Schema/WSDL视图，它的图形化用户界面极大地简化了复杂schema和WSDL文档的创建。您可以根据需要在各种视图间进行切换。Browser视图（浏览器视图）可用于浏览XSLT样式表对XML文档的转换结果和HTML文档。


良构性（well-formedness）检查和内置验证器（validator）
在您切换视图或保存文件时，XMLSpy会自动对XML文档进行良构型检查。如果是关联了schema（DTD或XML Schema）的XML文件，XMLSpy还会对它进行验证（validation）。对于其他类型的文档（如DTD等），XMLSpy也会作语法和结构上的检查。


结构化编辑
在Text视图中，行号、缩进、书签以及可展开/折迭的元素显示等功能将协助您快速而有效地浏览文档。


智能编辑
在Text视图中，如果正在编辑的XML文档已经关联了schema，那么自动完成功能将在编辑过程中提供极大的帮助。在您敲击键盘的同时，光标所在位置会出现一个列有元素（element）、属性（attribute）和允许出现的枚举型属性值（enumerated attribute values）的窗口。另外，在您完成首标签（opening tag[译注//正式名称为start tag]）的输入时，自动完成功能会自动为您插入相应的尾标签（closing tag[译注//正式名称为end tag]），而您在弹出窗口中选择的属性也会被自动插入并被引号括起来。如果一个元素下必须出现某些元素或/和属性，那么您还可以选择在该元素被插入时为它自动生成那些必需的成分。此外，每个视图都有一组输入助手（Entry Helper）[译注//输入助手是对IDE中一些窗口的统称，利用这些窗口，用户可以方便地往文档中插入成分。]，通过它们使您可以往文档中插入成分[译注//比如插入一个元素（element）]或为主窗口中选中的成分指定属性。


Schema的编辑和管理
您可以在Schema/WSDL视图中轻松而快捷地创建XML Schema。该视图免除了许多由学习XML Schema结构、语法和设计原则而带来的困难。您还可以创建DTD（XMLSpy会对它们的语法进行检查）、在Schema和DTD间进行转换和生成档案（documentation），SchemaAgent功能将使您能够访问并使用存放于其他服务器上的schema —— 所有这些都为专业的XML Schema管理和编辑提供了高效的XML开发环境。


内置的XSLT 1.0和XSLT 2.0处理器
内置的XSLT 1.0和XSLT 2.0处理器都是符合相关W3C草案[译注//这里的草案指的是W3C工作草案（Working Draft），即正在制定过程中而尚未定型的W3C文档]的。它们使您可以直接在IDE中用XSLT 1.0或XSLT 2.0样式表来转换XML文档，并用XSLT调试器对XSLT样式表进行调试。


内置的XQuery 1.0处理器
内置的XQuery 1.0处理器是符合2004年7月23日发布的W3C XQuery 1.0工作草案的。通过它，您可以直接在IDE中执行和调试XQuery文档。


XML文档的转换
XML文档的转换可以直接在IDE中进行（利用内置的XSLT处理器或其他外部的XSLT处理器）如果您要在XMLSpy 2005 IDE中生成PDF文件[译注//XSL分为XSLT和XSL-FO，前者一般用于将XML文档转换为另一个XML文档或HTML文档，而后者一般用于将XML文档转换为PDF等文件格式。]，可以使用外部的FO处理器；在您指定样式表之后，只需一个点击即可将XML转换为PDF。此外，可以在IDE中给XSLT转换（transformation）传递参数值。


XPath求值
对于一个给定的XML文档，XPath求值（Evaluate XPath）功能可以列出一个XPath表达式返回的序列（或结点集）。您可以将文档结点（Document Node）或选择一个元素作为上下文结点（context node）。在创建XSLT样式表的过程中常常需要对XPath表达式进行求值，此时XPath求值功能是非常有用的。您还可以浏览返回序列中的各个结点。


XSLT 1.0/2.0调试器
XMLSpy 2005提供的XSLT 1.0和XSLT 2.0调试器是符合相关W3C草案的。您可以使用XSLT调试器来调试XSLT样式表。XSLT调试器在一个XML文件上运行要调试的XSLT样式表，并按转换的步骤逐步生成输出结果，其间您可以看到上下文结点（context node）、被执行的模板（template）以及转换过程中各步的其他细节。


XQuery 1.0调试器
XQuery 1.0调试器是符合W3C于2004年7月23日发布的XQuery 1.0工作草案的。XQuery调试器用于调试XQuery文档，功能与XSLT相似。


XML工程管理
在XMLSpy 2005 IDE中，您可以将相关的文件组织为工程（project）。与其他开发工具不同的是，在XMLSpy中，工程可以是一个树状结构（即可以在一个工程下创建另一个工程）。工程（project）中可以包含schema文件、XML数据文件、转换文件[译注//如一个XSLT文件]和输出文件等。工程中的文件被列在Project窗口（工程窗口）中，以便于访问工程中的文件。此外，您还可以为整个项目或整个目录做统一的设定，比如为整个目录的文件指定一个schema文件或XSLT文件。


Authentic视图
Authentic视图是XMLSpy 2005提供的一种图形化的XML文档视图。用户可以像使用字处理软件那样轻易地将数据录入XML文档。StyleVision Power Stylesheet是一个已经用StyleVision 2005创建好的样式表，用于指定在Authentic视图中如何格式化XML文档、以及如何进行数据录入。注意：Altova的免费软件Authentic 2005 Desktop Edition中也提供了Authentic视图。


数据库导入
您可以将数据库中的数据导入为一个XML文件、并生成一个与数据库结构对应的XML Schema文件。XMLSpy 2005目前支持下列数据库的导入：MS Access、MS SQL Server、Oracle、MySQL、Sybase、IBM DB2。


WSDL和SOAP
在Schema/WSDL视图中，您可以通过易用的图形用户界面创建和编辑WSDL文档。您也可以在IDE中创建、编辑并调试SOAP请求（SOAP request）。


对比XML文件（寻找差异）
XMLSpy 2005的对比功能让您能够发现两个XML文件的差异。您可以设置各种选项以配置该功能，比如忽略属性或子元素的次序、是否解析实体（entity）、是否忽略命名空间（namespace）等。对比功能还可用于进行文件夹的比较。


与Visual Studio .NET集成
XMLSpy 2005可以与您的Visual Studio .NET开发环境集成。您只要从Altova网站下载一个可执行程序然后运行它即可。


与Eclipse 3.0集成
Eclipse 3.0是一个集成了以插件形式发布的不同类型应用的开放源码框架。XMLSpy 2005 for the Eclipse Platform是一个Eclipse 3.0的插件，通过它您可以在Eclipse 3.0 Platform中使用XMLSpy 2005的功能（如果已经安装的话）。


代码生成
如果您要使用Java、C++或C#代码来处理XML文件中的数据，代码生成功能可以依据XML文档为您生成包含有关schema（DTD或XML Schema）的类定义代码。在XMLSpy 2005中，您可以直接根据DTD或XML Schema生成这样的代码。
```

3 XML Notepad 2007
台湾的范士展老师在其PPT中推荐了此编辑软件 不曾用 不熟悉
4.notepad++
简易编辑器  功能强大 很好用

```
    Notepad++ 是一款非常有特色的编辑器，是开源软件，可以免费使用。

    功能有：
    ①、内置支持多达 27 种语法高亮度显示(囊括各种常见的源代码、脚本，值得一提的是，完美支持 .nfo 文件查看)，也支持自定义语言；
    ②、可自动检测文件类型，根据关键字显示节点，节点可自由折叠/打开，代码显示得非常有层次感！这是此软件最具特色的体现之一；
    ③、可打开双窗口，在分窗口中又可打开多个子窗口，允许快捷切换全屏显示模式(F11)，支持鼠标滚轮改变文档显示比例，等等；
    ④、提供数个特色东东，如 邻行互换位置、宏功能，等等...现在网上有很多文件编辑器，这个却是不可多得的一款，不论是日常使用还是手写编程代码，都能让你体会到它独有的优势和方便。

    支持的语言: C, C++ , Java , C#, XML, HTML, PHP, Javascript , RC resource file, makefile, ASCII art file (extension .nfo , screenshot1, screenshot2), doxygen, ini file, batch file, ASP , VB/VBS source files , SQL , Objective-C , CSS, Pascal, Perl, Python and Lua.
```
