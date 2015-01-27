# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2015-01-14
# version: 0.1
__author__ = 'lifuxin'
'''

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
        # topicWordFreqStatFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/TopicWord/topicWordFreqStat"
        # # 输出
        # tweetWordStatFile = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/TopicWord/tweetWordStat"
        # 输入
        topicWordFreqStatFile = "../all_asc_tweetsOutput/mixedTopic/DataSet/trainTopicWordFreqStat"
        # 输出
        tweetWordStatFile = "../all_asc_tweetsOutput/mixedTopic/DataSet/trainTweetWordStat"


        topicWordFreqStatReader = open(topicWordFreqStatFile,'r')
        tweetWordStatWriter = open(tweetWordStatFile,'w')

        #1 10:1 30:1 37:1 48:1 59:1
        tweetIdWords = {}
        for readLine in topicWordFreqStatReader:
            tweetIdFreqArray = readLine.strip("\n").split(' ')
            wordNo = tweetIdFreqArray[0]
            tweetIdFreqs = tweetIdFreqArray[1:]
            for tweetIdFreq in tweetIdFreqs:
                arr = tweetIdFreq.split(":")
                if len(arr) <=1:
                    continue
                tweetId = arr[0]
                freq = arr[1]
                if tweetId in tweetIdWords:
                    tweetIdWords[tweetId] = tweetIdWords[tweetId] + str(wordNo) + ":" +str(freq)+" "
                else:
                    tweetIdWords[tweetId] = str(wordNo) + ":" +str(freq)+" "
        topicWordFreqStatReader.close()
        for tweetId in tweetIdWords.keys():
            tweetWordStatWriter.write(str(tweetId)+" "+tweetIdWords[tweetId]+"\n")
        tweetWordStatWriter.flush(),tweetWordStatWriter.close()

