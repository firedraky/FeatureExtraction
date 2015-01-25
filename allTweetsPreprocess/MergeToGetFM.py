# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2015-01-08
# version: 0.1
__author__ = 'lifuxin'
'''
    将各个属性进行整理，然后得到特征矩阵:
    得到的特征矩阵分为三类：
'''
if __name__ == "__main__":
    # 输入：
    preContentFile = "../all_asc_tweetsOutput/superbowl/Preprocess/precontent"

    # sentimentFile = "../all_asc_tweetsOutput/filterData/HumanLabel/mergedSentiment"
    sentimentFile = "../all_asc_tweetsOutput/superbowl/sentiment"

    yearFile = "../all_asc_tweetsOutput/superbowl/year"
    monthFile = "../all_asc_tweetsOutput/superbowl/month"
    dayFile = "../all_asc_tweetsOutput/superbowl/day"
    hourFile = "../all_asc_tweetsOutput/superbowl/hour"
    minFile = "../all_asc_tweetsOutput/superbowl/min"

    publicWordPMIFile = "../Dictionary/publicwordPMI"

    topicWordsFreqFile = "../all_asc_tweetsOutput/superbowl/TopicWord/topicWordsFreq"
    relationAttributeFile = "../all_asc_tweetsOutput/superbowl/Feature/RelationAtt"

    topicName = "superbowl"
    # 输出：
    FMatrixWithNPWfilename = "../all_asc_tweetsOutput/superbowl/Feature/FeatureMatrixWithNPW"
    FMatrixWithNPWsetZerofilename = "../all_asc_tweetsOutput/superbowl/Feature/FeatureMatrixWithNPWsetZero"
    FMatrixWithoutNPWfilename = "../all_asc_tweetsOutput/superbowl/Feature/FeatureMatrixWithoutNPW"
    FMatrixWithNPWsetzeroRelationfilename = "../all_asc_tweetsOutput/superbowl/Feature/FeatureMatrixWithNPWRelation"

    arffwithNPWriter = open(FMatrixWithNPWfilename,"w")
    arffwithNPsetzeroWriter = open(FMatrixWithNPWsetZerofilename,"w")
    arffwithoutNPWriter = open(FMatrixWithoutNPWfilename,"w")
    FMatrixWithNPWsetzeroRelationWriter = open(FMatrixWithNPWsetzeroRelationfilename,"w")

    # 为确保安全，非文本特征的标号从20000开始
    emocNo=20000
    negNo = 20001
    yearNo = 20002
    monthNo = 20003
    dayNo = 20004
    hourNo = 20005
    minNo = 20006
    ParentsAttNo = 20007
    ChildrenAttNo = 20008
    TopicNo = 20009
    sentimentNo = 20010


    sentimentReader = open(sentimentFile,"r")
    yearReader = open(yearFile,"r")
    monthReader = open(monthFile,"r")
    dayReader = open(dayFile,"r")
    hourReader = open(hourFile,"r")
    minReader = open(minFile,"r")
    publicwordReader = open(publicWordPMIFile,"r")
    topicWordReader = open(topicWordsFreqFile,"r")



    TweetNo=1
    DicTweetRelationAtt={}
    with open(relationAttributeFile,"r") as relationAttReader:
        for relationatts in relationAttReader:
            relationattarr = relationatts.strip().split(" ")
            DicTweetRelationAtt[TweetNo] = relationattarr
            TweetNo = TweetNo+1
    relationAttReader.close()

    tweetNo=1
    tweetdic={}
    for sentiment in sentimentReader:
        tweetlis=[]
        tweetlis.append(sentiment.strip())
        year = yearReader.readline().strip()
        month = monthReader.readline().strip()
        day = dayReader.readline().strip()
        hour = hourReader.readline().strip()
        min = minReader.readline().strip()
        tweetlis.extend([year,month,day,hour,min])
        tweetdic[tweetNo]=tweetlis
        tweetNo = tweetNo +1
    sentimentReader.close()
    yearReader.close(),monthReader.close(),dayReader.close(),hourReader.close(),minReader.close()

    wordNO=1
    publicworddic = {}
    for publicword in publicwordReader:
        wordvalue = publicword.strip().split()
        publicworddic[wordvalue[0]] = [wordvalue[1],wordNO]
        wordNO = wordNO+1
    publicwordReader.close()

    nonpublicworddic = {}
    for nonpublicword in topicWordReader:
        wordvalue=nonpublicword.strip().split()
        nonpublicworddic[wordvalue[0]] = [wordvalue[1],wordNO]
        wordNO = wordNO+1
    topicWordReader.close()

    num_publicword = publicworddic.__len__()
    num_nonpublicword = nonpublicworddic.__len__()
    numtextfeature = publicworddic.__len__()+nonpublicworddic.__len__()



    tweetNo = 0
    with open(preContentFile,"r") as contentreader:
        for tweetcontent in contentreader:
            tweetNo = tweetNo+1
            arffwithNPWriter.write("{"), arffwithoutNPWriter.write("{")
            arffwithNPsetzeroWriter.write("{")
            FMatrixWithNPWsetzeroRelationWriter.write("{")
            wordarr = tweetcontent.strip().split()
            num_EMO=0
            num_NEG=0
            num_ADD_MIN=0
            wordarrdic={}
            wordwithNPsetzerodic={}
            wordwithoutNPdic={}
            for word in wordarr:
                # 公共情感词
                if word in publicworddic.keys():
                    wordarrdic[publicworddic[word][1]]=publicworddic[word][0]
                    wordwithNPsetzerodic[publicworddic[word][1]]=publicworddic[word][0]
                    wordwithoutNPdic[publicworddic[word][1]]=publicworddic[word][0]
                    #arffwithNPWriter.write(str(publicworddic[word][1])+" "+str(publicworddic[word][0])+",")
                elif word in nonpublicworddic.keys():
                    wordarrdic[nonpublicworddic[word][1]]=nonpublicworddic[word][0]
                    wordwithNPsetzerodic[nonpublicworddic[word][1]]=0
                    #arffwithNPWriter.write(str(nonpublicworddic[word][1])+" "+str(nonpublicworddic[word][0])+",")
                elif word == "POSEMOC":
                    num_EMO = num_EMO+1;
                elif word == "NEGEMOC":
                    num_EMO = num_EMO - 1;
                elif word == "NEGWORD":
                    num_NEG = num_NEG+1
                elif word == "POSADD":
                    num_ADD_MIN = num_ADD_MIN +1
                elif word == "NEGMIS":
                    num_ADD_MIN = num_ADD_MIN -1
            wordarrdiclist = sorted(wordarrdic.items())
            for wordNo,value in wordarrdiclist:
                arffwithNPWriter.write(str(wordNo)+" "+str(value)+",")

            wordwithoutNPWdiclist = sorted(wordwithoutNPdic.items())
            for wordNo,value in wordwithoutNPWdiclist:
                arffwithoutNPWriter.write(str(wordNo)+" "+str(value)+",")

            wordwithNPsetzerodiclist = sorted(wordwithNPsetzerodic.items())
            for wordNo,value in wordwithNPsetzerodiclist:
                arffwithNPsetzeroWriter.write(str(wordNo)+" "+str(value)+",")
                FMatrixWithNPWsetzeroRelationWriter.write(str(wordNo)+" "+str(value)+",")

            arffwithNPWriter.write(str(emocNo)+" "+str(num_EMO)+","+str(negNo)+" "+\
                                   str(num_NEG)+","+str(yearNo)+" "+str(tweetdic[tweetNo][1])+\
                                   ","+str(monthNo)+" "+str(tweetdic[tweetNo][2])+","+\
                                   str(dayNo)+" "+str(tweetdic[tweetNo][3])+","+\
                                   str(hourNo)+" "+str(tweetdic[tweetNo][4])+","+\
                                   str(minNo)+" "+str(tweetdic[tweetNo][5])+","+\
                                   str(sentimentNo)+" "+tweetdic[tweetNo][0]+"}\n")

            arffwithoutNPWriter.write(str(emocNo)+" "+str(num_EMO)+","+str(negNo)+" "+str(num_NEG)+","+\
                                      str(yearNo)+" "+str(tweetdic[tweetNo][1])+","+\
                                      str(monthNo)+" "+str(tweetdic[tweetNo][2])+","+\
                                      str(dayNo)+" "+str(tweetdic[tweetNo][3])+","+\
                                      str(hourNo)+" "+str(tweetdic[tweetNo][4])+","+\
                                      str(minNo)+" "+str(tweetdic[tweetNo][5])+","+\
                                      str(sentimentNo)+" "+tweetdic[tweetNo][0]+"}\n")

            arffwithNPsetzeroWriter.write(str(emocNo)+" "+str(num_EMO)+","+str(negNo)+" "+str(num_NEG)+","+\
                                          str(yearNo)+" "+str(tweetdic[tweetNo][1])+","+\
                                          str(monthNo)+" "+str(tweetdic[tweetNo][2])+","+\
                                          str(dayNo)+" "+str(tweetdic[tweetNo][3])+","+\
                                          str(hourNo)+" "+str(tweetdic[tweetNo][4])+","+\
                                          str(minNo)+" "+str(tweetdic[tweetNo][5])+","+\
                                          str(sentimentNo)+" "+tweetdic[tweetNo][0]+"}\n")
            FMatrixWithNPWsetzeroRelationWriter.write(str(emocNo)+" "+str(num_EMO)+","+str(negNo)+" "+str(num_NEG)+\
                                                      ","+str(yearNo)+" "+str(tweetdic[tweetNo][1])+","+\
                                                      str(monthNo)+" "+str(tweetdic[tweetNo][2])+","+\
                                                      str(dayNo)+" "+str(tweetdic[tweetNo][3])+","+\
                                                      str(hourNo)+" "+str(tweetdic[tweetNo][4])+","+\
                                                      str(minNo)+" "+str(tweetdic[tweetNo][5])+","+\
                                                      str(ParentsAttNo)+" "+str(DicTweetRelationAtt[tweetNo][0])+","+\
                                                      str(ChildrenAttNo)+" "+str(DicTweetRelationAtt[tweetNo][1])+","+\
                                                      str(TopicNo)+" "+topicName+","+\
                                                      str(sentimentNo)+" "+tweetdic[tweetNo][0]+"}\n")
    contentreader.close()



    arffwithNPWriter.flush(),arffwithNPWriter.close()
    arffwithoutNPWriter.flush(),arffwithoutNPWriter.close()
    arffwithNPsetzeroWriter.flush(),arffwithNPsetzeroWriter.close()
    FMatrixWithNPWsetzeroRelationWriter.flush(),FMatrixWithNPWsetzeroRelationWriter.close()


