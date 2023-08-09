---
title: "a-review-of-all-most-common-api-editor-API-Specification-Automated-Testing-Documentation-Generation"
meta_title: ""
description: "this is meta description"
date: 2012-2-23T17:40:12Z
image: "/images/image-placeholder.png"
categories: ["工作"]
author: "haisheng"
tags: ["医疗信息标准", "译文","HIT","Keith Boone"]
draft: false
---


需求
* 1、DSL：要能够使用DSL来描述定义API
* 2、DSL编辑工具：要有易用的编辑工具来编写API定义
* 3、API的校验：最终的AP定义要能够可执行，可以用来确认API的动作 最好是cURL或者浏览器的服务交互来分析请求响应
* 4、API文档：从API定义中可以自动生成文档
* 5、解析器：支持多种语言，能从IDL中生成客户端代码，java、js、php、ruby、python等
* 6、范例：丰富的范例，简单的或者复杂情况的模板帮助新手上手

| 名称          | 优点                                                                                                                                                                                                                                                | 缺点                                                                 | 总结 |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------|:-----|
| RAML          | YAML；使用JSON Schema来定义请求响应的body；支持在markdown中内嵌文档；能够区分application/x-www-form-urlencoded and multipart/form-data requests；能够全面的描述API；SoapUI的插件支持API校验；API console和RAML2HTML支持文档的生成；多种语言的parser | Ruby parser 不成熟；RAML本身很新；没有客户端代码生成；测试插件不成熟 |      |
| API-Blueprint | Markdown; 使用Dredd来做API校验；API platform支持文档生成；支持本地生成文档无需发布；                                                                                                                                                                | 根据接口定义生成客户端；API DSL是用snowcrash来解析的；Apiary是收费的 |      |
| Swagger       | JSON；相对成熟；使用Swagger UI来生成文档；swagger-codegen来生成各语言的客户端；能够全面的描述API；                                                                                                                                                  | 使用SoapUI的插件来进行测试                                           |      |
| ioDocs        |                                                                                                                                                                                                                                                     |                                                                      |      |

## 参考文献

* 1、[API Specification, Automated Testing, and Documentation Generation Discussion](https://lonelyplanet.atlassian.net/wiki/display/PUB/API+Specification%2C+Automated+Testing%2C+and+Documentation+Generation+Discussion)
* 2、[Hello World Product API With Blueprint, RAML And Swagger](http://apievangelist.com/2014/03/08/hello-world-product-api-with-blueprint-raml-and-swagger/)
* 3、[A review of all most common API editors](https://medium.com/@orliesaurus/a-review-of-all-most-common-api-editors-6a720dc4f4e6)
* 4、[Evaluating API development tools](https://github.com/danmayer/danmayer.github.com/blob/79f8fda031cbeaf7f5f28dd16859965a711cfe22/_posts/2014-01-29-investigating-api-tooling.md)
* 5、[http://www.slideee.com/slide/another-api-blueprint-raml-and-swagger-comparison](http://www.slideee.com/slide/another-api-blueprint-raml-and-swagger-comparison)
