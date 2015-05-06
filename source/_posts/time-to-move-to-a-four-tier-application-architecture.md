title:	<微服务架构在Netflix的应用>系列博文-2 是时候转移到四层架构上来了
date: 2015-03-23 11:17:12
updated	:
permalink:
tags:
- 日记
- 架构
- 微服务
categories:
- 架构
- 微服务


---

>版权声明：
>欢迎转载本站的所有内容，本站的所有文章使用[知识共享署名-非商业性使用-相同方式共享 3.0 Unported许可协议](http://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)，唯一的要求就是保留署名权，请在转载时注明出处。

##  第二篇-是时候转移到四层架构上来了

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





新年伊始，你也许计划提升你现有的数字化体验或者从头构建新的网站或系统。如果你要做这些都话，首要的你要牢记在心的是”web“不再只是指 ”web browser“。专家这些年一直在提”mobile first approach“来进行系统开发。但今年的移动流量已经增长至接近60%，这已经是不能再拖的了。互联式设备数量的激增，流量从桌面端向移动端的转变，万物互联的潮水意味着项目必须以不同设备上的用户体验为出发点。
过去的专注于单个集成式的包含大多数功能和特性的整体式模型-既往的应用架构开始不适合这个你需要根据特殊设备特殊用户来调整用户体验的年代。此外，你不能通过很多旧的架构模式和行为实现现如今的系统所要求的敏捷性、灵活性和可扩展性的要求。

为了开发和部署能够有效的吸引和留住不同设备上的移动端的APP，你需要有一种崭新的应用设计的思路。本文中将会阐述为何整体式的架构模型不再适用，同时介绍一种新的架构模型，能够帮助你迎接当今web，乃至于未来web的挑战。

## 为什么软件架构的标准在变化

![](http://nginx.com/wp-content/uploads/2015/02/monolithic_architecture_post.png)
Monolithic Architecture, Source: Martin Fowler
在传统的 monolithic 架构中，应用程序处于中间那层，也就是说前端是展现层，后端是数据层。应用程序将数据传输给web浏览器，也就是展现层，它能给用户提供向应用程序请求信息、展现信息、管理和更改信息的方式，应用程序读写信息到数据层，数据层也就是数据库或其他存储设备负责管理和维护数据。应用程序本身负责与前后两层之间进行交互的业务逻辑以及数据的转换。

 并不是monolithic架构自身存在缺陷，只是它已经过时了，在智能手机和其他移动设备设计之前就已经存在了，那时候应用程序在展现层只需要跟一种实体进行交互，这种缺陷并不是由于层数亦或是层与层之间数据的处理方式，而是应用程序本身被写成一个单独的统一的代码块。monolithic的天性导致开发人员很难用敏捷性和灵活性对应用程序进行改造以适应移动终端用户的需求，满足运营团队自由伸缩应用程序规模以满足实际的需求。

 monolithic 的设计理念阻碍了应用程序开发流程诸多阶段的敏捷性。即使应用程序的功能是以模块化方式组织的，人以模块的更改都需要对整个应用程序进行编译和测试。这本身是恨耗时的，对于那些一年内只更新很少次的公司来讲可能是可以接受的，但要跟上如今的大环境，一年只更新几次的APP恐怕难以在竞争中存活下来。你需要很快的响应渐进式的更新来为用户提供更好的性能和最新的功能。在这样的一个世界里，更新APP永远不会给大多数用户带来不便。

Source: Martin Fowler

![](http://nginx.com/wp-content/uploads/2015/02/microservices_architecture_post.png)
Microservices Architecture, Source: Martin Fowler

 将应用程序拆分成模块长久以来被视为最佳实践。最近，开源项目的成功使得多数开发人员能够借助外部的一些库来实现特殊的功能。这些开源库常常用于那些开发人员不熟悉的特殊功能，或仅仅是为了节省时间，或者是出于维护安全性的考虑。对于 monolithic设计而言 就不存在从诸多方案中任选其一的灵活性，应用程序往往是由一些高度耦合的组件开发而成。

 最后一点，三层架构缺乏伸缩性。事实上，提出这种架构理念的年代并不存在 elasticity and rapid scaling 。由于应用程序的功能组件是打包成一个整体的，你要响应客户端需求变更的唯一方式就是对整体进行扩展。由于应用程序是紧耦合的，三层架构的应用程序通常是没有办法对某个特殊部分单独进行扩展的。不管是一个电子商务的平台、社交媒体的应用还是一个博客，现如今应用程序的基本要求是能够按需伸缩，成本越低越好。对应用程序进行伸缩控制的过程要简单、自动化和智能。比如说某个应用架构能够让你根据用户注册的突发量来部署额外的Node.js节点。
