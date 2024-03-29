---
title: "病人记录的健康信息PGHD指南"
meta_title: ""
description: "this is meta description"
date: 2015-08-12T17:25:12Z
image: "/images/image-placeholder.png"
categories: ["工作"]
author: "haisheng"
tags: ["互联网医疗", "PGHD","HIT"]
draft: false
---




##  病人记录的健康信息PGHD指南

为的是定义和提出一个将患者记录的健康信息整合到临床实践中的流程。

>有人在GG的博客上问了这样的一个[问题](http://www.healthintersections.com.au/?p=2359),随着各种穿戴式设备和消费者端的网站越来越多，如何使用Fhir来记录和表达患者记录的健康信息，这些信息又如何与传统的医疗信息系统整合，在患者的诊疗服务过程中发挥作用，作者答这不是个技术问题，更多是策略流程问题，一位专家对此问题的答案如下，这个问题很复杂，很复杂。
数据大致上可以分为5大类：1、不需要校验/核对的数
据，纯客观数据，如 患者抑郁自评工具（9条目病人健康问卷）（PHQ-9) ；2、不需要校验/核对的数据，直接来自设备/HealthKIT/google fit的数据；3、需要很少的校验，数据大部分是客观的，但是医生可能需要核对患者是否理解问题的范围，如 ADLs, pain score, family history HPI等；4、需要校验/核对的数据，一般的，如过敏、疾病、用药、免疫接种等，也就是能够为医师决策有帮助的，会记录到医生书写的病历中的数据；5、仅仅是介绍情况的数据，不会单独存储起来。
取决于采集的方式不同，确认的方式也各异。John Halamka提到了BIDMC 患者数据建议[原文链接：Patient Generated Health Data Guideline](http://www.healthintersections.com.au/wp-content/uploads/2015/08/bidmc-patient-data.pdf)，还有一个[屁屁踢](http://www.healthintersections.com.au/wp-content/uploads/2015/08/bidmc-patient-data-ppt.pdf),概括来讲，定义了将患者记录的健康信息整合到临床实践的流程。医生可能会使用PGHD来辅助决策，与其他在医疗机构内部采集和记录的数据一样。在数据之间出现不一致时需要进行判断。



[原文链接：Patient Generated Health Data Guideline](http://www.healthintersections.com.au/wp-content/uploads/2015/08/bidmc-patient-data.pdf)


### 目的

Beth Israel Deaconess支持将患者记录的健康信息纳入到患者病历中，使得医生和患者能够得到更好的诊断、评估和对健康状况的管理。该文档提出了一些医生在临床实践中使用患者记录的健康信息
的建议。

### PGHD的定义

健康相关的数据，包括健康史、症状、biometric data、治疗史、选择的生活方式和由患者、designees所创建、记录或收集的其他信息。PGHD包括从患者的电子设备、PatientSite的调查问卷和纸质调查问卷中获取的数据

#### PGHD的分类

目前医务人员能够拿到大量的由患者记录的或超出临床领域的文档，其中可能包括但不限于：

1、规定时间段内的检查检验(prescribed testing)
比如自动的blood pressure cuff 或holter monitors。这些检查检验是诊断性检查的医嘱，可以通过webOMR来评估，会出现在检查检验结果记录中。

2、患者自己上报的健康史
比如家庭史和社会史，症状日记，患者上报的疗效，免疫接种的更新信息

3、患者采集的生理数据
如居家血压记录、体重测量值、血糖仪的记录

#### 数据监管

患者提供给BIDMC的数据相当于授权给BIDMC将其作为患者病历的一部分来存储、管理和使用数据。

#### 隐私

PGHD 数据和存储在患者病历中的临床数据拥有同样的隐私策略

#### 使用数据来进行临床决策

医生可能会使用PGHD来辅助决策，与其他在医疗机构内部采集和记录的数据一样。在数据之间出现不一致时需要进行判断。


### 获取和使用PGHD数据的流程

PGHD 数据的采集和利用必须严格遵守以下流程：

* 1、申请
决定采集和上传PGHD是由医生和患者共同决定的，讨论indication，数据采集的时间长度和频率，以及期望达到的效果
* 2、采集
可以是电子形式或纸质方式来采集和记录数据，取决于患者和医生的喜好和需求。
* 3、传输
通过以上流程采集的用于临床诊疗的数据应该在符合现有政策的情况下传输到医疗中心以便整合到患者病历中。
    * a 对于纸质的数据，应通过扫描、总结和转录的方式整合到sheet和note中病历或表单中
    * b 对于电子化数据，应该安全的传输到BIDMC。有可能的话，PatientSite和其他应用程序应该采用标准化的方式来传输数据给BIDMC
* 4、存储
数据应该以满足现有BIDMC政策的方式安全存储。所有电子化采集的PGHD数据都应该附加描述何时何地何种方式采集和传输数据的元数据。
* 5、通知
根据具体厂家可以是主动或被动的方式告知医生。可以在数据采集之前就商定好。
* 6、回顾和核对
应由要求采集数据的医生负责回顾和核对患者记录的信息
* 7、动作


note
1、 PatientSite 是BIDMC出品的患者门户网站。
 