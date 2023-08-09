---
title: "piqi学习"
meta_title: ""
description: "this is meta description"
date: 2014-06-09T18:18:30Z
image: "/images/image-placeholder.png"
categories: ["工作"]
author: "haisheng"
tags: ["FHIR","piqi"]
draft: false
---


#piqi学习
*目标一：·piqi是什么

 *目标二：piqi与FHIR整合的可能性评估

*目标三：piqi用在文档内容校验上的可能性  

*目标四：基于piqi的消息引擎的设计

##piqi FAQ
*1. piq和JSON的区别在哪里  
Piq语言适合与人机交互，JSON则只是一种标准的、轻便的、高效的结构化数据的表达方式。  The Piq language is optimized for human interaction, whereas JSON is a standard, portable and reasonably efficient way of representing structured data.  

与JSON不同的是，Piq中有comment批注和逐字文本。字段名称也没有逗号分割和引号。这些特征都使得PIq更适合查看结构化数据或者在文本编辑器中编辑结构化数据.  Unlike JSON, Piq has comments and verbatim text literals. Also, there’s no comma-separators and quotes around field names. These and some other features make Piq a better choice for viewing structured data or editing it in a text editor.

Piq是一种强类型语言 JSON则是动态类型的.  Piq is a strongly typed language and JSON is dynamically typed.

Piq的使用离不开Piqi数据定义.有了数据定义之后,它就比JSON更强大.比如 在Piq中 字段默认值 甚至说字段本身都可以省略.  Piq can’t be used without Piqi data definitions. With data definitions, though, it is much more powerful than JSON. For example, in Piq, default field values and even field names can be omitted.

同时也可以在Piq中嵌入未分配类型的JSON.  And it is possible to embed untyped JSON in Piq!

Piq的数据模型更加强大.  Piq has a more powerful data model.

除了JSON所支持的所有数据类型,Piq/piqi还支持binary 二进制 enum枚举和variant(如tagged unions)还有一些其他优点 如支持浮点数NaN 正无穷 负无穷.   In addition to all data types supported by JSON, Piq/Piqi supports binaries, enums and variants (i.e. tagged unions). There are some other goodies, such as support for floating point NaN, negative and positive infinities.

Piq在持续改进中 而JSON木已成舟.  Piq is evolving, whereas JSON is set in stone.  

Piq最终将支持半结构化数据.  For example, Piq will eventually get support for semi-structured data.

需要注意的是 尽管存在差异,Piq格式的数据仍可以转换成JSON、XML、Protoco Buffer格式.这样你就可以使用PIq来对数据进行手动编辑,在其他目的下将其转换成其他格式即可.   Note that despite all the differences, data represented in Piq can be reliably converted to and from JSON, XML and Protocol Buffers binary formats. This way one can use Piq for manual data editing and convert it to other formats for other purposes.

*2. Piqi与Protocol Buffer的区别/How Piqi compares to Protocol Buffers?

作为数据序列化系统,piqi与protocol buffer是类似的,也兼容它.事实上,Piqi主要是受其启发.然而 却存在一些本质上的设计差异.  As a data serialization system, Piqi is very similar and compatible with Protocol Buffers. In fact, Piqi was largely inspired by it. However, there are some fundamental design differences.

Piqi是围绕着一个更加强大的数据模型而设计的.  Piqi is designed around a more powerful data model.

另外 对于protocol buffer中支持的record记录、enum枚举 、user-defined types自定义类型,Piqi中有list、type aliase和variant.  In addition to record and enum user-defined types supported by Protocol Buffer, Piqi has lists, type aliases and variants (aka tagged unions).

支持丰富的数据类型,这对于高级编程语言如OCaml和Erlang相当重要.比如,没有了list和variant,在处理数据时,就无法充分使用这些语言的功能.  Rich type support really makes a difference for high-level programming languages such as OCaml and Erlang. For example, without lists and variants, one can’t use utilize full potential of these languages when working with data.

相反的,protocol Bufffer是为Java、Python、C++等面向对象的语言设计的.  In contrast, Protocol Buffers was designed for object-oriented Java, Python and C++ languages.

Piqi是一种高级的数据定义语言.  Piqi is a high-level data definition language.

list、variant、record和aliase的组合可以很好地定义任何复杂的数据结构.在这方面protocol Buffer数据定义语言的层次就太低了.  Combination of lists, variants, records and aliases can be used to define any complex data structure in a very expressive way. Protocol Buffers data definition language is too low-level in this respect.

Portocol Buffer DDL的一些特性 如嵌套定义会给数据定义的表达能力带来负面作用.Piqi中拿掉了这些特性.  Some Protocol Buffers DDL’s features, like nested definitions, can negatively affect expressiveness of data definitions. Piqi avoids such features.  
##person实例
###person.piqi（schema定义）  
```

% this is an object of type "person" which is defined in module "person"
:person/person [
    .name "J. Random Hacker"
    .id 0

    .email "j.r.hacker@example.com"

    .phone [
        .number "(111) 123 45 67"
        % NOTE: phone is "home" by default
    ]

    .phone [
        .number "(222) 123 45 67"
        .mobile
    ]

    .phone [
        .number "(333) 123 45 67"
        .work
    ]
]

% another object of the same type
:person/person [
    .name "Joe User"
    .id 1

    % Joe User doesn't have an email

    .phone [ "(444) 123 45 67" ]
    .phone [ "(555) 123 45 67" .work ]
]

```
