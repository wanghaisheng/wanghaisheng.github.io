title:	Yelp公司总结的微服务架构的实践经验
date: 2015-03-23 18:46:12
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

##  Yelp公司总结的微服务架构的实践经验


英文版：
[Service Principles]((https://github.com/Yelp/service-principles)
中文版：
[Yelp公司总结的微服务架构的实践经验/](http://wanghaisheng.github.io/2015/03/23/service-principles)

# Service Principles

- [服务设计的原则](#service-principles)
  - [创建](#creation)
    - [首先探讨系统的整体架构](#discuss-the-organization-of-your-overall-system-first)
    - [核实是否能够给现有服务添加新的功能](#check-whether-you-can-add-your-feature-to-an-existing-service)
    - [考虑你的功能是否更适合作为一个库](#consider-whether-your-feature-is-better-suited-to-a-library)
    - [服务应由团队而不是个人负责管理](#services-are-curated-by-teams-not-individuals)
    - [服务是长期的commitment](#services-are-a-long-term-commitment)
    - [部署到分布式系统之前的考虑因素](#factor-in-the-overhead-of-deploying-a-distributed-system)
    - [服务大点更好](#prefer-larger-services)
    - [最小化服务调用链的深度](#minimize-the-depth-of-the-service-call-graph)
    - [最小化你的团队所拥有的服务数目](#minimize-the-number-of-services-owned-by-your-team)
  - [接口](#interfaces)
    - [接口要易于理解](#interfaces-should-be-easy-to-understand)
    - [接口要尽可能健壮](#interfaces-should-be-robust)
    - [接口变更应该要向后兼容](#changes-to-interfaces-should-be-backwards-compatible)
  - [测试](#testing)
    - [应该能够对任何接口变更进行自动化测试](#any-changes-to-your-service-should-be-able-to-be-tested-automatically)
    - [最主要的是测试你的接口](#your-interface-is-the-most-important-thing-to-test)
  - [运维](#operations)
    - [服务的运行由你来负责](#you-are-responsible-for-running-your-service)
    - [引导客户的期望值](#guide-your-clients’-expectations)
    - [故障计划](#plan-for-failure)
  - [补充材料](#additional-reading)


## 创建

### 首先探讨系统的整体架构

在你开始考虑设计服务之初，也就是动手写代码和设计之前，和团队成员、其他服务领域的专家聊一聊。除了如何与现有的特性、产品以及服务如何适配之外，考虑一下你想要额外添加的功能。考虑一种最合理的组织整体功能的方式。有时候添加新功能意味着要对现有组件进行重组。


我们希望避免那些简单的 "append-only"服务架构，也就是说development只存在于新的服务中

### 核实是否能够给现有服务添加新的功能

在编写新的服务之前，应该核实是否现有服务不包括你的功能。它可能会与现有的功能存在冲突，处理相同的信息，或者只是在现有服务功能范围内的演化。另一方面，如果给现有服务添加新的功能会让服务的使用者感到困惑的话，最好就不要添加新的功能了。

### 考虑你的功能是否更适合作为一个库

尽管这篇文档是讲服务的，但值得注意的是一些功能更适合做成库。为了帮助大家更好的决策，我们介绍了库与服务之间进行取舍的一些经验:

***升级速度***  对于库来讲更适合哪些用户期望很长时间才进行升级的场合(通常数周或数月，甚至于数年)。一般来说，这要求功能本身相对小且自包含，所以本身变更的可能就小。相反，如果你还正在进行开发，或者你希望能够快速推送一些bug修订给用户，这样的功能更适合作为一个服务。这样功能就回更复杂一些，常常需要依赖外部的一些库。

***性能和可靠性*** 库与调用请求的寻址空间一样，而服务则处于不同的网络地址。假使其他东西都是一样的，访问一个库 要比服务更快更可靠。但是，如果功能对资源需求较高，比如CPU,内存和硬盘，那么作为一个服务能够让客户端的运行效率更高，能够使得服务所依赖的硬件独立于客户端的硬件而水平扩展。

***技术无关性***
大多数情况下，Yelp使用的是Python，有一些后台服务是Java的。如果你的服务希望 Python and Java都能调用，那么做成服务能够帮你避免重复写两个库。

### 服务应由团队而不是个人负责管理

每个服务应由团队而不是个人负责管理，这样出了问题，就不会出现只有一个开发人员知道如何解决bug。实践中也就是说，每个服务从最开始都至少要2个人员参与，分摊维护的责任。

### 服务是长期的投入
Services are a long-term commitment

当你编写代码时，你的团队会进行持续的维护和运营支持。随着时间推移，你的服务用户将依赖服务才能够运营。你需要持续的监控性能、一致性和 brown-outs.你或许也要处理下游系统的故障。

### 部署到分布式系统之前的考虑因素

一个服务的推出往往花费的时间比你想象的要长。这可能是由于未预料到的不同服务间的交互，或者是搭建监控环境时的困难所导致的。负载测试没有100%完美的，因此需要部署成功之前制定一个多个阶段和迭代的持续计划。

### 服务大点更好Prefer larger services

尽量把相关功能整成一个较大的服务而非多个很小的服务。记住 你的大服务应该是逻辑内聚的，比如你仍然要具体的描述服务的功能。该原则的原理如下：

* 流程内调用比服务间调用要更快、更可靠
* 单独更改一个服务比在多个服务间协调变更要简单一些。实际上，更改服务接口的成本相对是很高的
* 在运营层面上，保证统一的流程正常运行的话，数量越少越容易.
* 有些运维任务必须在每个服务上单独进行，比如库版本的更新。服务更少这个工作量越小

### 最小化服务调用链的深度

在对服务进行架构时，调用链长度越小越好 (service ``A`` calls services ``B``, ``C`` and ``D``)比(``A`` calls ``B`` calls ``C`` calls ``D``)好。原理如下:

* 更容易来推出调用链; 在长度较小的情况下, B, C and D 没有依赖任何外部的服务，而在较长的情况下B和C服务都依赖其他服务。注意 这与 [three-tier architecture](http://en.wikipedia.org/wiki/Multitier_architecture#Three-tier_architecture)很匹配。
* 这样能提高性能，在较短的情况下，服务的调用可以并发执行(只要服务间互相独立即可)而较长的情况下只能串行执行


### 最小化你的团队所拥有的服务数目

你所在的团队可能负责某个产品或一些产品的交付。你们所开发的服务应该与这一目标相统一。如果你们所拥有的服务过多，也就是说你的团队过于面面俱到，或者你们服务的统一程度还不够.

如果你们团队已经在负责大量的重要服务，且新功能并不属于任何已有的服务，在你们团队能够接受构建新服务的任务之前你可能需要把任务推出去。也应避免2个以上团队负责某个服务的情况


## 接口

你的服务接口可能不只是对外发布的[REST](http://en.wikipedia.org/wiki/Representational_state_transfer) 接口. 日志、数据备份、数据流等其他服务使用的都要考虑在内。接口指的是对客户端有用的所有东西的总和.

> 比如我们一直在模仿的接口设计的实践, 参考 [GitHub API v3](https://developer.github.com/v3/) 和  [PayPal REST API](https://developer.paypal.com/docs/api/)

### 接口要易于理解

在设计接口时, 要遵循如下最佳实践:

* 使用自描述的名称。对内对外保持一直
* 让领域专家评审你的接口
* 使用一种显而易见的方式来完成每个操作
* 在将现有功能移植成服务时不一定会成为最好的网络节点。远端执行会改变一致性、可靠性和性能的本质。设计服务的边界时应保证与其他系统是松耦合的.
* 将读与更新操作的接口分离. (See [CQRS](http://martinfowler.com/bliki/CQRS.html) as an example)
* 尽可能的最小化、简单化你的接口。这样测试起来也方便
* 尽可能对存在疑虑的地方写上文档
* 跟自己发问: "在没有和你请教之前，新人能够看懂你的接口?"

### 接口要尽可能健壮

设计接口时把它当做是暴露给整个互联网来使用的。只暴露那些客户端需要的信息。尽可能不要提供不安全的、高成本的操作

将只读和能够改变状态的方法区分开来。理想情况下，只读方法是可缓存的且是幂等的


###  接口变更应该要向后兼容

接口应该有某种版本控制机制。当改变一个服务接口时，之前存在的客户端仍然能够调用你之前版本的接口。你不能破坏这些客户端。要么做好计划持续的支持这些旧的客户端，要么花些时间使得它们和更新相协调。同时有多个版本的接口并存是可以接受的。


## 测试

### 应该能够对任何接口变更进行自动化测试

Yelp没有单独的QA工程师。相反我们靠计算机来进行校验工作。你的服务由你来负责维护测试工具。测试应该在开发和测试环境中都能够快速可靠的完成。

一个优秀的测试工具就像一个金字塔。最基础的是单元测试：很多快速的很小的测试代码中的单个实现的细节。中间一层是集成测试，这时候对服务进行交互的多个组件进行校验。最上面是很小但很重要的验收测试，主要校验你的服务是否能够与其他服务进行交互

### 最主要的是测试你的接口

接口是你们协议的重要部分，也就是客户端使用和交互的东西。如果你改变了接口，破坏或改变它原来的功能你会影响所有调用你服务的客户端。这个影响是很大的。

这也就是为什么接口测试是最主要的。接口测试能够告诉你客户端实际看到的是什么，持续的测试能够保证客户端总是看到这些结果。确保接口的所有现用版本的性能是一致的。尽可能早的编写测试，整个黑盒测试所看到的结果应该驱动你的接口设计

## 运维

###  服务的运行由你来负责

你的团队负责你们服务的持续运维。运维团队是解决整体站点问题的第一道防线，但是涉及到服务就只能做些边边角角的工作。监控服务的健康度是你的职责所在，做一些有意义的提醒以及出现问题时的方案。你是最了解服务运行机制的人，因此你也是发现和解决问题的最佳人选

为服务编写runbook。其中应包含常见的运维场景(诸如部署、监控和问题处理)。记录已知的错误。

### 引导客户的诉求
你要能够准确清晰的向客户传达你们服务的运行特征。我们建议你要积极地监控和对服务进行测试以理解这些特征，以确保哪些你所承诺要达到的维护程度。

比如，如果我告诉客户99.99%的正常运行情况下99%的请求都在100ms以下。也就是说我要不停的监控性能和可用性来保证我的承诺。

不同服务运维承诺不同是可取的。a "cat picture of the day"服务的正常运行时间只是团队内部用来调剂气氛的就不需要实时的监控和提醒了。一个生产系统中的对主要节点很重要的服务就需要多关注正常运行时间、性能和其他可能会出现的问题


### 故障计划

SOA的特质之一是分布式系统中故障场景数量的急剧增加。从运维角度来看，这意味着你的服务必须
 strive to be honest about the collaborating services and datastores it requires to operate, and those whose downtime can be gracefully handled.

服务启动之初就要有如何确定外部的依赖关系和记录它们之间关系的计划。外部链接的指标，以及主动式和开发层面的保护措施以保障服务在外部故障之后的处理。最后一点，你要实时的监控这些潜在的weak points，根据严重程度来提醒当班团队.

另外，服务可能在跨机器、跨rack和跨数据中心间运行，每种情况都可能出现故障。要深刻理解这样的场景下服务的表型。

设计良好的服务要考虑所有的故障点，做出合理的决策来减少每个故障的可能性。


## 补充材料

* [Martin Fowler on Microservices](http://martinfowler.com/articles/microservices.html)
* [Law of Demeter](http://en.wikipedia.org/wiki/Law_of_Demeter)
* [Steve Yegge's Google Platforms Rant](http://steverant.pen.io/)
* [The Fallacies of Distributed Computing](http://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)
* [Designing Poetic APIs](http://pyvideo.org/video/2647/designing-poetic-apis)
