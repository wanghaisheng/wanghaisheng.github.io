title:     FHIR——介绍
date:   2012-6-11 00:00:12
updated	:
permalink:
tags:
- 医疗信息标准
- FHIR
- HIT
- 信息交换
categories:
- 医疗信息标准
- FHIR
---

http://www.hl7.org/implement/standards/fhir/introduction.htm
介绍Introduction
Fast Healthcare Interoperability Resources 定义了一个医疗卫生资源的集合。这些资源所表达的是一个个模块化的医学概念，通过交换它们以达到在医疗保健及相关流程中快速高效地解决问题。这些资源涵盖了医疗卫生的基本元素-病人、入院、诊断报告、药物和问题列表以及其中的一些参与者，同时也支持更加丰富和复杂的临床模型。资源的简单的直接的定义是基于充分的需求收集、正规分析以及与其他标准的交叉对应而来。

技术上来讲，FHIR是面向web的，在可能或合适的情况下，使用开放的internet标准来表达数据。资源基于简单的XML，使用基于http的restful协议，这样每个资源都有一定的url。注意尽管定义的资源要支持基于http的RESTful架构，但是使用这些资源时不一定非要是这种架构。该规范也定义了一种基于分类消息的框架和使用这些资源来构建文档的方法。另外，也可以在基于soa的架构中使用这些资源。这种灵活性为很广范围的互操作性问题提供了一致的解决方案。

Roadmap
新增
概述

FHIR定义了医疗卫生流程相关的信息交互中使用到的一些资源，这些资源是：

    模块化的Granular -它们是自身事务范围和操作的最小单元
    独立的Independent -无需引用其他资源就可理解资源的内容
    简单的Simple -每个资源都易于理解和实现 each resource is easy to understand and implement without needing tooling or infrastructure (though that can be used if desired)
    RESTful - resources are able to be used in a RESTful exchange context
    灵活的Flexible - 资源也可用于其他语境中如SOA架构、消息resources can also be used in other contexts, such as messaging or SOA architectures, and moved in and out of RESTful paradigms as convenient
    可扩展Extensible -在不影响互操作性的前提下对资源扩展以满足本地化需求 resources can be extended to cater for local requirements without impacting on interoperability
    支持web Web Enabled - where possible or appropriate, open internet standards are used for data representation
    免费使用Free for use -FHIR标准本身是免费的-任何人都可以实现FHIR或者衍生出相关标准，没有任何的IP限制。

除了一些基本的资源之外，FHIR定义了一个轻量级的实现框架，支持这些资源在RESTful、典型的消息交互、以人为主的临床文档和企业SOA架构环境中的应用。每一种方法都有自己的优点——FHIR provides the underpinning enablement that makes the choosing one of these painless and enables enterprises to choose their own paradigm without forsaking interoperability with other paradigms.

尽管资源很简单 很容易理解，Though the resources are simple and easy to understand, they are backed by a thorough, global requirements gathering and formal modeling process that ensures that the content of the resources is stable and reliable. The resource contents are mapped to solid underlying ontologies and models using computable languages (including RDF) so that the definitions and contents of the resources can be leveraged by computational analysis and conversion processes.

FHIR also provides an underlying conformance framework and tooling that allows different implementation contexts and enterprises to describe their context and use of resources in formal computable ways and to empower computed interoperability that leverages both the conformance and definitional frameworks.

The combination of the resources and the 3 supporting layers (implementation frameworks, definitional thoroughness, and conformance tooling) frees healthcare data so that it can easily flow to where it needs to be (hospital production systems, mobile clinical systems, cloud based data stores, national health repositories, research databases, etc.) without having to pass through format and semantic inter-conversion hurdles along the way.

Compared to the all the other approaches, FHIR... [-- Obligatory: insert your FHIR FIRE related joke here --].
该规范包含如下部分：
基本架构：定义和使用资源最基本的一些（资源格式、基本数据类型、管理编码的框架、使用扩展的规则、规范资源如何使用的方法）
交换协议：用以支持资源的交换（(HTTP RESTful协议、消息和文档以及一个通用的实现网页）
管理性资源：整个医疗流程中遇到的基本资源
基本的临床/医学组件：大多数临床实践中能够遇到的核心可重用临床资源
Resources
所有资源都包含以下部分：
一个永不会变的主id
结构化数据-资源的计算机化的正式表示
扩展性章节-HL7中没有定义的额外数据
文本表示-人可读的表示

因为主id是从不改变或被重用的，资源可能通过主id来引用，我们知道这是一个稳定的引用。虽然在没有明确引用其他资源的时候我们也能读和或改变这些资源，但是这些引用的存在会影响系统的状况，实现当中我们始终要求维护数据以及系统完整性。
交换规范很简单、直截了当，是基于XML表示的资源直接描述。每个资源独立描述，尽管资源之间有一些共同的数据模式即数据类型存在。
对于每个资源，该规范定义了：

    资源的含义以及范围
    资源的语义和业务内涵
    资源的XML内容模型 如XML UML schema等

除了简单的XML定义之外，也提供了XML schema和UML类图。UML类图表示了和XML格式一样的逻辑模型，尽管由于一些UML中的问题的，我们不能直接从这些UML模型中自动地得到符合或能够与该规范中定义的XML互操作的软件。
每个xml元素都有一个正式的定义，其中包括定义、需求声明、额外注释、与v3 RIM的对应、v2的对应。
另外，对于每个资源，也描述了一些与RESTful 有关的特性

    从id以及type和本地基础URL衍生出RESTful实现中的相对URL
    与特定资源相关的事务
    与特定资源相关的额外的搜索变量

每个资源都支持同样的一组事务-读、写、删除等等。每个资源类型所支持的一个特别重要的事务是提供一致性声明，它指定了系统支持所定义的内容模型中那一部分，支持那些其他的交互或事务。如果不支持其他的事务，就必须支持一致性交换。比如如果一致性交互返回一个错误error，就不支持任何操作。
