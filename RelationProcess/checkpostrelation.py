#!/usr/bin/env python
# -*- coding: cp936 -*-
from __future__ import division  
'readTextFile.py -- read and display text file'

#   通过content，author.name，author.nickname三个文件得到tweet之间的relation



#   函数：将列表元素写入到文件里
def listwrite2file(tweetrelationfilewriter,authorname2tweetNos):
    for content in authorname2tweetNos:
        tweetrelationfilewriter.write(str(content))
        tweetrelationfilewriter.write(str(" "))
                     


# attempt to open file for reading

#发状态的作者集合，set去掉重复名字
authorset=set()
authornicknameset=set()
#nickname到authorname的映射
nickname2authorname={}
#作者名字到tweet号的映射
authorname2tweetNo={}

try:
    #authorname每个tweet的作者列表（有重复）
    authornamefilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\author.name','r')
#    authornicknamefilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\实验数据预处理\\Obama\\author.nickname','r')
except IOError,e:
    print ("***  file open error:",e)
else:
    # 遍历作者名字文件，将作者的名字存入到作者集合中（去掉重复作者），同时，记录每个作者发布的tweet状态号
    tweetNo=1
    for authorname in authornamefilereader:
        authorname=authorname.strip('\n')
#        nickname=authornicknamefilereader.readline()
#        nickname=nickname.strip('\n')
#        if len(nickname)!=0:
#            authornicknameset.add(nickname)
#            nickname2authorname[nickname]=authorname
        #   如果当前作者不存在于作者集中，那么就将作者添加到作者集，并且初始化作者到tweetNo的映射
        #   否则，说明作者之前已经添加过，直接将作者发布的tweetNo添加到之前添加的tweetNo集中
        if authorname not in authorset:
            authorset.add(authorname)
            authorname2tweetNo[authorname]=[tweetNo]
        else:
            authorname2tweetNo[authorname].append(tweetNo)
        tweetNo=tweetNo+1
    authornamefilereader.close()
#    authornicknamefilereader.close()

#   得到的结构体：
#   authorset authornicknameset 作者集合
#   nickname2authorname  nickname到authorname的映射
#   authorname2tweetNo  作者名字到tweet号的映射

#   遍历每一条tweet content，查询content中的@符号，发现@的作者s
#   然后通过字典集authorname2tweetNo 查询该作者发的tweets，记录到文件中
try:
    contentfilereader = open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\content','r')
    tweetrelationfilewriter = open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\tweetrelation','w')
except IoError,e:
    print ("*** contentfilereader file open error:",e)
else:
    tweetNo=1
    for content in contentfilereader:
        content = content.strip('\n')
        tweetNo=tweetNo+1
        if len(content)!=0:
             startpos=content.find('@')
             while startpos!=-1:
                endpos=content.find(' ',startpos)
                if endpos!=-1:
                     atauthorname=content[startpos+1:endpos]
                     content=content[endpos:len(content)]
                else:
                     atauthorname=content[startpos+1:len(content)]
#                atauthorname = atauthorname.strip(":")

                # 将该作者发布的tweetNo输出到文件中
                if atauthorname in authorset:
                    listwrite2file(tweetrelationfilewriter,authorname2tweetNo[atauthorname])
                elif atauthorname in authornicknameset:
                    listwrite2file(tweetrelationfilewriter,authorname2tweetNo[authornicknameset[atauthorname]])
                if endpos==-1:
                     break
                else:
                    startpos=content.find('@')
        tweetrelationfilewriter.write('\n')
    contentfilereader.close();

tweetrelationfilewriter.flush()
tweetrelationfilewriter.close()
                    

                

