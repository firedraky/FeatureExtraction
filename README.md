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
正向表情符号：:),;), :-),^_^,^^,:-),-),:D,;],:],:P,;P,:p,;p,-__-,-_-
负向表情符号：:(,:-(,:[
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



##################################################################
#
#   百万数据处理
#   封闭的带表情符号数据集合，数量是 1915200
#        all_asc_tweetsOutput/filterData/EmocCloseData
###################################################################
1. 人工标注数据
    humanLabel.py: 将EmocCloseData中带表情符号的数据进行正／负标注，然后输出需要人工标注的数据
        输入：   封闭的数据集：all_asc_tweetsOutput/filterData/EmocCloseData
        输出：   已经按照正负标注好的数据：all_asc_tweetsOutput/filterData/HumanLabel/EmocCloseDataLabel
                需要人工标注的数据：all_asc_tweetsOutput/filterData/HumanLabel/humanLabelContent
                需要人工标注的数据的位置，tweetId：all_asc_tweetsOutput/filterData/HumanLabel/humanLabelNumber

    进行人工标注数据：
        输出： all_asc_tweetsOutput/filterData/HumanLabel/humanLabel500

    mergeHumanLabel.py: 合并人工标注的数据HumanLabel/humanLabel500 和 通过表情符号标注的数据HumanLabel/EmocCloseDataLabel
        输入：   已正负标注好的数据：all_asc_tweetsOutput/filterData/HumanLabel/EmocCloseDataLabel
                人工标注的数据：all_asc_tweetsOutput/filterData/HumanLabel/humanLabel500
                人工标注数据对应的位置：all_asc_tweetsOutput/filterData/HumanLabel/humanLabelNumber
        输出：   合并的数据标注：all_asc_tweetsOutput/filterData/HumanLabel/mergedLabel
                合并的数据标注情感：all_asc_tweetsOutput/filterData/HumanLabel/mergedSentiment

    统计 mergeLabel中正类／负类的数据量比例：
        正类：994822
        负类：119763
        标注的中性数据：100

    注意：
        positive : 1
        neutral : 0
        negative : -1
        unknown : 2
2. 处理混合数据
    allTweetsPreprocess/divide.py:
        删除掉输出的sentiment 和 label, 因为已经之前有标注好的

    ProcessingData/PreprocessandgetFrequency.py:

    SentimentDiffusion/checkposrelation.py:

    RelationProcess/relationsentiment.py:

    StatisticData
        allusersametweetvar.py : 作者情感一致性检验
        check@relationsentiment.py ： 统计direct和mutual边的情感一致性
        checkhyperlinkgraph.py ： 得到图的基本信息，以及画图用的数据，以一定的格式存储
        getEachAuthorSentiemnt.py ： 统计每个作者所发的tweet中，正，中，负三类情感的数量

    FeatureProcess
        getRelationAtt.py : 根据tweetrelation得到relation feature （parent，child）

3. 处理某个话题领域的话题相关情感词
    allTweetsPreprocess/divide.py:

    ProcessingData/PreprocessandgetFrequency.py:

    SentimentDiffusion/checkposrelation.py:

    RelationProcess/relationsentiment.py:

    FeatureProcess
        getRelationAtt.py : 根据tweetrelation得到relation feature （parent，child）

    allTweetsPreprocess/selectTopicWord.py:

4. 得到混合数据的特征矩阵
    FeatureProcess
        MergeToGetFM.py ：根据各个特征，得到不同的特征矩阵

5. 得到某个话题领域的特征矩阵
    FeatureProcess
        MergeToGetFM.py ：根据各个特征，得到不同的特征矩阵

6. 从混合话题数据中抽取出初始训练数据。选择正、中、负 1:1:1 的初始训练数据
    allTweetsPreprocess/RandomSamplingData.py : 蓄水池方法

7. 生成arff的前缀g
    allTweetsPreprocess/generateAttPrefix.py

8. 数据格式转换为spark mllib的格式
    allTweetsPreprocess/formatConvert.py:
    将weka格式的数据转化为spark mllib数据要求的格式
    对于label和topicname的对应：
        positive:0
        neutral:1
        negative:2
        unknown:3

7. 情感分类 AdaptiveCotrain