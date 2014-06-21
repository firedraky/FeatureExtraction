FeatureExtraction
=================

从tweet数据中提取文本特征以及非文本特征


一、目录结构：

-Dictionary
	-hownet
	-hownetPMI
	-wordnet
	-wordnetPMI
	-publicwordPMI
	-WORDPMI
	-mergeWordnetandhownet.py
-input
	-sorteddata
	-topicwordPMI
-output
-Divide
	-divide.py
-ProcessingData
	-PreprocessandgetFrequency.py
-SentimentDiffusion
	-checkposrelation.py
-RelationProcess
	-relationsentiment.py
-StatisticData
	-allusersametweetvar.py
	-check@relationsentiment.py
	-checkhyperlinkgraph.py
	-getEachAuthorSentiemnt.py
-FeatureProcess
	-getRelationAtt.py
	-gettopicwordPMI.py
	-MergeToGetFM.py

-StatisticResult
	-alllink.net
	-allinkstr
	-authorsentimentstat
	-graphbasicinfo
	-notsinglelink.net
	-RelationDirectMutualStat
	-SentimentConsistent
-Feature
	-attprefix
	-RelationAtt
	-nonpublicwordPMI
	-nonpublicwordfreqge2
	-removednonpublicword
	-FeatureMatrixWithNPW
	-FeatureMatrixWithNPWRelation
	-FeatureMatrixWithNPWsetZero
	-FeatureMatrixWithoutNPW

二、目录内容说明：
1.Dictionary：
数据：
1）主要包含了两个公共情感词库：hownet和wordnet
2）由PMI-IR计算共现次数，得到的hownetPMI值和wordnetPMI
3）合并两个PMI文件，得到情感词的WORDPMI
4）选择得到公共情感词的PMI文件
由于公共情感词基本不变，所以该目录的结构和文件也无需修改。
脚本：
1）mergeWordnetandhownet.py ： 用于将两个情感词库合并，同时去重，得到公共情感词PMI库
2.input：
1）sorteddata：按时间排序，并且有一个格式的源数据
2）topicwordPMI：后续得到的话题相关的情感词PMI-IR值

3.DivideData：
1）divide.py ： 用于处理源数据，根据sorteddata得到tweet数据集的各个字段
                每个字段都分别存入到一个文件中。同时，根据rating得到情感标记

4.ProcessingData
1)PreprocessandgetFrequency.py: 预处理数据，将分割后的杂乱文本处理得到预处理文本。
                                同时，得到话题中包含的单词以及词频：
                                precontent，topicword和topicwordfrequency
5.SentimentDiffusion
1)checkposrelation.py:根据作者文件和文本文件得到tweetrelation

6.RelationProcess
1）relationsentiment.py:根据tweetrelation和sentiment文件得到，当前tweet的情感，
                        以及与其有关联的tweet的情感

7.StatisticData ： 实验前的数据统计
1）allusersametweetvar.py : 作者情感一致性检验
2）check@relationsentiment.py ： 统计direct和mutual边的情感一致性
3）checkhyperlinkgraph.py ： 得到图的基本信息，以及画图用的数据，以一定的格式存储
4）getEachAuthorSentiemnt.py ： 统计每个作者所发的tweet中，正，中，负三类情感的数量

8.StatisticResult：统计结果文件，保存统计结果的
	-alllink.net
	-allinkstr
	-authorsentimentstat
	-graphbasicinfo
	-notsinglelink.net
	-RelationDirectMutualStat
	-SentimentConsistent

9.FeatureProcess ： 处理各个特征，得到特征矩阵的文件
1）getRelationAtt.py : 根据tweetrelation得到relation feature （parent，child）
2）gettopicwordPMI.py ： 根据话题相关的情感词topicwordPMI以及topicword词频，得到非公共情感词库及其PMI
3）MergeToGetFM.py ：根据各个特征，得到不同的特征矩阵


10.Feature ： 特征和特征矩阵集
	-attprefix
	-RelationAtt
	-nonpublicwordPMI
	-nonpublicwordfreqge2
	-removednonpublicword
	-FeatureMatrixWithNPW
	-FeatureMatrixWithNPWRelation
	-FeatureMatrixWithNPWsetZero
	-FeatureMatrixWithoutNPW
