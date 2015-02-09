title:	读< 从业务角度看API >
date: 2015-02-09 13:42:12
updated	: 
permalink: 
tags:
- 日记
- HTTP API
- REST
categories:
- 日记
- HTTP API
- REST


---

>版权声明：
>欢迎转载本站的所有内容，本站的所有文章使用[知识共享署名-非商业性使用-相同方式共享 3.0 Unported许可协议](http://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)，唯一的要求就是保留署名权，请在转载时注明出处。

##  第二篇，读< 从业务角度看API >
[英文](http://www.infoq.com/articles/web-apis-business-perspective)
[中文]() 
作者：Matt McLarty



观点1：API是当今信息技术趋势的核心，比如说移动终端、云计算、物联网、大数据、社交网络。涉足各行各业，如能源、汽车、电商等
观点2：虽然和API在整个技术领域应用相比是九牛一毛，在open WEB领域，API俨然已经成为相当重要的创新和收益的业务模式，对比，Kin Lane在[API Evangelist](http://apievangelist.com/index.html)网站上撰文进行了详细的阐述, [Mehdi Medjaoui](https://medium.com/@medjawii/5-ways-an-api-is-more-than-an-api-bddcdb0517ca)也在博文中就此进行了总结 。
事实上，现如今web API是隐藏在解决方案背后的，也就是API的业务模式也就是业务本身
观点3：API的业务价值、商业价值是可以度量的。传统意义上，由于服务器和存储设备成本高昂，他们所拥有的数据一定程度成为自身的债务。现如今，伴随着大数据和物联网、万物互联IoT等技术发展，拥有数据意味着可以将其转换为新的机会和收入来源。
观点4：如何确定那些数据、服务可以通过API暴露，以及如何实现这些API，可以通过如下三个数据的属性来判断：

|名称|描述|
|------|-------|
|Data Applicability|<ul><li>这些数据是否能够帮助我们实现核心业务价值</li><li>这些数据是否能够形成业务上的差异性</li><li>需要那些商品化处理才能将这些数据对外发布</li></ul>|
|Data Accuracy|<ul><li>目前这些数据的及时性如何</li><li>数据是否来自可信的来源</li><li>正确的用户出于正确的目的是否可以访问数据</li></ul>|
|Data Accessibility|<ul><li>有哪些数据可供程序使用</li><li>这些数据有哪些不同的访问方式</li><li>开发人员利用这些数据构建APP的难易程度如何</li><li>数据访问的规模是否能满足客户的需求</li></ul>|

总结下来，也就是两方面：
1、有用的API“Useful APIs”  能够提供准确适当的数据
2、可用的API “Usable APIs”能够访问到数据

观点5：有用的API
开发API时常见的误区是认为所有数据都是有用的。不是说你开放了数据，开发人员就能从中增加收益、创新、开拓新的业务。API和Open Data本身是远远不够的。
“This “medium is the message” thinking was responsible for many of the failed SOA initiatives that occurred in enterprise integration over the last decade”这句是什么意思，没有搞懂
举出Google  Map、Facebook、Twitter的例子说明只有正确的数据结合API才能攫取最大的效益，
观点6：Amazon API的案例
API对于开放API之外的机构而言，在业务上帮助作用拥有巨大潜力。对于Amazon，API是从内部缘起的。
经验教训一：将API定位为产品、解决方案的构建基石。Brad Stone在[](http://brad-stone.com/book/)书中花了一章来阐述API是Amazon整个技术架构的基础，Kin Lane在博文[The Secret to Amazons Success Internal APIs](http://apievangelist.com/2012/01/12/the-secret-to-amazons-success-internal-apis/)中讨论了如何保证程序能够访问这些API接口。
经验教训二：如何使用基于API的方法来采集、分析、改进和分发数据。Jeff Bezos 讲到["We don’t make money when we sell things. We make money when we help customers make purchase decisions."](http://www.businessinsider.com/bezos-pioneering-requires-being-misunderstood-2013-1).只有恰当的、准确的、可用的数据才能帮助用户进行决策，这对于亚马逊来讲至关重要。
“Data-Enabled Disruption (DED)”[图示](DED_Cycle.jpg)
经验教训三： 战略与战术定位之间的权衡。早期，Jeff Bezos认识到万维网的巨大潜力，随即产生了要创建一个巨大的能够存放任何东西的商店。
在分析了市场之后，以在线图书零售为突破口来优化整个供应链，企业文化(ensuring timely execution while maintaining religious devotion to the future vision—is now a tenet of Amazon’s culture, where solutions must add value both in what they deliver and what they enable)一方面能够实现功能，一方面能够传递价值。
见[下图](5Fig2.png)
每种服务都对应着一个API，每个都是基于早期的解决方案所产生的。

观点6：可用的API以及API设计的重要性
虽然亚马逊很成功，但它们的API设计却不是很好，也不易用。随着API的爆发性增长和其必要性的认可度提高，API的可用性成为众多公司主宰行业或者初创公司试图开拓创新服务的关键。

移动设备和consumerization of IT引发了企业应用开发的[模式转变](https://www.linkedin.com/today/post/article/20140716032508-16039030-the-rebirthing-of-the-mobile-app?trk=hb_ntf_MEGAPHONE_ARTICLE_POST)。从一开始的终端到CS架构到现在的分布式网络。在之前的文章[the shedding of tiers](https://www.youtube.com/watch?v=23nyxjRPe94),为了适应云端和移动端的发展，正在从n层web模型向以API为中心的而转变。
以远程通讯领域为例，多年来大玩家们一方面互相竞争，另一方面寻求能够为用户提供网络之外的增值服务。这个行业在过去15年间经历过很大分裂，如VOIP的出现，业务和服务的整合，以及移动设备服务的改革，在上述环节中，API都发挥了作用，尽管仍然主导着传统的telco服务，但难以维系其优势，在Alan Quayle的文章[a-brief-history-of-telco-apis]()(http://alanquayle.com/2012/06/a-brief-history-of-telco-apis/)中指出在像Parlay X和OneAPI这样的协作项目中这些玩家困难重重。

Twilio公司成立于2007年，旨在提供易用的语音和短信服务，所有应用都部署在云端。他们认识到API是他们最核心的业务渠道，尽管SMS和VOIP服务是恨有用的，但要和大玩家竞争，commoditized telco services是远远不够的。Twilio也意识到他们服务的最初用户并非终端用户，而是调用API构建APP的开发人员，而且发展最快的是移动APP，于是开发了诸多衡量是否能够很好的服务客户的指标。除了像传统的统计数据如端到端的调用响应时间，他们还测量了新上手的开发人员从注册他们的api到开发好应用花多长时间，这极大的提高了易用性，成为了和大公司的主要差异点，当开发人员在选择SMS VOIP服务的时候，优势就显现出来了。

总结：
1、API 与业务策略要统一
2、实现过程中通过API保证数据可用、准确
3、确保API是有用的、可用的
4、像亚马逊一样形成a disciplined culture of iterative Data-Enabled Disruption
5、像Twilio一样形成优质的API开发人员用户体验来差异化和竞争对手的业务
