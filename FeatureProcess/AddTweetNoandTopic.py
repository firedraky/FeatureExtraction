# -*- coding: cp936 -*-
__author__ = 'lifuxin'

TweetNoPos=0
TopicPos = 6971
LabelPos = 6972

TweetNo = 1
Topic="tacobell"
topictweetNowriter=open("../tacobell/AddTweetAndTopic/tacobelltopictweetfeature","w")
with open("../tacobell/AddTweetAndTopic/arffwithNPW0relation","r") as tweetReader:
    for tweet in tweetReader:
        TweetNoAtt=str(TweetNoPos)+" "+str(TweetNo)+","
        TopicAtt=str(TopicPos)+" "+Topic+","
        tweetarr=tweet.strip().split("{")
        tweet = "{"+TweetNoAtt+tweetarr[1]
        tweetarr = tweet.split(",6971")
        tweet = tweetarr[0]+","+TopicAtt+str(LabelPos)+" "+tweetarr[1]
        topictweetNowriter.write(tweet+"\n")
        TweetNo = TweetNo+1
tweetReader.close()
topictweetNowriter.flush(),topictweetNowriter.close()



