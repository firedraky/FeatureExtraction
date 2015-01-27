# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2015-01-14
# version: 0.1
__author__ = 'lifuxin'
'''
    计算topic word在每个tweet中出现的次数
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
        # # 输入
        # topicwordFile = "../all_asc_tweetsOutput/SpecialDomain/alltopicword"
        # tweetsFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Divided/content"
        # # 输出
        # topicWordFreqStatFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/TopicWord/topicWordFreqStat"


        # 输入
        topicwordFile = "../all_asc_tweetsOutput/SpecialDomain/alltopicword"
        tweetsFile = "../all_asc_tweetsOutput/mixedTopic/DataSet/trainPrecontent"

        # 输出
        topicWordFreqStatFile = "../all_asc_tweetsOutput/mixedTopic/DataSet/trainTopicWordFreqStat"

        topicwordReader = open(topicwordFile,'r')
        topicWordFreqStatWriter = open(topicWordFreqStatFile,'w')

        wordNo = 1
        for readLine in topicwordReader:
            # topicWord = readLine.strip("\n").split('\t')[0]
            topicWord = readLine.strip("\n")
            tweetsReader = open(tweetsFile,'r')

            tweetWordFreqString = ""
            tweetId = 1
            for tweet in tweetsReader:
                # tweet = tweet.strip("\n")
                # wordCount = tweet.count(topicWord)
                wordArray = tweet.strip("\n").split(" ")
                wordCount = 0
                for word in wordArray:
                    if word == topicWord:
                        wordCount = wordCount+1
                if wordCount != 0:
                    tweetWordFreqString =tweetWordFreqString+str(tweetId)+":"+str(wordCount)+" "

                tweetId = tweetId +1
            tweetsReader.close()
            topicWordFreqStatWriter.write(str(wordNo) + " "+tweetWordFreqString+"\n")
            wordNo = wordNo +1
        topicwordReader.close()
        topicWordFreqStatWriter.flush(),topicWordFreqStatWriter.close()

