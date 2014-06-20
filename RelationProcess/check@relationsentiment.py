#!/usr/bin/env python
# -*- coding: cp936 -*-

from __future__ import division  
'readTextFile.py -- read and display text file'
import string
# 通过遍历relation关系文件和sentiment情感标记文件，得到direct和mutial @关系和情感一致性比对

maxTweetNo=90000000
        

# tweetNo到每条tweet的情感标记的映射
tweetNo2sentiment={}
Num_positive=0
Num_neturl=0
Num_negative=0
try:
    sentimentfilereader = open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\sentiment','r')
except IOError,e:
    print ("*** authorname file open error:",e)
else:
    i=1
    for eachline in sentimentfilereader:
        eachline = eachline.strip('\n')
        tweetNo2sentiment[i]=eachline
        if eachline == "positive":
            Num_positive = Num_positive +1
        elif eachline == "neutral":
            Num_neturl = Num_neturl +1
        elif eachline == "negative":
            Num_negative = Num_negative +1
        i=i+1
    sentimentfilereader.close()

# 将tweets之间的@关系存下来
tweetNo2tweetNos={}
try:
    relationreader = open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\tweetrelation','r')
except IOError,e:
    print ("*** authorname file open error:",e)
else:
    tweetNo = 0
    for eachline in relationreader:
        tweetNo = tweetNo+1
        eachline = eachline.strip('\n')
        tweetNo2tweetNos[tweetNo] = eachline
    relationreader.close()

# direct@ 情感一致数量
Num_directat=0 #@边，两个tweet情感一致的数量
Num_directatPositive=0#@边，两个tweet情感一致，并且为正类的数量 
Num_directatNegative=0#@边，两个tweet情感一致，并且为负类的数量 
Num_directatNetural=0#@边，两个tweet情感一致，并且为中类的数量 
TotalNum_directat=0#总的@边数
Num_mutialat=0#互相@边，两个tweet情感一致的数量
TotalNum_mutialat=0#互相@的总边数

TotalNum_directatNonNetural=0#@边总数，但是不包含中性
Num_directatPositive=0 #@边，两个tweet情感一致，并且为正类，但是不包含中性
Num_directatNegative=0 #@边，两个tweet情感一致，并且为负类，但是不包含中性


number_all_parentssentiment=0 #当前tweet的所有相关联边，tweet号小于它的情感和
number_parents=0
number_all_childrensentiment=0 #当前tweet的所有相关联边，tweet号大于它的情感和
number_children=0
number_one_parensentiment=0 #当前tweet的所有相关联边，tweet号小于它，并且是最近的情感
number_one_parent=0
number_one_child=0
number_one_childsentiment=0 #当前tweet的所有相关联边，tweet号大于它，并且是最近的情感
try:
    relationfilereader = open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\tweetrelation','r')
except IOError,e:
    print ("*** authorname file open error:",e)
else:
    tweetNo = 0
    for eachline in relationfilereader:
        tweetNo=tweetNo+1
        eachline = eachline.strip('\n')
        if eachline =='':
            continue
        minparentNo=-1
        maxchildNo=maxTweetNo
        numbers = eachline.split(' ')
        for number in numbers:
            if number =='':
                continue
            # 考虑本分的两个特征的不同情况下，情感一致的概率
            
            if string.atoi(number) < tweetNo:
                #parent
                if string.atoi(number) > minparentNo:
                    minparentNo=string.atoi(number)
                number_parents= number_parents+1
                if tweetNo2sentiment[tweetNo] == tweetNo2sentiment[string.atoi(number)]:
                    number_all_parentssentiment=number_all_parentssentiment+1
            if string.atoi(number) > tweetNo: #child
                if string.atoi(number) < maxchildNo:
                    maxchildNo=string.atoi(number)
                number_children = number_children+1
                if tweetNo2sentiment[tweetNo] == tweetNo2sentiment[string.atoi(number)]:
                    number_all_childrensentiment=number_all_childrensentiment+1
            
            

            TotalNum_directat=TotalNum_directat+1
            if tweetNo2sentiment[tweetNo] != "neutral" and  tweetNo2sentiment[string.atoi(number)]!="neutral":
                TotalNum_directatNonNetural = TotalNum_directatNonNetural+1
            if tweetNo2sentiment[tweetNo] == tweetNo2sentiment[string.atoi(number)]:
                Num_directat=Num_directat+1
                if tweetNo2sentiment[tweetNo]=="positive":
                    Num_directatPositive = Num_directatPositive+1
                elif tweetNo2sentiment[tweetNo]=="neutral":
                    Num_directatNetural = Num_directatNetural+1
                elif tweetNo2sentiment[tweetNo]=="negative":
                    Num_directatNegative = Num_directatNegative+1
            # 判断 number那条tweet是否@了tweetNo这条tweet
            if str(tweetNo) in tweetNo2tweetNos[string.atoi(number)].split(' '):
                TotalNum_mutialat=TotalNum_mutialat+1
                if tweetNo2sentiment[string.atoi(number)] == tweetNo2sentiment[tweetNo]:
                    
                    Num_mutialat=Num_mutialat+1
        #  minparentNo , maxchildNo
        if minparentNo != -1:
            number_one_parent = number_one_parent+1
            if tweetNo2sentiment[tweetNo] == tweetNo2sentiment[minparentNo]:
                number_one_parensentiment=number_one_parensentiment+1
        if maxchildNo != maxTweetNo:
            number_one_child = number_one_child+1
            if tweetNo2sentiment[tweetNo] == tweetNo2sentiment[maxchildNo]:
                number_one_childsentiment=number_one_childsentiment+1
            
    relationfilereader.close()
#statisticfilewriter = open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\directat','w')
print "Num_directatPositive:",Num_directatPositive,"Num_directatNetural:",Num_directatNetural,"Num_directatNegative:",Num_directatNegative
print "Num_directat:",Num_directat,"TotalNum_directatNonNetural",TotalNum_directatNonNetural,"TotalNum_directat:",TotalNum_directat
print "（Num_directatPositive+Num_directatNegative）/TotalNum_directatNonNetural",(Num_directatPositive+Num_directatNegative)/TotalNum_directatNonNetural,"Num_directat/TotalNum_directat:",Num_directat/TotalNum_directat
print Num_mutialat,TotalNum_mutialat,Num_mutialat/TotalNum_mutialat
print "Num_positive:",Num_positive,"Num_neturl:",Num_neturl,"Num_negative:",Num_negative,"Random direct: ",pow(Num_positive/3232,2)+pow(Num_neturl/3232,2)+pow(Num_negative/3232,2)
print "random direct without netural:",pow(Num_positive/(Num_positive+Num_negative),2)+pow(Num_negative/(Num_positive+Num_negative),2)

print "number_all_parentssentiment/number_parents:",number_all_parentssentiment/number_parents
print "number_all_childrensentiment/number_children",number_all_childrensentiment/number_children
print "number_one_parensentiment/number_one_parent",number_one_parensentiment/number_one_parent
print "number_one_childsentiment/number_one_child",number_one_childsentiment/number_one_child
#statisticfilewriter.flush()
#statisticfilewriter.close()
