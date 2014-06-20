#!/usr/bin/env python
# -*- coding: cp936 -*-
from __future__ import division  
'readTextFile.py -- read and display text file'
# 写入： alllinkfile  notsinglelinkfile  alllinkstrfile  : 作者发布的tweet @ 其他作者图
# 通过tweet之间的@关系，得到需要的信息

# attempt to open file for reading
hyperlinkcount=0#超链接数
authorset=set()#发状态的作者集合，set去掉重复名字
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
    authornamefilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\author.name','r')
    contentfilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\content','r')
    #tweetidfilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\tweet.id','r')
    #authornicknamefilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\author.nickname','r')
    pubdatefilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\pub.date.GMT','r')
    tweetsentimentfilereader = open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\sentiment','r')
    
    alllinkfile=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\alllink.net','w')
    notsinglelinkfile=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\notsinglelink.net','w')
    alllinkstrfile=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\alllinkstr','w')
except IOError,e:
    print ("*** authorname file open error:",e)
else:
    i=1
    for eachLine in authornamefilereader:
        eachLine=eachLine.strip('\n')
        # authorset 作者集（去除掉重复的作者）
        # name2number 作者-序号 字典
        if eachLine not in authorset:
            authorset.add(eachLine)
            name2number[eachLine]=i
            i=i+1
    authornamefilereader.close()
#print authorset
authornamefilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\author.name','r')
alllinkfile.write("*Vertices"+' '+str(len(authorset))+'\n')

# 将作者的编号和作者的名字输出到 alllinkfile
i=1
for author,number in name2number.items():
    alllinkfile.write(' '+str(number)+' '+author+'\n')
    i=i+1

alllinkfile.write("*Arcs"+'\n')
notsinglelinkfile.write("*Arcs"+'\n')
# 遍历content 查询content中的@信息，然后根据@后的作者信息，得到@关联边
for contentline in contentfilereader:
    author=authornamefilereader.readline()
    author=author.strip('\n')
    if len(contentline)!=0:
        startpos=contentline.find('@')
        while startpos!=-1:
            endpos=contentline.find(' ',startpos)
            # name ： @后面的作者名字
            if endpos!=-1:
                name=contentline[startpos+1:endpos]
                
                contentline=contentline[endpos:len(contentline)]
                #print contentline
            else:
                name=contentline[startpos+1:len(contentline)]

            # author遍历content每条tweet的发布人，name是content中包含的人名
            # authornotsingleset 存储存在关联边的@ 作者，即非孤立作者点
            # alllinkstrfile 存储作者之间的@ direct关系：即author @ 了name
            # alllinkfile 
            if name in authorset:
                authornotsingleset.add(author)
                authornotsingleset.add(name)
                alllinkstrfile.write(' '+author+' ')
                alllinkstrfile.write(name+'\n')
                alllinkfile.write(' '+str(name2number[author])+' ')
                alllinkfile.write(str(name2number[name])+'\n')

                notsinglelinkfile.write(' '+str(name2number[author])+' ')
                notsinglelinkfile.write(str(name2number[name])+'\n')
                hyperlinkcount=hyperlinkcount+1
            if endpos==-1:
                break
            else:
                startpos=contentline.find('@')


# 关系图指标的计算
print '总链接数：'
print hyperlinkcount
print 'ratio : '
setsize=len(authorset)
fulllink=setsize*(setsize-1)/2;
ratio=hyperlinkcount/fulllink
print ratio
alllinkfile.flush()
alllinkfile.close()
alllinkstrfile.flush()
alllinkstrfile.close()
print '总author数量:'
print len(authorset)
print '非独立点数：'
print len(authornotsingleset)

#print authornotsingleset



#输出只有非独立点的图的顶点

notsinglelinkfile.write("*Vertices"+' '+str(len(authornotsingleset))+'\n')
for nonsingleauthor in authornotsingleset:
    notsinglelinkfile.write(' '+str(name2number[nonsingleauthor])+' '+nonsingleauthor+'\n')

notsinglelinkfile.flush()
notsinglelinkfile.close()
    
