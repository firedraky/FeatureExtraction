# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2015-01-08
# version: 0.1
import shutil
__author__ = 'lifuxin'
'''
    将各个属性进行整理，然后得到特征矩阵:
    得到的特征矩阵分为三类：
'''

if __name__ == "__main__":
    topicnameSet = {"DamnItsTrue","BieberD3D","Egypt","Ff",
                    "MentionKe","NEVERSAYNEVERD3D",
                    "TeamFollowBack","Twitition",
                    "cumanNANYA","fb","februarywish",
                    "icantdateyou","improudtosay",
                    "jfb","nowplaying","nw",
                    "pickone","purpleglasses","shoutout","superbowl"}



    for topicname in topicnameSet:
        print topicname
        sourceFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/TopicWord/topicWordFreqStat"
        dstFile = "/Users/lifuxin/Program/SentimentClassification/MultiClassSVM/SpecialDomain/"+topicname+"/configInfo/topicWordFreqStat"
        # print sourceFile +"\tto\t"  + dstFile
        shutil.copyfile(sourceFile, dstFile)

        sourceFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/TopicWord/tweetWordStat"
        dstFile = "/Users/lifuxin/Program/SentimentClassification/MultiClassSVM/SpecialDomain/"+topicname+"/configInfo/tweetWordStat"
        shutil.copyfile(sourceFile, dstFile)

        sourceFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Divided/author.name"
        dstFile = "/Users/lifuxin/Program/SentimentClassification/MultiClassSVM/SpecialDomain/"+topicname+"/configInfo/author.name"
        shutil.copyfile(sourceFile, dstFile)

        sourceFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/SparkDataSet/testFile"
        dstFile = "/Users/lifuxin/Program/SentimentClassification/MultiClassSVM/SpecialDomain/"+topicname+"/data/testFile"
        shutil.copyfile(sourceFile, dstFile)