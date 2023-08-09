---
title: "<微服务架构在Netflix的应用>系列博文-3 微服务架构在Netflix的应用：架构设计的经验教训"
meta_title: ""
description: "this is meta description"
date: 2015-03-23T11:27:12Z
image: "/images/image-placeholder.png"
categories: ["工作"]
author: "haisheng"
tags: ["架构","微服务"]
draft: false
---





##  第三篇-微服务架构在Netflix的应用：架构设计的经验教训

<微服务架构在Netflix的应用>系列博文-共四篇

英文版： [第一部分： The Four-Tier Engagement Platform]((http://blogs.forrester.com/ted_schadler/13-11-20-mobile_needs_a_four_tier_engagement_platform/)
中文版：
[第一部分：移动应用所需要的四层架构/](http://wanghaisheng.github.io/2015/03/23/time-to-move-to-a-four-tier-application-architecture)


英文版： [第二部分：http://nginx.com/blog/time-to-move-to-a-four-tier-application-architecture/](http://nginx.com/blog/time-to-move-to-a-four-tier-application-architecture/)
中文版：
[第二部分：是时候转移到四层架构上来了/](http://wanghaisheng.github.io/2015/03/23/time-to-move-to-a-four-tier-application-architecture)


英文版： [第三部分：微服务架构在Netflix的应用：架构设计的经验教训](http://nginx.com/blog/microservices-at-netflix-architectural-best-practices/)
中文版：
[第三部分：微服务架构在Netflix的应用：架构设计的经验教训](http://wanghaisheng.github.io/2015/03/23/microservices-at-netflix-architectural-best-practices)

英文版：
[第四部分：Adopting Microservices at Netflix: Lessons for Team and Process Design ](http://nginx.com/blog/adopting-microservices-at-netflix-lessons-for-team-and-process-design/)
中文版：
[第四部分：微服务架构在Netflix的应用：团队和流程设计相关的经验教训](http://wanghaisheng.github.io/2015/03/23/adopting-microservices-at-netflix-lessons-for-team-and-process-design)






在最近的一些博客里我们解释了采用[四层的架构](http://nginx.com/blog/time-to-move-to-a-four-tier-application-architecture/)对于开发和部署[微服务](http://nginx.com/blog/building-microservices-free-ebook-oreilly-nginx/)的应用程序是很重要的。
如果你仍然采用十年前的开发流程和应用架构，你不能很快地获取和满足移动端用户的需求，移动端用户可以从越来越多的APP中进行选择。


向微服务架构的转换给市场上的公司带来了很多的机会。对于系统架构和开发人员，它在为用户提供新的用户体验的同时又带来了一种前所未有的控制力和速度。但在现在这样紧张的节骨眼上，感觉上是不允许出一点差错的。现实世界中，你不可能革新期间就停止APP的开发和部署的。你深深明白未来的成功取决于能否成功迁移到微服务架构中来，但是你该怎么来做呢？


[![Netflix_Logo_Digital+Video](http://nginx.com/wp-content/uploads/2015/02/Netflix_Logo_Digital-Video-300x169.png)](http://nginx.com/wp-content/uploads/2015/02/Netflix_Logo_Digital-Video.png)

幸运的是，微服务的早期实践者本着开源的精神慷慨地分享他们的专业知识，不仅有开源代码，也会在会议上做一些演讲，写一些博客。Netflix就是其中之一。Adrian Cockcroft作为web工程和云计算架构师总监负责监督了公司内负责DVD租赁系统的100人的工程师团队从传统开发模式到只需要很少人员负责数百个后台服务的微服务架构来为数百万的Nrtflix客户提供数字娱乐服务。Battery Ventures公司的技术人员Cockcroft是微服务和云架构方面著名的布道者，目前供职于Nginx技术咨询委员会。
后续的两篇文章中，我们会给大家将一些从去年Cockcroft做的2场演讲，一场是10月的NGINX大会上，一场是几个月之后的硅谷微服务meetup中的一些启发。
* 这篇里面主要是给微服务架构一个定义，阐述了一些设计微服务架构的最佳实践
* 后面的一篇讨论了采用软件设计新思路以及绕着这种新思路来重组团队的原因和方式。


## 什么是微服务架构?

Cockcroft 把微服务架构定义为由松耦合的有相应语境的元素构成的一种面向服务的架构

松耦合意味着你可以独立更新这些服务。更新其中一个服务并不会改变其他的服务。
如果你的系统里有大量的特殊服务，但是又必须同时更新它们，它们又不是微服务，因为它们不是松耦合的。在向微服务迁移的时候人们常常会把数据库的耦合看的过重，也就是所有服务都连的是同一个数据库，更新其中一个服务就意味着要改变数据库的schema。这种情况你需要对数据库进行拆分


_bounded contexts_的概念来源于Eric Evans的书 _Domain Driven Design_ 。就软件开发的目的而言，拥有恰当语境的微服务本身是自包含的。由于微服务和其他微服务之间交互是严格通过API来进行的，你不需要共享数据结构、数据库表结构和对象的内部表达形式，在不了解其他服务的内部结构的情况下你也可以理解和更新一个微服务的代码。

如果你开发的是互联网应用，你已经很熟悉这些概念了，实际上只不过用的不是同样的叫法。大多数移动APP都用到了一些后台服务，这样用户可以在APP里实现Facebook里共享、从Google Map里得到地理位置、在Foursquare找到一家餐馆。假如你的APP与这些服务是紧耦合的，这样你在更新之前必须与开发团队进行协调来确保你的更新不会破坏任何东西。

在使用微服务架构时，你要把其他的开发团队看作是这些后台服务：也就是那些你的微服务通过API交互的外部服务。微服务之间最通用的协议就是它们的API足够稳定，也是向前兼容的。

就跟Google Map 的API不可能事先提醒就进行更改是不能所接受的，这样的话，你是API可以演进，但是必须要与之前的版本兼容

## 微服务架构设计的最佳实践

Cockcroft解释他在Netflix的职位是云架构师，他的职责不是管理架构，而是发现和标准化公司工程师所形成的架构。Netflix开发团队提出了几条设计和实现微服务架构的最佳实践

###  每个微服务的数据单独存储

 不同微服务不要使用同一个后台数据存储。让开发团队选择适合每个微服务的数据库。或许，不同团队使用同样的数据结构来存储会减少工作量，但当其中某个团队想要更改数据结构的时候，其他服务不得不跟着改变。

 数据的拆分会使得数据管理异常复杂，是因为单独的存储系统不容易同步，易于出现不一致的情况，外键也会发生意外的改变。你需要一个后台运行的[主数据管理](http://en.wikipedia.org/wiki/Master_data_management)的工具来发现和修复不一致的情况。比如，你需要检查每个存储订阅者ID的数据库来确保所有的ID都是同一个。这个工具可以自己写或者直接买。很多商用的关系型数据库都提供此类核对，它常常过于耦合，不能支持很好的伸缩性。

### 使用类似程度的成熟度来维护代码

微服务中所有代码都保持同样的类似程度的成熟度和稳定度。也就是说，你想要重写或给一个运行良好的已部署好的微服务添加一些代码的话，最好的方式常常 是对于新的或要改动的代码，新建一个微服务，现有的微服务丢着不管就行。 [编辑注：这种架构常常称之为[immutable infrastructure](http://highops.com/insights/immutable-infrastructure-what-is-it/) principle.] 这样的话，你可以迭代式的部署和测试新代码，直至没有bug，性能足够好,现有的微服务不会出现故障或性能下降.一旦新的微服务和原始的服务一样稳定，如果确实需要进行功能合并的话，你可以将其合并在一起，或者处于性能的考虑合并它们。然而，就Cockcroft’s的经验来讲，常常是你发现你的服务太大而要进行拆分。


###  每个微服务都单独进行编译构建

每个微服务都单独进行编译构建，这样你就从代码库里某个版本中抽取单独的组件。这样，你可以拿到多个类似文件的微服务，但却是不同的版本的。这样如果要对codebase进行清理会比较麻烦，但对于在新建微服务时添加新文件时的便利性的话，是值得的。The asymmetry is intentional: 你想要引入新的微服务、文件或者功能，很容易又不会存在风险

### 部署到容器之中

将微服务部署到容器中很重要是因为这意味着你需要一款部署的工具。只要一个微服务是在容器之中，该工具就应该知道如何部署。无论是那种容器都没有关系。也就是说，Docker看起来很快会成为容器的行业标准。

###  将服务器看做是无状态的

将那些特别是部署了客户端代码的服务器视作是可替换的一组之中的一个。这些服务器的功能都是一样的，你无须关心某一个。只需要关心要实现你的目标是否数量足够，你可以使用自动伸缩来按需调整数目。如果其中一个服务器宕机了，可以由其他一个替换。避免了那些单个服务器完成特殊功能的系统中存在的雪崩现象，

Cockcroft打了个比方，你把服务器看做奶牛而不是宠物。如果生产系统中某个服务器负责某个特殊的功能，你通过名称认识这个服务器，这个服务器宕机后大家都回很难过，这也就是一个宠物。相反，如果你把服务器看作是一些奶牛。你关心的是你每天能挤多少奶，如果有一天你发现今天挤的奶少了，你知道是哪头牛有问题，你可以换掉它。

## Netflix Delivery Architecture is Built on nginx

下面是一段软广吧。不过nginx还是很NB的。
Netflix is a longtime nginx user and became the first customer of NGINX, Inc. after it incorporated in 2011. Indeed, [Netflix chose nginx](http://nginx.com/news/nginx-inc-consulted-netflix-open-connect-initiative/) as the heart of their delivery infrastructure, the [Netflix Open Connect](https://openconnect.itp.netflix.com/software/index.html "Open Connect Appliance Software") Content Delivery Network (CDN), one of the largest CDNs in the world. With the ability to serve thousands, and sometimes millions, of requests per second, nginx is an optimal solution for high-performance HTTP delivery and enables companies like Netflix to offer high-quality digital experiences to millions of customers every day.<a name="videos"></a>

## Video Recordings

### Fast Delivery

[Fast Delivery nginx.conf2014, October 2014 ](https://www.youtube.com/embed/5qJ_BibbMLw)

### Migrating to Microservices, Part 1
[Migrating to Microservices, Part 1 Silicon Valley Microservices Meetup, August 2014](https://www.youtube.com/embed/1wiMLkXz26M)

### Migrating to Microservices, Part 2

Silicon Valley Microservices Meetup, August 2014
