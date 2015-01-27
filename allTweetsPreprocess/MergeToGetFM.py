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
    # topicnameSet = {"DamnItsTrue","BieberD3D","Egypt","Ff",
    #                 "MentionKe","NEVERSAYNEVERD3D",
    #                 "TeamFollowBack","Twitition",
    #                 "cumanNANYA","fb","februarywish",
    #                 "icantdateyou","improudtosay",
    #                 "jfb","nowplaying","nw",
    #                 "pickone","purpleglasses","shoutout","superbowl"}
    topicnameSet = {"mixedTopic"}

    for topicname in topicnameSet:
        print topicname
        # # 输入：
        # preContentFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Preprocess/precontent"
        # contentFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Divided/content"
        #
        # sentimentFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Divided/sentiment"
        #
        # yearFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Divided/year"
        # monthFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Divided/month"
        # dayFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Divided/day"
        # hourFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Divided/hour"
        # minFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Divided/min"
        #
        # publicWordPMIFile = "../Dictionary/publicwordPMI"
        # topicWordsFreqFile = "../all_asc_tweetsOutput/SpecialDomain/alltopicword"
        # relationAttributeFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Feature/RelationAtt"
        #
        # # 输出：
        # FMatrixWithNPWfilename = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Feature/FeatureMatrixWithNPW"
        # FMatrixWithNPWsetZerofilename = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Feature/FeatureMatrixWithNPWsetZero"
        # FMatrixWithoutNPWfilename = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Feature/FeatureMatrixWithoutNPW"
        # FMatrixWithNPWsetzeroRelationfilename = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Feature/FeatureMatrixWithNPWRelation"


        # 输入：
        preContentFile = "../all_asc_tweetsOutput/mixedTopic/Preprocess/precontent"
        contentFile = "../all_asc_tweetsOutput/mixedTopic/Divided/content"

        sentimentFile = "../all_asc_tweetsOutput/filterData/HumanLabel/mergedSentiment"

        yearFile = "../all_asc_tweetsOutput/mixedTopic/Divided/year"
        monthFile = "../all_asc_tweetsOutput/mixedTopic/Divided/month"
        dayFile = "../all_asc_tweetsOutput/mixedTopic/Divided/day"
        hourFile = "../all_asc_tweetsOutput/mixedTopic/Divided/hour"
        minFile = "../all_asc_tweetsOutput/mixedTopic/Divided/min"

        publicWordPMIFile = "../Dictionary/publicwordPMI"

        topicWordsFreqFile = "../all_asc_tweetsOutput/SpecialDomain/alltopicword"

        relationAttributeFile = "../all_asc_tweetsOutput/mixedTopic/Feature/RelationAtt"

        # 输出：
        FMatrixWithNPWfilename = "../all_asc_tweetsOutput/mixedTopic/Feature/FeatureMatrixWithNPW"
        FMatrixWithNPWsetZerofilename = "../all_asc_tweetsOutput/mixedTopic/Feature/FeatureMatrixWithNPWsetZero"
        FMatrixWithoutNPWfilename = "../all_asc_tweetsOutput/mixedTopic/Feature/FeatureMatrixWithoutNPW"
        FMatrixWithNPWsetzeroRelationfilename = "../all_asc_tweetsOutput/mixedTopic/Feature/FeatureMatrixWithNPWRelation"




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

        contentReader = open(contentFile,"r")



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
            wordvalue = publicword.strip().lower().split()
            publicworddic[wordvalue[0]] = [wordvalue[1],wordNO]
            wordNO = wordNO+1
        publicwordReader.close()

        nonpublicworddic = {}
        # for nonpublicword in topicWordReader:
        #     wordvalue=nonpublicword.strip().split()
        #     nonpublicworddic[wordvalue[0]] = [wordvalue[1],wordNO]
        #     wordNO = wordNO+1
        # topicWordReader.close()
        for nonpublicword in topicWordReader:
            topicword=nonpublicword.strip().lower()
            nonpublicworddic[topicword] = [0,wordNO]
            wordNO = wordNO+1
        topicWordReader.close()

        num_publicword = publicworddic.__len__()
        num_nonpublicword = nonpublicworddic.__len__()
        numtextfeature = publicworddic.__len__()+nonpublicworddic.__len__()



        tweetNo = 0
        with open(preContentFile,"r") as precontentreader:
            for tweetcontent in precontentreader:
                tweetcontent = tweetcontent.lower()
                tweetNo = tweetNo+1

                contentStr = contentReader.readline().strip().lower()
                contentwordArr = contentStr.strip().split()

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
                    # elif word in nonpublicworddic.keys():
                    #     wordarrdic[nonpublicworddic[word][1]]=nonpublicworddic[word][0]
                    #     wordwithNPsetzerodic[nonpublicworddic[word][1]]=0
                    elif word == "POSEMOC".lower():
                        num_EMO = num_EMO+1;
                    elif word == "NEGEMOC".lower():
                        num_EMO = num_EMO - 1;
                    elif word == "NEGWORD".lower():
                        num_NEG = num_NEG+1
                    elif word == "POSADD".lower():
                        num_ADD_MIN = num_ADD_MIN +1
                    elif word == "NEGMIS".lower():
                        num_ADD_MIN = num_ADD_MIN -1

                for word in contentwordArr:
                     if word in nonpublicworddic.keys():
                        wordarrdic[nonpublicworddic[word][1]]=nonpublicworddic[word][0]
                        wordwithNPsetzerodic[nonpublicworddic[word][1]]=0
                        #arffwithNPWriter.write(str(nonpublicworddic[word][1])+" "+str(nonpublicworddic[word][0])+",")

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
                                                          str(TopicNo)+" "+topicname+","+\
                                                          str(sentimentNo)+" "+tweetdic[tweetNo][0]+"}\n")
        precontentreader.close()
        contentReader.close()


        arffwithNPWriter.flush(),arffwithNPWriter.close()
        arffwithoutNPWriter.flush(),arffwithoutNPWriter.close()
        arffwithNPsetzeroWriter.flush(),arffwithNPsetzeroWriter.close()
        FMatrixWithNPWsetzeroRelationWriter.flush(),FMatrixWithNPWsetzeroRelationWriter.close()


