title:   openCDS系列 I——内部数据结构
date:   2012-6-5 13:23:12
updated	:
permalink:
tags:
- 医疗信息标准
- OpenCDS
- HIT
- 临床决策支持
categories:
- 医疗信息标准
- 临床决策支持

---

译自Notes on OpenCDS Internal Data Structure

目的
openCDS的内部数据结构大致上是基于HL7 2011年9月份投票版中VMR(虚拟医疗记录)的逻辑模型。该逻辑模型中严格定义了所有的数据元素，数据元素的定义都有对应的内部数据结构。
内部数据结构更多地与schema保持一致，schema是对逻辑模型的说明性补充材料。schema
提供了2种方式来定义数据关联。
1.嵌套式 XML和对象结构中特有的
2.列表式 关系型数据库结构中特有的
内部数据结构中嵌套式结构位于父类的子节点中，这样临床声明中的嵌套数据出现在闭合式数据元素的末尾。罗列式的数据关系位于一个“已评估个体”所有其他数据的末尾。
内部数据结构不是对外部的schema的完完全全的实现，抑或说，因为它试图使用单一的列表数据结构，这样规则编辑人员就可以很容易的使用。这意味着所有的嵌套式数据源是都被映射成列表式的，并且与列表格式的数据整合起来。
需要注意的是OpenCDS的使用者是否在嵌套式和列表式结构间复制数据。2种结构都可能用到，但是一个数据元素只能是其中的一种结构。
下面是一个VMR的实例，
嵌套式 相关的实体entity和临床声明都嵌套在源临床声明中

```
<vmr>
   <templateId root=""/>
   <patient>
            <id root=""/>
            <demographics/>
            <clinicalStatements>
                     <adverseEvents>
                               <adverseEvent>
                                        . . .
                                        <relatedEntityInRole>
                                                 <targetRole/>
                                                 <administrableSubstance>
                                                           . . .
                                                 </administrableSubstance>
                                        </relatedEntityInRole>
                                        <relatedClinicalStatement>
                                                 <targetRelationshipToSource/>
                                                 <observationResult>
                                                           . . .
                                                 </observationResult>
                                        </relatedClinicalStatement>
                               </adverseEvent>
                     </adverseEvents>
            </clinicalStatements>
   </patient>
</ vmr>
```
罗列式 每个临床声明和实体entity以及他们间的关系都单独罗列出来，没有嵌套
```
<vmr>
   <templateId root=""/>
   <patient>
            <id root=""/>
            <demographics/>
            <clinicalStatements>
                     <adverseEvents>
                               <adverseEvent>
                                        <id root="adverseEventId"/>
                                        . . .
                               </adverseEvent>
                     </adverseEvents>
                     <observationResults>
                               <observationResult>
                                        <id root="observationId"/>
                                        . . .
                               </observationResult>
                     </observationResults>
            </clinicalStatements>
            <clinicalStatementRelationships>
                     <clinicalStatementRelationship>
                               <sourceId root="adverseEventId"/>
                               <targetId root="observationId"/>
                               <targetRelationshipToSource code="reasonFor">
                     </clinicalStatementRelationship>
            </clinicalStatementRelationships>
            <clinicalStatementEntityInRoleRelationships>
                     <clinicalStatementEntityInRoleRelationship>
                               <clinicalStatementId root="adverseEventId"/>
                               <entityId root="substanceId"/>
                               <role code="allergen"/>
                     </clinicalStatementEntityInRoleRelationship>
            </clinicalStatementEntityInRoleRelationships>
            <entityLists>
                     <administrableSubstances>
                               <administrableSubstance>
                                        <id root="substanceId"/>
                                        . . .
                               </administrableSubstance>
                     </administrableSubstances>
            </entityLists>
   </patient>
</vmr>
```
内部结构
数据类型
起初通过复制得到内部数据类型
我们一开始通过复制逻辑模型和schema中的数据类型得到内部数据类型的定义。然后对数据类型的不同类做出一些改变将其变为可以在Drools和OpenCDS中可用的java bean
移除所有JaxB生成的所有批注，除了类的描述以外以及导入的JaxB类和生成代码中的所有方法。
利用Eclipse，我们进行如下操作：
1.添加getter setter方法
2.添加hash code和equal方法
3.添加toString方法
4.在类的头部添加Apache许可证的批注
修改一些内部数据类型
修改或优化一些内部数据类型以便我们使用。特别地，如下需要改变：
1.将CD数据类型(概念描述符)中嵌套式的displayName变为CD的一个属性，这是为了方便编辑rule。
2.将II数据类型中的root和extension改为一个单独的字符串，成为“root^extension”
的形式，这是为了在rule中将其作为唯一标识符来使用。注意II的实例并不包含extension 只包含root
3.将TS数据类型更换为java.util.Date数据类型
映射工具
有一个完成内部和外部数据类型间对应的映射工具类MappingUtility。映射的方法的命名如"DT2InternalDT"或"InternalDT2DT" DT表示数据类型的名称。
vMR中的类
外部的schema中定义的所有VMR中的类在内部结构中都有，除了以下几个：
* 1.RelatedEntity
*  2.RelatedClinicalStatement
* 3.RelatedEntityInRole
如如上三个类中的数据被标准化地分割为2部分。第一部分包含在Realted_class中包含的原始的实体或临床声明，将其移至对应的临床声明或者实体列表中去。第二部分包含了关系的本质，以及源和目标的id，这些关系类从原来的嵌套式结构更改为如下对应的列表式内部类结构：
* EntityRelationship
* ClinicalStatementRelationship
* ClinicalStatementEntityInRoleRelationship
需要注意的是对vmr类的处理和数据类型的一样，同时还有一个相关联的Mapper类，其中实现了pullIn和pushOut方法。在alpha版本以后对这些方法进行了修订，从原来的内部java bean中移除，转移到单独的方法中。
也有一些原本不属于vmr所定义的内部类，它们旨在简化rule的编辑。
从外部结构映射
接口org.opencds.vmr.v1_0.mappings.inPayloadUnmarshaller.java
PayloadUnmarshaller.java
此接口能够从DSS消息中读取base64编码的负载，将其转化为结构化的jaxb元素就可作为CDSInput。然后调用PayloadUnmarshaller接口来产生一个内部的vmr数据结构，这样推理引擎就可以处理了。
IBuildFactLists.java
该接口接收一个JaxB CDSInput 的元素，将其转化为内部的vmr结构，也就是一些事实的列表，这其中其实就是对提交数据的标准化，以便推理引擎的使用。
我们也提供了一种支持Drool 事实列表的实现。用户与不同的推理引擎交互就需要不同的内部结构，但是仍然是基于vmr的，我们也可以按照需要来替换这个模块。
向外部结构映射
接口org.opencds.vmr.v1_0.mappings.out
IBuildResultSet.java
该接口接收推理引擎处理过的事实列表，产生一个CDSOutput schema结构
的结构化输出，然后该结构进一步被IMappingOutbound接口 处理。
IMappingOutbound.java该接口接收IBuildResultSet 产生的 CDSOutput structure，产生一个base64编码的字符串作为DSS 服务的响应。
使用OpenCDS vMR
下面是对vMR的组织结构的概述，也是你如何使用它大体上的指导。首先，是一个VMR的组织结构概览，后面有一些在OpenCDS中如何使用它的建议，输入和输出都是一样。
Abstract Base Classes
在VMR中有2大类数据结构：临床声明表示感兴趣的活动/行为，实体就是指人/地，物在这些医疗活动中所拥有的角色。这些抽象类不可能单独实例化，但你可以在rule中涉及到它们。比如，你可以研究基本类中的通用元素来得到大概的结论一个特殊的活动是否发生，没有发生，已计划或者已预订。
临床声明
我们将医疗活动分为8类，对于每个类都有一个base类。临床声明自身就是如下子类的base类，包含它们所共有的元素。
* AdverseEventBase
* EncounterBase
* GoalBase
* ObservationBase
* ProblemBase
* ProcedureBase
* SubstanceAdministrationBase
* SupplyBase
EntityBase
它包含了所有人、地点，组织和其他事物的通用元素。它是EvaluatedPerson和其他7类entity的基础。
实例化的类
如下所列不是抽象类。你可以实例化其中之一来给OpenCDS传递数据，你也可以在rule中实例化它们来返回从OpenCDS中推论出的数据给你的应用程序。
EvaluatedPerson
它是VMR的根类，所有的ClinicalStatements和相关的entity都与一个EvaluatedPerson关联起来（更通俗的讲就是patient）。在家族病史或者传染病接触或其他类似的场景中，vmr也可能包含与patient 相关的其他的EvaluatedPerson 。这些EvaluatedPerson有2个属性：1）他们与病人有某种医学上的关系2）他们可能有某些和病人一样的医疗活动相关的数据。
然而，总是只有一个person 也就是patient，也是vmr中所关注的。OpenCDS中编写的rule旨在辅助patient的医疗服务。
当EvaluatedPerson继承自entityBase类时，采取与其他次要的entity不同的处理方法。patient是vmr的客体，而其他实体则参与与病人相关的医疗活动当中。
entity类
这些就是在医疗活动中扮演某个角色的次要实体。他们可能是用药、医护人员、实验室样本或者是医疗路径。
* AdministrableSubstance
* Entity
* Facility
* Organization
* Person
* Organization
* Specimen
Event类
这些类用来描述一个已经发生或者正在发生的医疗活动
* AdverseEvent
* EncounterEvent
* Goal
* ObservationResult
* Problem
* ProcedureEvent
* SubstanceAdministrationEvent
* SubstanceDispensationEvent
* SupplyEvent
DeniedEvent类 这些类用来描述一个并未发生的医疗活动，比如 血压的UnconductedObservation意味着并没有采集血压值（本来应该已经采集了的）。DeniedProblem表示病人并没有所描述的症状或问题
* DeniedAdverseEvent
* MissedAppointment
* UnconductedObservation
* DeniedProblem
* UndeliveredProcedure
* UndeliveredSubstanceAdministration
* UndeliveredSupply
Proposal类
这些类大多数openCDS的输出。如病人需要MMR，或者HbA1c检测，但他们也能表示输入。比如，会有一些类如给病人某种药物的提议，openCDS会依据病人目前的用药进行一些药物-药物反应评估。提议/建议没有医嘱或申请权威性强，常常用来给医务人员传递一些需要考虑的信息。
* AppointmentProposal
* GoalProposal
* ObservationProposal
* ProcedureProposal
* SubstanceAdministrationProposal
* SupplyProposal
Request and Order类
申请和医嘱常常是由医务人员为解决病人的某个问题或症状而提出的，它们比proposal要更正式一些，表示一些必须完成的请求，通常由辅助人员来完成
* AppointmentRequest
* ObservationOrder
* ProcedureOrder
* SubstanceAdministrationOrder
* SupplyOrder
Populating Data for submission to OpenCDS
Choose your structureVMR是非常灵活的，通常不止一种解决办法。一般而言，根据你的数据选择最接近的结构化方法是不错的思路。
如果你的数据是对象结构或者xml格式，嵌套式结构可能更适合你的输入。
另一方面，如果你从关系型数据库获取数据，罗列式的可能效果更好。
Use a template
一个模板就是对特定目的的输入数据的约束和要求的集合。因为不止一种方法来表示事物，最好为特定目的收集模板，这样rule就可以重用和共享。
随着时间的推移，OpenCDS会收集和发布模板。如果不存在一个模板能够满足你的特殊需要，在你开发rule的时候把需求记录下来，我们会帮你一起构建一个模板。
一旦openCDS中记录了一个模板，我们就会为它分配一个模板标识符templateID，可以在rule中引用这个templateID来确保提交的数据满足规则作者的要求。
注意同一个模板可以用在以不同结构提交的数据中 如对象/xml结构或者列表/关系型结构，因为模板解决数据内容的问题 而不是它们的结构。
Use Best Practices
我们会收集表达各种通用医疗数据结构的最佳实践，以及这些数据结构中的元素。在管理rule时我们也会努力这么做。
这些最佳实践会在单独的文档中记录。
Populating Data in rules for return from OpenCDS
OpenCDS Output StructureOpenCDS的输出结构的一部分是预先定义好的，但仍有不止一种方法来构建输出。只要有2种选择1）单个结果元素2）CDS输出结构包含Vmr的结构化数据
单个元素结果
如果你选择这种类型的结果，你的输出数据就是一个单一元素，使用任意ISO21090中支持的任意数据类型
。比如你可能返回布尔值 true，或者返回23的一个整数值。
CDSOutput Result如果你选择这种结果，你的输出会将你发送给OpenCDS的输入进行重组。某些情况下，甚至会很类似。
Use a template <write me>

Use Best Practices <write me>
