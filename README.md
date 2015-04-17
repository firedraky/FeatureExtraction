FeatureExtraction
===================

该文件描述了从tweet数据中提取文本特征以及非文本特征的基本流程

##目录结构：

>Dictionary<br>
    1）主要包含了两个公共情感词库：hownet和wordnet<br>
    2）由PMI-IR计算共现次数，得到的hownetPMI值和wordnetPMI<br>
    3）合并两个PMI文件，得到情感词的WORDPMI<br>
    4）选择得到公共情感词的PMI文件<br>
    由于公共情感词基本不变，所以该目录的结构和文件也无需修改。<br>
>>hownet<br>
>>hownetPMI<br>
>>wordnet<br>
>>wordnetPMI<br> 
>>publicwordPMI<br> 
>>WORDPMI<br> 
>>mergeWordnetandhownet.py<br>
    用于将两个情感词库合并，同时去重，得到公共情感词PMI库<br>

>input<br>
>>sorteddata<br>
    按时间排序，并且有一个格式的源数据<br>
>>topicwordPMI<br>
    后续得到的话题相关的情感词PMI-IR值<br>

>output<br>

>DivideData<br>
    正向表情符号：:),;), :-),^_^,^^,:-),-),:D,;],:],:P,;P,:p,;p,-__-,-_-   <br>
    负向表情符号：:(,:-(,:[    <br>
>>divide.py<br>
    用于处理源数据，根据sorteddata得到tweet数据集的各个字段 <br>
    每个字段都分别存入到一个文件中。同时，根据rating得到情感标记   <br>
    
>ProcessingData<br>
>>PreprocessandgetFrequency.py<br>
    预处理数据，将分割后的杂乱文本处理得到预处理文本。同时，得到话题中包含的单词以及词频<br>
    输出：precontent，topicword和topicwordfrequency

>SentimentDiffusion<br>
>>checkposrelation.py<br>
    根据作者文件和文本文件得到tweetrelation  <br>

>RelationProcess<br>
>>relationsentiment.py<br>
    根据tweetrelation和sentiment文件得到，当前tweet的情感，以及与其有关联的tweet的情感   <br>

>StatisticData<br>
    实验前的数据统计<br>
>>allusersametweetvar.py<br>
    作者情感一致性检验   <br>
>>check@relationsentiment.py<br>
    统计direct和mutual边的情感一致性  <br>
>>checkhyperlinkgraph.py<br>
    得到图的基本信息，以及画图用的数据，以一定的格式存储  <br>
>>getEachAuthorSentiemnt.py<br>
    统计每个作者所发的tweet中，正，中，负三类情感的数量    <br>
    
>StatisticResult<br>
    统计结果文件，保存统计结果的  <br>
>>authorsentimentstat    <br>
>>RelationDirectMutualStat    <br>
>>SentimentConsistent   <br>  
>>RelationDirectMutualStat    <br>
>>SentimentConsistent   <br>  
>>alllink.net   <br>
>>allinkstr <br>
>>graphbasicinfo    <br>
>>notsinglelink.net <br>
    
>FeatureProcess<br>
    处理各个特征，得到特征矩阵的文件    <br>
>>getRelationAtt.py     <br>
    根据tweetrelation得到relation feature （parent，child）    <br>
>>gettopicwordPMI.py    <br>
    根据话题相关的情感词topicwordPMI以及topicword词频，得到非公共情感词库及其PMI  <br>
>>MergeToGetFM.py   <br>
    根据各个特征，得到不同的特征矩阵    <br>

>Feature<br>
    生成的特征和特征矩阵集  <br>
>>attprefix    <br>
>>RelationAtt    <br>
>>nonpublicwordPMI    <br>
>>nonpublicwordfreqge2    <br>
>>removednonpublicword    <br>
>>FeatureMatrixWithNPW    <br>
>>FeatureMatrixWithNPWRelation    <br>
>>FeatureMatrixWithNPWsetZero    <br>
>>FeatureMatrixWithoutNPW    <br>


##################################################################
#
#   百万数据处理
#   封闭的带表情符号数据集合，数量是 1915200
#        all_asc_tweetsOutput/filterData/EmocCloseData
###################################################################
FilterData
    fitlerData.py 根据需求过滤数据
    得到带表情符号的数据，以及通过带表情符号得到封闭数据集
    输出：all_asc_tweetsOutput/filterEmocData 含有表情符号的数据集 1208266条tweets
         all_asc_tweetsOutput/EmocCloseData 封闭数据集  1915200条tweets

#####################################################################
HashTag 筛选话题
allTweetsPreprocess/statHashTag.py
    输出：all_asc_tweetsOutput/HashTagStat HashTag统计信息
手工过滤，筛选20个话题 topicData/
    BieberD3D	857
    DamnItsTrue	608
    Egypt	2148
    MentionKe	3749
    NEVERSAYNEVER3D	896
    TeamFollowBack	1495
    Twitition	1467
    cumanNANYA	1425
    fb	820
    februarywish	739
    Ff	5231
    icantdateyou	667
    improudtosay	563
    jfb	1560
    nowplaying	5888
    nw	669
    pickone	643
    shoutout	2933
    Superbowl	2344
    purpleglasses 744
##################################################################
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

    ### allTweetsPreprocess/selectTopicWord.py:

4 Opinion word and target word extraction
    输入： public word set, publicwordPMI 和 content,author.name
    使用Java程序得到dependency relation，Opinion word set 和 target word set

4.2 合并所有话题下的topicword
    allTweetsPreprocess/mergeTopicword.py :
    输出：all_asc_tweetsOutput/SpecialDomain/alltopicword

5. 得到某个话题领域的特征矩阵
    allTweetsPreprocess
        训练数据，测试数据
        MergeToGetFM.py ：根据各个特征，得到不同的特征矩阵
        输出：主要FeatureMatrixWithNPWRelation


6. 从混合话题数据中抽取出初始训练数据。选择正、中、负 1:1:1 的初始训练数据
    训练数据
    allTweetsPreprocess/RandomSamplingData.py : 蓄水池方法
    输出除了训练数据和测试数据的特征向量，还包含precontent

7. 生成arff的前缀
    allTweetsPreprocess/generateAttPrefix.py

8. 数据格式转换为spark mllib的格式
    allTweetsPreprocess/formatConvert.py:
    将weka格式的数据转化为spark mllib数据要求的格式
    对于label和topicname的对应：
        positive:0
        neutral:1
        negative:2
        unknown:3

    属性：
    20000 表情符号
    20001 否定词个数
    20002 年份
    20003 月份
    20004 日期
    20005 小时
    20006 分钟
    20007 父节点
    20008 子节点
    20009 话题
    20010 标记
8. 计算topic word在每个tweet中出现的次数
    训练数据，测试数据，跑两次
    getTopicWordFreq.py 输出格式： topicwordNo tweetId:freq tweetId:freq ...
    getTweetWordStat.py 输出格式： tweetId wordNo:freq wordNo:freq ...

8.2 将处理好的数据move到AdaptiveCotrain工程目录下
    allTweetsPreprocess/moveData.bash
7. 情感分类 AdaptiveCotrain

8. 使用 StanfordParser／GenerateTuples生成三元组
    通过moveTASC2Tuple.sh将AdaptiveCotrain生成的各类情感词移到 StanfordParser 目录下
    使用generateTuples.sh批量生成三元组(话题相关情感词)
    生成通用话题情感词三元组：generatePublicWordTuples.sh

9. 将不同话题下的不同分类结果的二元组合并到一个文件中
   mergeTuples.sh  合并二元组 ＝》
topicname   author     dependentWordString(opinion word) weight
例子：
DamnItsTrue     sekarAthaya        my      0.43459480489818014

10.考虑3个变量的组合：author topicdomain   opinionword
    statistic.sh