#!/usr/bin/env python
# -*- coding: cp936 -*-
from __future__ import division  
'readTextFile.py -- read and display text file'
# 写入： alllinkfile  notsinglelinkfile  alllinkstrfile  : 作者发布的tweet @ 其他作者图
# 通过tweet之间的@关系，得到需要的信息

# attempt to open file for reading
hyperlinkcount=0#超链接数
authorset=set()#发状态的作者集合，set去掉重复名字
atauthorset=set()#状态中被@的作者集合，set去掉重复名字
authornotsingleset=set()#不是孤立点的作者集合
name2number={}#作者名字到tweet号的映射


# 读取作者名字：authornamefilereader
# 读取tweet内容：contentfilereader
# 读取tweet id(936467521)：tweetidfilereader
# 读取作者nick name：authornicknamefilereader
# 读取tweet 发布日期：pubdatefilereader
# 读取每条tweet的情感标签 tweetsentimentfilereader

try:
    #authorname每个tweet的作者列表（有重复）
    authornamefilereader=open('Z:\\TweetAnalysisSeries\\test','r')
    contentfilereader=open('Z:\\TweetAnalysisSeries\\test','r')
except IOError,e:
    print ("*** authorname file open error:",e)
else:
    i=1
    for eachLine in authornamefilereader:
        eachLine=eachLine.strip('\n').split('\t')
        # authorset 作者集（去除掉重复的作者）
        # name2number 作者-序号 字典
        if eachLine[1] not in authorset:
            authorset.add(eachLine[1])
            name2number[eachLine[1]]=i
            i=i+1
    authornamefilereader.close()
#print authorset

    
# 遍历content 查询content中的@信息，然后根据@后的作者信息，得到@关联边
for contentsline in contentfilereader:
    temp=contentsline.strip('\n').split('\t')
    content=temp[4]
    author=temp[1]
    if len(content)!=0:
        startpos=content.find('@')
        while startpos!=-1:
            endpos=content.find(' ',startpos)
            # name ： @后面的作者名字
            if endpos!=-1:
                name=content[startpos+1:endpos]
                
                content=content[endpos:len(content)]
                #print contentline
            else:
                name=content[startpos+1:len(content)]

            # author遍历content每条tweet的发布人，name是content中包含的人名
            if name in authorset:
                atauthorset.add(name)
                atauthorset.add(author)
            if endpos==-1:
                break
            else:
                startpos=content.find('@')

print atauthorset
authornamefilereader.close()
contentfilereader.close()


tweetsreader=open('Z:\\TweetAnalysisSeries\\test','r')
tweetidwriter=open('Z:\\TweetAnalysisSeries\\tweetid','w')
authorwriter=open('Z:\\TweetAnalysisSeries\\author','w')
publishtimewriter=open('Z:\\TweetAnalysisSeries\\publishtime','w')
contentwriter=open('Z:\\TweetAnalysisSeries\\content','w')
for lines in tweetsreader:
    line=lines.strip('\n').split('\t')
    tweetid=line[0]
    authorcontent=line[1]
    publishtime=line[3]
    content=line[4]
    if authorcontent in atauthorset:
        tweetidwriter.write(tweetid+"\n")
        authorwriter.write(authorcontent+"\n")
        publishtimewriter.write(publishtime+"\n")
        contentwriter.write(content+"\n")
tweetidwriter.flush(),tweetidwriter.close()
authorwriter.flush(),authorwriter.close()
publishtimewriter.flush(),publishtimewriter.close()
contentwriter.flush(),contentwriter.close()
