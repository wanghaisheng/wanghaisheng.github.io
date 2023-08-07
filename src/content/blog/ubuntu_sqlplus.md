---
title: "ubuntu下sqlplus上下光标键乱码解决方法"
meta_title: ""
description: "this is meta description"
date: 2010-10-22T19:15:57Z
image: "/images/image-placeholder.png"
categories: ["Oracle","Ubuntu"]
author: "John Doe"
tags: ["Ubuntu"]
draft: false
---



ubuntu下sqlplus上下光标键乱码解决方法

我的系统是ubuntu10.10，oracle版本为10gXE
遇到如题所述的问题时，可以这样解决该问题：

1 、安装插件：  
 ```sudo apt-get install rlwrap```  


2、在当前用户下设置一个命令别名：
```alias sqlplus='rlwrap sqlplus'```  


3、重新键入sqlplus命令即可尽情享用上下左右光标键了
