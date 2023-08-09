---
title: "译自Good Exchange Specifications- Microsoft vs Apple  by Grahame Grieve"
meta_title: ""
description: "this is meta description"
date: 2012-2-24T12:46:12Z
image: "/images/image-placeholder.png"
categories: ["工作"]
author: "haisheng"
tags: ["医疗信息标准", "译文","HIT","Grahame Grieve"]
draft: false
---



# 译自Good Exchange Specifications: Microsoft vs Apple  by Grahame Grieve

构建一个标准之初你必须要做的选择之一是如何进行领域分析。这是一个你如何使用story board故事版的问题。这里有苹果的做法，也有微软的做法。
苹果的做法
苹果的方法很简单：你以文档形式记录下你的story board，然后为你所接受的story board开发一种解决方案。接着产生一个十分有效的解决这些story board的精心制作的简单的workflow/product。你尽可能的覆盖他们的工作流的话，用户将希望有这样的结果，这也能很好的为他们服务。如果你没有覆盖他们的工作流程，那么，他们就不会是乖宝宝了。
微软的做法
这并不是很简单：一旦你以文档形式记录了你的story board，那么就总结概括一些你所看到的事物，解决通用的情况。你将会得到一个能够裁剪成你所想不到的所有用途下的灵活的、健壮的产品。用户将永远不会喜欢你们的产品，但是他们会不断的使用和购买他们，因为它们能帮用户完成他们所需要的。
顺便说一下，我是通过个人对Steve和Bill的了解学到的这两种方式的，因此你可以把它们当作信条。当然也不是-这只是我不断使用它们的产品而对他们工作所产生的感觉。同时，它只是一个stereotype。Anyone who’s tried to teach their grandma how to shoot rogue applications on their iPhone knows that Apple can produce some spectacularly bad UI as well。我也确信在微软有一些很好的易于使用的UI-但总的来说，这些stereotype在很长时间内还是正确的。

这两个都可以应用到标准上-你可以自己做业务分析，解决标准中的那些问题。它会很容易使用，适合特定的目的。它也能工作。也就是说当story board满足实施人员的问题时它就能工作。如果他们没有。。。那么，就会有另一种标准。如果你概化了需求，那么你的标准会比任一用户需要的更加复杂-但是至少它能用。
Thomas Beale
我认为一个好的解决方案是构建一个通用的框架，逐渐的增加一些更多的针对特殊use case的层，同时也保留通用层的可访问。特殊的usecase可以说生成的schema，业务流程特殊服务定义或者其他。但是二者都需要：一个通用的目的的计算和针对特殊行业actor使用的平台。
