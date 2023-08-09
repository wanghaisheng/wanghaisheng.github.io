---
title: "中文版GraphQL标准"
meta_title: ""
description: "this is meta description"
date: 2015-07-29T16:52:33Z
image: "/images/image-placeholder.png"
categories: ["工作"]
author: "haisheng"
tags: ["API", "GraphQL"]
draft: false
---


title: 中文版GraphQL标准
date: 2015-07-29 16:52:33
updated	:
permalink:
tags:
- API
- GraphQL
categories:
- API
- 译文

---
# GraphQL


_Working Draft – July 2015_

**Introduction**

This is a Draft RFC Specification for GraphQL, a query language created by Facebook in 2012 for describing the capabilities and requirements of data models for client‐server applications. The development of this standard started in 2015\. GraphQL is a new and evolving language and is not complete. Significant enhancement will continue in future editions of this specification.

**Copyright notice**

Copyright (c) 2015, Facebook, Inc. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

*   Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
*   Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
*   Neither the name Facebook nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



1.  [<span class="spec-secid">1</span>Overview](#sec-Overview)
2.  [<span class="spec-secid">2</span>Language](#sec-Language)
    1.  [<span class="spec-secid">2.1</span>Source Text](#sec-Source-Text)
        1.  [<span class="spec-secid">2.1.1</span>White Space](#sec-White-Space)
        2.  [<span class="spec-secid">2.1.2</span>Line Terminators](#sec-Line-Terminators)
        3.  [<span class="spec-secid">2.1.3</span>Comments](#sec-Comments)
        4.  [<span class="spec-secid">2.1.4</span>Insignificant Commas](#sec-Insignificant-Commas)
        5.  [<span class="spec-secid">2.1.5</span>Lexical Tokens](#sec-Source-Text.Lexical-Tokens)
        6.  [<span class="spec-secid">2.1.6</span>Ignored Tokens](#sec-Source-Text.Ignored-Tokens)
        7.  [<span class="spec-secid">2.1.7</span>Punctuators](#sec-Punctuators)
        8.  [<span class="spec-secid">2.1.8</span>Names](#sec-Names)
    2.  [<span class="spec-secid">2.2</span>Query Document](#sec-Language.Query-Document)
        1.  [<span class="spec-secid">2.2.1</span>Operations](#sec-Language.Query-Document.Operations)
        2.  [<span class="spec-secid">2.2.2</span>Selection Sets](#sec-Selection-Sets)
        3.  [<span class="spec-secid">2.2.3</span>Fields](#sec-Language.Query-Document.Fields)
        4.  [<span class="spec-secid">2.2.4</span>Arguments](#sec-Language.Query-Document.Arguments)
        5.  [<span class="spec-secid">2.2.5</span>Field Alias](#sec-Field-Alias)
        6.  [<span class="spec-secid">2.2.6</span>Fragments](#sec-Language.Query-Document.Fragments)
            1.  [<span class="spec-secid">2.2.6.1</span>Type Conditions](#sec-Type-Conditions)
            2.  [<span class="spec-secid">2.2.6.2</span>Inline Fragments](#sec-Inline-Fragments)
        7.  [<span class="spec-secid">2.2.7</span>Input Values](#sec-Input-Values)
            1.  [<span class="spec-secid">2.2.7.1</span>Int Value](#sec-Int-Value)
            2.  [<span class="spec-secid">2.2.7.2</span>Float Value](#sec-Float-Value)
            3.  [<span class="spec-secid">2.2.7.3</span>Boolean Value](#sec-Boolean-Value)
            4.  [<span class="spec-secid">2.2.7.4</span>String Value](#sec-String-Value)
            5.  [<span class="spec-secid">2.2.7.5</span>Enum Value](#sec-Enum-Value)
            6.  [<span class="spec-secid">2.2.7.6</span>List Value](#sec-List-Value)
            7.  [<span class="spec-secid">2.2.7.7</span>Input Object Values](#sec-Input-Object-Values)
        8.  [<span class="spec-secid">2.2.8</span>Variables](#sec-Language.Query-Document.Variables)
            1.  [<span class="spec-secid">2.2.8.1</span>Variable use within Fragments](#sec-Variable-use-within-Fragments)
        9.  [<span class="spec-secid">2.2.9</span>Input Types](#sec-Input-Types)
        10.  [<span class="spec-secid">2.2.10</span>Directives](#sec-Language.Query-Document.Directives)
            1.  [<span class="spec-secid">2.2.10.1</span>Fragment Directives](#sec-Fragment-Directives)
3.  [<span class="spec-secid">3</span>Type System](#sec-Type-System)
    1.  [<span class="spec-secid">3.1</span>Types](#sec-Types)
        1.  [<span class="spec-secid">3.1.1</span>Scalars](#sec-Scalars)
            1.  [<span class="spec-secid">3.1.1.1</span>Built-in Scalars](#sec-Built-in-Scalars)
                1.  [<span class="spec-secid">3.1.1.1.1</span>Int](#sec-Int)
                2.  [<span class="spec-secid">3.1.1.1.2</span>Float](#sec-Float)
                3.  [<span class="spec-secid">3.1.1.1.3</span>String](#sec-String)
                4.  [<span class="spec-secid">3.1.1.1.4</span>Boolean](#sec-Boolean)
                5.  [<span class="spec-secid">3.1.1.1.5</span>ID](#sec-ID)
        2.  [<span class="spec-secid">3.1.2</span>Objects](#sec-Objects)
            1.  [<span class="spec-secid">3.1.2.1</span>Object Field Arguments](#sec-Object-Field-Arguments)
            2.  [<span class="spec-secid">3.1.2.2</span>Object Field deprecation](#sec-Object-Field-deprecation)
            3.  [<span class="spec-secid">3.1.2.3</span>Object type validation](#sec-Object-type-validation)
        3.  [<span class="spec-secid">3.1.3</span>Interfaces](#sec-Interfaces)
            1.  [<span class="spec-secid">3.1.3.1</span>Interface type validation](#sec-Interface-type-validation)
        4.  [<span class="spec-secid">3.1.4</span>Unions](#sec-Unions)
            1.  [<span class="spec-secid">3.1.4.1</span>Union type validation](#sec-Union-type-validation)
        5.  [<span class="spec-secid">3.1.5</span>Enums](#sec-Enums)
        6.  [<span class="spec-secid">3.1.6</span>Input Objects](#sec-Input-Objects)
        7.  [<span class="spec-secid">3.1.7</span>Lists](#sec-Lists)
        8.  [<span class="spec-secid">3.1.8</span>Non-Null](#sec-Non-Null)
    2.  [<span class="spec-secid">3.2</span>Directives](#sec-Type-System.Directives)
        1.  [<span class="spec-secid">3.2.1</span>@skip](#sec--skip)
        2.  [<span class="spec-secid">3.2.2</span>@include](#sec--include)
    3.  [<span class="spec-secid">3.3</span>Starting types](#sec-Starting-types)
4.  [<span class="spec-secid">4</span>Introspection](#sec-Introspection)
    1.  [<span class="spec-secid">4.1</span>General Principles](#sec-General-Principles)
        1.  [<span class="spec-secid">4.1.1</span>Naming conventions](#sec-Naming-conventions)
        2.  [<span class="spec-secid">4.1.2</span>Documentation](#sec-Documentation)
        3.  [<span class="spec-secid">4.1.3</span>Deprecation](#sec-Deprecation)
        4.  [<span class="spec-secid">4.1.4</span>Type Name Introspection](#sec-Type-Name-Introspection)
    2.  [<span class="spec-secid">4.2</span>Schema Introspection](#sec-Schema-Introspection)
        1.  [<span class="spec-secid">4.2.1</span>The "__Type" Type](#sec-The-__Type-Type)
        2.  [<span class="spec-secid">4.2.2</span>Type Kinds](#sec-Type-Kinds)
            1.  [<span class="spec-secid">4.2.2.1</span>Scalar](#sec-Scalar)
            2.  [<span class="spec-secid">4.2.2.2</span>Object](#sec-Object)
            3.  [<span class="spec-secid">4.2.2.3</span>Union](#sec-Union)
            4.  [<span class="spec-secid">4.2.2.4</span>Interface](#sec-Interface)
            5.  [<span class="spec-secid">4.2.2.5</span>Enum](#sec-Enum)
            6.  [<span class="spec-secid">4.2.2.6</span>Input Object](#sec-Input-Object)
            7.  [<span class="spec-secid">4.2.2.7</span>List](#sec-List)
            8.  [<span class="spec-secid">4.2.2.8</span>Non-null](#sec-Non-null)
            9.  [<span class="spec-secid">4.2.2.9</span>Combining List and Non-Null](#sec-Combining-List-and-Non-Null)
5.  [<span class="spec-secid">5</span>Validation](#sec-Validation)
    1.  [<span class="spec-secid">5.1</span>Fields](#sec-Validation.Fields)
        1.  [<span class="spec-secid">5.1.1</span>Field Selections on Objects, Interfaces, and Unions Types](#sec-Field-Selections-on-Objects-Interfaces-and-Unions-Types)
        2.  [<span class="spec-secid">5.1.2</span>Field Selection Merging](#sec-Field-Selection-Merging)
        3.  [<span class="spec-secid">5.1.3</span>Leaf Field Selections](#sec-Leaf-Field-Selections)
    2.  [<span class="spec-secid">5.2</span>Arguments](#sec-Validation.Arguments)
        1.  [<span class="spec-secid">5.2.1</span>Argument Names](#sec-Argument-Names)
        2.  [<span class="spec-secid">5.2.2</span>Argument Values Type Correctness](#sec-Argument-Values-Type-Correctness)
            1.  [<span class="spec-secid">5.2.2.1</span>Compatible Values](#sec-Compatible-Values)
            2.  [<span class="spec-secid">5.2.2.2</span>Required Arguments](#sec-Required-Arguments)
    3.  [<span class="spec-secid">5.3</span>Fragments](#sec-Validation.Fragments)
        1.  [<span class="spec-secid">5.3.1</span>Fragment Declarations](#sec-Fragment-Declarations)
            1.  [<span class="spec-secid">5.3.1.1</span>Fragment Spread Type Existence](#sec-Fragment-Spread-Type-Existence)
            2.  [<span class="spec-secid">5.3.1.2</span>Fragments On Composite Types](#sec-Fragments-On-Composite-Types)
            3.  [<span class="spec-secid">5.3.1.3</span>Fragments Must Be Used](#sec-Fragments-Must-Be-Used)
        2.  [<span class="spec-secid">5.3.2</span>Fragment Spreads](#sec-Fragment-Spreads)
            1.  [<span class="spec-secid">5.3.2.1</span>Fragment spread target defined](#sec-Fragment-spread-target-defined)
            2.  [<span class="spec-secid">5.3.2.2</span>Fragment spreads must not form cycles](#sec-Fragment-spreads-must-not-form-cycles)
            3.  [<span class="spec-secid">5.3.2.3</span>Fragment spread is possible](#sec-Fragment-spread-is-possible)
                1.  [<span class="spec-secid">5.3.2.3.1</span>Object Spreads In Object Scope](#sec-Object-Spreads-In-Object-Scope)
                2.  [<span class="spec-secid">5.3.2.3.2</span>Abstract Spreads in Object Scope](#sec-Abstract-Spreads-in-Object-Scope)
                3.  [<span class="spec-secid">5.3.2.3.3</span>Object Spreads In Abstract Scope](#sec-Object-Spreads-In-Abstract-Scope)
                4.  [<span class="spec-secid">5.3.2.3.4</span>Abstract Spreads in Abstract Scope](#sec-Abstract-Spreads-in-Abstract-Scope)
    4.  [<span class="spec-secid">5.4</span>Directives](#sec-Validation.Directives)
        1.  [<span class="spec-secid">5.4.1</span>Directives Are Defined](#sec-Directives-Are-Defined)
    5.  [<span class="spec-secid">5.5</span>Operations](#sec-Validation.Operations)
        1.  [<span class="spec-secid">5.5.1</span>Variables](#sec-Validation.Operations.Variables)
            1.  [<span class="spec-secid">5.5.1.1</span>Variable Default Values Are Correctly Typed](#sec-Variable-Default-Values-Are-Correctly-Typed)
            2.  [<span class="spec-secid">5.5.1.2</span>Variables Are Input Types](#sec-Variables-Are-Input-Types)
            3.  [<span class="spec-secid">5.5.1.3</span>All Variable Uses Defined](#sec-All-Variable-Uses-Defined)
            4.  [<span class="spec-secid">5.5.1.4</span>All Variables Used](#sec-All-Variables-Used)
            5.  [<span class="spec-secid">5.5.1.5</span>All Variable Usages are Allowed](#sec-All-Variable-Usages-are-Allowed)
6.  [<span class="spec-secid">6</span>Execution](#sec-Execution)
    1.  [<span class="spec-secid">6.1</span>Evaluating requests](#sec-Evaluating-requests)
    2.  [<span class="spec-secid">6.2</span>Evaluating operations](#sec-Evaluating-operations)
    3.  [<span class="spec-secid">6.3</span>Evaluating selection sets](#sec-Evaluating-selection-sets)
    4.  [<span class="spec-secid">6.4</span>Evaluating a grouped field set](#sec-Evaluating-a-grouped-field-set)
        1.  [<span class="spec-secid">6.4.1</span>Field entries](#sec-Field-entries)
        2.  [<span class="spec-secid">6.4.2</span>Normal evaluation](#sec-Normal-evaluation)
        3.  [<span class="spec-secid">6.4.3</span>Serial execution](#sec-Serial-execution)
        4.  [<span class="spec-secid">6.4.4</span>Error handling](#sec-Error-handling)
        5.  [<span class="spec-secid">6.4.5</span>Nullability](#sec-Nullability)
7.  [<span class="spec-secid">7</span>Response](#sec-Response)
    1.  [<span class="spec-secid">7.1</span>Serialization Format](#sec-Serialization-Format)
        1.  [<span class="spec-secid">7.1.1</span>JSON Serialization](#sec-JSON-Serialization)
    2.  [<span class="spec-secid">7.2</span>Response Format](#sec-Response-Format)
        1.  [<span class="spec-secid">7.2.1</span>Data](#sec-Data)
        2.  [<span class="spec-secid">7.2.2</span>Errors](#sec-Errors)
8.  [<span class="spec-secid">A</span>Appendix: Notation Conventions](#sec-Appendix-Notation-Conventions)
    1.  [<span class="spec-secid">A.1</span>Context-Free Grammar](#sec-Context-Free-Grammar)
    2.  [<span class="spec-secid">A.2</span>Lexical and Syntactical Grammar](#sec-Lexical-and-Syntactical-Grammar)
    3.  [<span class="spec-secid">A.3</span>Grammar Notation](#sec-Grammar-Notation)
    4.  [<span class="spec-secid">A.4</span>Grammar Semantics](#sec-Grammar-Semantics)
    5.  [<span class="spec-secid">A.5</span>Algorithms](#sec-Algorithms)
9.  [<span class="spec-secid">B</span>Appendix: Grammar Summary](#sec-Appendix-Grammar-Summary)
    1.  [<span class="spec-secid">B.1</span>Ignored Tokens](#sec-Appendix-Grammar-Summary.Ignored-Tokens)
    2.  [<span class="spec-secid">B.2</span>Lexical Tokens](#sec-Appendix-Grammar-Summary.Lexical-Tokens)
    3.  [<span class="spec-secid">B.3</span>Query Document](#sec-Appendix-Grammar-Summary.Query-Document)

</div>

</header>

<section id="sec-Overview">

## <span class="spec-secid" title="link to this section">[1](#sec-Overview)</span>Overview

GraphQL is a query language designed to build client applications by providing an intuitive and flexible syntax and system for describing their data requirements and interactions.

For example, this GraphQL request will receive the name of the user with id 4 from the Facebook implementation of GraphQL.

```
{
  user(id: 4) {
    name
  }
}

```

Which produces the resulting data (in JSON):

```
{
  "user": {
    "name": "Mark Zuckerberg"
  }
}

```

GraphQL is not a programming language capable of arbitrary computation, but is instead a language used to query application servers that have capabilities defined in this specification. GraphQL does not mandate a particular programming language or storage system for application servers that implement it. Instead, application servers take their capabilities and map them to a uniform language, type system, and philosophy that GraphQL encodes. This provides a unified interface friendly to product development and a powerful platform for tool‐building.

GraphQL has a number of design principles:

*   **Hierarchical**: Most product development today involves the creation and manipulation of view hierarchies. To achieve congruence with the structure of these applications, a GraphQL query itself is structured hierarchically. The query is shaped just like the data it returns. It is a natural way for clients to describe data requirements.
*   **Product‐centric**: GraphQL is unapologetically driven by the requirements of views and the front‐end engineers that write them. GraphQL starts with their way of thinking and requirements and build the language and runtime necessary to enable that.
*   **Strong‐typing**: Every GraphQL server defines an application‐specific type system. Queries are executed within the context of that type system. Given a query, tools can ensure that the query is both syntactically correct and valid within the GraphQL type system before execution, i.e. at development time, and the server can make certain guarantees about the shape and nature of the response.
*   **Client‐specified queries**: Through its type system, a GraphQL server publishes the capabilities that its clients are allowed to consume. It is the client that is responsible for specifying exactly how it will consume those published capabilities. These queries are specified at field‐level granularity. In the majority of client‐server applications written without GraphQL, the server determines the data returned in its various scripted endpoints. A GraphQL query, on the other hand, returns exactly what a client asks for and no more.
*   **Introspective**: GraphQL is introspective. A GraphQL server’s type system must be queryable by the GraphQL language itself, as will be described in this specification. GraphQL introspection serves as a powerful platform for building common tools and client software libraries.

Because of these principles, GraphQL is a powerful and productive environment for building client applications. Product developers and designers building applications against working GraphQL servers -- supported with quality tools -- can quickly become productive without reading extensive documentation and with little or no formal training. To enable that experience, there must be those that build those servers and tools.

The following formal specification serves as a reference for those builders. It describes the language and its grammar; the type system and the introspection system used to query it; and the execution and validation engines with the algorithms to power them. The goal of this specification is to provide a foundation and framework for an ecosystem of GraphQL tools, client libraries, and server implementations -- spanning both organizations and platforms -- that has yet to be built. We look forward to working with the community in order to do that.



<section id="sec-Language">

## <span class="spec-secid" title="link to this section">[2](#sec-Language)</span>Language

Clients use the GraphQL query language to make requests to a GraphQL service. We refer to these request sources as documents. A document may contain operations (queries and mutations are both operations) as well as fragments, a common unit of composition allowing for query reuse.

A GraphQL document is defined as a syntactic grammar where terminal symbols are tokens (indivisible lexical units). These tokens are defined in a lexical grammar which matches patterns of source characters (defined by a double‐colon `::`).

<section id="sec-Source-Text">

### <span class="spec-secid" title="link to this section">[2.1](#sec-Source-Text)</span>Source Text

<div class="spec-production d2" id="SourceCharacter"><span class="spec-nt">[SourceCharacter](#SourceCharacter)</span>

<div class="spec-rhs"><span class="spec-prose">Any Unicode character</span></div>

</div>

GraphQL documents are expressed as a sequence of [Unicode](http://unicode.org/standard/standard.html) characters. However, with few exceptions, most of GraphQL is expressed only in the original ASCII range so as to be as widely compatible with as many existing tools, languages, and serialization formats as possible. Other than within comments, Non‐ASCII Unicode characters are only found within <span class="spec-nt">[StringValue](#StringValue)</span>.

<section id="sec-White-Space">

#### <span class="spec-secid" title="link to this section">[2.1.1](#sec-White-Space)</span>White Space

<div class="spec-production d2" id="WhiteSpace"><span class="spec-nt">[WhiteSpace](#WhiteSpace)</span>

<div class="spec-rhs"><span class="spec-prose">Horizontal Tab (U+0009)</span></div>

<div class="spec-rhs"><span class="spec-prose">Vertical Tab (U+000B)</span></div>

<div class="spec-rhs"><span class="spec-prose">Form Feed (U+000C)</span></div>

<div class="spec-rhs"><span class="spec-prose">Space (U+0020)</span></div>

<div class="spec-rhs"><span class="spec-prose">No-break Space (U+00A0)</span></div>

</div>

White space is used to improve legibility of source text and act as separation between tokens, and any amount of white space may appear before or after any token. White space between tokens is not significant to the semantic meaning of a GraphQL query document, however white space characters may appear within a <span class="spec-nt">String</span> or <span class="spec-nt">[Comment](#Comment)</span> token.



<section id="sec-Line-Terminators">

#### <span class="spec-secid" title="link to this section">[2.1.2](#sec-Line-Terminators)</span>Line Terminators

<div class="spec-production d2" id="LineTerminator"><span class="spec-nt">[LineTerminator](#LineTerminator)</span>

<div class="spec-rhs"><span class="spec-prose">New Line (U+000A)</span></div>

<div class="spec-rhs"><span class="spec-prose">Carriage Return (U+000D)</span></div>

<div class="spec-rhs"><span class="spec-prose">Line Separator (U+2028)</span></div>

<div class="spec-rhs"><span class="spec-prose">Paragraph Separator (U+2029)</span></div>

</div>

Like white space, line terminators are used to improve the legibility of source text, any amount may appear before or after any other token and have no significance to the semantic meaning of a GraphQL query document. Line terminators are not found within any other token.



<section id="sec-Comments">

#### <span class="spec-secid" title="link to this section">[2.1.3](#sec-Comments)</span>Comments

<div class="spec-production d2" id="Comment"><span class="spec-nt">[Comment](#Comment)</span>

<div class="spec-rhs"><span class="spec-t">#</span><span class="spec-nt list optional">[CommentChar](#CommentChar)<span class="spec-mods"><span class="spec-mod list">list</span><span class="spec-mod optional">opt</span></span></span></div>

</div>

<div class="spec-production d2" id="CommentChar"><span class="spec-nt">[CommentChar](#CommentChar)</span>

<div class="spec-rhs"><span class="spec-constrained"><span class="spec-nt">[SourceCharacter](#SourceCharacter)</span><span class="spec-butnot"><span class="spec-nt">[LineTerminator](#LineTerminator)</span></span></span></div>

</div>

GraphQL source documents may contain single‐line comments, starting with the <span class="spec-t">#</span> marker.

A comment can contain any Unicode code point except <span class="spec-nt">[LineTerminator](#LineTerminator)</span> so a comment always consists of all code points starting with the <span class="spec-t">#</span> character up to but not including the line terminator.

Comments behave like white space and may appear after any token, or before a line terminator, and have no significance to the semantic meaning of a GraphQL query document.



<section id="sec-Insignificant-Commas">

#### <span class="spec-secid" title="link to this section">[2.1.4](#sec-Insignificant-Commas)</span>Insignificant Commas

<div class="spec-production d2" id="Comma"><span class="spec-nt">[Comma](#Comma)</span>

<div class="spec-rhs"><span class="spec-t">,</span></div>

</div>

Similar to white space and line terminators, commas (<span class="spec-t">,</span>) are used to improve the legibility of source text and separate lexical tokens but are otherwise syntactically and semantically insignificant within GraphQL query documents.

Non‐significant comma characters ensure that the absence or presence of a comma does not meaningfully alter the interpreted syntax of the document, as this can be a common user‐error in other languages. It also allows for the stylistic use of either trailing commas or line‐terminators as list delimiters which are both often desired for legibility and maintainability of source code.



<section id="sec-Source-Text.Lexical-Tokens">

#### <span class="spec-secid" title="link to this section">[2.1.5](#sec-Source-Text.Lexical-Tokens)</span>Lexical Tokens

<div class="spec-production d2" id="Token"><span class="spec-nt">[Token](#Token)</span>

<div class="spec-rhs"><span class="spec-nt">[Punctuator](#Punctuator)</span></div>

<div class="spec-rhs"><span class="spec-nt">[Name](#Name)</span></div>

<div class="spec-rhs"><span class="spec-nt">[IntValue](#IntValue)</span></div>

<div class="spec-rhs"><span class="spec-nt">[FloatValue](#FloatValue)</span></div>

<div class="spec-rhs"><span class="spec-nt">[StringValue](#StringValue)</span></div>

</div>

A GraphQL document is comprised of several kinds of indivisible lexical tokens defined here in a lexical grammar by patterns of source Unicode characters.

Tokens are later used as terminal symbols in a GraphQL query document syntactic grammars.



<section id="sec-Source-Text.Ignored-Tokens">

#### <span class="spec-secid" title="link to this section">[2.1.6](#sec-Source-Text.Ignored-Tokens)</span>Ignored Tokens

<div class="spec-production d2" id="Ignored"><span class="spec-nt">[Ignored](#Ignored)</span>

<div class="spec-rhs"><span class="spec-nt">[WhiteSpace](#WhiteSpace)</span></div>

<div class="spec-rhs"><span class="spec-nt">[LineTerminator](#LineTerminator)</span></div>

<div class="spec-rhs"><span class="spec-nt">[Comment](#Comment)</span></div>

<div class="spec-rhs"><span class="spec-nt">[Comma](#Comma)</span></div>

</div>

Before and after every lexical token may be any amount of ignored tokens including <span class="spec-nt">[WhiteSpace](#WhiteSpace)</span> and <span class="spec-nt">[Comment](#Comment)</span>. No ignored regions of a source document are significant, however ignored source characters may appear within a lexical token in a significant way, for example a <span class="spec-nt">String</span> may contain white space characters.

No characters are ignored while parsing a given token, as an example no white space characters are permitted between the characters defining a <span class="spec-nt">[FloatValue](#FloatValue)</span>.



<section id="sec-Punctuators">

#### <span class="spec-secid" title="link to this section">[2.1.7](#sec-Punctuators)</span>Punctuators

<div class="spec-production d2" id="Punctuator"><span class="spec-nt">[Punctuator](#Punctuator)</span>

<div class="spec-oneof">

| <span class="spec-t">!</span> | <span class="spec-t">$</span> | <span class="spec-t">(</span> | <span class="spec-t">)</span> | <span class="spec-t">...</span> | <span class="spec-t">:</span> | <span class="spec-t">=</span> | <span class="spec-t">@</span> | <span class="spec-t">[</span> | <span class="spec-t">]</span> | <span class="spec-t">{</span> | <span class="spec-t">}</span> |

</div>

</div>

GraphQL documents include punctuation in order to describe structure. GraphQL is a data description language and not a programming language, therefore GraphQL lacks the punctionation often used to describe mathematical expressions.



<section id="sec-Names">

#### <span class="spec-secid" title="link to this section">[2.1.8](#sec-Names)</span>Names

<div class="spec-production d2" id="Name"><span class="spec-nt">[Name](#Name)</span>

<div class="spec-rhs"><span class="spec-rx">/[_A-Za-z][_0-9A-Za-z]*/</span></div>

</div>

GraphQL query documents are full of named things: operations, fields, arguments, directives, fragments, and variables. All names must follow the same grammatical form.

Names in GraphQL are case‐sensitive. That is to say `name`, `Name`, and `NAME` all refer to different names. Underscores are significant, which means `other_name` and `othername` are two different names.

Names in GraphQL are limited to this <acronym>ASCII</acronym> subset of possible characters to support interoperation with as many other systems as possible.





<section id="sec-Language.Query-Document">

### <span class="spec-secid" title="link to this section">[2.2](#sec-Language.Query-Document)</span>Query Document

<div class="spec-production" id="Document"><span class="spec-nt">[Document](#Document)</span>

<div class="spec-rhs"><span class="spec-nt list">[Definition](#Definition)<span class="spec-mods"><span class="spec-mod list">list</span></span></span></div>

</div>

<div class="spec-production" id="Definition"><span class="spec-nt">[Definition](#Definition)</span>

<div class="spec-rhs"><span class="spec-nt">[OperationDefinition](#OperationDefinition)</span></div>

<div class="spec-rhs"><span class="spec-nt">[FragmentDefinition](#FragmentDefinition)</span></div>

</div>

A GraphQL query document describes a complete file or request string received by a GraphQL service. A document contains multiple definitions of Operations and Fragments. GraphQL query documents are only executable by a server if they contain an operation. However documents which do not contain operations may still be parsed and validated to allow client to represent a single request across many documents.

If a query document contains only one query operation, that operation may be represented in the shorthand form, which omits the query keyword and operation name. Otherwise, if a GraphQL query document contains multiple operations, each operation must be named. When submitting a query document with multiple operations to a GraphQL service, the name of the desired operation to be executed must also be provided.

<section id="sec-Language.Query-Document.Operations">

#### <span class="spec-secid" title="link to this section">[2.2.1](#sec-Language.Query-Document.Operations)</span>Operations

<div class="spec-production" id="OperationDefinition"><span class="spec-nt">[OperationDefinition](#OperationDefinition)</span>

<div class="spec-rhs"><span class="spec-nt">[OperationType](#OperationType)</span><span class="spec-nt">[Name](#Name)</span><span class="spec-nt optional">[VariableDefinitions](#VariableDefinitions)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt optional">[Directives](#Directives)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt">[SelectionSet](#SelectionSet)</span></div>

<div class="spec-rhs"><span class="spec-nt">[SelectionSet](#SelectionSet)</span></div>

</div>

<div class="spec-production" id="OperationType"><span class="spec-nt">[OperationType](#OperationType)</span>

<div class="spec-oneof">

| <span class="spec-t">query</span> | <span class="spec-t">mutation</span> |

</div>

</div>

There are two types of operations that GraphQL models:

*   query – a read‐only fetch.
*   mutation – a write followed by a fetch.

Each operation is represented by an operation name and a selection set.

**Query shorthand**

If a document contains only one query operation, and that query defines no variables and contains no directives, that operation may be represented in a short‐hand form which omits the query keyword and query name.

For example, this unnamed query operation is written via query shorthand.

```
{
  field
}

```

<div class="spec-note">many examples below will use the query short‐hand syntax.</div>



<section id="sec-Selection-Sets">

#### <span class="spec-secid" title="link to this section">[2.2.2](#sec-Selection-Sets)</span>Selection Sets

<div class="spec-production" id="SelectionSet"><span class="spec-nt">[SelectionSet](#SelectionSet)</span>

<div class="spec-rhs"><span class="spec-t">{</span><span class="spec-nt list">[Selection](#Selection)<span class="spec-mods"><span class="spec-mod list">list</span></span></span><span class="spec-t">}</span></div>

</div>

<div class="spec-production" id="Selection"><span class="spec-nt">[Selection](#Selection)</span>

<div class="spec-rhs"><span class="spec-nt">[Field](#Field)</span></div>

<div class="spec-rhs"><span class="spec-nt">[FragmentSpread](#FragmentSpread)</span></div>

<div class="spec-rhs"><span class="spec-nt">[InlineFragment](#InlineFragment)</span></div>

</div>

An operation selects the set of information it needs, and will receive exactly that information and nothing more, avoiding over‐fetching and under‐fetching data.

```
{
  id
  firstName
  lastName
}

```

In this query, the `id`, `firstName`, and `lastName` fields form a selection set. Selection sets may also contain fragment references.



<section id="sec-Language.Query-Document.Fields">

#### <span class="spec-secid" title="link to this section">[2.2.3](#sec-Language.Query-Document.Fields)</span>Fields

<div class="spec-production" id="Field"><span class="spec-nt">[Field](#Field)</span>

<div class="spec-rhs"><span class="spec-nt optional">[Alias](#Alias)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt">[Name](#Name)</span><span class="spec-nt optional">[Arguments](#Arguments)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt optional">[Directives](#Directives)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt optional">[SelectionSet](#SelectionSet)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span></div>

</div>

A selection set is primarily composed of fields. A field describes one discrete piece of information available to request within a selection set.

Some fields describe complex data or relationships to other data. In order to further explore this data, a field may itself contain a selection set, allowing for deeply nested requests. All GraphQL operations must specify their selections down to fields which return scalar values to ensure an unambiguosly shaped response.

For example, this operation selects fields of complex data and relationships down to scalar values.

```
{
  me {
    id
    firstName
    lastName
    birthday {
      month
      day
    }
    friends {
      name
    }
  }
}

```

Fields in the top‐level selection set of an operation often represent some information that is globally accessible to your application and its current viewer. Some typical examples of these top fields include references to a current logged‐in viewer, or accessing certain types of data referenced by a unique identifier.

```
# `me` could represent the currently logged in viewer.
{
  me {
    name
  }
}

# `user` represents one of many users in a graph of data, referred to by a
# unique identifier.
{
  user(id: 4) {
    name
  }
}

```



<section id="sec-Language.Query-Document.Arguments">

#### <span class="spec-secid" title="link to this section">[2.2.4](#sec-Language.Query-Document.Arguments)</span>Arguments

<div class="spec-production" id="Arguments"><span class="spec-nt">[Arguments](#Arguments)</span>

<div class="spec-rhs"><span class="spec-t">(</span><span class="spec-nt list">[Argument](#Argument)<span class="spec-mods"><span class="spec-mod list">list</span></span></span><span class="spec-t">)</span></div>

</div>

<div class="spec-production" id="Argument"><span class="spec-nt">[Argument](#Argument)</span>

<div class="spec-rhs"><span class="spec-nt">[Name](#Name)</span><span class="spec-t">:</span><span class="spec-nt">[Value](#Value)</span></div>

</div>

Fields are conceptually functions which return values, and occasionally accept arguments which alter their behavior. These arguments often map directly to function arguments within a GraphQL server’s implementation.

In this example, we want to query a specific user (requested via the `id` argument) and their profile picture of a specific `size`:

```
{
  user(id: 4) {
    id
    name
    profilePic(size: 100)
  }
}

```

Many arguments can exist for a given field:

```
{
  user(id: 4) {
    id
    name
    profilePic(width: 100, height: 50)
  }
}

```

**Arguments are unordered**

Arguments may be provided in any syntactic order and maintain identical semantic meaning.

These two queries are semantically identical:

```
{
  picture(width: 200, height: 100)
}

```

```
{
  picture(height: 100, width: 200)
}

```



<section id="sec-Field-Alias">

#### <span class="spec-secid" title="link to this section">[2.2.5](#sec-Field-Alias)</span>Field Alias

<div class="spec-production" id="Alias"><span class="spec-nt">[Alias](#Alias)</span>

<div class="spec-rhs"><span class="spec-nt">[Name](#Name)</span><span class="spec-t">:</span></div>

</div>

By default, the key in the response object will use the field name queried. However, you can define a different name by specifying an alias.

In this example, we can fetch two profile pictures of different sizes and ensure the resulting object will not have duplicate keys:

```
{
  user(id: 4) {
    id
    name
    smallPic: profilePic(size: 64)
    bigPic: profilePic(size: 1024)
  }
}

```

Which returns the result:

```
{
  "user": {
    "id": 4,
    "name": "Mark",
    "smallPic": "https://cdn.site.io/pic-4-64.jpg",
    "bigPic": "https://cdn.site.io/pic-4-1024.jpg"
  }
}

```

Since the top level of a query is a field, it also can be given an alias:

```
{
  zuck: user(id: 4) {
    id
    name
  }
}

```

Returns the result:

```
{
  "zuck": {
    "id": 4,
    "name": "Mark Zuckerberg"
  }
}

```

A field’s response key is its alias if an alias is provided, and it is otherwise the field’s name.



<section id="sec-Language.Query-Document.Fragments">

#### <span class="spec-secid" title="link to this section">[2.2.6](#sec-Language.Query-Document.Fragments)</span>Fragments

<div class="spec-production" id="FragmentSpread"><span class="spec-nt">[FragmentSpread](#FragmentSpread)</span>

<div class="spec-rhs"><span class="spec-t">...</span><span class="spec-nt">[FragmentName](#FragmentName)</span><span class="spec-nt optional">[Directives](#Directives)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span></div>

</div>

<div class="spec-production" id="FragmentDefinition"><span class="spec-nt">[FragmentDefinition](#FragmentDefinition)</span>

<div class="spec-rhs"><span class="spec-t">fragment</span><span class="spec-nt">[FragmentName](#FragmentName)</span><span class="spec-t">on</span><span class="spec-nt">[TypeCondition](#TypeCondition)</span><span class="spec-nt optional">[Directives](#Directives)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt">[SelectionSet](#SelectionSet)</span></div>

</div>

<div class="spec-production" id="FragmentName"><span class="spec-nt">[FragmentName](#FragmentName)</span>

<div class="spec-rhs"><span class="spec-constrained"><span class="spec-nt">[Name](#Name)</span><span class="spec-butnot"><span class="spec-t">on</span></span></span></div>

</div>

Fragments are the primary unit of composition in GraphQL.

Fragments allow for the reuse of common repeated selections of fields, reducing duplicated text in the document. Inline Fragments can be used directly within a selection to condition upon a type condition when querying against an interface or union.

For example, if we wanted to fetch some common information about mutual friends as well as friends of some user:

```
query noFragments {
  user(id: 4) {
    friends(first: 10) {
      id
      name
      profilePic(size: 50)
    }
    mutualFriends(first: 10) {
      id
      name
      profilePic(size: 50)
    }
  }
}

```

The repeated fields could be extracted into a fragment and composed by a parent fragment or query.

```
query withFragments {
  user(id: 4) {
    friends(first: 10) {
      ...friendFields
    }
    mutualFriends(first: 10) {
      ...friendFields
    }
  }
}

fragment friendFields on User {
  id
  name
  profilePic(size: 50)
}

```

Fragments are consumed by using the spread operator (`...`). All fields selected by the fragment will be added to the query field selection at the same level as the fragment invocation. This happens through multiple levels of fragment spreads.

For example:

```
query withNestedFragments {
  user(id: 4) {
    friends(first: 10) {
      ...friendFields
    }
    mutualFriends(first: 10) {
      ...friendFields
    }
  }
}

fragment friendFields on User {
  id
  name
  ...standardProfilePic
}

fragment standardProfilePic on User {
  profilePic(size: 50)
}

```

The queries `noFragments`, `withFragments`, and `withNestedFragments` all produce the same response object.

<section id="sec-Type-Conditions">

##### <span class="spec-secid" title="link to this section">[2.2.6.1](#sec-Type-Conditions)</span>Type Conditions

<div class="spec-production" id="TypeCondition"><span class="spec-nt">[TypeCondition](#TypeCondition)</span>

<div class="spec-rhs"><span class="spec-nt">[NamedType](#NamedType)</span></div>

</div>

Fragments must specify the type they apply to. In this example, `friendFields` can be used in the context of querying a `User`.

Fragments cannot be specified on any input value (scalar, enumeration, or input object).

Fragments can be specified on object types, interfaces, and unions.

Selections within fragments only return values when concrete type of the object it is operating on matches the type of the fragment.

For example in this query on the Facebook data model:

```
query FragmentTyping {
  profiles(handles: ["zuck", "cocacola"]) {
    handle
    ...userFragment
    ...pageFragment
  }
}

fragment userFragment on User {
  friends {
    count
  }
}

fragment pageFragment on Page {
  likers {
    count
  }
}

```

The `profiles` root field returns a list where each element could be a `Page` or a `User`. When the object in the `profiles` result is a `User`, `friends` will be present and `likers` will not. Conversely when the result is a `Page`, `likers` will be present and `friends` will not.

```
{
  "profiles" : [
    {
      "handle" : "zuck",
      "friends" : { "count" : 1234 }
    },
    {
      "handle" : "cocacola",
      "likers" : { "count" : 90234512 }
    }
  ]
}

```



<section id="sec-Inline-Fragments">

##### <span class="spec-secid" title="link to this section">[2.2.6.2](#sec-Inline-Fragments)</span>Inline Fragments

<div class="spec-production" id="InlineFragment"><span class="spec-nt">[InlineFragment](#InlineFragment)</span>

<div class="spec-rhs"><span class="spec-t">...</span><span class="spec-t">on</span><span class="spec-nt">[TypeCondition](#TypeCondition)</span><span class="spec-nt optional">[Directives](#Directives)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt">[SelectionSet](#SelectionSet)</span></div>

</div>

Fragments can be defined inline within a selection set. This is done to conditionally include fields based on their runtime type. This feature of standard fragment inclusion was demonstrated in the `query FragmentTyping` example. We could accomplish the same thing using inline fragments.

```
query inlineFragmentTyping {
  profiles(handles: ["zuck", "cocacola"]) {
    handle
    ... on User {
      friends {
        count
      }
    }
    ... on Page {
      likers {
        count
      }
    }
  }
}

```





<section id="sec-Input-Values">

#### <span class="spec-secid" title="link to this section">[2.2.7](#sec-Input-Values)</span>Input Values

<div class="spec-production" id="Value"><span class="spec-nt">[Value](#Value)<span class="spec-mods"><span class="spec-params"><span class="spec-param">Const</span></span></span></span>

<div class="spec-rhs"><span class="spec-condition not">Const</span><span class="spec-nt">[Variable](#Variable)</span></div>

<div class="spec-rhs"><span class="spec-nt">[IntValue](#IntValue)</span></div>

<div class="spec-rhs"><span class="spec-nt">[FloatValue](#FloatValue)</span></div>

<div class="spec-rhs"><span class="spec-nt">[StringValue](#StringValue)</span></div>

<div class="spec-rhs"><span class="spec-nt">[BooleanValue](#BooleanValue)</span></div>

<div class="spec-rhs"><span class="spec-nt">[EnumValue](#EnumValue)</span></div>

<div class="spec-rhs"><span class="spec-nt">[ListValue](#ListValue)<span class="spec-mods"><span class="spec-params"><span class="spec-param conditional">Const</span></span></span></span></div>

<div class="spec-rhs"><span class="spec-nt">[ObjectValue](#ObjectValue)<span class="spec-mods"><span class="spec-params"><span class="spec-param conditional">Const</span></span></span></span></div>

</div>

Field and directive arguments accept input values of various literal primitives; input values can be scalars, enumeration values, lists, or input objects.

If not defined as constant (for example, in <span class="spec-nt">[DefaultValue](#DefaultValue)</span>), input values can be specified as a variable. List and inputs objects may also contain variables (unless defined to be constant).

<section id="sec-Int-Value">

##### <span class="spec-secid" title="link to this section">[2.2.7.1](#sec-Int-Value)</span>Int Value

<div class="spec-production d2" id="IntValue"><span class="spec-nt">[IntValue](#IntValue)</span>

<div class="spec-rhs"><span class="spec-nt">[IntegerPart](#IntegerPart)</span></div>

</div>

<div class="spec-production d2" id="IntegerPart"><span class="spec-nt">[IntegerPart](#IntegerPart)</span>

<div class="spec-rhs"><span class="spec-nt optional">[NegativeSign](#NegativeSign)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-t">0</span></div>

<div class="spec-rhs"><span class="spec-nt optional">[NegativeSign](#NegativeSign)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt">[NonZeroDigit](#NonZeroDigit)</span><span class="spec-nt list optional">[Digit](#Digit)<span class="spec-mods"><span class="spec-mod list">list</span><span class="spec-mod optional">opt</span></span></span></div>

</div>

<div class="spec-production d2" id="NegativeSign"><span class="spec-nt">[NegativeSign](#NegativeSign)</span>

<div class="spec-rhs"><span class="spec-t">-</span></div>

</div>

<div class="spec-production d2" id="Digit"><span class="spec-nt">[Digit](#Digit)</span>

<div class="spec-oneof">

| <span class="spec-t">0</span> | <span class="spec-t">1</span> | <span class="spec-t">2</span> | <span class="spec-t">3</span> | <span class="spec-t">4</span> | <span class="spec-t">5</span> | <span class="spec-t">6</span> | <span class="spec-t">7</span> | <span class="spec-t">8</span> | <span class="spec-t">9</span> |

</div>

</div>

<div class="spec-production d2" id="NonZeroDigit"><span class="spec-nt">[NonZeroDigit](#NonZeroDigit)</span>

<div class="spec-rhs"><span class="spec-constrained"><span class="spec-nt">[Digit](#Digit)</span><span class="spec-butnot"><span class="spec-t">0</span></span></span></div>

</div>

An Int number is specified without a decimal point or exponent (ex. `1`).



<section id="sec-Float-Value">

##### <span class="spec-secid" title="link to this section">[2.2.7.2](#sec-Float-Value)</span>Float Value

<div class="spec-production d2" id="FloatValue"><span class="spec-nt">[FloatValue](#FloatValue)</span>

<div class="spec-rhs"><span class="spec-nt">[IntegerPart](#IntegerPart)</span><span class="spec-nt">[FractionalPart](#FractionalPart)</span></div>

<div class="spec-rhs"><span class="spec-nt">[IntegerPart](#IntegerPart)</span><span class="spec-nt">[ExponentPart](#ExponentPart)</span></div>

<div class="spec-rhs"><span class="spec-nt">[IntegerPart](#IntegerPart)</span><span class="spec-nt">[FractionalPart](#FractionalPart)</span><span class="spec-nt">[ExponentPart](#ExponentPart)</span></div>

</div>

<div class="spec-production d2" id="FractionalPart"><span class="spec-nt">[FractionalPart](#FractionalPart)</span>

<div class="spec-rhs"><span class="spec-t">.</span><span class="spec-nt list">[Digit](#Digit)<span class="spec-mods"><span class="spec-mod list">list</span></span></span></div>

</div>

<div class="spec-production d2" id="ExponentPart"><span class="spec-nt">[ExponentPart](#ExponentPart)</span>

<div class="spec-rhs"><span class="spec-nt">[ExponentIndicator](#ExponentIndicator)</span><span class="spec-nt optional">[Sign](#Sign)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt list">[Digit](#Digit)<span class="spec-mods"><span class="spec-mod list">list</span></span></span></div>

</div>

<div class="spec-production d2" id="ExponentIndicator"><span class="spec-nt">[ExponentIndicator](#ExponentIndicator)</span>

<div class="spec-oneof">

| <span class="spec-t">e</span> | <span class="spec-t">E</span> |

</div>

</div>

<div class="spec-production d2" id="Sign"><span class="spec-nt">[Sign](#Sign)</span>

<div class="spec-oneof">

| <span class="spec-t">+</span> | <span class="spec-t">-</span> |

</div>

</div>

A Float number includes either a decimal point (ex. `1.0`) or an exponent (ex. `1e50`) or both (ex. `6.0221413e23`).



<section id="sec-Boolean-Value">

##### <span class="spec-secid" title="link to this section">[2.2.7.3](#sec-Boolean-Value)</span>Boolean Value

<div class="spec-production" id="BooleanValue"><span class="spec-nt">[BooleanValue](#BooleanValue)</span>

<div class="spec-oneof">

| <span class="spec-t">true</span> | <span class="spec-t">false</span> |

</div>

</div>

The two keywords `true` and `false` represent the two boolean values.



<section id="sec-String-Value">

##### <span class="spec-secid" title="link to this section">[2.2.7.4](#sec-String-Value)</span>String Value

<div class="spec-production d2" id="StringValue"><span class="spec-nt">[StringValue](#StringValue)</span>

<div class="spec-rhs"><span class="spec-t">""</span></div>

<div class="spec-rhs"><span class="spec-t">"</span><span class="spec-nt list">[StringCharacter](#StringCharacter)<span class="spec-mods"><span class="spec-mod list">list</span></span></span><span class="spec-t">"</span></div>

</div>

<div class="spec-production d2" id="StringCharacter"><span class="spec-nt">[StringCharacter](#StringCharacter)</span>

<div class="spec-rhs"><span class="spec-constrained"><span class="spec-nt">[SourceCharacter](#SourceCharacter)</span><span class="spec-butnot"><span class="spec-t">"</span><span class="spec-t">\</span><span class="spec-nt">[LineTerminator](#LineTerminator)</span></span></span></div>

<div class="spec-rhs"><span class="spec-t">\</span><span class="spec-nt">[EscapedUnicode](#EscapedUnicode)</span></div>

<div class="spec-rhs"><span class="spec-t">\</span><span class="spec-nt">[EscapedCharacter](#EscapedCharacter)</span></div>

</div>

<div class="spec-production d2" id="EscapedUnicode"><span class="spec-nt">[EscapedUnicode](#EscapedUnicode)</span>

<div class="spec-rhs"><span class="spec-t">u</span><span class="spec-rx">/[0-9A-Fa-f]{4}/</span></div>

</div>

<div class="spec-production d2" id="EscapedCharacter"><span class="spec-nt">[EscapedCharacter](#EscapedCharacter)</span>

<div class="spec-oneof">

| <span class="spec-t">"</span> | <span class="spec-t">\</span> | <span class="spec-t">/</span> | <span class="spec-t">b</span> | <span class="spec-t">f</span> | <span class="spec-t">n</span> | <span class="spec-t">r</span> | <span class="spec-t">t</span> |

</div>

</div>

Strings are lists of characters wrapped in double‐quotes `"`. (ex. `"Hello World"`). White space and other otherwise‐ignored characters are significant within a string value.



<section id="sec-Enum-Value">

##### <span class="spec-secid" title="link to this section">[2.2.7.5](#sec-Enum-Value)</span>Enum Value

<div class="spec-production" id="EnumValue"><span class="spec-nt">[EnumValue](#EnumValue)</span>

<div class="spec-rhs"><span class="spec-constrained"><span class="spec-nt">[Name](#Name)</span><span class="spec-butnot"><span class="spec-t">true</span><span class="spec-t">false</span><span class="spec-t">null</span></span></span></div>

</div>

Enum values are represented as unquoted names (ex. `MOBILE_WEB`). It is recommended that Enum values be “all caps”. Enum values are only used in contexts where the precise enumeration type is known. Therefore it’s not necessary to supply an enumeration type name in the literal.

An enum value cannot be “null” in order to avoid confusion. GraphQL does not supply a value literal to represent the concept <span class="spec-keyword">null</span>.



<section id="sec-List-Value">

##### <span class="spec-secid" title="link to this section">[2.2.7.6](#sec-List-Value)</span>List Value

<div class="spec-production" id="ListValue"><span class="spec-nt">[ListValue](#ListValue)<span class="spec-mods"><span class="spec-params"><span class="spec-param">Const</span></span></span></span>

<div class="spec-rhs"><span class="spec-t">[</span><span class="spec-t">]</span></div>

<div class="spec-rhs"><span class="spec-t">[</span><span class="spec-nt list">[Value](#Value)<span class="spec-mods"><span class="spec-params"><span class="spec-param conditional">Const</span></span><span class="spec-mod list">list</span></span></span><span class="spec-t">]</span></div>

</div>

Lists are ordered sequences of values wrapped in square‐brackets `[ ]`. The values of a List literal may be any value literal or variable (ex. `[1, 2, 3]`).

Commas are optional throughout GraphQL so trailing commas are allowed and repeated commas do not represent missing values.

**Semantics**

<div class="spec-semantic"><span class="spec-nt">[ListValue](#ListValue)</span>

<div class="spec-rhs"><span class="spec-t">[</span><span class="spec-t">]</span></div>

1.  Return a new empty list value.

</div>

<div class="spec-semantic"><span class="spec-nt">[ListValue](#ListValue)</span>

<div class="spec-rhs"><span class="spec-t">[</span><span class="spec-nt list">[Value](#Value)<span class="spec-mods"><span class="spec-mod list">list</span></span></span><span class="spec-t">]</span></div>

1.  Let <var>inputList</var> be a new empty list value.
2.  For each <span class="spec-nt list">[Value](#Value)<span class="spec-mods"><span class="spec-mod list">list</span></span></span>
    1.  Let <var>value</var> be the result of evaluating <span class="spec-nt">[Value](#Value)</span>.
    2.  Append <var>value</var> to <var>inputList</var>.
3.  Return <var>inputList</var>

</div>



<section id="sec-Input-Object-Values">

##### <span class="spec-secid" title="link to this section">[2.2.7.7](#sec-Input-Object-Values)</span>Input Object Values

<div class="spec-production" id="ObjectValue"><span class="spec-nt">[ObjectValue](#ObjectValue)<span class="spec-mods"><span class="spec-params"><span class="spec-param">Const</span></span></span></span>

<div class="spec-rhs"><span class="spec-t">{</span><span class="spec-t">}</span></div>

<div class="spec-rhs"><span class="spec-t">{</span><span class="spec-nt list">[ObjectField](#ObjectField)<span class="spec-mods"><span class="spec-params"><span class="spec-param conditional">Const</span></span><span class="spec-mod list">list</span></span></span><span class="spec-t">}</span></div>

</div>

<div class="spec-production" id="ObjectField"><span class="spec-nt">[ObjectField](#ObjectField)<span class="spec-mods"><span class="spec-params"><span class="spec-param">Const</span></span></span></span>

<div class="spec-rhs"><span class="spec-nt">[Name](#Name)</span><span class="spec-t">:</span><span class="spec-nt">[Value](#Value)<span class="spec-mods"><span class="spec-params"><span class="spec-param conditional">Const</span></span></span></span></div>

</div>

Input object literal values are unordered lists of keyed input values wrapped in curly‐braces `{ }`. The values of an object literal may be any input value literal or variable (ex. `{ name: "Hello world", score: 1.0 }`). We refer to literal representation of input objects as “object literals.”

**Semantics**

<div class="spec-semantic"><span class="spec-nt">[ObjectValue](#ObjectValue)</span>

<div class="spec-rhs"><span class="spec-t">{</span><span class="spec-t">}</span></div>

1.  Return a new input object value with no fields.

</div>

<div class="spec-semantic"><span class="spec-nt">[ObjectValue](#ObjectValue)</span>

<div class="spec-rhs"><span class="spec-t">{</span><span class="spec-nt list">[ObjectField](#ObjectField)<span class="spec-mods"><span class="spec-mod list">list</span></span></span><span class="spec-t">}</span></div>

1.  Let <var>inputObject</var> be a new input object value with no fields.
2.  For each <var>field</var> in <span class="spec-nt list">[ObjectField](#ObjectField)<span class="spec-mods"><span class="spec-mod list">list</span></span></span>
    1.  Let <var>name</var> be <span class="spec-nt">[Name](#Name)</span> in <var>field</var>.
    2.  If <var>inputObject</var> contains a field named <var>name</var> throw Syntax Error.
    3.  Let <var>value</var> be the result of evaluating <span class="spec-nt">[Value](#Value)</span> in <var>field</var>.
    4.  Add a field to <var>inputObject</var> of name <var>name</var> containing value <var>value</var>.
3.  Return <var>inputObject</var>

</div>





<section id="sec-Language.Query-Document.Variables">

#### <span class="spec-secid" title="link to this section">[2.2.8](#sec-Language.Query-Document.Variables)</span>Variables

<div class="spec-production" id="Variable"><span class="spec-nt">[Variable](#Variable)</span>

<div class="spec-rhs"><span class="spec-t">$</span><span class="spec-nt">[Name](#Name)</span></div>

</div>

<div class="spec-production" id="VariableDefinitions"><span class="spec-nt">[VariableDefinitions](#VariableDefinitions)</span>

<div class="spec-rhs"><span class="spec-t">(</span><span class="spec-nt list">[VariableDefinition](#VariableDefinition)<span class="spec-mods"><span class="spec-mod list">list</span></span></span><span class="spec-t">)</span></div>

</div>

<div class="spec-production" id="VariableDefinition"><span class="spec-nt">[VariableDefinition](#VariableDefinition)</span>

<div class="spec-rhs"><span class="spec-nt">[Variable](#Variable)</span><span class="spec-t">:</span><span class="spec-nt">[Type](#Type)</span><span class="spec-nt optional">[DefaultValue](#DefaultValue)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span></div>

</div>

<div class="spec-production" id="DefaultValue"><span class="spec-nt">[DefaultValue](#DefaultValue)</span>

<div class="spec-rhs"><span class="spec-t">=</span><span class="spec-nt">[Value](#Value)<span class="spec-mods"><span class="spec-params"><span class="spec-param">Const</span></span></span></span></div>

</div>

A GraphQL query can be parameterized with variables, maximizing query reuse, and avoiding costly string building in clients at runtime.

If not defined as constant (for example, in <span class="spec-nt">[DefaultValue](#DefaultValue)</span>), a <span class="spec-nt">[Variable](#Variable)</span> can be supplied for an input value.

Variables must be defined at the top of an operation and are in scope throughout the execution of that operation.

In this example, we want to fetch a profile picture size based on the size of a particular device:

```
query getZuckProfile($devicePicSize: Int) {
  user(id: 4) {
    id
    name
    profilePic(size: $devicePicSize)
  }
}

```

Values for those variables are provided to a GraphQL service along with a request so they may be substituted during execution. If providing JSON for the variables’ values, we could run this query and request profilePic of size `60` width:

```
{
  "devicePicSize": 60
}

```

<section id="sec-Variable-use-within-Fragments">

##### <span class="spec-secid" title="link to this section">[2.2.8.1](#sec-Variable-use-within-Fragments)</span>Variable use within Fragments

Query variables can be used within fragments. Query variables have global scope with a given operation, so a variable used within a fragment must be declared in any top‐level operation that transitively consumes that fragment. If a variable is referenced in a fragment and is included by an operation that does not define that variable, the operation cannot be executed.





<section id="sec-Input-Types">

#### <span class="spec-secid" title="link to this section">[2.2.9](#sec-Input-Types)</span>Input Types

<div class="spec-production" id="Type"><span class="spec-nt">[Type](#Type)</span>

<div class="spec-rhs"><span class="spec-nt">[NamedType](#NamedType)</span></div>

<div class="spec-rhs"><span class="spec-nt">[ListType](#ListType)</span></div>

<div class="spec-rhs"><span class="spec-nt">[NonNullType](#NonNullType)</span></div>

</div>

<div class="spec-production" id="NamedType"><span class="spec-nt">[NamedType](#NamedType)</span>

<div class="spec-rhs"><span class="spec-nt">[Name](#Name)</span></div>

</div>

<div class="spec-production" id="ListType"><span class="spec-nt">[ListType](#ListType)</span>

<div class="spec-rhs"><span class="spec-t">[</span><span class="spec-nt">[Type](#Type)</span><span class="spec-t">]</span></div>

</div>

<div class="spec-production" id="NonNullType"><span class="spec-nt">[NonNullType](#NonNullType)</span>

<div class="spec-rhs"><span class="spec-nt">[NamedType](#NamedType)</span><span class="spec-t">!</span></div>

<div class="spec-rhs"><span class="spec-nt">[ListType](#ListType)</span><span class="spec-t">!</span></div>

</div>

GraphQL describes the types of data expected by query variables. Input types may be lists of another input type, or a non‐null variant of any other input type.

**Semantics**

<div class="spec-semantic"><span class="spec-nt">[Type](#Type)</span>

<div class="spec-rhs"><span class="spec-nt">[Name](#Name)</span></div>

1.  Let <var>name</var> be the string value of <span class="spec-nt">[Name](#Name)</span>
2.  Let <var>type</var> be the type defined in the Schema named <var>name</var>
3.  <var>type</var> must not be <span class="spec-keyword">null</span>
4.  Return <var>type</var>

</div>

<div class="spec-semantic"><span class="spec-nt">[Type](#Type)</span>

<div class="spec-rhs"><span class="spec-t">[</span><span class="spec-nt">[Type](#Type)</span><span class="spec-t">]</span></div>

1.  Let <var>itemType</var> be the result of evaluating <span class="spec-nt">[Type](#Type)</span>
2.  Let <var>type</var> be a List type where <var>itemType</var> is the contained type.
3.  Return <var>type</var>

</div>

<div class="spec-semantic"><span class="spec-nt">[Type](#Type)</span>

<div class="spec-rhs"><span class="spec-nt">[Type](#Type)</span><span class="spec-t">!</span></div>

1.  Let <var>nullableType</var> be the result of evaluating <span class="spec-nt">[Type](#Type)</span>
2.  Let <var>type</var> be a Non‐Null type where <var>nullableType</var> is the contained type.
3.  Return <var>type</var>

</div>



<section id="sec-Language.Query-Document.Directives">

#### <span class="spec-secid" title="link to this section">[2.2.10](#sec-Language.Query-Document.Directives)</span>Directives

<div class="spec-production" id="Directives"><span class="spec-nt">[Directives](#Directives)</span>

<div class="spec-rhs"><span class="spec-nt list">[Directive](#Directive)<span class="spec-mods"><span class="spec-mod list">list</span></span></span></div>

</div>

<div class="spec-production" id="Directive"><span class="spec-nt">[Directive](#Directive)</span>

<div class="spec-rhs"><span class="spec-t">@</span><span class="spec-nt">[Name](#Name)</span><span class="spec-nt optional">[Arguments](#Arguments)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span></div>

</div>

Directives provide a way to describe alternate runtime execution and type validation behavior in a GraphQL document.

In some cases, you need to provide options to alter GraphQL’s execution behavior in ways field arguments will not suffice, such as conditionally including or skipping a field. Directives provide this by describing additional information to the executor.

Directives have a name along with a list of arguments which may accept values of any input type.

Directives can be used to describe additional information for fields, fragments, and operations.

As future versions of GraphQL adopts new configurable execution capabilities, they may be exposed via directives.

<section id="sec-Fragment-Directives">

##### <span class="spec-secid" title="link to this section">[2.2.10.1](#sec-Fragment-Directives)</span>Fragment Directives

Fragments may include directives to alter their behavior. At runtime, the directives provided on a fragment spread override those described on the definition.

For example, the following query:

```
query hasConditionalFragment($condition: Boolean) {
  ...maybeFragment @include(if: $condition)
}

fragment maybeFragment on Query {
  me {
    name
  }
}

```

Will have identical runtime behavior as

```
query hasConditionalFragment($condition: Boolean) {
  ...maybeFragment
}

fragment maybeFragment on Query @include(if: $condition) {
  me {
    name
  }
}

```

<div class="spec-algo" id="FragmentSpreadDirectives()"><span class="spec-call">[FragmentSpreadDirectives](#FragmentSpreadDirectives())(<var>fragmentSpread</var>)</span>

1.  Let <var>directives</var> be the set of directives on <var>fragmentSpread</var>
2.  Let <var>fragmentDefinition</var> be the FragmentDefinition in the document named <var>fragmentSpread</var> refers to.
3.  For each <var>directive</var> in directives on <var>fragmentDefinition</var>
    1.  If <var>directives</var> does not contain a directive named <var>directive</var>.
    2.  Add <var>directive</var> into <var>directives</var>
4.  Return <var>directives</var>

</div>









<section id="sec-Type-System">

## <span class="spec-secid" title="link to this section">[3](#sec-Type-System)</span>Type System

The GraphQL Type system describes the capabilities of a GraphQL server and is used to determine if a query is valid. The type system also describes the input types of query variables to determine if values provided at runtime are valid.

A GraphQL server’s capabilities are referred to as that server’s “schema”. A schema is defined in terms of the types and directives it supports.

A given GraphQL schema must itself be internally valid. This section describes the rules for this validation process where relevant.

A GraphQL schema is represented by a root type for each kind of operation: query and mutation; this determines the place in the type system where those operations begin.

All types within a GraphQL schema must have unique names. No two provided types may have the same name. No provided type may have a name which conflicts with any built in types (including Scalar and Introspection types).

All directives within a GraphQL schema must have unique names. A directive and a type may share the same name, since there is no ambiguity between them.

<section id="sec-Types">

### <span class="spec-secid" title="link to this section">[3.1](#sec-Types)</span>Types

The fundamental unit of any GraphQL Schema is the type. There are eight kinds of types in GraphQL.

The most basic type is a `Scalar`. A scalar represents a primitive value, like a string or an integer. Oftentimes, the possible responses for a scalar field are enumerable. GraphQL offers an `Enum` type in those cases, where the type specifies the space of valid responses.

Scalars and Enums form the leaves in response trees; the intermediate levels are `Object` types, which define a set of fields, where each field is another type in the system, allowing the definition of arbitrary type hierarchies.

GraphQL supports two abstract types: interfaces and unions.

An `Interface` defines a list of fields; `Object` types that implement that interface are guaranteed to implement those fields. Whenever the type system claims it will return an interface, it will return a valid implementing type.

A `Union` defines a list of possible types; similar to interfaces, whenever the type system claims a union will be returned, one of the possible types will be returned.

All of the types so far are assumed to be both nullable and singular: e.g. a scalar string returns either null or a singular string. The type system might want to define that it returns a list of other types; the `List` type is provided for this reason, and wraps another type. Similarly, the `Non-Null` type wraps another type, and denotes that the result will never be null. These two types are referred to as “wrapping types”; non‐wrapping types are referred to as “base types”. A wrapping type has an underlying “base type”, found by continually unwrapping the type until a base type is found.

Finally, oftentimes it is useful to provide complex structs as inputs to GraphQL queries; the `Input Object` type allows the schema to define exactly what data is expected from the client in these queries.

<section id="sec-Scalars">

#### <span class="spec-secid" title="link to this section">[3.1.1](#sec-Scalars)</span>Scalars

As expected by the name, a scalar represents a primitive value in GraphQL. GraphQL responses take the form of a hierarchical tree; the leaves on these trees are GraphQL scalars.

All GraphQL scalars are representable as strings, though depending on the response format being used, there may be a more appropriate primitive for the given scalar type, and server should use those types when appropriate.

GraphQL provides a number of built‐in scalars, but type systems can add additional scalars with semantic meaning. For example, a GraphQL system could define a scalar called `Time` which, while serialized as a string, promises to conform to ISO‐8601\. When querying a field of type `Time`, you can then rely on the ability to parse the result with an ISO‐8601 parser and use a client‐specific primitive for time. Another example of a potentially useful custom scalar is `Url`, which serializes as a string, but is guaranteed by the server to be a valid URL.

**Result Coercion**

A GraphQL server, when preparing a field of a given scalar type, must uphold the contract the scalar type describes, either by coercing the value or producing an error.

For example, a GraphQL server could be preparing a field with the scalar type `Int` and encounter a floating‐point number. Since the server must not break the contract by yielding a non‐integer, the server should truncate the fractional value and only yield the integer value. If the server encountered a boolean `true` value, it should return `1`. If the server encountered a string, it may attempt to parse the string for a base‐10 integer value. If the server encounters some value that cannot be reasonably coerced to an `Int`, then it must raise a field error.

Since this coercion behavior is not observable to clients of the GraphQL server, the precise rules of coercion are left to the implementation. The only requirement is that the server must yield values which adhere to the expected Scalar type.

**Input Coercion**

If a GraphQL server expects a scalar type as input to an argument, coercion is observable and the rules must be well defined. If an input value does not match a coercion rule, a query error must be raised.

GraphQL has different constant literals to represent integer and floating‐point input values, and coercion rules may apply differently depending on which type of input value is encountered. GraphQL may be parameterized by query variables, the values of which are often serialized when sent over a transport like HTTP. Since some common serializations (ex. JSON) do not discriminate between integer and floating‐point values, they are interpreted as an integer input value if they have an empty fractional part (ex. `1.0`) and otherwise as floating‐point input value.

<section id="sec-Built-in-Scalars">

##### <span class="spec-secid" title="link to this section">[3.1.1.1](#sec-Built-in-Scalars)</span>Built-in Scalars

GraphQL provides a basic set of well‐defined Scalar types. A GraphQL server should support all of these types, and a GraphQL server which provide a type by these names must adhere to the behavior described below.

<section id="sec-Int">

###### <span class="spec-secid" title="link to this section">[3.1.1.1.1](#sec-Int)</span>Int

The Int scalar type represents a signed 32‐bit numeric non‐fractional values. Response formats that support a 32‐bit integer or a number type should use that type to represent this scalar.

**Result Coercion**

GraphQL servers should coerce non‐int raw values to Int when possible otherwise they must raise a field error. Examples of this may include returning `1` for the floating‐point number `1.0`, or `2` for the string `"2"`.

**Input Coercion**

When expected as an input type, only integer input values are accepted. All other input values, including strings with numeric content, must raise a query error indicating an incorrect type. If the integer input value represents a value less than -2<sup>31</sup> or greater than or equal to 2<sup>31</sup>, a query error should be raised.

<div class="spec-note">Numeric integer values larger than 32‐bit should either use String or a custom‐defined Scalar type, as not all platforms and transports support encoding integer numbers larger than 32‐bit.</div>



<section id="sec-Float">

###### <span class="spec-secid" title="link to this section">[3.1.1.1.2](#sec-Float)</span>Float

The Float scalar type represents signed double‐precision fractional values as specified by [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point). Response formats that support an appropriate double‐precision number type should use that type to represent this scalar.

**Result Coercion**

GraphQL servers should coerce non‐floating‐point raw values to Float when possible otherwise they must raise a field error. Examples of this may include returning `1.0` for the integer number `1`, or `2.0` for the string `"2"`.

**Input Coercion**

When expected as an input type, both integer and float input values are accepted. Integer input values are coerced to Float by adding an empty fractional part, for example `1.0` for the integer input value `1`. All other input values, including strings with numeric content, must raise a query error indicating an incorrect type. If the integer input value represents a value not representable by IEEE 754, a query error should be raised.



<section id="sec-String">

###### <span class="spec-secid" title="link to this section">[3.1.1.1.3](#sec-String)</span>String

The String scalar type represents textual data, represented as UTF‐8 character sequences. The String type is most often used by GraphQL to represent free‐form human‐readable text. All response formats must support string representations, and that representation must be used here.

**Result Coercion**

GraphQL servers should coerce non‐string raw values to String when possible otherwise they must raise a field error. Examples of this may include returning the string `"true"` for a boolean true value, or the string `"1"` for the integer `1`.

**Input Coercion**

When expected as an input type, only valid UTF‐8 string input values are accepted. All other input values must raise a query error indicating an incorrect type.



<section id="sec-Boolean">

###### <span class="spec-secid" title="link to this section">[3.1.1.1.4](#sec-Boolean)</span>Boolean

The Boolean scalar type represents `true` or `false`. Response formats should use a built‐in boolean type if supported; otherwise, they should use their representation of the integers `1` and `0`.

**Result Coercion**

GraphQL servers should coerce non‐boolean raw values to Boolean when possible otherwise they must raise a field error. Examples of this may include returning `true` for any non‐zero number.

**Input Coercion**

When expected as an input type, only boolean input values are accepted. All other input values must raise a query error indicating an incorrect type.



<section id="sec-ID">

###### <span class="spec-secid" title="link to this section">[3.1.1.1.5](#sec-ID)</span>ID

The ID scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type is serialized in the same way as a `String`; however, it is not intended to be human‐readable. While it is often numeric, it should always serialize as a `String`.

**Result Coercion**

GraphQL is agnostic to ID format, and serializes to string to ensure consistency across many formats ID could represent, from small auto‐increment numbers, to large 128‐bit random numbers, to base64 encoded values, or string values of a format like [GUID](http://en.wikipedia.org/wiki/Globally_unique_identifier).

GraphQL servers should coerce as appropriate given the ID formats they expect, when coercion is not possible they must raise a field error.

**Input Coercion**

When expected as an input type, any string (such as `"4"`) or integer (such as `4`) input value should be coerced to ID as appropriate for the ID formats a given GraphQL server expects. Any other input value, including float input values (such as `4.0`), must raise a query error indicating an incorrect type.







<section id="sec-Objects">

#### <span class="spec-secid" title="link to this section">[3.1.2](#sec-Objects)</span>Objects

GraphQL queries are hierarchical and composed, describing a tree of information. While Scalar types describe the leaf values of these hierarchical queries, Objects describe the intermediate levels.

GraphQL Objects represent a list of named fields, each of which yield a value of a specific type. Object values are serialized as unordered maps, where the queried field names (or aliases) are the keys and the result of evaluating the field is the value.

For example, a type `Person` could be described as:

```
type Person {
  name: String
  age: Int
  picture: Url
}

```

Where `name` is a field that will yield a `String` value, and `age` is a field that will yield an `Int` value, and `picture` a field that will yield a `Url` value.

A query of an object value must select at least one field. This selection of fields will yield an unordered map containing exactly the subset of the object queried. Only fields that are declared on the object type may validly be queried on that object.

For example, selecting all the fields of `Person`:

```
{
  name
  age
  picture
}

```

Would yield the object:

```
{
  "name": "Mark Zuckerberg",
  "age": 30,
  "picture": "http://some.cdn/picture.jpg"
}

```

While selecting a subset of fields:

```
{
  name
  age
}

```

Must only yield exactly that subset:

```
{
  "name": "Mark Zuckerberg",
  "age": 30
}

```

A field of an Object type may be a Scalar, Enum, another Object type, an Interface, or a Union. Additionally, it may be any wrapping type whose underlying base type is one of those five.

For example, the `Person` type might include a `relationship`:

```
type Person {
  name: String
  age: Int
  picture: Url
  relationship: Person
}

```

Valid queries must supply a nested field set for a field that returns an object, so this query is not valid:

```
{
  name
  relationship
}

```

However, this example is valid:

```
{
  name
  relationship {
    name
  }
}

```

And will yield the subset of each object type queried:

```
{
  "name": "Mark Zuckerberg",
  "relationship": {
    "name": "Priscilla Chan"
  }
}

```

**Result Coercion**

Determining the result of coercing an object is the heart of the GraphQL executor, so this is covered in that section of the spec.

**Input Coercion**

Objects are never valid inputs.

<section id="sec-Object-Field-Arguments">

##### <span class="spec-secid" title="link to this section">[3.1.2.1](#sec-Object-Field-Arguments)</span>Object Field Arguments

Object fields are conceptually functions which yield values. Occasionally object fields can accept arguments to further specify the return value. Object field arguments are defined as a list of all possible argument names and their expected input types.

For example, a `Person` type with a `picture` field could accept an argument to determine what size of an image to return.

```
type Person {
  name: String
  picture(size: Int): Url
}

```

GraphQL queries can optionally specify arguments to their fields to provide these arguments.

This example query:

```
{
  name
  picture(size: 600)
}

```

May yield the result:

```
{
  "name": "Mark Zuckerberg",
  "picture": "http://some.cdn/picture_600.jpg"
}

```

The type of an object field argument can be any Input type.



<section id="sec-Object-Field-deprecation">

##### <span class="spec-secid" title="link to this section">[3.1.2.2](#sec-Object-Field-deprecation)</span>Object Field deprecation

Fields in an object may be marked as deprecated as deemed necessary by the application. It is still legal to query for these fields (to ensure existing clients are not broken by the change), but the fields should be appropriately treated in documentation and tooling.



<section id="sec-Object-type-validation">

##### <span class="spec-secid" title="link to this section">[3.1.2.3](#sec-Object-type-validation)</span>Object type validation

Object types have the potential to be invalid if incorrectly defined. This set of rules must be adhered to by every Object type in a GraphQL schema.

1.  The fields of an Object type must have unique names within that Object type; no two fields may share the same name.
2.  An object type must be a super‐set of all interfaces it implements.
    1.  The object type must include a field of the same name for every field defined in an interface.
        1.  The object field must include an argument of the same name for every argument defined by the interface field.
            1.  The object field argument must accept the same type (invariant) as the interface field argument.
        2.  The object field must be of a type which is equal to the interface field.





<section id="sec-Interfaces">

#### <span class="spec-secid" title="link to this section">[3.1.3](#sec-Interfaces)</span>Interfaces

GraphQL Interfaces represent a list of named fields and their arguments. GraphQL object can then implement an interface, which guarantees that they will contain the specified fields.

Fields on a GraphQL interface have the same rules as fields on a GraphQL object; their type can be Scalar, Object, Enum, Interface, or Union, or any wrapping type whose base type is one of those five.

For example, an interface may describe a required field and types such as `Person` or `Business` may then implement this interface.

```
interface NamedEntity {
  name: String
}

type Person : NamedEntity {
  name: String
  age: Int
}

type Business : NamedEntity {
  name: String
  employeeCount: Int
}

```

Fields which yield an interface are useful when one of many Object types are expected, but some fields should be guaranteed.

To continue the example, a `Contact` might refer to `NamedEntity`.

```
type Contact {
  entity: NamedEntity
  phoneNumber: String
  address: String
}

```

This allows us to write a query for a `Contact` that can select the common fields.

```
{
  entity {
    name
  }
  phoneNumber
}

```

When querying for fields on an interface type, only those fields declared on the interface may be queried. In the above example, `entity` returns a `NamedEntity`, and `name` is defined on `NamedEntity`, so it is valid. However, the following would not be a valid query:

```
{
  entity {
    name
    age
  }
  phoneNumber
}

```

because `entity` refers to a `NamedEntity`, and `age` is not defined on that interface. Querying for `age` is only valid when the result of `entity` is a `Person`; the query can express this using a fragment or an inline fragment:

```
{
  entity {
    name
    ... on Person {
      age
    }
  },
  phoneNumber
}

```

**Result Coercion**

The interface type should have some way of determining which object a given result corresponds to. Once it has done so, the result coercion of the interface is the same as the result coercion of the object.

**Input Coercion**

Interfaces are never valid inputs.

<section id="sec-Interface-type-validation">

##### <span class="spec-secid" title="link to this section">[3.1.3.1](#sec-Interface-type-validation)</span>Interface type validation

Interface types have the potential to be invalid if incorrectly defined.

1.  The fields of an Interface type must have unique names within that Interface type; no two fields may share the same name.





<section id="sec-Unions">

#### <span class="spec-secid" title="link to this section">[3.1.4](#sec-Unions)</span>Unions

GraphQL Unions represent an object that could be one of a list of GraphQL Object types, but provides for no guaranteed fields between those types. They also differ from interfaces in that Object types declare what interfaces they implement, but are not aware of what unions contain them.

With interfaces and objects, only those fields defined on the type can be queried directly; to query other fields on an interface, typed fragments must be used. This is the same as for unions, but unions do not define any fields, so **no** fields may be queried on this type without the use of typed fragments.

For example, we might have the following type system:

```
Union SearchResult = Photo | Person

type Person {
  name: String
  age: Int
}

type Photo {
  height: Int
  width: Int
}

type SearchQuery {
  firstSearchResult: SearchResult
}

```

When querying the `firstSearchResult` field of type `SearchQuery`, the query would ask for all fields inside of a fragment indicating the appropriate type. If the query wanted the name if the result was a Person, and the height if it was a photo, the following query is invalid, because the union itself defines no fields:

```
{
  firstSearchResult {
    name
    height
  }
}

```

Instead, the query would be:

```
{
  firstSearchResult {
    ... on Person {
      name
    }
    ... on Photo {
      height
    }
  }
}

```

**Result Coercion**

The union type should have some way of determining which object a given result corresponds to. Once it has done so, the result coercion of the union is the same as the result coercion of the object.

**Input Coercion**

Unions are never valid inputs.

<section id="sec-Union-type-validation">

##### <span class="spec-secid" title="link to this section">[3.1.4.1](#sec-Union-type-validation)</span>Union type validation

Union types have the potential to be invalid if incorrectly defined.

1.  The member types of an Union type must all be Object base types; Scalar, Interface and Union types may not be member types of a Union. Similarly, wrapping types may not be member types of a Union.
2.  A Union type must define two or more member types.





<section id="sec-Enums">

#### <span class="spec-secid" title="link to this section">[3.1.5](#sec-Enums)</span>Enums

GraphQL Enums are a variant on the Scalar type, which represents one of a finite set of possible values.

GraphQL Enums are not references for a numeric value, but are unique values in their own right. They serialize as a string: the name of the represented value.

**Result Coercion**

GraphQL servers must return one of the defined set of possible values, if a reasonable coercion is not possible they must raise a field error.

**Input Coercion**

GraphQL has a constant literal to represent enum input values. GraphQL string literals must not be accepted as an enum input and instead raise a query error.

Query variable transport serializations which have a different representation for non‐string symbolic values (for example, [EDN](https://github.com/edn-format/edn)) should only allow such values as enum input values. Otherwise, for most transport serializations that do not, strings may be interpreted as the enum input value with the same name.



<section id="sec-Input-Objects">

#### <span class="spec-secid" title="link to this section">[3.1.6](#sec-Input-Objects)</span>Input Objects

Fields can define arguments that the client passes up with the query, to configure their behavior. These inputs can be Strings or Enums, but they sometimes need to be more complex than this.

The `Object` type defined above is inappropriate for re‐use here, because `Object`s can contain fields that express circular references or references to interfaces and unions, neither of which is appropriate for use as an input argument. For this reason, input objects have a separate type in the system.

An `Input Object` defines a set of input fields; the input fields are either scalars, enums, or other input objects. This allows arguments to accept arbitrarily complex structs.

**Result Coercion**

An input object is never a valid result.

**Input Coercion**

The input to an input object should be an unordered map, otherwise an error should be thrown. The result of the coercion is an unordered map, with an entry for each input field, whose key is the name of the input field. The value of an entry in the coerced map is the result of input coercing the value of the entry in the input with the same key; if the input does not have a corresponding entry, the value is the result of coercing null. The input coercion above should be performed according to the input coercion rules of the type declared by the input field.



<section id="sec-Lists">

#### <span class="spec-secid" title="link to this section">[3.1.7](#sec-Lists)</span>Lists

A GraphQL list is a special collection type which declares the type of each item in the List (referred to as the _item type_ of the list). List values are serialized as ordered lists, where each item in the list is serialized as per the item type. To denote that a field uses a List type the item type is wrapped in square brackets like this: `pets: [Pet]`.

**Result Coercion**

GraphQL servers must return an ordered list as the result of a list type. Each item in the list must be the result of a result coercion of the item type. If a reasonable coercion is not possible they must raise a field error. In particular, if a non‐list is returned, the coercion should fail, as this indicates a mismatch in expectations between the type system and the implementation.

**Input Coercion**

When expected as an input, list values are accepted only when each item in the list can be accepted by the list’s item type.

If the value passed as an input to a list type is _not_ as list, it should be coerced as though the input was a list of size one, where the value passed is the only item in the list. This is to allow inputs that accept a “var args” to declare their input type as a list; if only one argument is passed (a common case), the client can just pass that value rather than constructing the list.



<section id="sec-Non-Null">

#### <span class="spec-secid" title="link to this section">[3.1.8](#sec-Non-Null)</span>Non-Null

By default, all types in GraphQL are nullable; the <span class="spec-keyword">null</span> value is a valid response for all of the above types. To declare a type that disallows null, the GraphQL Non‐Null type can be used. This type declares an underlying type, and this type acts identically to that underlying type, with the exception that `null` is not a valid response for the wrapping type. A trailing exclamation mark is used to denote a field that uses a Non‐Null type like this: `name: String!`.

**Result Coercion**

In all of the above result coercion, `null` was considered a valid value. To coerce the result of a Non Null type, the result coercion of the underlying type should be performed. If that result was not `null`, then the result of coercing the Non Null type is that result. If that result was `null`, then an error should be raised.

**Input Coercion**

<div class="spec-note">that `null` is not a value in GraphQL, so a query cannot look like:</div>

```
{
  field(arg: null)
}

```

to indicate that the argument is null. Instead, an argument would be null only if it is omitted:

```
{
  field
}

```

Or if passed a variable of a nullable type that at runtime was not provided a value:

```
query withNullableVariable($var: String) {
  field(arg: $var)
}

```

Hence, if the value for a Non Null type is hard‐coded in the query, it is always coerced using the input coercion for the wrapped type.

When a Non Null input has its value set using a variable, the coerced value should be `null` if the provided value is `null`-like in the provided representation, or if the provided value is omitted. Otherwise, the coerced value is the result of running the wrapped type’s input coercion on the provided value.





<section id="sec-Type-System.Directives">

### <span class="spec-secid" title="link to this section">[3.2](#sec-Type-System.Directives)</span>Directives

A GraphQL schema includes a list of the directives the execution engine supports.

GraphQL implementations should provide the `@skip` and `@include` directives.

<section id="sec--skip">

#### <span class="spec-secid" title="link to this section">[3.2.1](#sec--skip)</span>@skip

The `@skip` directive may be provided for fields or fragments, and allows for conditional exclusion during execution as described by the if argument.

In this example `experimentalField` will be queried only if the `$someTest` is provided a `false` value.

```
query myQuery($someTest: Boolean) {
  experimentalField @skip(if: $someTest)
}

```



<section id="sec--include">

#### <span class="spec-secid" title="link to this section">[3.2.2](#sec--include)</span>@include

The `@include` directive may be provided for fields or fragments, and allows for conditional inclusion during execution as described by the if argument.

In this example `experimentalField` will be queried only if the `$someTest` is provided a `true` value.

```
query myQuery($someTest: Boolean) {
  experimentalField @include(if: $someTest)
}

```

The `@skip` directive has precedence over the `@include` directive should both be provided in the same context.





<section id="sec-Starting-types">

### <span class="spec-secid" title="link to this section">[3.3](#sec-Starting-types)</span>Starting types

A GraphQL schema includes types, indicating where query and mutation operations start. This provides the initial entry points into the type system. The query type must always be provided, and is an Object base type. The mutation type is optional; if it is null, that means the system does not support mutations. If it is provided, it must be an object base type.

The fields on the query type indicate what fields are available at the top level of a GraphQL query. For example, a basic GraphQL query like this one:

```
query getMe {
  me
}

```

Is valid when the type provided for the query starting type has a field named “me”. Similarly

```
mutation setName {
  setName(name: "Zuck") {
    newName
  }
}

```

Is valid when the type provided for the mutation starting type is not null, and has a field named “setName” with a string argument named “name”.





<section id="sec-Introspection">

## <span class="spec-secid" title="link to this section">[4](#sec-Introspection)</span>Introspection

A GraphQL server supports introspection over its schema. This schema is queried using GraphQL itself, creating a powerful platform for tool‐building.

Take an example query for a trivial app. In this case there is a User type with three fields: id, user, and birthday.

For example, given a server with the following type definition:

```
type User {
  id: String
  name: String
  birthday: Date
}

```

The query

```
{
  __type(name: "User") {
    name
    fields {
      name
      type {
        name
      }
    }
  }
}

```

would return

```
{
  "__type": {
    "name" : "User",
    "fields": [
      {
        "name": "id",
        "type": { "name": "String" }
      },
      {
        "name": "name",
        "type": { "name": "String" }
      },
      {
        "name": "birthday",
        "type": { "name": "Date" }
      },
    ]
  }
}

```

<section id="sec-General-Principles">

### <span class="spec-secid" title="link to this section">[4.1](#sec-General-Principles)</span>General Principles

<section id="sec-Naming-conventions">

#### <span class="spec-secid" title="link to this section">[4.1.1](#sec-Naming-conventions)</span>Naming conventions

Types and fields required by the GraphQL introspection system that are used in the same context as user‐defined type and fields are prefixed with two underscores. This in order to avoid naming collisions with user‐defined GraphQL types. Conversely, GraphQL type system authors must not define any types, fields, arguments, or any other type system artifact with two leading underscores.



<section id="sec-Documentation">

#### <span class="spec-secid" title="link to this section">[4.1.2](#sec-Documentation)</span>Documentation

All types in the introspection system provide a `description` field of type `String` to allow type designers to publish documentation in addition to capabilities. A GraphQL server may return the `description` field using Markdown syntax. Therefore it is recommended that any tool that displays description use a Markdown renderer.



<section id="sec-Deprecation">

#### <span class="spec-secid" title="link to this section">[4.1.3](#sec-Deprecation)</span>Deprecation

To support the management of backwards compatibility, GraphQL fields and enum values can indicate whether or not they are deprecated (`isDeprecated: Boolean`) and a description of why it is deprecated (`deprecationReason: String`).

Tools built using GraphQL introspection should respect deprecation by discouraging deprecated use through information hiding or developer‐facing warnings.



<section id="sec-Type-Name-Introspection">

#### <span class="spec-secid" title="link to this section">[4.1.4](#sec-Type-Name-Introspection)</span>Type Name Introspection

GraphQL supports type name introspection at any point within a query by the meta field `__typename: String!` when querying against any Object, Interface, or Union. It returns the name of the object type currently being queried.

This is most often used when querying against Interface or Union types to identify which actual type of the possible types has been returned.

This field is implicit and does not appear in the fields list in any defined type.





<section id="sec-Schema-Introspection">

### <span class="spec-secid" title="link to this section">[4.2](#sec-Schema-Introspection)</span>Schema Introspection

The schema introspection system is accessible from the meta‐fields `__schema` and `__type` which are accessible from the type of the root of a query operation.

```
__schema : __Schema!
__type(name: String!) : __Type

```

These fields are implicit and do not appear in the fields list in the root type of the query operation.

The schema of the GraphQL schema introspection system:

```
type __Schema {
  types: [__Type!]!
  queryType: __Type!
  mutationType: __Type
  directives: [__Directive!]!
}

type __Type {
  kind: __TypeKind!
  name: String
  description: String

  # OBJECT and INTERFACE only
  fields(includeDeprecated: Boolean = false): [__Field!]

  # OBJECT only
  interfaces: [__Type!]

  # INTERFACE and UNION only
  possibleTypes: [__Type!]

  # ENUM only
  enumValues(includeDeprecated: Boolean = false): [__EnumValue!]

  # INPUT_OBJECT only
  inputFields: [__InputValue!]

  # NON_NULL and LIST only
  ofType: __Type
}

type __Field {
  name: String!
  description: String
  args: [__InputValue!]!
  type: __Type!
  isDeprecated: Boolean!
  deprecationReason: String
}

type __InputValue {
  name: String!
  description: String
  type: __Type!
  defaultValue: String
}

type __EnumValue {
  name: String!
  description: String
  isDeprecated: Boolean!
  deprecationReason: String
}

enum __TypeKind {
  SCALAR
  OBJECT
  INTERFACE
  UNION
  ENUM
  INPUT_OBJECT
  LIST
  NON_NULL
}

type __Directive {
  name: String!
  description: String
  args: [__InputValue!]!
  onOperation: Boolean!
  onFragment: Boolean!
  onField: Boolean!
}

```

<section id="sec-The-__Type-Type">

#### <span class="spec-secid" title="link to this section">[4.2.1](#sec-The-__Type-Type)</span>The "__Type" Type

`__Type` is at the core of the type introspection system. It represents scalars, interfaces, object types, unions, enums in the system.

`__Type` also represents type modifiers, which are used to modify a type that it refers to (`ofType: __Type`). This is how we represent lists, non‐nullable types, and the combinations thereof.



<section id="sec-Type-Kinds">

#### <span class="spec-secid" title="link to this section">[4.2.2](#sec-Type-Kinds)</span>Type Kinds

There are several different kinds of type. In each kind, different fields are actually valid. These kinds are listed in the `__TypeKind` enumeration.

<section id="sec-Scalar">

##### <span class="spec-secid" title="link to this section">[4.2.2.1](#sec-Scalar)</span>Scalar

Represents scalar types such as Int, String, and Boolean. Scalars cannot have fields.

A GraphQL type designer should describe the data format and scalar coercion rules in the description field of any scalar.

Fields

*   `kind` must return `__TypeKind.SCALAR`.
*   `name` must return a String.
*   `description` may return a String or <span class="spec-keyword">null</span>.
*   All other fields must return <span class="spec-keyword">null</span>.



<section id="sec-Object">

##### <span class="spec-secid" title="link to this section">[4.2.2.2](#sec-Object)</span>Object

Object types represent concrete instantiations of sets of fields. The introspection types (e.g. `__Type`, `__Field`, etc) are examples of objects.

Fields

*   `kind` must return `__TypeKind.OBJECT`.
*   `name` must return a String.
*   `description` may return a String or <span class="spec-keyword">null</span>.
*   `fields`: The set of fields query‐able on this type.
    *   Accepts the argument `includeDeprecated` which defaults to <span class="spec-keyword">false</span>. If <span class="spec-keyword">true</span>, deprecated fields are also returned.
*   `interfaces`: The set of interfaces that an object implements.
*   All other fields must return <span class="spec-keyword">null</span>.



<section id="sec-Union">

##### <span class="spec-secid" title="link to this section">[4.2.2.3](#sec-Union)</span>Union

Unions are an abstract types where no common fields are declared. The possible types of a union are explicitly listed out in `possibleTypes`. Types can be made parts of unions without modification of that type.

Fields

*   `kind` must return `__TypeKind.UNION`.
*   `name` must return a String.
*   `description` may return a String or <span class="spec-keyword">null</span>.
*   `possibleTypes` returns the list of types that can be represented within this union. They must be object types.
*   All other fields must return <span class="spec-keyword">null</span>.



<section id="sec-Interface">

##### <span class="spec-secid" title="link to this section">[4.2.2.4](#sec-Interface)</span>Interface

Interfaces is an abstract type where there are common fields declared. Any type that implements an interface must define all the fields with names and types exactly matching. The implementations of this interface are explicitly listed out in `possibleTypes`.

Fields

*   `kind` must return `__TypeKind.INTERFACE`.
*   `name` must return a String.
*   `description` may return a String or <span class="spec-keyword">null</span>.
*   `fields`: The set of fields required by this interface.
    *   Accepts the argument `includeDeprecated` which defaults to <span class="spec-keyword">false</span>. If <span class="spec-keyword">true</span>, deprecated fields are also returned.
*   `possibleTypes` returns the list of types that implement this interface. They must be object types.
*   All other fields must return <span class="spec-keyword">null</span>.



<section id="sec-Enum">

##### <span class="spec-secid" title="link to this section">[4.2.2.5](#sec-Enum)</span>Enum

Enums are special scalars that can only have a defined set of values.

Fields

*   `kind` must return `__TypeKind.ENUM`.
*   `name` must return a String.
*   `description` may return a String or <span class="spec-keyword">null</span>.
*   `enumValues`: The list of `EnumValue`. There must be at least one and they must have unique names.
    *   Accepts the argument `includeDeprecated` which defaults to <span class="spec-keyword">false</span>. If <span class="spec-keyword">true</span>, deprecated enum values are also returned.
*   All other fields must return <span class="spec-keyword">null</span>.



<section id="sec-Input-Object">

##### <span class="spec-secid" title="link to this section">[4.2.2.6](#sec-Input-Object)</span>Input Object

Input objects are composite types used as inputs into queries defined as a list of named input values.

For example the input object `Point` could be defined as:

```
type Point {
  x: Int
  y: Int
}

```

Fields

*   `kind` must return `__TypeKind.INPUT_OBJECT`.
*   `name` must return a String.
*   `description` may return a String or <span class="spec-keyword">null</span>.
*   `inputFields`: a list of `InputValue`.
*   All other fields must return <span class="spec-keyword">null</span>.



<section id="sec-List">

##### <span class="spec-secid" title="link to this section">[4.2.2.7](#sec-List)</span>List

Lists represent sequences of values in GraphQL. A List type is a type modifier: it wraps another type instance in the `ofType` field, which defines the type of each item in the list.

Fields

*   `kind` must return `__TypeKind.LIST`.
*   `ofType`: Any type.
*   All other fields must return <span class="spec-keyword">null</span>.



<section id="sec-Non-null">

##### <span class="spec-secid" title="link to this section">[4.2.2.8](#sec-Non-null)</span>Non-null

GraphQL types are nullable. The value <span class="spec-keyword">null</span> is a valid response for field type.

A Non‐null type is a type modifier: it wraps another type instance in the `ofType` field. Non‐null types do not allow <span class="spec-keyword">null</span> as a response, and indicate required inputs for arguments and input object fields.

*   `kind` must return `__TypeKind.NON_NULL`.
*   `ofType`: Any type except Non‐null.
*   All other fields must return <span class="spec-keyword">null</span>.



<section id="sec-Combining-List-and-Non-Null">

##### <span class="spec-secid" title="link to this section">[4.2.2.9](#sec-Combining-List-and-Non-Null)</span>Combining List and Non-Null

List and Non‐Null can compose, representing more complex types.

If the modified type of a List is Non‐Null, then that List may not contain any <span class="spec-keyword">null</span> items.

If the modified type of a Non‐Null is List, then <span class="spec-keyword">null</span> is not accepted, however an empty list is accepted.

If the modified type of a List is a List, then each item in the first List is another List of the second List’s type.

A Non‐Null type cannot modify another Non‐Null type.









<section id="sec-Validation">

## <span class="spec-secid" title="link to this section">[5](#sec-Validation)</span>Validation

GraphQL does not just verify if a request is syntactically correct.

Prior to execution, it can also verify that a request is valid within the context of a given GraphQL schema. Validation is primarily targeted at development‐time tooling. Any client‐side tooling should return errors and not allow the formulation of queries known to violate the type system at a given point in time.

Total request validation on the server‐side during execution is optional. As schemas and systems change over time existing clients may end up emitting queries that are no longer valid given the current type system. Servers (as described in the Execution section of this spec) attempt to satisfy as much as the request as possible and continue to execute in the presence of type system errors rather than cease execution completely.

For this section of this schema, we will assume the following type system in order to demonstrate examples:

```
enum DogCommand { SIT, DOWN, HEEL }

type Dog : Pet {
  name: String!
  nickname: String
  barkVolume: Int
  doesKnowCommand(dogCommand: DogCommand!) : Boolean!
  isHousetrained(atOtherHomes: Boolean): Boolean!
}

interface Sentient {
  name: String!
}

interface Pet {
  name: String!
}

type Alien : Sentient {
  name: String!
  homePlanet: String
}

type Human : Sentient {
  name: String!
}

type Cat : Pet {
  name: String!
  nickname: String
  meowVolume: Int
}

union CatOrDog = Cat | Dog
union DogOrHuman = Dog | Human
union HumanOrAlien = Human | Alien

```

<section id="sec-Validation.Fields">

### <span class="spec-secid" title="link to this section">[5.1](#sec-Validation.Fields)</span>Fields

<section id="sec-Field-Selections-on-Objects-Interfaces-and-Unions-Types">

#### <span class="spec-secid" title="link to this section">[5.1.1](#sec-Field-Selections-on-Objects-Interfaces-and-Unions-Types)</span>Field Selections on Objects, Interfaces, and Unions Types

**Formal Specification**

*   For each <var>selection</var> in the document.
*   Let <var>fieldName</var> be the target field of <var>selection</var>
*   <var>fieldName</var> must be defined on type in scope

**Explanatory Text**

The target field of a field selection must defined on the scoped type of the selection set. There are no limitations on alias names.

For example the following fragment would not pass validation:

```
fragment fieldNotDefined on Dog {
  meowVolume
}

fragment aliasedLyingFieldTargetNotDefined on Dog {
  barkVolume: kawVolume
}

```

For interfaces, direct field selection can only be done on fields. Fields of concrete implementors is not relevant to the validity of the given interface‐typed selection set.

For example, the following is valid:

```
fragment interfaceFieldSelection on Pet {
  name
}

```

and the following is invalid:

```
fragment definedOnImplementorsButNotInterface on Pet {
  nickname
}

```

Because fields are not declared on unions, direct field selection on union‐typed selection set. This is true even if concrete implementors of the union define the fieldName.

For example the following is invalid

```
fragment directFieldSelectionOnUnion on CatOrDog {
  directField
}

fragment definedOnImplementorsQueriedOnUnion on CatOrDog {
  name
}

```



<section id="sec-Field-Selection-Merging">

#### <span class="spec-secid" title="link to this section">[5.1.2](#sec-Field-Selection-Merging)</span>Field Selection Merging

**Formal Specification**

*   Let <var>set</var> be any selection set defined in the GraphQL document
*   Let <var>setForKey</var> be the set of selections with a given response key in <var>set</var>
*   All members of <var>setForKey</var> must:
    *   Have identical target fields
    *   Have identical sets of arguments.
    *   Have identical sets of directives.

**Explanatory Text**

Selection names are de‐duplicated and merged for validation, but the target field, arguments, and directives must all be identical.

For human‐curated GraphQL, this rules seem a bit counterintuitive since it appears to be clear developer error. However in the presence of nested fragments or machine‐generated GraphQL, requiring unique selections is a burdensome limitation on tool authors.

The following selections correctly merge:

```
fragment mergeIdenticalFields on Dog {
  name
  name
}

fragment mergeIdenticalAliasesAndFields on Dog {
  otherName: name
  otherName: name
}

```

The following is not able to merge:

```
fragment conflictingBecauseAlias on Dog {
  name: nickname
  name
}

```

Identical arguments are also merged if they have identical arguments. Both values and variables can be correctly merged.

For example the following correctly merge:

```
fragment mergeIdenticalFieldsWithIdenticalArgs on Dog {
  doesKnowCommand(dogCommand: SIT)
  doesKnowCommand(dogCommand: SIT)
}

fragment mergeIdenticalFieldsWithIdenticalValues on Dog {
  doesKnowCommand(dogCommand: $dogCommand)
  doesKnowCommand(dogCommand: $dogCommand)
}

```

The following do not correctly merge:

```
fragment conflictingArgsOnValues on Dog {
  doesKnowCommand(dogCommand: SIT)
  doesKnowCommand(dogCommand: HEEL)
}

fragment conflictingArgsValueAndVar on Dog {
  doesKnowCommand(dogCommand: SIT)
  doesKnowCommand(dogCommand: $dogCommand)
}

fragment conflictingArgsWithVars on Dog {
  doesKnowCommand(dogCommand: $varOne)
  doesKnowCommand(dogCommand: $varTwo)
}

```

The same logic applies to directives. The set of directives on each selection with the same response key in a given scope must be identical.

The following is valid:

```
fragment mergeSameFieldsWithSameDirectives on Dog {
  name @include(if: true)
  name @include(if: true)
}

```

and the following is invalid:

```
fragment conflictingDirectiveArgs on Dog {
  name @include(if: true)
  name @include(if: false)
}

```



<section id="sec-Leaf-Field-Selections">

#### <span class="spec-secid" title="link to this section">[5.1.3](#sec-Leaf-Field-Selections)</span>Leaf Field Selections

**Formal Specification**

*   For each <var>selection</var> in the document
*   Let <var>selectionType</var> be the result type of <var>selection</var>
*   If <var>selectionType</var> is a scalar:
    *   The subselection set of that selection must be empty
*   If <var>selectionType</var> is an interface, union, or object
    *   The subselection set of that selection must NOT BE empty

**Explanatory Text**

Field selections on scalars are never allowed: scalars are the leaf nodes of any GraphQL query.

The following is valid.

```
fragment scalarSelection: Dog {
  barkVolume
}

```

The following is invalid.

```
fragment scalarSelectionsNotAllowedOnBoolean : Dog {
  barkVolume {
    sinceWhen
  }
}

```

Conversely the leaf field selections of GraphQL queries must be scalars. Leaf selections on objects, interfaces, and unions without subfields are disallowed.

Let’s assume the following query root type of the schema:

```
type QueryRoot {
  human: Human
  pet: Pet
  catOrDog: CatOrDog
}

```

The following examples are invalid

```
query directQueryOnObjectWithoutSubFields {
  human
}

query directQueryOnInterfaceWithoutSubFields {
  pet
}

query directQueryOnUnionWithoutSubFields {
  catOrDog
}

```





<section id="sec-Validation.Arguments">

### <span class="spec-secid" title="link to this section">[5.2](#sec-Validation.Arguments)</span>Arguments

Arguments are provided to both fields and directives. The following validation rules apply in both cases.

<section id="sec-Argument-Names">

#### <span class="spec-secid" title="link to this section">[5.2.1](#sec-Argument-Names)</span>Argument Names

**Formal Specification**

*   For each <var>argument</var> in the document
*   Let <var>argumentName</var> be the Name of <var>argument</var>.
*   Let <var>argumentDefinition</var> be the argument definition provided by the parent field or definition named <var>argumentName</var>.
*   <var>argumentDefinition</var> must exist.

**Explanatory Text**

Every argument provided to a field or directive must be defined in the set of possible arguments of that field or directive.

For example the following are valid:

```
fragment argOnRequiredArg on Dog {
  doesKnowCommand(dogCommand: SIT)
}

fragment argOnOptional on Dog {
  isHousetrained(atOtherHomes: true) @include(if: true)
}

```

the following is invalid since `command` is not defined on `DogCommand`.

```
fragment invalidArgName on Dog {
  doesKnowCommand(command: CLEAN_UP_HOUSE)
}

```

and this is also invalid as `unless` is not defined on `@include`.

```
fragment invalidArgName on Dog {
  isHousetrained(atOtherHomes: true) @include(unless: false)
}

```

In order to explore more complicated argument examples, let’s add the following to our type system:

```
type Arguments {
  multipleReqs(x: Int!, y: Int!)
  booleanArgField(booleanArg: Boolean)
  floatArgField(floatArg: Float)
  intArgField(intArg: Int)
  nonNullBooleanArgField(nonNullBooleanArg: Boolean!)
}

```

Order does not matter in arguments. Therefore both the following example are valid.

```
fragment multipleArgs on Arguments {
  multipleReqs(x: 1, y: 2)
}

fragment multipleArgsReverseOrder on Arguments {
  multipleReqs(y: 1, x: 2)
}

```



<section id="sec-Argument-Values-Type-Correctness">

#### <span class="spec-secid" title="link to this section">[5.2.2](#sec-Argument-Values-Type-Correctness)</span>Argument Values Type Correctness

<section id="sec-Compatible-Values">

##### <span class="spec-secid" title="link to this section">[5.2.2.1](#sec-Compatible-Values)</span>Compatible Values

**Formal Specification**

*   For each <var>argument</var> in the document
*   Let <var>value</var> be the Value of <var>argument</var>
*   If <var>value</var> is not a Variable
    *   Let <var>argumentName</var> be the Name of <var>argument</var>.
    *   Let <var>argumentDefinition</var> be the argument definition provided by the parent field or definition named <var>argumentName</var>.
    *   Let <var>type</var> be the type expected by <var>argumentDefinition</var>.
    *   The type of <var>literalArgument</var> must be coercible to <var>type</var>.

**Explanatory Text**

Literal values must be compatible with the type defined by the argument they are being provided to, as per the coercion rules defined in the Type System chapter.

For example, an Int can be coerced into a Float.

```
fragment goodBooleanArg on Arguments {
  booleanArgField(booleanArg: true)
}

fragment coercedIntIntoFloatArg on Arguments {
  floatArgField(floatArg: 1)
}

```

An incoercible conversion, is string to int. Therefore, the following example is invalid.

```
fragment stringIntoInt on Arguments {
  intArgField(intArg: "3")
}

```



<section id="sec-Required-Arguments">

##### <span class="spec-secid" title="link to this section">[5.2.2.2](#sec-Required-Arguments)</span>Required Arguments

*   For each Field or Directive in the document.
*   Let <var>arguments</var> be the arguments provided by the Field or Directive.
*   Let <var>argumentDefinitions</var> be the set of argument definitions of that Field or Directive.
*   For each <var>definition</var> in <var>argumentDefinitions</var>
    *   Let <var>type</var> be the expected type of <var>definition</var>
    *   If <var>type</var> is Non‐Null
        *   Let <var>argumentName</var> be the name of <var>definition</var>
        *   Let <var>argument</var> be the argument in <var>arguments</var> named <var>argumentName</var>
        *   <var>argument</var> must exist.

**Explanatory Text**

Arguments can be required. Arguments are required if the type of the argument is non‐null. If it is not non‐null, the argument is optional.

For example the following are valid:

```
fragment goodBooleanArg on Arguments {
  booleanArgField(booleanArg: true)
}

fragment goodNonNullArg on Arguments {
  nonNullBooleanArgField(nonNullBooleanArg: true)
}

```

The argument can be omitted from a field with a nullable argument.

Therefore the following query is valid:

```
fragment goodBooleanArgDefault on Arguments {
  booleanArgField
}

```

but this is not valid on a non‐null argument.

```
fragment missingRequiredArg on Arguments {
  notNullBooleanArgField
}

```







<section id="sec-Validation.Fragments">

### <span class="spec-secid" title="link to this section">[5.3](#sec-Validation.Fragments)</span>Fragments

<section id="sec-Fragment-Declarations">

#### <span class="spec-secid" title="link to this section">[5.3.1](#sec-Fragment-Declarations)</span>Fragment Declarations

<section id="sec-Fragment-Spread-Type-Existence">

##### <span class="spec-secid" title="link to this section">[5.3.1.1](#sec-Fragment-Spread-Type-Existence)</span>Fragment Spread Type Existence

**Formal Specification**

*   For each named spread <var>namedSpread</var> in the document
*   Let <var>fragment</var> be the target of <var>namedSpread</var>
*   The target type of <var>fragment</var> must be defined in the schema

**Explanatory Text**

Fragments must be specified on types that exist in the schema. This applies for both named and inline fragments. If they are not defined in the schema, the query does not validate.

For example the following fragments are valid:

```
fragment correctType on Dog {
  name
}

fragment inlineFragment on Dog {
  ... on Dog {
    name
  }
}

```

and the following do not validate:

```
fragment notOnExistingType on NotInSchema {
  name
}

fragment inlineNotExistingType on Dog {
  ... on NotInSchema {
    name
  }
}

```



<section id="sec-Fragments-On-Composite-Types">

##### <span class="spec-secid" title="link to this section">[5.3.1.2](#sec-Fragments-On-Composite-Types)</span>Fragments On Composite Types

**Formal Specification**

*   For each <var>fragment</var> defined in the document.
*   The target type of fragment must have kind <span class="spec-nt">UNION</span>, <span class="spec-nt">INTERFACE</span>, or <span class="spec-nt">OBJECT</span>.

**Explanatory Text**

Fragments can only be declared on unions, interfaces, and objects. They are invalid on scalars. They can only be applied on non‐leaf fields. This rule applies to both inline and named fragments.

The following fragment declarations are valid:

```
fragment fragOnObject on Dog {
  name
}

fragment fragOnInterface on Pet {
  name
}

fragment fragOnUnion on CatOrDog {
  ... on Dog {
    name
  }
}

```

and the following are invalid:

```
fragment fragOnScalar on Int {
  something
}

fragment inlineFragOnScalar on Dog {
  ... on Boolean {
    somethingElse
  }
}

```



<section id="sec-Fragments-Must-Be-Used">

##### <span class="spec-secid" title="link to this section">[5.3.1.3](#sec-Fragments-Must-Be-Used)</span>Fragments Must Be Used

**Formal Specification**

*   For each <var>fragment</var> defined in the document.
*   <var>fragment</var> must be the target of at least one spread in the document

**Explanatory Text**

Defined fragments must be used within a query document.

For example the following is an invalid query document:

```
fragment nameFragment on Dog { # unused
  name
}

{
  dog {
    name
  }
}

```





<section id="sec-Fragment-Spreads">

#### <span class="spec-secid" title="link to this section">[5.3.2](#sec-Fragment-Spreads)</span>Fragment Spreads

Field selection is also determined by spreading fragments into one another. The selection set of the target fragment is unioned with the selection set at the level at which the target fragment is referenced.

<section id="sec-Fragment-spread-target-defined">

##### <span class="spec-secid" title="link to this section">[5.3.2.1](#sec-Fragment-spread-target-defined)</span>Fragment spread target defined

**Formal Specification**

*   For every <var>namedSpread</var> in the document.
*   Let <var>fragment</var> be the target of <var>namedSpread</var>
*   <var>fragment</var> must be defined in the document

**Explanatory Text**

Named fragment spreads must refer to fragments defined within the document. If the target of a spread is not defined, this is an error:

```
{
  dog {
    ...undefinedFragment
  }
}

```



<section id="sec-Fragment-spreads-must-not-form-cycles">

##### <span class="spec-secid" title="link to this section">[5.3.2.2](#sec-Fragment-spreads-must-not-form-cycles)</span>Fragment spreads must not form cycles

**Formal Specification**

*   For each <var>fragmentDefinition</var> in the document
*   Let <var>visited</var> be the empty set.
*   <span class="spec-call">DetectCycles(<var>fragmentDefinition</var>, <var>visited</var>)</span>

<span class="spec-call">DetectCycles(<var>fragmentDefinition</var>, <var>visited</var>)</span> :

*   Let <var>spreads</var> be all fragment spread descendants of <var>fragmentDefinition</var>
*   For each <var>spread</var> in <var>spreads</var>
    *   <var>visited</var> must not contain <var>spread</var>
    *   Let <var>nextVisited</var> be the set including <var>spread</var> and members of <var>visited</var>
    *   Let <var>nextFragmentDefinition</var> be the target of <var>spread</var>
    *   <span class="spec-call">DetectCycles(<var>nextFragmentDefinition</var>, <var>nextVisited</var>)</span>

**Explanatory Text**

The graph of fragment spreads must not form any cycles including spreading itself. Otherwise an operation could infinitely spread or infinitely execute on cycles in the underlying data.

This invalidates fragments that would result in an infinite spread:

```
{
  dog {
    ...nameFragment
  }
}

fragment nameFragment on Dog {
  name
  ...barkVolumeFragment
}

fragment barkVolumeFragment on Dog {
  barkVolume
  ...nameFragment
}

```

If the above fragments were inlined, this would result in the infinitely large:

```
{
  dog {
    name
    barkVolume
    name
    barkVolume
    name
    barkVolume
    name
    # forever...
  }
}

```

This also invalidates fragments that would result in an infinite recursion when executed against cyclic data:

```
{
  dog {
    ...dogFragment
  }
}

fragment dogFragment on Dog {
  name
  owner {
    ...ownerFragment
  }
}

fragment ownerFragment on Dog {
  name
  pets {
    ...dogFragment
  }
}

```



<section id="sec-Fragment-spread-is-possible">

##### <span class="spec-secid" title="link to this section">[5.3.2.3](#sec-Fragment-spread-is-possible)</span>Fragment spread is possible

**Formal Specification**

*   For each <var>spread</var> (named or inline) in defined in the document.
*   Let <var>fragment</var> be the target of <var>spread</var>
*   Let <var>fragmentType</var> be the type condition of <var>fragment</var>
*   Let <var>parentType</var> be the type of the selection set containing <var>spread</var>
*   Let <var>applicableTypes</var> be the intersection of <span class="spec-call">[GetPossibleTypes](#GetPossibleTypes())(<var>fragmentType</var>)</span> and <span class="spec-call">[GetPossibleTypes](#GetPossibleTypes())(<var>parentType</var>)</span>
*   <var>applicableTypes</var> must not be empty.

<div class="spec-algo" id="GetPossibleTypes()"><span class="spec-call">[GetPossibleTypes](#GetPossibleTypes())(<var>type</var>)</span>

1.  If <var>type</var> is an object type, return a set containing <var>type</var>
2.  If <var>type</var> is an interface type, return the set of types implementing <var>type</var>
3.  If <var>type</var> is a union type, return the set of possible types of <var>type</var>

</div>

**Explanatory Text**

Fragments are declared on a type and will only apply when the runtime object type matches the type condition. They also are spread within the context of a parent type. A fragment spread is only valid if its type condition could ever apply within the parent type.

and the following valid fragments:

<section id="sec-Object-Spreads-In-Object-Scope">

###### <span class="spec-secid" title="link to this section">[5.3.2.3.1](#sec-Object-Spreads-In-Object-Scope)</span>Object Spreads In Object Scope

In the scope of a object type, the only valid object type fragment spread is one that applies to the same type that is in scope.

For example

```
fragment dogFragment on Dog {
  ... on Dog {
    barkVolume
  }
}

```

and the following is invalid

```
fragment catInDogFragmentInvalid on Dog {
  ... on Cat {
    meowVolume
  }
}

```



<section id="sec-Abstract-Spreads-in-Object-Scope">

###### <span class="spec-secid" title="link to this section">[5.3.2.3.2](#sec-Abstract-Spreads-in-Object-Scope)</span>Abstract Spreads in Object Scope

In scope of an object type, unions or interface spreads can be used if the object type implements the interface or is a member of the union.

For example

```
fragment petNameFragment on Pet {
  name
}

fragment interfaceWithinObjectFragment on Dog {
  ...petNameFragment
}

```

is valid because <span class="spec-nt">Dog</span> implements Pet.

Likewise

```
fragment catOrDogNameFragment on CatOrDog {
  ... on Cat {
    meowVolume
  }
}

fragment unionWithObjectFragment on Dog {
  ...CatOrDogFragment
}

```

is valid because <span class="spec-nt">Dog</span> is a member of the <span class="spec-nt">CatOrDog</span> union. It is worth noting that if one inspected the contents of the <span class="spec-nt">CatOrDogNameFragment</span> you could note that the no valid results would ever be returned. However we do not specify this as invalid because we only consider the fragment declaration, not its body.



<section id="sec-Object-Spreads-In-Abstract-Scope">

###### <span class="spec-secid" title="link to this section">[5.3.2.3.3](#sec-Object-Spreads-In-Abstract-Scope)</span>Object Spreads In Abstract Scope

Union or interface spreads can be used within the context of an object type fragment, but only if the object type is one of the possible types of the that interface or union.

For example, the following fragments are valid:

```
fragment petFragment on Pet {
  name
  ... on Dog {
    barkVolume
  }
}

fragment catOrDogFragment on CatOrDog {
  ... on Cat {
    meowVolume
  }
}

```

<var>petFragment</var> is valid because <span class="spec-nt">Dog</span> implements the interface <span class="spec-nt">Pet</span>. <var>catOrDogFragment</var> is valid because <span class="spec-nt">Cat</span> is a member of the <span class="spec-nt">CatOrDog</span> union.

By contrast the following fragments are invalid:

```
fragment sentientFragment on Sentient {
  ... on Dog {
    barkVolume
  }
}

fragment humanOrAlienFragment on HumanOrAlien {
  ... on Cat {
    meowVolume
  }
}

```

<span class="spec-nt">Dog</span> does not implement the interface <span class="spec-nt">Sentient</span> and therefore <var>sentientFragment</var> can never return meaningful results. Therefore the fragment is invalid. Likewise <span class="spec-nt">Cat</span> is not a member of the union <span class="spec-nt">HumanOrAlien</span>, and it can also never return meaningful results, making it invalid.



<section id="sec-Abstract-Spreads-in-Abstract-Scope">

###### <span class="spec-secid" title="link to this section">[5.3.2.3.4](#sec-Abstract-Spreads-in-Abstract-Scope)</span>Abstract Spreads in Abstract Scope

Union or interfaces fragments can be used within each other. As long as there exists at least _one_ object type that exists in the intersection of the possible types of the scope and the spread, the spread is considered valid.

So for example

```
fragment unionWithInterface on Pet {
  ...dogOrHumanFragment
}

fragment dogOrHumanFragment on DogOrHuman {
  ... on Dog {
    barkVolume
  }
}

```

is consider valid because <span class="spec-nt">Dog</span> implements interface <span class="spec-nt">Pet</span> and is a member of <span class="spec-nt">DogOrHuman</span>.

However

```
fragment nonIntersectingInterfaces on Pet {
  ...sentientFragment
}

fragment sentientFragment on Sentient {
  name
}

```

is not valid because there exists no type that implements both <span class="spec-nt">Pet</span> and <span class="spec-nt">Sentient</span>.









<section id="sec-Validation.Directives">

### <span class="spec-secid" title="link to this section">[5.4](#sec-Validation.Directives)</span>Directives

<section id="sec-Directives-Are-Defined">

#### <span class="spec-secid" title="link to this section">[5.4.1](#sec-Directives-Are-Defined)</span>Directives Are Defined

**Formal Specification**

*   For every <var>directive</var> in a document.
*   Let <var>directiveName</var> be the name of <var>directive</var>.
*   Let <var>directiveDefinition</var> be the directive named <var>directiveName</var>.
*   <var>directiveDefinition</var> must exist.

**Explanatory Text**

GraphQL servers define what directives they support. For each usage of a directive, the directive must be available on that server.





<section id="sec-Validation.Operations">

### <span class="spec-secid" title="link to this section">[5.5](#sec-Validation.Operations)</span>Operations

<section id="sec-Validation.Operations.Variables">

#### <span class="spec-secid" title="link to this section">[5.5.1](#sec-Validation.Operations.Variables)</span>Variables

<section id="sec-Variable-Default-Values-Are-Correctly-Typed">

##### <span class="spec-secid" title="link to this section">[5.5.1.1](#sec-Variable-Default-Values-Are-Correctly-Typed)</span>Variable Default Values Are Correctly Typed

**Formal Specification**

*   For every <var>operation</var> in a document
*   For every <var>variable</var> on each <var>operation</var>
    *   Let <var>variableType</var> be the type of <var>variable</var>
    *   If <var>variableType</var> is non‐null it cannot have a default value
    *   If <var>variable</var> has a default value it must be of the same types or able to be coerced to <var>variableType</var>

**Explanatory Text**

Variable defined by operations are allowed to define default values if the type of that variable not non‐null.

For example the following query will pass validation.

```
query houseTrainedQuery($atOtherHomes: Boolean = true) {
  dog {
    isHousetrained(atOtherHomes: $atOtherHomes)
  }
}

```

However if the variable is defined as non‐null, default values are unreachable. Therefore queries such as the following fail validation

```
query houseTrainedQuery($atOtherHomes: Boolean! = true) {
  dog {
    isHousetrained(atOtherHomes: $atOtherHomes)
  }
}

```

Default values must be compatible with the types of variables. Types much match or they must be coercible to the type.

Non‐matching types fail, such as in the following example:

```
query houseTrainedQuery($atOtherHomes: Boolean = "true") {
  dog {
    isHousetrained(atOtherHomes: $atOtherHomes)
  }
}

```

However if a type is coercible the query will pass validation.

For example:

```
query intToFloatQuery($floatVar: Float = 1) {
  arguments {
    floatArgField(floatArg: $floatVar)
  }
}

```



<section id="sec-Variables-Are-Input-Types">

##### <span class="spec-secid" title="link to this section">[5.5.1.2](#sec-Variables-Are-Input-Types)</span>Variables Are Input Types

**Formal Specification**

*   For every <var>operation</var> in a <var>document</var>
*   For every <var>variable</var> on each <var>operation</var>
    *   Let <var>variableType</var> be the type of <var>variable</var>
    *   While <var>variableType</var> is <span class="spec-nt">LIST</span> or <span class="spec-nt">NON_NULL</span>
        *   Let <var>variableType</var> be the referenced type of <var>variableType</var>
    *   <var>variableType</var> must of kind <span class="spec-nt">SCALAR</span>, <span class="spec-nt">ENUM</span> or <span class="spec-nt">INPUT_OBJECT</span>

**Explanatory Text**

Variables can only be scalars, enums, input objects, or lists and non‐null variants of those types. These are known as input types. Object, unions, and interfaces cannot be used as inputs.

The following queries are valid:

```
query takesBoolean($atOtherHomes: Boolean) {
  # ...
}

query takesComplexInput($complexInput: ComplexInput) {
  # ...
}

query TakesListOfBooleanBang($booleans: [Boolean!]) {
  # ...
}

```

The following queries are invalid:

```
query takesCat($cat: Cat) {
  # ...
}

query takesDogBang($dog: Dog!) {
  # ...
}

query takesListOfPet($pets: [Pet]) {
  # ...
}

query takesCatOrDog($catOrDog: CatOrDog) {
  # ...
}

```



<section id="sec-All-Variable-Uses-Defined">

##### <span class="spec-secid" title="link to this section">[5.5.1.3](#sec-All-Variable-Uses-Defined)</span>All Variable Uses Defined

**Formal Specification**

*   For each <var>operation</var> in a document
    *   For each <var>variableUsage</var> in scope, variable must be operation’s variable list.
    *   Let <var>fragments</var> be every fragment reference by that operation transitively
    *   For each <var>fragment</var> in <var>fragments</var>
        *   For each <var>variableUsage</var> in scope of <var>fragment</var>, variable must be <var>operation</var>‘s variable list.

**Explanatory Text**

Variables are scoped on a per‐operation basis. That means that any variable used within the context of a operation must be defined at the top level of that operation

For example:

```
query variableIsDefined($atOtherHomes: Boolean) {
  dog {
    isHousetrained(atOtherHomes: $booleanArg)
  }
}

```

is valid. $<var>atOtherHomes</var> is defined by the operation.

By contrast the following query is invalid:

```
query variableIsNotDefined {
  dog {
    isHousetrained(atOtherHomes: $atOtherHomes)
  }
}

```

$<var>atOtherHomes</var> is not defined by the operation.

Fragments complicate this rule. Any fragment transitively included by an operation has access to the variables defined by that operation. Fragments can appear within multiple operations and therefore variable usages must correspond to variable definitions in all of those operations.

For example the following is valid:

```
query variableIsDefinedUsedInSingleFragment($atOtherHomes: Boolean) {
  dog {
    ...isHousetrainedFragment
  }
}

fragment isHousetrainedFragment on Dog {
  isHousetrained(atOtherHomes: $atOtherHomes}
}

```

since <var>isHousetrainedFragment</var> is used within the context of the operation <var>variableIsDefinedUsedInSingleFragment</var> and the variable is defined by that operation.

On the contrary is a fragment is included within an operation that does not define a referenced variable, this is a validation error.

```
query variableIsNotDefinedUsedInSingleFragment {
  dog {
    ...isHousetrainedFragment
  }
}

fragment isHousetrainedFragment on Dog {
  isHousetrained(atOtherHomes: $atOtherHomes}
}

```

This applies transitively as well, so the following also fails:

```
query variableIsNotDefinedUsedInNestedFragment {
  dog {
    ...outerHousetrainedFragment
  }
}

fragment outerHousetrainedFragment on Dog {
  ...isHousetrainedFragment
}

fragment isHousetrainedFragment on Dog {
  isHousetrained(atOtherHomes: $atOtherHomes}
}

```

Variables must be defined in all operations in which a fragment is used.

```
query housetrainedQueryOne($atOtherHomes: Boolean) {
  dog {
    ...isHousetrainedFragment
  }
}

query housetrainedQueryTwo($atOtherHomes: Boolean) {
  dog {
    ...isHousetrainedFragment
  }
}

fragment isHousetrainedFragment on Dog {
  isHousetrained(atOtherHomes: $atOtherHomes}
}

```

However the following does not validate:

```
query housetrainedQueryOne($atOtherHomes: Boolean) {
  dog {
    ...isHousetrainedFragment
  }
}

query housetrainedQueryTwoNotDefined {
  dog {
    ...isHousetrainedFragment
  }
}

fragment isHousetrainedFragment on Dog {
  isHousetrained(atOtherHomes: $atOtherHomes)
}

```

This is because <var>housetrainedQueryTwoNotDefined</var> does not define a variable $<var>atOtherHomes</var> but that variable is used by <var>isHousetrainedFragment</var> which is included in that operation.



<section id="sec-All-Variables-Used">

##### <span class="spec-secid" title="link to this section">[5.5.1.4](#sec-All-Variables-Used)</span>All Variables Used

**Formal Specification**

*   For every <var>operation</var> in the document.
*   Let <var>variables</var> be the variables defined by that <var>operation</var>
*   Each <var>variable</var> in <var>variables</var> must be used at least once in either the operation scope itself or any fragment transitively referenced by that operation.

**Explanatory Text**

All variables defined by an operation must be used in that operation or a fragment transitively included by that operation. Unused variables cause a validation error.

For example the following is invalid:

```
query variableUnused($atOtherHomes: Boolean) {
  dog {
    isHousetrained
  }
}

```

because $<var>atOtherHomes</var> in not referenced.

These rules apply to transitive fragment spreads as well:

```
query variableUsedInFragment($atOtherHomes: Boolean) {
  dog {
    ...isHousetrainedFragment
  }
}

fragment isHousetrainedFragment on Dog {
  isHousetrained(atOtherHomes: $atOtherHomes)
}

```

The above is valid since $<var>atOtherHomes</var> is used in <var>isHousetrainedFragment</var> which is included by <var>variableUsedInFragment</var>.

If that fragment did not have a reference to $<var>atOtherHomes</var> it would be not valid:

```
query variableNotUsedWithinFragment($atOtherHomes: Boolean) {
  ...isHousetrainedWithoutVariableFragment
}

fragment isHousetrainedWithoutVariableFragment on Dog {
  isHousetrained
}

```

All operations in a document must use all of their variables.

As a result, the following document does not validate.

```
query queryWithUsedVar($atOtherHomes: Boolean) {
  dog {
    ...isHousetrainedFragment
  }
}

query queryWithExtraVar($atOtherHomes: Boolean, $extra: Int) {
  dog {
    ...isHousetrainedFragment
  }
}

fragment isHousetrainedFragment on Dog {
  isHousetrained(atOtherHomes: $atOtherHomes)
}

```

This document is not valid because <var>queryWithExtraVar</var> defines an extraneous variable.



<section id="sec-All-Variable-Usages-are-Allowed">

##### <span class="spec-secid" title="link to this section">[5.5.1.5](#sec-All-Variable-Usages-are-Allowed)</span>All Variable Usages are Allowed

**Formal Specification**

*   For each <var>operation</var> in <var>document</var>
*   Let <var>variableUsages</var> be all usages transitively included in the <var>operation</var>
*   For each <var>variableUsage</var> in <var>variableUsages</var>
    *   Let <var>variableType</var> be the type of variable definition in the operation
    *   Let <var>argumentType</var> be the type of the argument the variable is passed to.
    *   Let <var>hasDefault</var> be true if the variable definition defines a default.
    *   AreTypesCompatible(<var>argumentType</var>, <var>variableType</var>, <var>hasDefault</var>) must be true
*   AreTypesCompatible(<var>argumentType</var>, <var>variableType</var>, <var>hasDefault</var>):
    *   If <var>hasDefault</var> is true, treat the <var>variableType</var> as non‐null.
    *   If inner type of <var>argumentType</var> and <var>variableType</var> be different, return false
    *   If <var>argumentType</var> and <var>variableType</var> have different list dimensions, return false
    *   If any list level of <var>variableType</var> is not non‐null, and the corresponding level in <var>argument</var> is non‐null, the types are not compatible.

**Explanatory Text**

Variable usages must be compatible with the arguments they are passed to.

Validation failures occur when variables are used in the context of types that are complete mismatches, or if a nullable type in a variable is passed to a not‐null argument type.

Types must match:

```
query intCannotGoIntoBoolean($intArg: Int) {
  arguments {
    booleanArgField(booleanArg: $intArg)
  }
}

```

$<var>intArg</var> typed as <span class="spec-nt">Int</span> cannot be used as a argument to <var>booleanArg</var>, typed as <span class="spec-nt">Boolean</span>.

List cardinality must also be the same. For example, lists cannot be passed into singular values.

```
query booleanListCannotGoIntoBoolean($booleanListArg: [Boolean]) {
  arguments {
    booleanArgField(booleanArg: $booleanListArg)
  }
}

```

Nullability must also be respected. In general a nullable variable cannot be passed to a non‐null argument.

```
query booleanArgQuery($booleanArg: Boolean) {
  arguments {
    nonNullBooleanArgField(nonNullBooleanArg: $booleanArg)
  }
}

```

A notable exception is when default arguments are provided. They are, in effect, treated as non‐nulls.

```
query booleanArgQueryWithDefault($booleanArg: Boolean = true) {
  arguments {
    nonNullBooleanArgField(nonNullBooleanArg: $booleanArg)
  }
}

```

For list types, the same rules around nullability apply to both outer types and inner types. A nullable list cannot be passed to a non‐null list, and a lists of nullable values cannot be passed to a list of non‐null values.

```
query nonNullListToList($nonNullBooleanList: ![Boolean]) {
  arguments {
    booleanListArgField(booleanListArg: $nonNullBooleanList)
  }
}

```

However a nullable list could not be passed to a non‐null list.

```
query listToNonNullList($booleanList: [Boolean]) {
  arguments {
    nonNullBooleanListField(nonNullBooleanListArg: $booleanList)
  }
}

```

This would fail validation because a `[T]` cannot be passed to a `[T]!`.

Similarly a `[T]` cannot be passed to a `[T!]`.









<section id="sec-Execution">

## <span class="spec-secid" title="link to this section">[6](#sec-Execution)</span>Execution

This section describes how GraphQL generates a response from a request.

<section id="sec-Evaluating-requests">

### <span class="spec-secid" title="link to this section">[6.1](#sec-Evaluating-requests)</span>Evaluating requests

To evaluate a request, the executor must have a parsed `Document` (as defined in the “Query Language” part of this spec) and a selected operation name to run if the document defines multiple operations.

The executor should find the `Operation` in the `Document` with the given operation name. If no such operation exists, the executor should throw an error. If the operation is found, then the result of evaluating the request should be the result of evaluating the operation according to the “Evaluating operations” section.



<section id="sec-Evaluating-operations">

### <span class="spec-secid" title="link to this section">[6.2](#sec-Evaluating-operations)</span>Evaluating operations

The type system, as described in the “Type System” part of the spec, must provide a “Query Root” and a “Mutation Root” object.

If the operation is a mutation, the result of the operation is the result of evaluating the mutation’s top level selection set on the “Mutation Root” object. This selection set should be evaluated serially.

If the operation is a query, the result of the operation is the result of evaluating the query’s top level selection set on the “Query Root” object.



<section id="sec-Evaluating-selection-sets">

### <span class="spec-secid" title="link to this section">[6.3](#sec-Evaluating-selection-sets)</span>Evaluating selection sets

To evaluate a selection set, the executor needs to know the object on which it is evaluating the set and whether it is being evaluated serially.

If the selection set is being evaluated on the `null` object, then the result of evaluating the selection set is `null`.

Otherwise, the selection set is turned into a grouped field set; each entry in the grouped field set is a list of fields that share a responseKey.

The selection set is converted to a grouped field set by calling `CollectFields`, initializing `visitedFragments` to an empty list.

<div class="spec-algo" id="CollectFields()"><span class="spec-call">[CollectFields](#CollectFields())(<var>objectType</var>, <var>selectionSet</var>, <var>visitedFragments</var>)</span>

1.  Initialize <var>groupedFields</var> to an empty list of lists.
2.  For each <var>selection</var> in <var>selectionSet</var>;
    1.  If <var>selection</var> provides the directive `@skip`, let <var>skipDirective</var> be that directive.
        1.  If <var>skipDirective</var>‘s <var>if</var> argument is <span class="spec-keyword">true</span>, continue with the next <var>selection</var> in <var>selectionSet</var>.
    2.  If <var>selection</var> provides the directive `@include`, let <var>includeDirective</var> be that directive.
        1.  If <var>includeDirective</var>‘s <var>if</var> argument is <span class="spec-keyword">false</span>, continue with the next <var>selection</var> in <var>selectionSet</var>.
    3.  If <var>selection</var> is a Field:
        1.  Let <var>responseKey</var> be the response key of <var>selection</var>.
        2.  Let <var>groupForResponseKey</var> be the list in <var>groupedFields</var> for <var>responseKey</var>; if no such list exists, create it as an empty list.
        3.  Append <var>selection</var> to the <var>groupForResponseKey</var>.
    4.  If <var>selection</var> is a FragmentSpread:
        1.  Let <var>fragmentSpreadName</var> be the name of <var>selection</var>.
        2.  If <var>fragmentSpreadName</var> is in <var>visitedFragments</var>, continue with the next <var>selection</var> in <var>selectionSet</var>.
        3.  Add <var>fragmentSpreadName</var> to <var>visitedFragments</var>.
        4.  Let <var>fragment</var> be the Fragment in the current Document whose name is <var>fragmentSpreadName</var>.
        5.  If no such <var>fragment</var> exists, continue with the next <var>selection</var> in <var>selectionSet</var>.
        6.  Let <var>fragmentType</var> be the type condition on <var>fragment</var>.
        7.  If <span class="spec-call">[doesFragmentTypeApply](#doesFragmentTypeApply())(<var>objectType</var>, <var>fragmentType</var>)</span> is false, continue with the next <var>selection</var> in <var>selectionSet</var>.
        8.  Let <var>fragmentSelectionSet</var> be the top‐level selection set of <var>fragment</var>.
        9.  Let <var>fragmentGroupedFields</var> be the result of calling <span class="spec-call">[CollectFields](#CollectFields())(<var>objectType</var>, <var>fragmentSelectionSet</var>)</span>.
        10.  For each <var>fragmentGroup</var> in <var>fragmentGroupedFields</var>:
            1.  Let <var>responseKey</var> be the response key shared by all fields in <var>fragmentGroup</var>
            2.  Let <var>groupForResponseKey</var> be the list in <var>groupedFields</var> for <var>responseKey</var>; if no such list exists, create it as an empty list.
            3.  Append all items in <var>fragmentGroup</var> to <var>groupForResponseKey</var>.
    5.  If <var>selection</var> is an inline fragment:
        1.  Let <var>fragmentType</var> be the type condition on <var>selection</var>.
        2.  If <span class="spec-call">[doesFragmentTypeApply](#doesFragmentTypeApply())(<var>objectType</var>, <var>fragmentType</var>)</span> is false, continue with the next <var>selection</var> in <var>selectionSet</var>.
        3.  Let <var>fragmentSelectionSet</var> be the top‐level selection set of <var>selection</var>.
        4.  Let <var>fragmentGroupedFields</var> be the result of calling <span class="spec-call">[CollectFields](#CollectFields())(<var>objectType</var>, <var>fragmentSelectionSet</var>)</span>.
        5.  For each <var>fragmentGroup</var> in <var>fragmentGroupedFields</var>:
            1.  Let <var>responseKey</var> be the response key shared by all fields in <var>fragmentGroup</var>
            2.  Let <var>groupForResponseKey</var> be the list in <var>groupedFields</var> for <var>responseKey</var>; if no such list exists, create it as an empty list.
            3.  Append all items in <var>fragmentGroup</var> to <var>groupForResponseKey</var>.
3.  Return <var>groupedFields</var>.

</div>

<div class="spec-algo" id="doesFragmentTypeApply()"><span class="spec-call">[doesFragmentTypeApply](#doesFragmentTypeApply())(<var>objectType</var>, <var>fragmentType</var>)</span>

1.  If <var>fragmentType</var> is an Object Type:
    1.  if <var>objectType</var> and <var>fragmentType</var> are the same type, return <span class="spec-keyword">true</span>, otherwise return <span class="spec-keyword">false</span>.
2.  If <var>fragmentType</var> is an Interface Type:
    1.  if <var>objectType</var> is an implementation of <var>fragmentType</var>, return <span class="spec-keyword">true</span> otherwise return <span class="spec-keyword">false</span>.
3.  If <var>fragmentType</var> is a Union:
    1.  if <var>objectType</var> is a possible type of <var>fragmentType</var>, return <span class="spec-keyword">true</span> otherwise return <span class="spec-keyword">false</span>.

</div>

The result of evaluating the selection set is the result of evaluating the corresponding grouped field set. The corresponding grouped field set should be evaluated serially if the selection set is being evaluated serially, otherwise it should be evaluated normally.



<section id="sec-Evaluating-a-grouped-field-set">

### <span class="spec-secid" title="link to this section">[6.4](#sec-Evaluating-a-grouped-field-set)</span>Evaluating a grouped field set

The result of evaluating a grouped field set will be an unordered map. There will be an entry in this map for every item in the grouped field set.

<section id="sec-Field-entries">

#### <span class="spec-secid" title="link to this section">[6.4.1](#sec-Field-entries)</span>Field entries

Each item in the grouped field set can potentially create an entry in the result map. That entry in the result map is the result is the result of calling `GetFieldEntry` on the corresponding item in the grouped field set. `GetFieldEntry` can return `null`, which indicates that there should be no entry in the result map for this item. Note that this is distinct from returning an entry with a string key and a null value, which indicates that an entry in the result should be added for that key, and its value should be null.

`GetFieldEntry` assumes the existence of two functions that are not defined in this section of the spec. It is expected that the type system provides these methods:

*   `ResolveFieldOnObject`, which takes an object type, a field, and an object, and returns the result of resolving that field on the object.
*   `GetFieldTypeFromObjectType`, which takes an object type and a field, and returns that field’s type on the object type, or `null` if the field is not valid on the object type.

<div class="spec-algo" id="GetFieldEntry()"><span class="spec-call">[GetFieldEntry](#GetFieldEntry())(<var>objectType</var>, <var>object</var>, <var>fields</var>)</span>

1.  Let <var>firstField</var> be the first entry in the ordered list <var>fields</var>. Note that <var>fields</var> is never empty, as the entry in the grouped field set would not exist if there were no fields.
2.  Let <var>responseKey</var> be the response key of <var>firstField</var>.
3.  Let <var>fieldType</var> be the result of calling <span class="spec-call">[GetFieldTypeFromObjectType](#GetFieldTypeFromObjectType())(<var>objectType</var>, <var>firstField</var>)</span>.
4.  If <var>fieldType</var> is <span class="spec-keyword">null</span>, return <span class="spec-keyword">null</span>, indicating that no entry exists in the result map.
5.  Let <var>resolvedObject</var> be <span class="spec-call">[ResolveFieldOnObject](#ResolveFieldOnObject())(<var>objectType</var>, <var>object</var>, <var>fieldEntry</var>)</span>.
6.  If <var>resolvedObject</var> is <span class="spec-keyword">null</span>, return <span class="spec-call">tuple(<var>responseKey</var>, <span class="spec-keyword">null</span>)</span>, indicating that an entry exists in the result map whose value is `null`.
7.  Let <var>subSelectionSet</var> be the result of calling <span class="spec-call">[MergeSelectionSets](#MergeSelectionSets())(<var>fields</var>)</span>.
8.  Let <var>responseValue</var> be the result of calling <span class="spec-call">[CompleteValue](#CompleteValue())(<var>fieldType</var>, <var>resolvedObject</var>, <var>subSelectionSet</var>)</span>.
9.  Return <span class="spec-call">tuple(<var>responseKey</var>, <var>responseValue</var>)</span>.

</div>

<div class="spec-algo" id="GetFieldTypeFromObjectType()"><span class="spec-call">[GetFieldTypeFromObjectType](#GetFieldTypeFromObjectType())(<var>objectType</var>, <var>firstField</var>)</span>

1.  Call the method provided by the type system for determining the field type on a given object type.

</div>

<div class="spec-algo" id="ResolveFieldOnObject()"><span class="spec-call">[ResolveFieldOnObject](#ResolveFieldOnObject())(<var>objectType</var>, <var>object</var>, <var>firstField</var>)</span>

1.  Call the method provided by the type system for determining the resolution of a field on a given object.

</div>

<div class="spec-algo" id="MergeSelectionSets()"><span class="spec-call">[MergeSelectionSets](#MergeSelectionSets())(<var>fields</var>)</span>

1.  Let <var>selectionSet</var> be an empty list.
2.  For each <var>field</var> in <var>fields</var>:
    1.  Let <var>fieldSelectionSet</var> be the selection set of <var>field</var>.
    2.  If <var>fieldSelectionSet</var> is null or empty, continue to the next field.
    3.  Append all selections in <var>fieldSelectionSet</var> to <var>selectionSet</var>.
3.  Return <var>selectionSet</var>.

</div>

<div class="spec-algo" id="CompleteValue()"><span class="spec-call">[CompleteValue](#CompleteValue())(<var>fieldType</var>, <var>result</var>, <var>subSelectionSet</var>)</span>

1.  If the <var>fieldType</var> is a Non‐Null type:
    1.  Let <var>innerType</var> be the inner type of <var>fieldType</var>.
    2.  Let <var>completedResult</var> be the result of calling <span class="spec-call">[CompleteValue](#CompleteValue())(<var>innerType</var>, <var>result</var>)</span>.
    3.  If <var>completedResult</var> is <span class="spec-keyword">null</span>, throw a field error.
    4.  Return <var>completedResult</var>.
2.  If <var>result</var> is <span class="spec-keyword">null</span> or a value similar to <span class="spec-keyword">null</span> such as <span class="spec-keyword">undefined</span> or <span class="spec-nt">NaN</span>, return <span class="spec-keyword">null</span>.
3.  If <var>fieldType</var> is a List type:
    1.  If <var>result</var> is not a collection of values, throw a field error.
    2.  Let <var>innerType</var> be the inner type of <var>fieldType</var>.
    3.  Return a list where each item is the result of calling <span class="spec-call">[CompleteValue](#CompleteValue())(<var>innerType</var>, <var>resultItem</var>)</span>, where <var>resultItem</var> is each item in <var>result</var>.
4.  If <var>fieldType</var> is a Scalar or Enum type:
    1.  Return the result of “coercing” <var>result</var>, ensuring it is a legal value of <var>fieldType</var>, otherwise <span class="spec-keyword">null</span>.
5.  If <var>fieldType</var> is an Object, Interface, or Union type:
    1.  Return the result of evaluating <var>subSelectionSet</var> on <var>fieldType</var> normally.

</div>



<section id="sec-Normal-evaluation">

#### <span class="spec-secid" title="link to this section">[6.4.2](#sec-Normal-evaluation)</span>Normal evaluation

When evaluating a grouped field set without a serial execution order requirement, the executor can determine the entries in the result map in whatever order it chooses. Because the resolution of fields other than top‐level mutation fields is always side effect–free and idempotent, the execution order must not affect the result, and hence the server has the freedom to evaluate the field entries in whatever order it deems optimal.

For example, given the following grouped field set to be evaluated normally:

```
{
  birthday {
    month
  }
  address {
    street
  }
}

```

A valid GraphQL executor can resolve the four fields in whatever order it chose.



<section id="sec-Serial-execution">

#### <span class="spec-secid" title="link to this section">[6.4.3](#sec-Serial-execution)</span>Serial execution

Observe that based on the above sections, the only time an executor will run in serial execution order is on the top level selection set of a mutation operation and on its corresponding grouped field set.

When evaluating a grouped field set serially, the executor must consider each entry from the grouped field set in the order provided in the grouped field set. It must determine the corresponding entry in the result map for each item to completion before it continues on to the next item in the grouped field set:

For example, given the following selection set to be evaluated serially:

```
{
  changeBirthday(birthday: $newBirthday) {
    month
  }
  changeAddress(address: $newAddress) {
    street
  }
}

```

The executor must, in serial:

*   Run `getFieldEntry` for `changeBirthday`, which during `CompleteValue` will evaluate the `{ month }` sub‐selection set normally.
*   Run `getFieldEntry` for `changeAddress`, which during `CompleteValue` will evaluate the `{ street }` sub‐selection set normally.

As an illustrative example, let’s assume we have a mutation field `changeTheNumber` that returns an object containing one field, `theNumber`. If we execute the following selection set serially:

```
{
  first: changeTheNumber(newNumber: 1) {
    theNumber
  }
  second: changeTheNumber(newNumber: 3) {
    theNumber
  }
  third: changeTheNumber(newNumber: 2) {
    theNumber
  }
}

```

The executor will evaluate the following serially:

*   Resolve the `changeTheNumber(newNumber: 1)` field
*   Evaluate the `{ theNumber }` sub‐selection set of `first` normally
*   Resolve the `changeTheNumber(newNumber: 3)` field
*   Evaluate the `{ theNumber }` sub‐selection set of `second` normally
*   Resolve the `changeTheNumber(newNumber: 2)` field
*   Evaluate the `{ theNumber }` sub‐selection set of `third` normally

A correct executor must generate the following result for that selection set:

```
{
  "first": {
    "theNumber": 1
  },
  "second": {
    "theNumber": 3
  },
  "third": {
    "theNumber": 2
  }
}

```



<section id="sec-Error-handling">

#### <span class="spec-secid" title="link to this section">[6.4.4](#sec-Error-handling)</span>Error handling

If an error occurs when resolving a field, it should be treated as though the field returned null, and an error must be added to the “errors” list in the response.



<section id="sec-Nullability">

#### <span class="spec-secid" title="link to this section">[6.4.5](#sec-Nullability)</span>Nullability

If the result of resolving a field is null (either because the function to resolve the field returned null or because an error occurred), and that field is marked as being non‐null in the type system, then the result of evaluating the entire field set that contains this field is now null.

If the field was null because of an error, then the error has already been logged, and the “errors” list in the response must not be affected.

If the field resolution function returned null, and the field was non‐null, then no error has been logged, so an appropriate error must be added to the “errors” list.







<section id="sec-Response">

## <span class="spec-secid" title="link to this section">[7](#sec-Response)</span>Response

When a GraphQL server receives a request, it must return a well‐formed response. The server’s response describes the result of executing the requested operation if successful, and describes any errors encountered during the request.

A response may contain both a partial response as well as encountered errors in the case that an error occurred on a field which was replaced with null.

<section id="sec-Serialization-Format">

### <span class="spec-secid" title="link to this section">[7.1](#sec-Serialization-Format)</span>Serialization Format

GraphQL does not require a specific serialization format. However, clients should use a serialization format that supports the major primitives in the GraphQL response. In particular, the serialization format must support representations of the following four primitives:

*   Map
*   List
*   String
*   Null

A serialization format may support the following primitives, however, strings may be used as a substitute for those primitives.

*   Boolean
*   Int
*   Float
*   Enum Value

<section id="sec-JSON-Serialization">

#### <span class="spec-secid" title="link to this section">[7.1.1](#sec-JSON-Serialization)</span>JSON Serialization

JSON is the preferred serialization format for GraphQL, though as noted above, GraphQL does not require a specific serialization format. For consistency and ease of notation, examples of the response are given in JSON throughout the spec. In particular, in our JSON examples, we will represent primitives using the following JSON concepts:

| GraphQL Value | JSON Value |
| --- | --- |
| Map | Object |
| List | Array |
| Null | <span class="spec-keyword">null</span> |
| String | String |
| Boolean | <span class="spec-keyword">true</span> or <span class="spec-keyword">false</span> |
| Int | Number |
| Float | Number |
| Enum Value | String |





<section id="sec-Response-Format">

### <span class="spec-secid" title="link to this section">[7.2](#sec-Response-Format)</span>Response Format

A response to a GraphQL operation must be a map.

If the operation included execution, the response map must contain an entry with key `data`. The value of this entry is described in the “Data” section. If the operation failed before execution, due to a syntax error, missing information, or validation error, this entry must not be present.

If the operation encountered any errors, the response map must contain an entry with key `errors`. The value of this entry is described in the “Errors” section. If the operation completed without encountering any errors, this entry must not be present.

The response map may also contain an entry with key `extensions`. This entry, if set, must have a map as its value. This entry is reserved for implementors to extend the protocol however they see fit, and hence there are no additional restrictions on its contents.

To ensure future changes to the protocol do not break existing servers and clients, the top level response map must not contain any entries other than the three described above.

<section id="sec-Data">

#### <span class="spec-secid" title="link to this section">[7.2.1](#sec-Data)</span>Data

The `data` entry in the response will be the result of the execution of the requested operation. If the operation was a query, this output will be an object of the schema’s query root type; if the operation was a mutation, this output will be an object of the schema’s mutation root type.

If an error was encountered before execution begins, the `data` entry should not be present in the result.

If an error was encountered during the execution that prevented a valid response, the `data` entry in the response should be `null`.



<section id="sec-Errors">

#### <span class="spec-secid" title="link to this section">[7.2.2](#sec-Errors)</span>Errors

The `errors` entry in the response is a non‐empty list of errors, where each error is a map.

If no errors were encountered during the requested operation, the `errors` entry should not be present in the result.

Every error must contain an entry with the key `message` with a string description of the error intended for the developer as a guide to understand and correct the error.

If an error can be associated to a particular point in the requested GraphQL document, it should contain an entry with the key `locations` with a list of locations, where each location is a map with the keys `line` and `column`, both positive numbers starting from `1` which describe the beginning of an associated syntax element.

GraphQL servers may provide additional entries to error as they choose to produce more helpful or machine‐readable errors, however future versions of the spec may describe additional entries to errors.

If the `data` entry in the response is `null` or not present, the `errors` entry in the response must not be empty. It must contain at least one error. The errors it contains should indicate why no data was able to be returned.

If the `data` entry in the response is not `null`, the `errors` entry in the response may contain any errors that occurred during execution. If errors occurred during execution, it should contain those errors.







<section id="sec-Appendix-Notation-Conventions">

## <span class="spec-secid" title="link to this section">[A](#sec-Appendix-Notation-Conventions)</span>Appendix: Notation Conventions

This specification document contains a number of notation conventions used to describe technical concepts such as language grammar and semantics as well as runtime algorithms.

This appendix seeks to explain these notations in greater detail to avoid ambiguity.

<section id="sec-Context-Free-Grammar">

### <span class="spec-secid" title="link to this section">[A.1](#sec-Context-Free-Grammar)</span>Context-Free Grammar

A context‐free grammar consists of a number of productions. Each production has an abstract symbol called a “non‐terminal” as its left‐hand side, and zero or more possible sequences of non‐terminal symbols and or terminal characters as its right‐hand side.

Starting from a single goal non‐terminal symbol, a context‐free grammar describes a language: the set of possible sequences of characters that can be described by repeatedly replacing any non‐terminal in the goal sequence with one of the sequences it is defined by, until all non‐terminal symbols have been replaced by terminal characters.

Terminals are represented in this document in a monospace font in two forms: a specific unicode character or sequence of unicode characters (ex. <span class="spec-t">=</span> or <span class="spec-t">terminal</span>), and a pattern of unicode characters defined by a regular expression (ex <span class="spec-rx">/[0-9]+/</span>).

Non‐terminal production rules are represented in this document using the following notation for a non‐terminal with a single definition:

<div class="spec-production" id="NonTerminalWithSingleDefinition"><span class="spec-nt">[NonTerminalWithSingleDefinition](#NonTerminalWithSingleDefinition)</span>

<div class="spec-rhs"><span class="spec-nt">NonTerminal</span><span class="spec-t">terminal</span></div>

</div>

While using the following notation for a production with a list of definitions:

<div class="spec-production" id="NonTerminalWithManyDefinitions"><span class="spec-nt">[NonTerminalWithManyDefinitions](#NonTerminalWithManyDefinitions)</span>

<div class="spec-rhs"><span class="spec-nt">OtherNonTerminal</span><span class="spec-t">terminal</span></div>

<div class="spec-rhs"><span class="spec-t">terminal</span></div>

</div>

A definition may refer to itself, which describes repetitive sequences, for example:

<div class="spec-production" id="ListOfLetterA"><span class="spec-nt">[ListOfLetterA](#ListOfLetterA)</span>

<div class="spec-rhs"><span class="spec-t">a</span></div>

<div class="spec-rhs"><span class="spec-nt">[ListOfLetterA](#ListOfLetterA)</span><span class="spec-t">a</span></div>

</div>



<section id="sec-Lexical-and-Syntactical-Grammar">

### <span class="spec-secid" title="link to this section">[A.2](#sec-Lexical-and-Syntactical-Grammar)</span>Lexical and Syntactical Grammar

The GraphQL language is defined in a syntactic grammar where terminal symbols are tokens. Tokens are defined in a lexical grammar which matches patterns of source characters. The result of parsing a sequence of source unicode characters produces a GraphQL AST.

A Lexical grammar production describes non‐terminal “tokens” by patterns of terminal unicode characters. No “whitespace” or other ignored characters may appear between any terminal unicode characters in the lexical grammar production. A lexical grammar production is distinguished by a two colon `::` definition.

<div class="spec-production d2" id="Word"><span class="spec-nt">[Word](#Word)</span>

<div class="spec-rhs"><span class="spec-rx">/[A-Za-z]+/</span></div>

</div>

A Syntactical grammar production describes non‐terminal “rules” by patterns of terminal Tokens. Whitespace and other ignored characters may appear before or after any terminal Token. A syntactical grammar production is distinguished by a one colon `:` definition.

<div class="spec-production" id="Sentence"><span class="spec-nt">[Sentence](#Sentence)</span>

<div class="spec-rhs"><span class="spec-nt">Noun</span><span class="spec-nt">Verb</span></div>

</div>



<section id="sec-Grammar-Notation">

### <span class="spec-secid" title="link to this section">[A.3](#sec-Grammar-Notation)</span>Grammar Notation

This specification uses some additional notation to describe common patterns, such as optional or repeated patterns, or parameterized alterations of the definition of a non‐terminal. This section explains these short‐hand notations and their expanded definitions in the context‐free grammar.

**Constraints**

A grammar production may specify that certain expansions are not permitted by using the phrase “but not” and then indicating the expansions to be excluded.

For example, the production:

<div class="spec-production" id="SafeName"><span class="spec-nt">[SafeName](#SafeName)</span>

<div class="spec-rhs"><span class="spec-constrained"><span class="spec-nt">[Name](#Name)</span><span class="spec-butnot"><span class="spec-nt">SevenCarlinWords</span></span></span></div>

</div>

means that the nonterminal <span class="spec-nt">[SafeName](#SafeName)</span> may be replaced by any sequence of characters that could replace <span class="spec-nt">[Name](#Name)</span> provided that the same sequence of characters could not replace <span class="spec-nt">SevenCarlinWords</span>.

A grammar may also list a number of restrictions after “but not” seperated by “or”.

For example:

<div class="spec-production" id="NonBooleanName"><span class="spec-nt">[NonBooleanName](#NonBooleanName)</span>

<div class="spec-rhs"><span class="spec-constrained"><span class="spec-nt">[Name](#Name)</span><span class="spec-butnot"><span class="spec-t">true</span><span class="spec-t">false</span></span></span></div>

</div>

**Optionality and Lists**

A subscript suffix “<span class="spec-nt optional">Symbol<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span>” is shorthand for two possible sequences, one including that symbol and one excluding it.

As an example:

<div class="spec-production" id="Sentence"><span class="spec-nt">[Sentence](#Sentence)</span>

<div class="spec-rhs"><span class="spec-nt">Noun</span><span class="spec-nt">Verb</span><span class="spec-nt optional">Adverb<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span></div>

</div>

is shorthand for

<div class="spec-production" id="Sentence"><span class="spec-nt">[Sentence](#Sentence)</span>

<div class="spec-rhs"><span class="spec-nt">Noun</span><span class="spec-nt">Verb</span></div>

<div class="spec-rhs"><span class="spec-nt">Noun</span><span class="spec-nt">Verb</span><span class="spec-nt">Adverb</span></div>

</div>

A subscript suffix “<span class="spec-nt list">Symbol<span class="spec-mods"><span class="spec-mod list">list</span></span></span>” is shorthand for a list of one or more of that symbol.

As an example:

<div class="spec-production" id="Book"><span class="spec-nt">[Book](#Book)</span>

<div class="spec-rhs"><span class="spec-nt">Cover</span><span class="spec-nt list">Page<span class="spec-mods"><span class="spec-mod list">list</span></span></span><span class="spec-nt">Cover</span></div>

</div>

is shorthand for

<div class="spec-production" id="Book"><span class="spec-nt">[Book](#Book)</span>

<div class="spec-rhs"><span class="spec-nt">Cover</span><span class="spec-nt">[Page_list](#Page_list)</span><span class="spec-nt">Cover</span></div>

</div>

<div class="spec-production" id="Page_list"><span class="spec-nt">[Page_list](#Page_list)</span>

<div class="spec-rhs"><span class="spec-nt">Page</span></div>

<div class="spec-rhs"><span class="spec-nt">[Page_list](#Page_list)</span><span class="spec-nt">Page</span></div>

</div>

**Parameterized Grammar Productions**

A symbol definition subscript suffix parameter in braces “<span class="spec-nt">Symbol<span class="spec-mods"><span class="spec-params"><span class="spec-param">Param</span></span></span></span>” is shorthand for two symbol definitions, one appended with that parameter name, the other without. The same subscript suffix on a symbol is shorthand for that variant of the definition. If the parameter starts with “?”, that form of the symbol is used if in a symbol definition with the same parameter. Some possible sequences can be included or excluded conditionally when respectively prefixed with “[+Param]” and “[~Param]”.

As an example:

<div class="spec-production" id="Example"><span class="spec-nt">[Example](#Example)<span class="spec-mods"><span class="spec-params"><span class="spec-param">Param</span></span></span></span>

<div class="spec-rhs"><span class="spec-nt">A</span></div>

<div class="spec-rhs"><span class="spec-nt">B<span class="spec-mods"><span class="spec-params"><span class="spec-param">Param</span></span></span></span></div>

<div class="spec-rhs"><span class="spec-nt">C<span class="spec-mods"><span class="spec-params"><span class="spec-param conditional">Param</span></span></span></span></div>

<div class="spec-rhs"><span class="spec-condition">Param</span><span class="spec-nt">D</span></div>

<div class="spec-rhs"><span class="spec-condition not">Param</span><span class="spec-nt">E</span></div>

</div>

is shorthand for

<div class="spec-production" id="Example"><span class="spec-nt">[Example](#Example)</span>

<div class="spec-rhs"><span class="spec-nt">A</span></div>

<div class="spec-rhs"><span class="spec-nt">B_param</span></div>

<div class="spec-rhs"><span class="spec-nt">C</span></div>

<div class="spec-rhs"><span class="spec-nt">E</span></div>

</div>

<div class="spec-production" id="Example_param"><span class="spec-nt">[Example_param](#Example_param)</span>

<div class="spec-rhs"><span class="spec-nt">A</span></div>

<div class="spec-rhs"><span class="spec-nt">B_param</span></div>

<div class="spec-rhs"><span class="spec-nt">C_param</span></div>

<div class="spec-rhs"><span class="spec-nt">D</span></div>

</div>



<section id="sec-Grammar-Semantics">

### <span class="spec-secid" title="link to this section">[A.4](#sec-Grammar-Semantics)</span>Grammar Semantics

This specification describes the semantic value of many grammar productions in the form of a list of algorithmic steps.

For example, this describes how a parser should interpret a unicode escape sequence which appears in a string literal:

<div class="spec-semantic d2"><span class="spec-nt">[EscapedUnicode](#EscapedUnicode)</span>

<div class="spec-rhs"><span class="spec-t">u</span><span class="spec-rx">/[0-9A-Fa-f]{4}/</span></div>

1.  Let <var>codePoint</var> be the number represented by the four‐digit hexidecimal sequence.
2.  The string value is the unicode character represented by <var>codePoint</var>.

</div>



<section id="sec-Algorithms">

### <span class="spec-secid" title="link to this section">[A.5](#sec-Algorithms)</span>Algorithms

This specification describes some algorithms used by the static and runtime semantics, they’re defined in the form of a function‐like syntax along with a list of algorithmic steps to take.

For example, this describes if a fragment should be spread into place given a runtime <var>objectType</var> and the fragment’s <var>fragmentType</var>:

<div class="spec-algo" id="doesFragmentTypeApply()"><span class="spec-call">[doesFragmentTypeApply](#doesFragmentTypeApply())(<var>objectType</var>, <var>fragmentType</var>)</span>

1.  If <var>fragmentType</var> is an Object Type:
    1.  if <var>objectType</var> and <var>fragmentType</var> are the same type, return <span class="spec-keyword">true</span>, otherwise return <span class="spec-keyword">false</span>.
2.  If <var>fragmentType</var> is an Interface Type:
    1.  if <var>objectType</var> is an implementation of <var>fragmentType</var>, return <span class="spec-keyword">true</span> otherwise return <span class="spec-keyword">false</span>.
3.  If <var>fragmentType</var> is a Union:
    1.  if <var>objectType</var> is a possible type of <var>fragmentType</var>, return <span class="spec-keyword">true</span> otherwise return <span class="spec-keyword">false</span>.

</div>





<section id="sec-Appendix-Grammar-Summary">

## <span class="spec-secid" title="link to this section">[B](#sec-Appendix-Grammar-Summary)</span>Appendix: Grammar Summary

<div class="spec-production d2" id="SourceCharacter"><span class="spec-nt">[SourceCharacter](#SourceCharacter)</span>

<div class="spec-rhs"><span class="spec-prose">Any Unicode code point</span></div>

</div>

<section id="sec-Appendix-Grammar-Summary.Ignored-Tokens">

### <span class="spec-secid" title="link to this section">[B.1](#sec-Appendix-Grammar-Summary.Ignored-Tokens)</span>Ignored Tokens

<div class="spec-production d2" id="Ignored"><span class="spec-nt">[Ignored](#Ignored)</span>

<div class="spec-rhs"><span class="spec-nt">[WhiteSpace](#WhiteSpace)</span></div>

<div class="spec-rhs"><span class="spec-nt">[LineTerminator](#LineTerminator)</span></div>

<div class="spec-rhs"><span class="spec-nt">[Comment](#Comment)</span></div>

<div class="spec-rhs"><span class="spec-nt">[Comma](#Comma)</span></div>

</div>

<div class="spec-production d2" id="WhiteSpace"><span class="spec-nt">[WhiteSpace](#WhiteSpace)</span>

<div class="spec-rhs"><span class="spec-prose">Horizontal Tab (U+0009)</span></div>

<div class="spec-rhs"><span class="spec-prose">Vertical Tab (U+000B)</span></div>

<div class="spec-rhs"><span class="spec-prose">Form Feed (U+000C)</span></div>

<div class="spec-rhs"><span class="spec-prose">Space (U+0020)</span></div>

<div class="spec-rhs"><span class="spec-prose">No-break Space (U+00A0)</span></div>

</div>

<div class="spec-production d2" id="LineTerminator"><span class="spec-nt">[LineTerminator](#LineTerminator)</span>

<div class="spec-rhs"><span class="spec-prose">New Line (U+000A)</span></div>

<div class="spec-rhs"><span class="spec-prose">Carriage Return (U+000D)</span></div>

<div class="spec-rhs"><span class="spec-prose">Line Separator (U+2028)</span></div>

<div class="spec-rhs"><span class="spec-prose">Paragraph Separator (U+2029)</span></div>

</div>

<div class="spec-production d2" id="Comment"><span class="spec-nt">[Comment](#Comment)</span>

<div class="spec-rhs"><span class="spec-t">#</span><span class="spec-nt list optional">[CommentChar](#CommentChar)<span class="spec-mods"><span class="spec-mod list">list</span><span class="spec-mod optional">opt</span></span></span></div>

</div>

<div class="spec-production d2" id="CommentChar"><span class="spec-nt">[CommentChar](#CommentChar)</span>

<div class="spec-rhs"><span class="spec-constrained"><span class="spec-nt">[SourceCharacter](#SourceCharacter)</span><span class="spec-butnot"><span class="spec-nt">[LineTerminator](#LineTerminator)</span></span></span></div>

</div>

<div class="spec-production d2" id="Comma"><span class="spec-nt">[Comma](#Comma)</span>

<div class="spec-rhs"><span class="spec-t">,</span></div>

</div>



<section id="sec-Appendix-Grammar-Summary.Lexical-Tokens">

### <span class="spec-secid" title="link to this section">[B.2](#sec-Appendix-Grammar-Summary.Lexical-Tokens)</span>Lexical Tokens

<div class="spec-production d2" id="Token"><span class="spec-nt">[Token](#Token)</span>

<div class="spec-rhs"><span class="spec-nt">[Punctuator](#Punctuator)</span></div>

<div class="spec-rhs"><span class="spec-nt">[Name](#Name)</span></div>

<div class="spec-rhs"><span class="spec-nt">[IntValue](#IntValue)</span></div>

<div class="spec-rhs"><span class="spec-nt">[FloatValue](#FloatValue)</span></div>

<div class="spec-rhs"><span class="spec-nt">[StringValue](#StringValue)</span></div>

</div>

<div class="spec-production d2" id="Punctuator"><span class="spec-nt">[Punctuator](#Punctuator)</span>

<div class="spec-oneof">

| <span class="spec-t">!</span> | <span class="spec-t">$</span> | <span class="spec-t">(</span> | <span class="spec-t">)</span> | <span class="spec-t">...</span> | <span class="spec-t">:</span> | <span class="spec-t">=</span> | <span class="spec-t">@</span> | <span class="spec-t">[</span> | <span class="spec-t">]</span> | <span class="spec-t">{</span> | <span class="spec-t">|</span> | <span class="spec-t">}</span> |

</div>

</div>

<div class="spec-production d2" id="Name"><span class="spec-nt">[Name](#Name)</span>

<div class="spec-rhs"><span class="spec-rx">/[_A-Za-z][_0-9A-Za-z]*/</span></div>

</div>

<div class="spec-production d2" id="IntValue"><span class="spec-nt">[IntValue](#IntValue)</span>

<div class="spec-rhs"><span class="spec-nt">[IntegerPart](#IntegerPart)</span></div>

</div>

<div class="spec-production d2" id="IntegerPart"><span class="spec-nt">[IntegerPart](#IntegerPart)</span>

<div class="spec-rhs"><span class="spec-nt optional">[NegativeSign](#NegativeSign)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-t">0</span></div>

<div class="spec-rhs"><span class="spec-nt optional">[NegativeSign](#NegativeSign)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt">[NonZeroDigit](#NonZeroDigit)</span><span class="spec-nt list optional">[Digit](#Digit)<span class="spec-mods"><span class="spec-mod list">list</span><span class="spec-mod optional">opt</span></span></span></div>

</div>

<div class="spec-production d2" id="NegativeSign"><span class="spec-nt">[NegativeSign](#NegativeSign)</span>

<div class="spec-rhs"><span class="spec-t">-</span></div>

</div>

<div class="spec-production d2" id="Digit"><span class="spec-nt">[Digit](#Digit)</span>

<div class="spec-oneof">

| <span class="spec-t">0</span> | <span class="spec-t">1</span> | <span class="spec-t">2</span> | <span class="spec-t">3</span> | <span class="spec-t">4</span> | <span class="spec-t">5</span> | <span class="spec-t">6</span> | <span class="spec-t">7</span> | <span class="spec-t">8</span> | <span class="spec-t">9</span> |

</div>

</div>

<div class="spec-production d2" id="NonZeroDigit"><span class="spec-nt">[NonZeroDigit](#NonZeroDigit)</span>

<div class="spec-rhs"><span class="spec-constrained"><span class="spec-nt">[Digit](#Digit)</span><span class="spec-butnot"><span class="spec-t">0</span></span></span></div>

</div>

<div class="spec-production d2" id="FloatValue"><span class="spec-nt">[FloatValue](#FloatValue)</span>

<div class="spec-rhs"><span class="spec-nt">[IntegerPart](#IntegerPart)</span><span class="spec-nt">[FractionalPart](#FractionalPart)</span></div>

<div class="spec-rhs"><span class="spec-nt">[IntegerPart](#IntegerPart)</span><span class="spec-nt">[ExponentPart](#ExponentPart)</span></div>

<div class="spec-rhs"><span class="spec-nt">[IntegerPart](#IntegerPart)</span><span class="spec-nt">[FractionalPart](#FractionalPart)</span><span class="spec-nt">[ExponentPart](#ExponentPart)</span></div>

</div>

<div class="spec-production d2" id="FractionalPart"><span class="spec-nt">[FractionalPart](#FractionalPart)</span>

<div class="spec-rhs"><span class="spec-t">.</span><span class="spec-nt list">[Digit](#Digit)<span class="spec-mods"><span class="spec-mod list">list</span></span></span></div>

</div>

<div class="spec-production d2" id="ExponentPart"><span class="spec-nt">[ExponentPart](#ExponentPart)</span>

<div class="spec-rhs"><span class="spec-nt">[ExponentIndicator](#ExponentIndicator)</span><span class="spec-nt optional">[Sign](#Sign)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt list">[Digit](#Digit)<span class="spec-mods"><span class="spec-mod list">list</span></span></span></div>

</div>

<div class="spec-production d2" id="ExponentIndicator"><span class="spec-nt">[ExponentIndicator](#ExponentIndicator)</span>

<div class="spec-oneof">

| <span class="spec-t">e</span> | <span class="spec-t">E</span> |

</div>

</div>

<div class="spec-production d2" id="Sign"><span class="spec-nt">[Sign](#Sign)</span>

<div class="spec-oneof">

| <span class="spec-t">+</span> | <span class="spec-t">-</span> |

</div>

</div>

<div class="spec-production d2" id="StringValue"><span class="spec-nt">[StringValue](#StringValue)</span>

<div class="spec-rhs"><span class="spec-t">""</span></div>

<div class="spec-rhs"><span class="spec-t">"</span><span class="spec-nt list">[StringCharacter](#StringCharacter)<span class="spec-mods"><span class="spec-mod list">list</span></span></span><span class="spec-t">"</span></div>

</div>

<div class="spec-production d2" id="StringCharacter"><span class="spec-nt">[StringCharacter](#StringCharacter)</span>

<div class="spec-rhs"><span class="spec-constrained"><span class="spec-nt">[SourceCharacter](#SourceCharacter)</span><span class="spec-butnot"><span class="spec-t">"</span><span class="spec-t">\</span><span class="spec-nt">[LineTerminator](#LineTerminator)</span></span></span></div>

<div class="spec-rhs"><span class="spec-t">\</span><span class="spec-nt">[EscapedUnicode](#EscapedUnicode)</span></div>

<div class="spec-rhs"><span class="spec-t">\</span><span class="spec-nt">[EscapedCharacter](#EscapedCharacter)</span></div>

</div>

<div class="spec-production d2" id="EscapedUnicode"><span class="spec-nt">[EscapedUnicode](#EscapedUnicode)</span>

<div class="spec-rhs"><span class="spec-t">u</span><span class="spec-rx">/[0-9A-Fa-f]{4}/</span></div>

</div>

<div class="spec-production d2" id="EscapedCharacter"><span class="spec-nt">[EscapedCharacter](#EscapedCharacter)</span>

<div class="spec-oneof">

| <span class="spec-t">"</span> | <span class="spec-t">\</span> | <span class="spec-t">/</span> | <span class="spec-t">b</span> | <span class="spec-t">f</span> | <span class="spec-t">n</span> | <span class="spec-t">r</span> | <span class="spec-t">t</span> |

</div>

</div>



<section id="sec-Appendix-Grammar-Summary.Query-Document">

### <span class="spec-secid" title="link to this section">[B.3](#sec-Appendix-Grammar-Summary.Query-Document)</span>Query Document

<div class="spec-production" id="Document"><span class="spec-nt">[Document](#Document)</span>

<div class="spec-rhs"><span class="spec-nt list">[Definition](#Definition)<span class="spec-mods"><span class="spec-mod list">list</span></span></span></div>

</div>

<div class="spec-production" id="Definition"><span class="spec-nt">[Definition](#Definition)</span>

<div class="spec-rhs"><span class="spec-nt">[OperationDefinition](#OperationDefinition)</span></div>

<div class="spec-rhs"><span class="spec-nt">[FragmentDefinition](#FragmentDefinition)</span></div>

</div>

<div class="spec-production" id="OperationDefinition"><span class="spec-nt">[OperationDefinition](#OperationDefinition)</span>

<div class="spec-rhs"><span class="spec-nt">[SelectionSet](#SelectionSet)</span></div>

<div class="spec-rhs"><span class="spec-nt">[OperationType](#OperationType)</span><span class="spec-nt">[Name](#Name)</span><span class="spec-nt optional">[VariableDefinitions](#VariableDefinitions)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt optional">[Directives](#Directives)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt">[SelectionSet](#SelectionSet)</span></div>

</div>

<div class="spec-production" id="OperationType"><span class="spec-nt">[OperationType](#OperationType)</span>

<div class="spec-oneof">

| <span class="spec-t">query</span> | <span class="spec-t">mutation</span> |

</div>

</div>

<div class="spec-production" id="SelectionSet"><span class="spec-nt">[SelectionSet](#SelectionSet)</span>

<div class="spec-rhs"><span class="spec-t">{</span><span class="spec-nt list">[Selection](#Selection)<span class="spec-mods"><span class="spec-mod list">list</span></span></span><span class="spec-t">}</span></div>

</div>

<div class="spec-production" id="Selection"><span class="spec-nt">[Selection](#Selection)</span>

<div class="spec-rhs"><span class="spec-nt">[Field](#Field)</span></div>

<div class="spec-rhs"><span class="spec-nt">[FragmentSpread](#FragmentSpread)</span></div>

<div class="spec-rhs"><span class="spec-nt">[InlineFragment](#InlineFragment)</span></div>

</div>

<div class="spec-production" id="Field"><span class="spec-nt">[Field](#Field)</span>

<div class="spec-rhs"><span class="spec-nt optional">[Alias](#Alias)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt">[Name](#Name)</span><span class="spec-nt optional">[Arguments](#Arguments)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt optional">[Directives](#Directives)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt optional">[SelectionSet](#SelectionSet)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span></div>

</div>

<div class="spec-production" id="Alias"><span class="spec-nt">[Alias](#Alias)</span>

<div class="spec-rhs"><span class="spec-nt">[Name](#Name)</span><span class="spec-t">:</span></div>

</div>

<div class="spec-production" id="Arguments"><span class="spec-nt">[Arguments](#Arguments)</span>

<div class="spec-rhs"><span class="spec-t">(</span><span class="spec-nt list">[Argument](#Argument)<span class="spec-mods"><span class="spec-mod list">list</span></span></span><span class="spec-t">)</span></div>

</div>

<div class="spec-production" id="Argument"><span class="spec-nt">[Argument](#Argument)</span>

<div class="spec-rhs"><span class="spec-nt">[Name](#Name)</span><span class="spec-t">:</span><span class="spec-nt">[Value](#Value)</span></div>

</div>

<div class="spec-production" id="FragmentSpread"><span class="spec-nt">[FragmentSpread](#FragmentSpread)</span>

<div class="spec-rhs"><span class="spec-t">...</span><span class="spec-nt">[FragmentName](#FragmentName)</span><span class="spec-nt optional">[Directives](#Directives)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span></div>

</div>

<div class="spec-production" id="InlineFragment"><span class="spec-nt">[InlineFragment](#InlineFragment)</span>

<div class="spec-rhs"><span class="spec-t">...</span><span class="spec-t">on</span><span class="spec-nt">[TypeCondition](#TypeCondition)</span><span class="spec-nt optional">[Directives](#Directives)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt">[SelectionSet](#SelectionSet)</span></div>

</div>

<div class="spec-production" id="FragmentDefinition"><span class="spec-nt">[FragmentDefinition](#FragmentDefinition)</span>

<div class="spec-rhs"><span class="spec-t">fragment</span><span class="spec-nt">[FragmentName](#FragmentName)</span><span class="spec-t">on</span><span class="spec-nt">[TypeCondition](#TypeCondition)</span><span class="spec-nt optional">[Directives](#Directives)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span><span class="spec-nt">[SelectionSet](#SelectionSet)</span></div>

</div>

<div class="spec-production" id="FragmentName"><span class="spec-nt">[FragmentName](#FragmentName)</span>

<div class="spec-rhs"><span class="spec-constrained"><span class="spec-nt">[Name](#Name)</span><span class="spec-butnot"><span class="spec-t">on</span></span></span></div>

</div>

<div class="spec-production" id="TypeCondition"><span class="spec-nt">[TypeCondition](#TypeCondition)</span>

<div class="spec-rhs"><span class="spec-nt">[NamedType](#NamedType)</span></div>

</div>

<div class="spec-production" id="Value"><span class="spec-nt">[Value](#Value)<span class="spec-mods"><span class="spec-params"><span class="spec-param">Const</span></span></span></span>

<div class="spec-rhs"><span class="spec-condition not">Const</span><span class="spec-nt">[Variable](#Variable)</span></div>

<div class="spec-rhs"><span class="spec-nt">[IntValue](#IntValue)</span></div>

<div class="spec-rhs"><span class="spec-nt">[FloatValue](#FloatValue)</span></div>

<div class="spec-rhs"><span class="spec-nt">[StringValue](#StringValue)</span></div>

<div class="spec-rhs"><span class="spec-nt">[BooleanValue](#BooleanValue)</span></div>

<div class="spec-rhs"><span class="spec-nt">[EnumValue](#EnumValue)</span></div>

<div class="spec-rhs"><span class="spec-nt">[ListValue](#ListValue)<span class="spec-mods"><span class="spec-params"><span class="spec-param conditional">Const</span></span></span></span></div>

<div class="spec-rhs"><span class="spec-nt">[ObjectValue](#ObjectValue)<span class="spec-mods"><span class="spec-params"><span class="spec-param conditional">Const</span></span></span></span></div>

</div>

<div class="spec-production" id="BooleanValue"><span class="spec-nt">[BooleanValue](#BooleanValue)</span>

<div class="spec-oneof">

| <span class="spec-t">true</span> | <span class="spec-t">false</span> |

</div>

</div>

<div class="spec-production" id="EnumValue"><span class="spec-nt">[EnumValue](#EnumValue)</span>

<div class="spec-rhs"><span class="spec-constrained"><span class="spec-nt">[Name](#Name)</span><span class="spec-butnot"><span class="spec-t">true</span><span class="spec-t">false</span><span class="spec-t">null</span></span></span></div>

</div>

<div class="spec-production" id="ListValue"><span class="spec-nt">[ListValue](#ListValue)<span class="spec-mods"><span class="spec-params"><span class="spec-param">Const</span></span></span></span>

<div class="spec-rhs"><span class="spec-t">[</span><span class="spec-t">]</span></div>

<div class="spec-rhs"><span class="spec-t">[</span><span class="spec-nt list">[Value](#Value)<span class="spec-mods"><span class="spec-params"><span class="spec-param conditional">Const</span></span><span class="spec-mod list">list</span></span></span><span class="spec-t">]</span></div>

</div>

<div class="spec-production" id="ObjectValue"><span class="spec-nt">[ObjectValue](#ObjectValue)<span class="spec-mods"><span class="spec-params"><span class="spec-param">Const</span></span></span></span>

<div class="spec-rhs"><span class="spec-t">{</span><span class="spec-t">}</span></div>

<div class="spec-rhs"><span class="spec-t">{</span><span class="spec-nt list">[ObjectField](#ObjectField)<span class="spec-mods"><span class="spec-params"><span class="spec-param conditional">Const</span></span><span class="spec-mod list">list</span></span></span><span class="spec-t">}</span></div>

</div>

<div class="spec-production" id="ObjectField"><span class="spec-nt">[ObjectField](#ObjectField)<span class="spec-mods"><span class="spec-params"><span class="spec-param">Const</span></span></span></span>

<div class="spec-rhs"><span class="spec-nt">[Name](#Name)</span><span class="spec-t">:</span><span class="spec-nt">[Value](#Value)<span class="spec-mods"><span class="spec-params"><span class="spec-param conditional">Const</span></span></span></span></div>

</div>

<div class="spec-production" id="VariableDefinitions"><span class="spec-nt">[VariableDefinitions](#VariableDefinitions)</span>

<div class="spec-rhs"><span class="spec-t">(</span><span class="spec-nt list">[VariableDefinition](#VariableDefinition)<span class="spec-mods"><span class="spec-mod list">list</span></span></span><span class="spec-t">)</span></div>

</div>

<div class="spec-production" id="VariableDefinition"><span class="spec-nt">[VariableDefinition](#VariableDefinition)</span>

<div class="spec-rhs"><span class="spec-nt">[Variable](#Variable)</span><span class="spec-t">:</span><span class="spec-nt">[Type](#Type)</span><span class="spec-nt optional">[DefaultValue](#DefaultValue)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span></div>

</div>

<div class="spec-production" id="Variable"><span class="spec-nt">[Variable](#Variable)</span>

<div class="spec-rhs"><span class="spec-t">$</span><span class="spec-nt">[Name](#Name)</span></div>

</div>

<div class="spec-production" id="DefaultValue"><span class="spec-nt">[DefaultValue](#DefaultValue)</span>

<div class="spec-rhs"><span class="spec-t">=</span><span class="spec-nt">[Value](#Value)<span class="spec-mods"><span class="spec-params"><span class="spec-param">Const</span></span></span></span></div>

</div>

<div class="spec-production" id="Type"><span class="spec-nt">[Type](#Type)</span>

<div class="spec-rhs"><span class="spec-nt">[NamedType](#NamedType)</span></div>

<div class="spec-rhs"><span class="spec-nt">[ListType](#ListType)</span></div>

<div class="spec-rhs"><span class="spec-nt">[NonNullType](#NonNullType)</span></div>

</div>

<div class="spec-production" id="NamedType"><span class="spec-nt">[NamedType](#NamedType)</span>

<div class="spec-rhs"><span class="spec-nt">[Name](#Name)</span></div>

</div>

<div class="spec-production" id="ListType"><span class="spec-nt">[ListType](#ListType)</span>

<div class="spec-rhs"><span class="spec-t">[</span><span class="spec-nt">[Type](#Type)</span><span class="spec-t">]</span></div>

</div>

<div class="spec-production" id="NonNullType"><span class="spec-nt">[NonNullType](#NonNullType)</span>

<div class="spec-rhs"><span class="spec-nt">[NamedType](#NamedType)</span><span class="spec-t">!</span></div>

<div class="spec-rhs"><span class="spec-nt">[ListType](#ListType)</span><span class="spec-t">!</span></div>

</div>

<div class="spec-production" id="Directives"><span class="spec-nt">[Directives](#Directives)</span>

<div class="spec-rhs"><span class="spec-nt list">[Directive](#Directive)<span class="spec-mods"><span class="spec-mod list">list</span></span></span></div>

</div>

<div class="spec-production" id="Directive"><span class="spec-nt">[Directive](#Directive)</span>

<div class="spec-rhs"><span class="spec-t">@</span><span class="spec-nt">[Name](#Name)</span><span class="spec-nt optional">[Arguments](#Arguments)<span class="spec-mods"><span class="spec-mod optional">opt</span></span></span></div>

</div>





<footer>Written in [Spec Markdown](http://leebyron.com/spec-md/).</footer>