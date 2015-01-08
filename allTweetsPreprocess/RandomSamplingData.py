# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2015-01-08
# version: 0.1
__author__ = 'lifuxin'
'''
    随机采集数据 : 蓄水池抽样
    注意，中性数据是人工标注数据，全部选择
    有四个标注：positive,neutral,negative,unknown
'''
import random

if __name__ == "__main__":
    # 输入：FeatureMatrixWithNPWRelation 带有话题相关情感词和relation 并且话题相关情感词设置为0
    featureFile = "../all_asc_tweetsOutput/mixedTopic/Feature/FeatureMatrixWithNPWRelation"
    numSampleData = 100

    # 输出：
    initialTrainFile = "../all_asc_tweetsOutput/mixedTopic/DataSet/trainFile"
    mixTopicTestFile = "../all_asc_tweetsOutput/mixedTopic/DataSet/testFile"

    featureReader = open(featureFile,"r")
    initialTrainWriter = open(initialTrainFile,"w")
    mixTopicTestWriter = open(mixTopicTestFile,"w")

    tweetId = 1

    numSelectedPositve = 0
    numSelectedNegative = 0
    numSelectedNeutral = 0

    selectedPositiveTweetIds={}
    selectedNegativeTweetIds={}
    selectedNeutralTweetIds={}

    for featureVector in featureReader:
        featureVector = featureVector.strip("\n")
        if "positive" in featureVector:
            if len(selectedPositiveTweetIds) < numSampleData:
                selectedPositiveTweetIds[numSelectedPositve+1] = tweetId # 1..numSampleData
                numSelectedPositve = numSelectedPositve+1
            else:
                # k/n 的概率选择该tweet，如果选择 随机 1/k的概率选择剔除某个tweet
                chooseTweetProb = random.randint(1,tweetId)
                if chooseTweetProb > numSampleData:
                    deleteNo = random.randint(1,numSampleData)
                    selectedPositiveTweetIds[deleteNo] = tweetId

        if "negative" in featureVector:
            if len(selectedNegativeTweetIds) < numSampleData:
                selectedNegativeTweetIds[numSelectedNegative+1] = tweetId # 1..numSampleData
                numSelectedNegative = numSelectedNegative+1
            else:
                # k/n 的概率选择该tweet，如果选择 随机 1/k的概率选择剔除某个tweet
                chooseTweetProb = random.randint(1,tweetId)
                if chooseTweetProb > numSampleData:
                    deleteNo = random.randint(1,numSampleData)
                    selectedNegativeTweetIds[deleteNo] = tweetId

        if "neutral" in featureVector:
            if len(selectedNeutralTweetIds) < numSampleData:
                selectedNeutralTweetIds[numSelectedNeutral+1] = tweetId # 1..numSampleData
                numSelectedNeutral = numSelectedNeutral+1
            else:
                # k/n 的概率选择该tweet，如果选择 随机 1/k的概率选择剔除某个tweet
                chooseTweetProb = random.randint(1,tweetId)
                if chooseTweetProb > numSampleData:
                    deleteNo = random.randint(1,numSampleData)
                    selectedNeutralTweetIds[deleteNo] = tweetId

        tweetId = tweetId+1
    featureReader.close()

    # 按照tweetId排序
    selectedPositiveTweetIdList = sorted(selectedPositiveTweetIds.items(),lambda x,y: cmp(int(x[1]),int(y[1])),reverse=False)
    selectedNegativeTweetIdList = sorted(selectedNegativeTweetIds.items(),lambda x,y: cmp(int(x[1]),int(y[1])),reverse=False)
    selectedNeutralTweetIdList = sorted(selectedNeutralTweetIds.items(),lambda x,y: cmp(int(x[1]),int(y[1])),reverse=False)

    selectedTweetIds = {}
    numSelected = 1
    for key,value in selectedPositiveTweetIdList:
        selectedTweetIds[numSelected] = value
        numSelected = numSelected+1

    for key,value in selectedNeutralTweetIdList:
        selectedTweetIds[numSelected] = value
        numSelected = numSelected+1

    for key,value in selectedNegativeTweetIdList:
        selectedTweetIds[numSelected] = value
        numSelected = numSelected+1

    selectedTweetIdList = sorted(selectedTweetIds.items(),lambda x,y: cmp(int(x[1]),int(y[1])),reverse=False)



    # 将选择好的数据输入到训练集，其余输入到测试集
    tweetId = 1
    seletedId = 0
    selectedTweetId = selectedTweetIdList[seletedId][1]
    featureReader = open(featureFile,"r")
    for featureVector in featureReader:
        featureVector = featureVector.strip("\n")
        if tweetId == selectedTweetId:
            initialTrainWriter.write(str(featureVector)+"\n")
            seletedId = seletedId + 1
            if seletedId < len(selectedTweetIdList):
                selectedTweetId = selectedTweetIdList[seletedId][1]
            else:
                selectedTweetId = -1
        else:
            mixTopicTestWriter.write(str(featureVector)+"\n")
        tweetId = tweetId +1

    initialTrainWriter.flush(),initialTrainWriter.close()
    mixTopicTestWriter.flush(),mixTopicTestWriter.close()
