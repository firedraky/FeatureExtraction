# -*- coding: cp936 -*-
__author__ = 'lifuxin'

ParentsAttNo = 6969
ChildrenAttNo = 6970
LabelAttNo = 6971

DicTweetRelationAtt={}
TweetNo=1
with open("../tacobell/beforepreprocess/output/RelationAtt","r") as relationattreader:
    for relationatts in relationattreader:
        relationattarr = relationatts.strip().split(" ")
        DicTweetRelationAtt[TweetNo] = relationattarr
        TweetNo = TweetNo+1

TweetNo = 1
arffwithNPW0relationwriter = open("../tacobell/afterpreprocess/output/arffwithNPW0relation","w")
with open("../tacobell/afterpreprocess/output/tacobellfeature","r") as tweetsarffreader:
    for tweetarff in tweetsarffreader:
        tweetarff = tweetarff.strip()
        tweetarffarr = tweetarff.split("6969 ")
        arffwithNPW0relationwriter.write(tweetarffarr[0]+
                                         str(ParentsAttNo)+" "+str(DicTweetRelationAtt[TweetNo][0])+","+
                                         str(ChildrenAttNo)+" "+str(DicTweetRelationAtt[TweetNo][1])+","+
                                         str(LabelAttNo)+" "+tweetarffarr[1]+"\n")
        TweetNo = TweetNo+1

arffwithNPW0relationwriter.flush()
arffwithNPW0relationwriter.close()
