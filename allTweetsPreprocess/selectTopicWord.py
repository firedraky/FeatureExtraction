# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2015-01-08
# version: 0.1
__author__ = 'lifuxin'
'''
    读取公共情感词publicwordPMI 和 话题内的词频统计 topicwordfrequency
    然后过滤出词频一定范围内，并且不是公共情感词的话题相关情感词，然后按照词频的降序输出
'''


if __name__  == "__main__":
    # 输入：
    publicWordPMIFile = "../Dictionary/publicwordPMI"
    topicwordFreqFile = "../all_asc_tweetsOutput/superbowl/Preprocess/topicwordfrequency"

    freqLThreshold = 1
    freqHThreshold = 200
    # 输出：
    topicWordsFreqFile = "../all_asc_tweetsOutput/superbowl/TopicWord/topicWordsFreq"
    removedTopicWordsFreqFile = "../all_asc_tweetsOutput/superbowl/TopicWord/removedTopicWordsFreq"

    publicWordDic={}
    topicWordFreqMap={}

    removedTopicWordWriter = open(removedTopicWordsFreqFile,"w")
    topicWordFreqWriter = open(topicWordsFreqFile,"w")

    # 读取公共情感词以及其PMI值
    with open(publicWordPMIFile,"r") as publicWordReader:
        for publicWordValue in publicWordReader:
            wordValue = publicWordValue.strip().split("\t")
            publicWordDic[wordValue[0]] = wordValue[1]
    publicWordReader.close()

    # 读取话题相关情感词词频文件
    with open(topicwordFreqFile,"r") as topicwordFreqReader:
        for topicWordFreq in topicwordFreqReader:
            wordFreq = topicWordFreq.strip().split("\t")
            if wordFreq.__len__()==2 and wordFreq[0] !="" and wordFreq[1]!="":
                if not publicWordDic.has_key(wordFreq[0]):
                    topicWordFreqMap[wordFreq[0]] = wordFreq[1]
                else:
                    removedTopicWordWriter.write(topicWordFreq)

    topicwordFreqReader.close()

    topicWordFreqList = sorted(topicWordFreqMap.items(),lambda x,y: cmp(int(x[1]),int(y[1])),reverse=True)

    for key,value in topicWordFreqList:
        if int(topicWordFreqMap[key])>= freqLThreshold and int(topicWordFreqMap[key]) <= freqHThreshold:
            topicWordFreqWriter.write(key+"\t"+value+"\n")
        else:
            removedTopicWordWriter.write(key+"\t"+value+"\n")


    topicWordFreqWriter.flush(),topicWordFreqWriter.close()
    removedTopicWordWriter.flush(),removedTopicWordWriter.close()


