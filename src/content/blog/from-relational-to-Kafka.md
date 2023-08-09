---
title: "关系型数据库向KAFKA迁移 FROM RELATIONAL INTO KAFKA"
meta_title: ""
description: "this is meta description"
date: 2015-04-26T14:19:12Z
image: "/images/image-placeholder.png"
categories: ["工作"]
author: "haisheng"
tags: ["日记", "数据仓库","KAFKA"]
draft: false
---





##  关系型数据库向KAFKA迁移 FROM RELATIONAL INTO KAFKA

英文版： [FROM RELATIONAL INTO KAFKA](http://ingest.tips/2015/04/26/from-relational-into-kafka/)
中文版：[关系型数据库向KAFKA迁移](http://wanghaisheng.github.io/2015/04/26/from-relational-to-Kafka)

去年我做了一个极受欢迎的“如何从数据仓库迁移到Hadoop”教程，大概内容可以在[percona 会议的网站上](https://www.percona.com/live/mysql-conference-2014/sessions/relational-hadoop-migrating-your-data-pipeline)
看到。过去的四年我基本上都在和如何从传统ER数据库向Hadoop进行数据迁移打交道。
目前，我正在做的是，如何将数据从数据仓库迁移到 Kafka  。之前我就说过，Hadoop是一个性价比极高的数据仓库的解决方案。但Kafka不是数据仓库，即使你可以直接
用Hive查询Kafka的数据，数据访问的模式是有质的差异。Kafka 是一个很棒的管道和消息总线。

为什么要把数据从关系型数据库迁移到Kafka上呢？因为如果有上以千记的系统都想要访问关系型数据库中的数据，你绝对不想让每个app都能直接访问OLTP数据库 业务数据库
。一旦业务数据库down掉之后，会直接带来经济损失。

把数据从业务数据库中迁移到Kafka中来，这样大家就可以不影响DBA工作的情况下即可访问数据，更重要的是，完全用不到DBA。
要怎么实现数据从业务数据库中迁移到Kafka呢？如果你是个DBA，不了解什么是Kafka，可以看一下这个[PPT:Kafka for DBAs](http://www.slideshare.net/gwenshap/kafka-for-dbas)
基本上有如下几种方式：
* 1、[Sqoop2](http://sqoop.apache.org/)能够从支持JDBC的任何数据源把数据导入到Kafka中去。它是直接访问数据库的，你需要DBA的配合。
* 2、[MySQL到Kafka CDC](https://github.com/wushujames/mysql-cdc-projects/wiki)James Cheng总结了所有与MySQL到Kafka CDC之间数据迁移的项目。
基于MySQL CDC的方式是很安全的，系统是从数据库的事务日志中拿到数据，无需直接访问生产系统的库表。
* 3、[bottledwater-pg](https://github.com/confluentinc/bottledwater-pg)Martin Kleppmann的开源项目，利用Postgres事务日志将Postgres中的数据迁移到Kafka，具体介绍请参考[Bottled Water: Real-time integration of PostgreSQL and Kafka](http://blog.confluent.io/2015/04/23/bottled-water-real-time-integration-of-postgresql-and-kafka/).其中导出的数据是Avro格式
保留了原始数据的schema，其他大部分项目都用的csv的文本格式。
* 4、对于Oracle的Redo日志而言，[GoldenGate](https://www.oracle.com/middleware/data-integration/goldengate/big-data/index.html)
提供了一个Flume adapter但价格不菲，据说[DBVisit](http://www.dbvisit.com/)正在尝试使用自己的CDC的方式来解决数据从Oracle到Kafka的迁移

等数据迁移到Kafka中的时候，可以做如下选择：

* 1、使用一些如Cloudera Search, Elastisearch 的文本索引技术
* 2、使用流处理方式来处理数据，将其导入到NoSQL数据库当做物化视图来使用
* 3、转移至审计系统
* 4、转移至监控系统
* 3、在不同的Dashboard进行展示
* 3、用作系统缓存
