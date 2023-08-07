---
title: "TWITTER REST API研究"
meta_title: ""
description: "this is meta description"
date: 2014-12-20T10:52:12Z
image: "/images/image-placeholder.png"
categories: ["HTTP API","REST"]
author: "John Doe"
tags: ["REST","HTTP API"]
draft: false
---


原文标题：[REST APIs](https://dev.twitter.com/rest/public)
原文作者：Twitter Inc
原文来源：[Twitter Inc]()
译者： [edwin_uestc](http://wanghaisheng.github.io/about/)
>版权声明：
>欢迎转载本站的所有内容，本站的所有文章使用[知识共享署名-非商业性使用-相同方式共享 3.0 Unported许可协议](http://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)，唯一的要求就是保留署名权，请在转载时注明出处。


## REST APIs
这样就能够以编程的方式读写Twitter数据。发一条推或者读取某个人的资料和他的粉丝信息等。通过OAuth来识别twitter应用程序和用户，返回的数据是JSON格式。

 entities(实体)
 retweets(转发)
 Tweet objects微博对象
### 概述
在1.1版本之中我们做了如下重大变化，在此列出 希望所有的开发人员不会错过这些重要信息。

1、Default entities and retweets

在一定的情况下，V1.1版本的接口中默认会返回 entities(实体) 和 retweets(转发)。 entities(实体) 是作为Tweet objects微博对象的一部分返回的，除非你将include_entities变量的值设为false。其中会包含时间流顺序组织的转发信息，除非include_rts参数的值为false

2、Authentication on all endpoints

我们使用OAuth1.0a或者Application-only authentication对来自应用程序的所有请求消息进行鉴权。
这种透明化的方式避免了滥用行为，也能够让我们对使用API的应用程序更好的分类。
这样我们就能对平台持续演进以更好的满足开发者的需求

3、Rate Limiting

对于每个endpoint，我们将频率限制划分为15分钟一段，在每段当中，单个应用调用的请求的上限为15次。
与V1版本的API相比，每个endpoint的调用次数都变多了，有些特殊的节点在一段内甚至可以达到180次，尤其有利于使用了GET statuses / show / :id, GET users / lookup, GET search / tweets 等接口的APP。详细信息请阅读API V1.1Rate Limiting相关文档和每个方法中具体对于调用上限的描述

4、Twitter client policies

所有再造了Twitter核心功能的应用斗称之为client客户端，都必须遵循某些约束，包括100，000用户令牌的限制。这点也仅仅适用于小型的客户端，并不适用于生态系统中的大多数应用程序。详情请查看[开发者守则](https://dev.twitter.com/terms/api-terms)


###
