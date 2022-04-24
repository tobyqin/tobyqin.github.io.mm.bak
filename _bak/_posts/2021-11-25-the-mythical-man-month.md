---
title: 人月神话笔记
categories: [Tech]
tags: [project management, software development]
date: 2021-11-25
layout: single
---

一些零零碎碎的读书笔记，这是一本比我年纪还大的书，作者布鲁克斯(FrederickP.Brooks.Jr.)写于 1975 年，源于作者在 IBM 公司任 System 计算机系列以及其庞大的软件系统 OS 项目经理时的实践经验。

正文开始。

## 焦油坑

编程的世界犹如史前时期的焦油坑，上帝见证了恐龙，猛犸，剑齿虎在里面挣扎，他们越挣扎，焦油就越紧，没有任何猛兽足够强壮和具有足够的技巧来挣脱束缚，最后都会沉入坑底。编程世界随着时间和资源的投入，最终会变的无比复杂，但还是会有更多人前仆后继，这个过程中有很多乐趣也有很多苦恼，这是一个许多人痛苦挣扎的焦油坑，多许多人而言，其中的乐趣远大于苦恼。

## 人月神话

在众多软件项目中，缺乏合理的时间进度是项目滞后的最主要原因。这个问题主要有 5 个原因。

1. 乐观主义和不真实的假设--假设一切都运作良好。
2. 错误将进度和工作量互换，假设人和月可以互换。
3. 不能持续进行估算，是的，估算也是需要持续进行的。
4. 缺少进度跟踪和监督。
5. 当意识到进度偏移时，下意识增加人力。

这个章节有很多名言被引用过，例如无论多少个母亲，孕育一个生命都需要十个月。**往进度滞后的项目加入更多的人力，只会让进度更落后 -- 对于错综复杂的项目尤其明显。**

## 外科手术队伍

对于大项软件项目，其中的每一部分都应该由一个团队解决，类似于外科手术队伍，而非一拥而上。这个队伍里所有专业的人都在解决问题，系统是一个或最多两个人的产物，在客观上达到概念的一致。**优秀的专业开发人员的生产率是较差的开发人员的 10 倍。**

## 贵族专制和系统设计

大教堂是历史上无与伦比的成就，达到了风格上的一致，但也代表了众多艺术家的技巧。系统设计也一样，概念一致性和完整性是架构师的责任，需要专制，但并不是只有架构师在创造并获得所有的荣誉，在实现过程中一样需要创造力和技术。

## 画蛇添足

项目经理不喜欢招第二次设计系统的架构师，因为往往在开发自己的第二个系统时，设计师所设计的系统的是最危险的，他们会不断装饰和润色，把第一次做系统的遗憾都想办法弥补掉，自律是设计师最重要的品质，设计师其实是用户的代理，易用性才是设计师的价值。

## 贯彻执行

如果确保所有人听从、理解并实现架构师的决策？文档是非常必要的工具，这也是架构师的产物。形式化定义比文字化叙述更有效，比如使用公式，图形等等。除此之外还有会议，日志，测试等流程可以确保项目被正确交付。为什么项目会失败：除了目标，人力，材料，时间和技术之外，交流其实更为重要，作者建议通过所有可能的途经来保持项目的透明度，非正式途经，会议，工作手册。另外为了提高交流的效率，大型项目合理的组织结构应该是树形的，参考前文的外科手术团队。

## 胸有成竹

实践是最好的老师，但如果不能从中学习，再多的实践也没有用。

## 削足适履

规模是软件系统产品用户成本一个重要部分，开发人员必须设置规模的目标，规模本身不是坏事，但是不必要的规模是不可取的。这里主要讲的是规模控制和管理，这是一件颇具技巧的事情。因为在一定的时间和空间要求下达到用户期望，对程序员的技艺有很高要求。

## 提纲挈领

项目记录决策是必要的，只有记录下来，分歧才会明朗，矛盾才会突出。文档还是同其他人沟通的渠道，只有书面计划是精确和可沟通的，如果一开始就认识到它的普遍性和重要性，就可以更好利用起来，而不会让它变成繁重的任务。

## 未雨绸缪

化学工程师很早就认识到，在实验室进行的化学反应，并不能在工厂中一步实现，普遍的做法是，选择一种方法，试试看，如果失败了，没关系，再试试别的。不管怎样，最重要的是先去尝试。一旦认识到实验性的系统必须被反复构建和丢弃，具有变更思想的重新设计不可避免，我们必须接受这样的事实，变化是与生俱来的。

## 干将莫邪

a good workman is known by his tools。巧匠因他的工具而出名。在软件项目中维护公共的通用工具有助于提高效率，另外项目经理必须意识到专业工具的需求，在这类工具不能吝啬人力和物力，对工具的熟练程度也极大影响了生产力。

## 另外一面

不同用户需要不同的文档，例如使用程序，验证程序，修改程序，这些文档的描述方式都不一样。作者认为正确维护文档的方式是将文档整合到源代码中，这也被称之为自动化文档。自动化文档激发了高级语言的使用，是一种值得推荐的方式。

## 没有银弹

软件工程中的根本和次要问题，没有任何技术或者管理上的进展，能许诺十年内使生产率，可靠性和简洁性获得数量级上的进步。这个章节很知名，我觉得大概的原因是作者用非常肯定的预期预测了未来，所以很多（聪明的）人总是想用各种方式来推翻作者的论断，无奈事实证明，真的没有银弹。作者基本的思路就是将软件工程拆分为了根本问题和次要问题，并尝试列举了其中的可能银弹，用来证明这样的事情并不现实，另外我还认为作者在激将和钓鱼，如果真的有人找到了银弹，对人类和社会而言，何尝不是一件好事。

解释一下银弹的背景：在所有恐怖民间传说的妖怪里，最可怕的是人狼，因为它们可以完全出乎意料地从熟悉的面孔变成可怕的怪物，为了对付人狼，我们在寻找可以消灭它们的银弹。大家熟悉的软件项目有一些人狼的特性，常常看似简单明了的东西，却有可能变成一个进度落后，超出预算，存在大量缺陷的怪物，因为我们听到了近乎绝望的寻求银弹的呼唤，寻求一种可以使软件成本降低，工作效率倍增的尚方宝剑。

## 再论没有银弹

属于再版后的番后篇，因为这篇文章发出后的确引来了极大地争议，其中有一篇论文作者也赞同其中的观点，叫《这就是银弹》，里面指出重用和交互的构件开发是解决软件根本困难的一种方法。对于解决软件的复杂性，可以有两种思路：层次化，通过分层来实现模块或者对象；增量化，持续地添加功能。但这也是导致系统复杂的原因，乐观主义是程序员的通病。还有另外一个观点，质量可以带来生产率的提高，关注质量，生产率会自然提高。

## 总结

软件开发的核心观点：概念完整性，一个整洁，优雅的产品必须向它的每个用户提供一个调理分明的概念模型，概念完整性是易用性中最重要的因素。结构师，结构师是用户的代理，也是概念模型的解释者，不清楚作者提到的结构师在当前的时代是哪类角色，不太像架构师，有点像产品经理，或者是二者的合体。

书本最后一部分主要是总结和观点再论述，这本书浓缩度极高，有点费脑子，不过推荐阅读。