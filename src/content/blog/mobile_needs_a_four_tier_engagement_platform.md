---
title: "<微服务架构在Netflix的应用>系列博文-1 移动应用所需要的四层架构"
meta_title: ""
description: "this is meta description"
date: 2015-03-23T11:17:12Z
image: "/images/image-placeholder.png"
categories: ["医疗信息标准", "译文"]
author: "John Doe"
tags: ["日记", "架构","微服务"]
draft: false
---


>版权声明：
>欢迎转载本站的所有内容，本站的所有文章使用[知识共享署名-非商业性使用-相同方式共享 3.0 Unported许可协议](http://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)，唯一的要求就是保留署名权，请在转载时注明出处。

##  第一篇-移动应用所需要的四层架构

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



Michael Facemire, John McCarthy和作者最近向整个软件技术行业发起了倡议：老式的web不是为移动APP和网站而设计的，也不能处理互联式产品的实时需求。是时候提出一种新架构了。

大致总结如下:

移动互联网把传统的web架构推到了悬崖的边缘。为传统PC的浏览器而设计的三层架构不够灵活，不能很好地扩展，也不能提供良好的移动端的用户体验，满足互联式产品的新兴需求。移动互联网的volatility and velocity of change需要的是一种分布式的四层架构，我们称之为“engagement platform”。
这个平台能够将技术功能分成4部分：客户端、分发端、集成聚合端、和服务端。

移动互联网APP的新需求需要将CDN、应用服务器供应商、移动端中间件供应商、PAAS供应商、各种初创公司和其他公司围绕着这四层架构整合起来。
CIO需要立即规划从三层架构到四层架构的迁移工作。

是时候扔掉三层架构，即表现层、应用层和数据层，转向能够满足新需求的四层架构模型：

>“engagement platform”支持分布式的四层架构，能够提供优质的用户体验、优异的性能，以及与任何设备之间的模块化集成。

Figure 1 The Four-Tier Engagement Platform Makes Delivery Its Own Tier
![](http://blogs.forrester.com/f/b/users/TSCHADLER/engagement_platform_2.png)

四层架构的处理流程如下:
* 客户端层负责不同设备的唯一性的确定。 这一展现层将每个app以及设备(桌面端、移动端，浏览器或原生APP)的特殊功能与后台应用程序的服务隔离起来。这个边界使得开发人员可以将后台服务的开发与消费它们的app独立开来，比如航班状态和入港通知等等。确定明确的边界提高了开发人员的效率，无需顾及繁重的维护工作，一个良好的网络环境也是很重要的。
* 分发层处理中间的和最后一英里的问题。通过客户端层的信息决定交付特定场景下具体内容的最佳方式。通过over-the-wire的内容转换—这里与聚合层不同，聚合层使用的基于协议的转换，利用 edge-of-network cache 功能来增加动态数据， 如Akamar等提供的CDN、如Instart Logic的分发优化方案、如Riverbed Stingray的应用分发控制和on-premises in-memory database caches一起完成这方面的任务
*  聚合层负责内部和外部服务的集成和数据的转换。这样的API层有两方面的角色，不同APP请求和服务
的发现和客户端请求与后台服务的双向转换。这样能够使得底层数据的组装和服务更加简洁，能够提供相对实时的数据格式的转换。服务组合外加上商务智能、分析、基于角色的访问等更加动态。
* 服务层包括了内部外部提供数据和功能。通过一系列连贯的可部署的服务来动态组装服务和业务流程。
该层负责为上述三层提供数据，不关心数据具体如何使用。其他几层可以部署在防火墙内也可以部署在防火墙外，或者二种方式相结合。这样不论是APP使用还是生态系统中其他系统使用，在服务的动态组合和访问上就提供了相当的灵活性

未来的展望

问: 如果未来是engagement platform的天下，如何实现呢？

答: 颠覆现在的软件行业的核心架构。IBM, Microsoft, Oracle, and Akamai一直在推三层架构，现在将被
Netflix, Kinvey, and Salesforce.com提出的四层架构所替代。

是时候供应商、投资人员、架构师和开发人员对如何来构建和使用engagement platform展开讨论了。

engagement platform”支持分布式的四层架构，能够提供优质的用户体验、优异的性能，以及与任何设备之间的模块化集成，并且能够推动这些颠覆的演化:

*  公司将依赖于供应商的生态系统来deliver engagement. 你无须购买这个engagement platform平台。而且这个engagement platform平台也不是全部受你直接控制。相反，你以松耦合的方式组装各种
engagement 功能，而且能够按需扩展，同时能够保持灵活性，也能够解决持续交付的问题。
* HTTP traffic on Nginx will surpass the traffic on Apache. If you don't know what those things are, don't worry about it. If you don't but think you should, then see the last chart here and learn about it here and here.
*  IBM, Oracle, Microsoft, SAP, and Salesforce.com will rethink their middleware products and architectures. Adding mobile app lipstick on an application server won't solve the delivery challenge by itself. These companies will slowly overcome their reluctance and begin to operate in a four-tier, ecosystem-dependent platform. But it will take five years for that to happen. Microsoft Azure is the farthest along, but still tentative in its strategy and execution.
* The content delivery network industry will accumulate content and performance optimization services. Akamai, Limelight, and Amazon CloudFront have done good work for the Web. But new approaches from Instart Logic and rumblings from Akamai point to the delivery-tier future.
*  Platform-as-a-service providers like Amazon, Google, IBM, Microsoft, and Salesforce will grow many new platform services. For example, services in the aggregation tier loosely coupled with an intelligent delivery tier will handle notification at scale, including personalized messages, open-message analytics, and device and network customization.
