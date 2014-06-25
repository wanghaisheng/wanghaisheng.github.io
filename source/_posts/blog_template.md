title: 博文模板
date: 2014-05-20 15:11:12
updated	: 
permalink: abc
tags:
- 模板
- 日记
categories:
- 日志
- 第一天

---
博文撰写可以使用Swig语法或者markDown语法 元数据部分请参考 本文源代码 正文部分请参考如下内容		

Swig语法

## 引用
{% blockquote Seth Godin http://sethgodin.typepad.com/seths_blog/2009/07/welcome-to-island-marketing.html Welcome to Island Marketing %}
Every interaction is both precious and an opportunity to delight.
{% endblockquote %}

## 代码块
{% codeblock .compact http://underscorejs.org/#compact Underscore.js %}
.compact([0, 1, false, 2, ‘’, 3]);
=> [1, 2, 3]
{% endcodeblock %}

## 链接
{% link webQQ http://w.qq.com/ true webQQ %}

## 图片 
{% img /images/th.jpeg 400 600 这是一张图片 %}


MarkDown语法

##引用 
> Every interaction is both precious and an opportunity to delight.



##代码块
```{bash}
.compact([0, 1, false, 2, ‘’, 3]);
=> [1, 2, 3]
```

##链接
[webQQ](http://w.qq.com/)

##图片
![这是一张图片](/images/th.jpeg)

对于本地图片，需要在source目录下面新建一个目录images，然后把图片放到目录中