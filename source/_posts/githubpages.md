title: Github pages 个人主页和项目主页的不同设置
date: 2014-06-25 22:05:57
tags:
- Github pages
- 博客
categories:

---


Github pages 个人主页和项目主页的不同设置

如果你想利用github pages来搭建属于自己的博客 亦或是为某个小项目做一个宣传页面  这里有点小坑 大家需要提防一下。  


1.如果你想做一个个人主页的话，比如我在github建了这样一个[repo](https://github.com/wanghaisheng/wanghaisheng.github.io)，除了需要有一个CNAME文件，内容如下，

```
 http://wanghaisheng.github.io
```
同时，github pages要求你要发布的网站内容必须位于master分支下。  

2.如果你只是想做一个项目主页的话，比如你在GitHub建了个项目叫作 wiki ，那么只需在这个项目下新建一个root branch叫作 gh-pages ，
那么push到这个branch里的内容都会发布到  
```
http://你的用户名.github.com/wiki  
```  
现成的例子如[bootstrap](http://twitter.github.com/bootstrap/)。

在每个项目的Admin页面里都有一个选项叫做 GitHub Pages ，勾选此选项则会自动为你生成上述的branch。  


具体操作可以参阅GitHub Pages主页。当然，这个项目页面也和个人主页一样支持自定义域名，只需建立一个名为 CNAME 的文件并包含所映射的域名，然后修改DNS设置就可以了。所以理论上你可以绑定任意数量的域名到GitHub。绑定域名后 http://你的用户名.github.com/projectname 和 你绑定的域名都能访问这个站点。
