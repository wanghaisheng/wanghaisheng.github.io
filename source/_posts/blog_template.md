title: xxxxx
date: 2014-05-20 15:11:12
updated	: 
permalink: 
tags:
- 碎碎念
- 碎碎念
categories:
- 碎碎念
- 碎碎念

---
博文撰写可以使用Swig语法或者markDown语法 元数据部分请参考 本文源代码 正文部分请参考如下内容		
>原文标题：[xxxxx]()
>原文作者：xxxxx
>原文来源：[xxxxx]()
>译者： [edwin_uestc](http://wanghaisheng.github.io/about/)
>版权声明：
>欢迎转载本站的所有内容，本站的所有文章使用[知识共享署名-非商业性使用-相同方式共享 3.0 Unported许可协议](http://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)，唯一的要求就是保留署名权，请在转载时注明出处。
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