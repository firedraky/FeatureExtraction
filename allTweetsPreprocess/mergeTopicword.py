__author__ = 'lifuxin'
# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2015-01-08
# version: 0.1
__author__ = 'lifuxin'
'''
    合并所有话题下的topicword
'''
import random

if __name__ == "__main__":
    topicnameSet = {"DamnItsTrue","BieberD3D","Egypt","Ff",
                    "MentionKe","NEVERSAYNEVERD3D",
                    "TeamFollowBack","Twitition",
                    "cumanNANYA","fb","februarywish",
                    "icantdateyou","improudtosay",
                    "jfb","nowplaying","nw",
                    "pickone","purpleglasses","shoutout","superbowl"}
    topicwordset = set()
    # 输出
    alltopicwordFileName = "../all_asc_tweetsOutput/SpecialDomain/alltopicword"
    alltopicwordWriter = open(alltopicwordFileName,"w")
    for topicname in topicnameSet:
        # 输入:
        print topicname
        topicwordFileName = "/Users/lifuxin/Program/SentimentClassification/DependencyParser/StanfordParser/"+ topicname+"/topicword"
        with open(topicwordFileName,"r") as topicwordReader:
            for topicword in topicwordReader:
                topicword = topicword.strip("\n").lower()
                if topicword not in topicwordset:
                    topicwordset.add(topicword)
        topicwordReader.close()
    for topicword in topicwordset:
        alltopicwordWriter.write(topicword+"\n")
    alltopicwordWriter.flush();alltopicwordWriter.close()
