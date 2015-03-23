title:	读< 与Roy Fielding谈论版本化、超媒体以及REST >
date: 2015-02-08 11:34:12
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

## 第一篇，读< 与Roy Fielding谈论版本化、超媒体以及REST >
全系列[Web APIs: From Start to Finish ](http://www.infoq.com/articles/Web-APIs-From-Start-to-Finish)
第一篇，读< 与Roy Fielding谈论版本化、超媒体以及REST >
[中文版](http://www.infoq.com/cn/articles/roy-fielding-on-versioning)
[英文版](http://www.infoq.com/articles/roy-fielding-on-versioning)
Roy的“Scrambled Eggs • Roy T. Fielding, Ph.D. | Senior Principal Scientist, Adobe”PPT解读
1、什么是作者所说的版本化，怎么理解所说的接口数量限制在某些名称内，什么样的名称，还有一点是这里所说的API版本和资源的版本的区别是什么，各自的设计初衷是什么，适用的场景有哪些？

>我所说的版本化，是指将客户端可见的接口数量限定在某些名称内，这样一来客户端就可以对每个操作进行标记，将这些操作归于该API的某一版本。

不幸的是，对接口名称进行版本化，只是从API作者的角度而言实现了对变更的管理。这一点是对接口设计哲学的短视行为：作者渴望对API进行控制，而忽略了客户对于良好的持续性的需求。

查看了 PPT，对于API的版本控制，常见的有如下实现方式(
在stackoverflow上看到一个相关问答，其中详细讨论了下述方法优劣[best-practices-for-api-versioning](http://stackoverflow.com/questions/389169/best-practices-for-api-versioning/)
):
* URL里带版本号
http://www.host.com/v1/users
* 资源名称里带版本号
• http://example.com/users.v1
* 查询参数里带版本号
• http://example.com/users?api=v1
* 在HTTP头中制定版本信息
• Content-Type: application/vnd.myname.v1+json

2、
>Hypertext as the Engine of Application State
http://stackoverflow.com/questions/717851/can-someone-explain-hypertext-as-engine-of-application-state-in-simple-terms

也就是说在web的世界里，事物的状态变化是通过link来实现的，你浏览网页，看到了一些内容，点击了其中一些链接跳转到其他的页面上，获取更多的内容
 Darrel Miller在stackoverflow上的回答
```
When attempting to explain hypermedia, I like to use the example of navigating in a car via signposts versus a map. I realize it doesn't directly answer you question but it may help.

When driving a car and you reach a particular intersection you are provided signposts to indicate where you can go from that point. Similarly, hypermedia provides you with a set of options based on your current state.

A traditional RPC based API is more like a map. With a map you tend to plan your route out based on a static set of road data. One problem with maps is that they can become out of date and they provide no information about traffic or other dynamic factors.

The advantage of signposts is that they can be changed on the fly to detour traffic due to construction or to control traffic flow.

I'm not suggesting that signposts are always a better option than a map. Obviously there are pros and cons but it is valuable to be aware of both options. It is the same with hypermedia. It is a valuable alternative to the traditional RPC interface.

````

作者强调Rest是一个可Evolvability演化的架构方式，他说不应该对API打上版本号标签，紧接着他抛出REST API版本控制的最佳实践也应该是怎么样的问题？
他把RESTAPI比喻成机器与机器交互的website，接着反问谁在网站的地址上看到过版本号这些玩意儿(对于网站而言，向后的兼容性简直是生命线，如果baidu哪天域名换成bidu呢 google换成bidu呢)，紧接着又引用了Paul在“ALWAYS SHIP TRUNK”PPT中的结论，web应用程序都没能很好的解决版本控制的问题，你自己怎么可能搞的定这难题。 接着便引出了Paul在ppt中的观点，如果要给web应用程序设计一个revision control system  版本控制系统，应该是什么样的呢？
随即引出了根据feature flag和具体情况激活不同的功能，给出了一种全局配置文件的例子
```
if (frags(“saml_auth”)) {
  credentials = saml.authenticate(user);
}
else {
  credentials = httpAuth.check(user);
}
• testable for conditional content (i.e., everything) • readable via all development interfaces
• writable with ops authority
````
后面就是广告时间了，展示了一下他的产品FRAGS的情况，去twitter上搜了一下，说这个产品的点子来源于Paul Hammond
[ using version control to manage web services.](http://www.paulhammond.org/2010/06/trunk/)，在这个长达96页的PPT里Paul介绍到：
要实现软件的 revision control，既有的分支、分布式分支的方法实现起来问题多多。接着指出现有的revision control的方案是面向可安装的软件这一种软件类型所设计的，他提出软件可以分为三种(要安装的软件、开源的要安装的软件、web应用程序或软件即服务)，考虑到我们不是所有服务器上的管理员，无法保证在公开测试、beta环境、QA环境和AB测试环境下同时发布更新，那么要怎么解决呢？(第39页开始)提出三种思路
* 第一种：基础架构和功能代码启动的分离，二者都可以单独部署，不会影响
* 第二种：同时运行多个版本的代码，来回切换，不论是后台还是UI(这里就需要一个revision control系统来解决代码运行时的动态切换并行存在的多个版本的代码)

* 传统的分支本身不能帮你解决运行时不同版本间的切换；
* 传统的分支不能帮你解决一次性多个版本的依赖关系变化的管理
到底怎么样才能解决不同版本切换时的revision control呢？考虑在应用程序内部，也就是代码层面控制不同的版本，换句话说，就是要在代码里利用分支来实现不同版本的控制。
紧接着从550-72利用大量的代码演示了如何利用配置文件来设置标记，实现不同功能(功能的切换、功能的启动与否、不同环境下的配置、不同比例的用户使用那些功能、生产环境下的功能测试等)的切换，74页总结了三类feature flag 功能标记
* 1、Development on user facing features UI界面的
* 2、Development on infrastructure 后台功能的
* 3、 Kill-switches 
```
# killswitch
if ($cfg['disable_login']) {
  error('Sorry, login is unavailable');
  exit;
}
````
通常而言，需要将三者混合使用，如下
```
# for development
$cfg['disable_search_tests_all'] = false;
$cfg['disable_search_ui_beta_test'] = false;
$cfg['disable_search_darklaunch'] = false;
# for post launch
$cfg['disable_search'] = false;
````

作者对于使用分支和feature flag的结论
```
* 1、前期使用分支来开发。Use branches for early development 
* 2、分支要合并到trunk下。Branches merged into trunk
* 3、功能差不多了要上线时使用flag。Use flags for rollout of almost-finished code
````

为了进一步了解feature flag究竟为何物，google一把，定位了几个不错的资源
1、[stackoverflow上关于feature-flag的讨论](http://stackoverflow.com/questions/7707383/what-is-a-feature-flag)
2、[看起来是百度前端团队某大神整理的feature-flag的材料](https://github.com/wangcheng714/feature-flag)
3、[概念的对比和介绍Feature Toggles (Feature Switches or Feature Flags) vs Feature Branches](http://technologyconversations.com/2014/08/26/feature-toggles-feature-switches-or-feature-flags-vs-feature-branches/)
4、[](http://code.flickr.com/blog/2009/12/02/flipping-out/）
5、[](http://techblog.outbrain.com/tag/feature-flags/)
6、[java代码示例](https://github.com/toutantic/featureflags)
7、[仍然是matrin大神的博文](http://martinfowler.com/bliki/FeatureToggle.html)



infoQ上另外一篇文章[不同api版本控制策略的成本分析](http://www.infoq.com/news/2013/12/api-versioning/)则指出
对于如下三种策略：
* 1、只有一个版本，所有消费端使用同一个版本，当API发生变更，消费端也要跟着变。![](first-type-version.png)
* 2、每个服务的版本都可以在生产环境中使用，客户端按需来就行![](second-type-version.png)
* 3、有多个版本存在，所有消费端都使用最新的一个版本，版本是向后兼容的![](third-type-version.png)

![成本分析图](version-type-cost.png)显示向后兼容的版本策略最划算








综上所述：
feature flag指的是将功能发布与代码部署分离feature release and code deployment,对于rest API 或者HTTP API 而言，完全没搞懂ROY大神推荐的是那种套路，是说并存多个向后兼容的版本，以feature flag的形式来配置，客户端只访问最新的版本？对于URL和http header 大神似乎不推荐使用任意带版本号的方法。