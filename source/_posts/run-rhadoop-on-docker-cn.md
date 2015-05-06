title:	Docker玩转Rhadoop
date: 2014-12-20 10:52:12
updated	:
permalink:
tags:
- 日记
- docker
- rhadoop
categories:
- rhadoop
- docker


---

>版权声明：
>欢迎转载本站的所有内容，本站的所有文章使用[知识共享署名-非商业性使用-相同方式共享 3.0 Unported许可协议](http://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)，唯一的要求就是保留署名权，请在转载时注明出处。

## Docker 玩转 RHadoop
网络上已经有了太多的 RHadoop 的安装使用的教程，鉴于其中的配置配置繁复，对软件版本的要求又极其苛刻，故笔者想用时下热门的 docker 来尝尝鲜，以下是心路历程，供看客参考，希望能给大家一些帮助。

### 1、软硬件环境

操作系统：OXS 10.10.1

docker安装版本：boot2docker(推荐大家使用https://github.com/unixorn/docker-helpers.zshplugin该插件可以省去大家不少功夫)

Hadoop镜像：sequenceiq/hadoop-ubuntu:2.6.0

###  2、事前准备
1、考虑到GFW的因素，拟将 sequenceiq/hadoop-ubuntu:2.6.0 镜像中的源替换成163的,顺便添加R语言安装的source
新建source.list
````
          deb http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse
          deb http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse
          deb http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse
          deb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse
          deb http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse
          deb-src http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse
          deb-src http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse
          deb-src http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse
          deb-src http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse
          deb-src http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse
          deb http://cran.r-project.org/bin/linux/ubuntu trusty/
````

2、下载好RHadoop的几个 tar.gz 安装包，版本以自己安装日期的最新版本号为准

````
rmr-2.3.3
rhdfs-1.0.8
rhbase-1.2.1
````
3、测试过程中会用到的测试数据 主要是wordcount程序中
````
subl  part-m-00000  
````
数据内容如下所示
````
10,3,tsinghua university,2004-05-26 15:21:00.0
23,4007,北京第一七一中学,2004-05-31 06:51:53.0
51,4016,大连理工大学,2004-05-27 09:38:31.0
89,4017,Amherst College,2004-06-01 16:18:56.0
92,4017,斯坦福大学,2012-11-28 10:33:25.0
99,4017,Stanford University Graduate School of Business,2013-02-19 12:17:15.0
113,4017,Stanford University,2013-02-19 12:17:15.0
123,4019,St Paul's Co-educational College - Hong Kong,2004-05-27 18:04:17.0
138,4019,香港苏浙小学,2004-05-27 18:59:58.0
172,4020,University,2004-05-27 19:14:34.0
182,4026,ff,2004-05-28 04:42:37.0
183,4026,ff,2004-05-28 04:42:37.0
189,4033,tsinghua,2011-09-14 12:00:38.0
195,4035,ba,2004-05-31 07:10:24.0
196,4035,ma,2004-05-31 07:10:24.0
197,4035,southampton university,2013-01-07 15:35:18.0
246,4067,美国史丹佛大学,2004-06-12 10:42:10.0
254,4067,美国史丹佛大学,2004-06-12 10:42:10.0
255,4067,美国休士顿大学,2004-06-12 10:42:10.0
257,4068,清华大学,2004-06-12 10:42:10.0
258,4068,北京八中,2004-06-12 17:34:02.0
262,4068,香港中文大学,2004-06-12 17:34:02.0
310,4070,首都师范大学初等教育学院,2004-06-14 15:35:52.0
312,4070,北京师范大学经济学院,2004-06-14 15:35:52.0
````
4、这些文件准备好了之后，最好放置在宿主机的某个文件夹下，比如我这里放在
````
/Users/wanghaisheng/docker
````
5、请确保docker成功安装，不同操作系统的安装教程请前往国内docker中文社区寻找答案
[docker中文社区站](http://www.docker.org.cn/)
[docker.cn ](https://docker.cn/)
[DockerPool](http://www.dockerpool.com/)

### 3、Hadoop 单机环境

1、从远端服务器拉取Hadoop镜像文件 由于GFW和网络原因，可能耗时较长 请耐心等待
````
~ docker pull sequenceiq/hadoop-ubuntu:2.6.0
````
2、把之前准备好的文件夹挂载到我们要启动的单机 Hadoop 容器中去，这里笔者比较懒，各位可以自行用喜欢的目录替换容器中的挂载目录(冒号后面的部分/Users/wanghaisheng/docker)
````
~ docker run -i -t  -v  /Users/wanghaisheng/docker:/Users/wanghaisheng/docker sequenceiq/hadoop-ubuntu:2.6.0 /etc/bootstrap.sh -bash
````

### 4、R的安装
1、修改源文件
````
cp /etc/apt/sources.list /etc/apt/sources.list_backup
rm /etc/apt/sources.list
cp /Users/wanghaisheng/docker/source.list /etc/apt/sources.list
````
2、从CRAN安装R
CRAN中具有最新的R版本，所以一般建议利用CRAN进行R的安装。其基本步骤为：
````
~ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
````
然后需要添加CRAN源到/etc/apt/sources.list:
````
deb http://cran.r-project.org/bin/linux/ubuntu xxx/
````
其中xxx为你的Ubuntu版本,这里的话就是trusty。同时CRAN的地址可以用任意你喜欢的镜像替换。这里我们在source.list中已经事先准备好了，直接进入下一步
````
~ sudo apt-get update
~ sudo apt-get install r-base r-base-dev
````
### 5、R的配置

1、需要运行如下命令，让R与系统中安装好得jdk环境关联起来
````
 	~ R CMD javareconf
````
2、启动启动R程序
````
	~ R
````
3、安装RHadoop会使用到的依赖包
````
install.packages("rJava")
install.packages("reshape2")
install.packages("Rcpp")
install.packages("iterators")
install.packages("itertools")
install.packages("digest")
install.packages("RJSONIO")
install.packages("functional")
install.packages("caTools")
````
### 6、rhdfs和rmr2的安装

1、配置环境变量，网络上大量的例子使用的是hadoop1.0.3，我们使用的是Apache2.6，这里的HADOOP_STREAMING路径可能大不一样，/hadoop-1.0.3/contrib/streaming/hadoop-streaming-1.0.3.jar)，PATH这里要添加hadoop的安装路径的bin目录，否则后续使用hadoop命令会出现not found
````
~ vi /etc/environment

    HADOOP_CMD=/usr/local/hadoop/bin/hadoop
    HADOOP_STREAMING=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar
	PATH=$PATH:/usr/local/hadoop/bin


~ source /etc/environment
````
2、安装rhdfs
````
~ R CMD INSTALL /Users/wanghaisheng/docker/rhdfs_1.0.8.tar.gz
````
3、安装rmr2
````
~  R CMD INSTALL /Users/wanghaisheng/docker/rmr2_3.3.0.tar.gz
````
### 7、测试rmr2-wordcount
1、启动R
2、载入rmr2包
````
library(rmr2)
````
3、执行如下命令
````
> small.ints = to.dfs(1:10)
> mapreduce(input = small.ints, map = function(k, v) cbind(v, v^2))
> from.dfs("/tmp/file1ea36ae45f9f")  
````
这里要注意的是 这个临时文件的名字是变化的 请自己根据上一条命令的返回信息进行替换

### 8、测试rmr2-MapReduce的R语言程序
1、首先，是基本的hdfs的文件操作。查看hdfs文件目录

hadoop的命令：hadoop fs -ls /usr
R语言函数：hdfs.ls(“/usr/“)

你会发现什么数据都没有，这时候把事先准备好的测试数据拿进来好了
````
hadoop fs -mkdir /user/hdfs

hadoop fs -mkdir /user/hdfs/o_same_school/  
hadoop  fs  -rm /user/hdfs/o_same_school/part-m-00000

hadoop fs -put  /Users/wanghaisheng/docker/part-m-00000  /user/hdfs/o_same_school/
hadoop fs -cat /user/hdfs/o_same_school/part-m-00000
看到了一堆数据了把！
````
2、启动R程序
````
> library(rhdfs)
Loading required package: rJava
HADOOP_CMD=/root/hadoop/hadoop-1.0.3/bin/hadoop
Be sure to run hdfs.init()

> hdfs.init()
hdfs.ls("/user/")

library(rmr2)
> input<- '/user/hdfs/o_same_school/part-m-00000'
> wordcount = function(input, output = NULL, pattern = " "){

  wc.map = function(., lines) {
            keyval(unlist( strsplit( x = lines,split = pattern)),1)
    }

    wc.reduce =function(word, counts ) {
            keyval(word, sum(counts))
    }

    mapreduce(input = input ,output = output, input.format = "text",
        map = wc.map, reduce = wc.reduce,combine = T)
}

> wordcount(input)
> from.dfs("/tmp/file24053f4a0d65")
````
这里要注意的是 这个临时文件的名字是变化的 请自己根据上一条命令的返回信息进行替换


### 参考文献
1.[Linux环境下RHadoop配置笔记](http://hijiangtao.github.io/2014/03/23/RHadoopSetupLinux/)
2.[RHadoop实践系列文章](http://blog.fens.me/series-rhadoop/)
