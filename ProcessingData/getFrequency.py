#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lifuxin'

import mergeWordnetandhownet

#   遍历tweet文件中的每条tweet内容，过滤掉#，@，http:// 开头的所有单词
#   将特殊标点符号转化为.
#   将正负表情符号分别替换成AAAAA和BBBBB
#   统计文件中的单词，通过词典，记录每个单词的词频，按照降序排列，输出到contentfrequency文件中

positivemo={":)",";)",":-)","^_^","^^",":-)","-)",":D",";]",":]",":P",";P",":p",";p","haha","Haha","Ha ha","ha ha","ha"}
negativemo={":(",":-(",":["}

negwords={"n't","don't","not","No","no","didn't","doesn't","hardly","neither","never","seldom","scarely","can't","few","litter","nothing", "none","nobody"}

puncarray={".","?","!",";","--","...","\"",","}
replacedic={"i'm":"i am","it's":"it is",
            "that's":"that is","let's":"let us","i've":"i have",
            "won't":"will not","he's":"he is"}
processedtweetwriter=open("result/precontent.txt",'w')

wordfredic={}
with open('file/content','r') as tweetreader:
    for tweetcontent in tweetreader:
        tweetcontent=tweetcontent.strip()
        #for punc in puncarray:
         #   tweetcontent=tweetcontent.replace(punc,'')
        wordarray = tweetcontent.split(" ")
        for word in wordarray:
            # 过滤掉开头为#号，@，或者http://开头的单词
            word=word.strip().lower();
            if word.startswith('#') or word.startswith('@') or word.startswith('http://') or word.isspace():
                continue
            # 开头是+，或者-
            if word.startswith("+"):
                processedtweetwriter.write("POSADD"+" ")
                continue
            elif word.startswith("-"):
                processedtweetwriter.write("NEGMIS"+" ")
                continue

            # 否定词个数
            # for negword in negwords:
            if word in negwords:
                processedtweetwriter.write("NEGWORD"+" ")
                continue

            # 缩写词
            if replacedic.has_key(word):
                word=replacedic[word]
                processedtweetwriter.write(word+" ")
                continue

            for punc in puncarray:
                word=word.replace(punc,'')

            # 是正负表情符号
            if word in positivemo:
                processedtweetwriter.write("POSEMOC"+" ")
                continue
            elif word in negativemo:
                processedtweetwriter.write("NEGEMOC"+" ")
                continue



            processedtweetwriter.write(word+" ")



            if wordfredic.has_key(word):
                wordfredic[word]=wordfredic[word]+1
            else:
                wordfredic[word]=1
        processedtweetwriter.write("\n")
processedtweetwriter.flush()
processedtweetwriter.close()
# 词典
worddiclist=sorted(wordfredic.items(),lambda x,y:cmp(x[1],y[1]),reverse=True)
topicwordfreqwriter=open("result/topicwordfrequency",'w')
topicwordwriter = open("result/topicword","w")
for key,value in worddiclist:
    topicwordfreqwriter.write(str(key)+"\t"+str(value)+"\n")
    topicwordwriter.write(str(key)+"\n")

topicwordfreqwriter.flush()
topicwordfreqwriter.close()
topicwordwriter.flush()
topicwordwriter.close()
#for key,value in wordfredic.iteritems():
 #   print key,value





