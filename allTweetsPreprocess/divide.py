# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2015-01-07
# version: 0.1
__author__ = 'lifuxin'
'''
    根据all_asc_tweets数据文件的格式处理数据
'''

import time
def write2tweetid(tweetid):
    tweetidFileWriter.write(str(tweetid))
    tweetidFileWriter.write("\n")

def write2pubdate(pubdate):
    #	Sun Jan 23 00:00:00 +0000 2011
    pubdatetime=time.strptime(pubdate,"%a %b %d %H:%M:%S +0000 %Y")
    pubdatefilewriter.write(str(pubdate))
    pubdatefilewriter.write("\n")

    yearfilewriter.write(str(pubdatetime[0]))
    yearfilewriter.write("\n")

    monthfilewriter.write(str(pubdatetime[1]))
    monthfilewriter.write("\n")

    dayfilewriter.write(str(pubdatetime[2]))
    dayfilewriter.write("\n")

    hourfilewriter.write(str(pubdatetime[3]))
    hourfilewriter.write("\n")

    minfilewriter.write(str(pubdatetime[4]))
    minfilewriter.write("\n")

    weekdayFileWriter.write(str(pubdatetime[6]))
    weekdayFileWriter.write("\n")


def write2content(content):
    # label = "neutral"
    label = "unknown"
    #contentfilewriter.write(str(content).lower())
    for emoc in positiveEmoc:
        if emoc in content:
            label = "positive"
    for emoc in negativeEmoc:
        if emoc in content:
            label = "negative"
    contentFileWriter.write(str(content))
    sentimentFileWriter.write(str(label)+"\n")
    labelFileWriter.write(labelMap[str(label)]+"\n")
    # contentFileWriter.write("\n")

def write2authorname(authorname):
    authornameFileWriter.write(str(authorname))
    authornameFileWriter.write("\n")


def write200(tmp):
    tmpFileWriter.write(str(tmp))
    tmpFileWriter.write("\n")

positiveEmoc = {":)",";)",":-)","^_^","^^",":-)","-)",":D",";]",":]",":P",";P",":p",";p","-__-","-_-"}
negativeEmoc ={":(",":-(",":["}

'''
   定义一个字典映射： position 到 函数的一个映射
'''
positionAction = {
    "1":write2tweetid,
    "2":write2authorname,
    "3":write200,
    "4":write2pubdate,
    "5":write2content
}

'''
    定义一个label Map映射，情感label字符串到数字label的映射
'''
labelMap = {
    "positive":"1",
    "neutral":"0",
    "negative":"-1",
    "unknown":"5"
}
global sentiment
if __name__ == "__main__":
    topicnameSet = {"DamnItsTrue","BieberD3D","Egypt","Ff",
                    "MentionKe","NEVERSAYNEVERD3D",
                    "TeamFollowBack","Twitition",
                    "cumanNANYA","fb","februarywish",
                    "icantdateyou","improudtosay",
                    "jfb","nowplaying","nw",
                    "pickone","purpleglasses","shoutout","superbowl"}
    for topicname in topicnameSet:
        print topicname
        # 输入
        # inputdatafile = "../all_asc_tweetsOutput/filterData/EmocCloseData"
        inputdatafile = "../all_asc_tweetsOutput/filterData/topicData/"+topicname
        # 输出
        outputdir = "../all_asc_tweetsOutput/SpecialDomain/"+topicname+"/Divided/"
        try:
            global tweetsFileReader,tweetidFileWriter,pubdatefilewriter,yearfilewriter
            global monthfilewriter,dayfilewriter,hourfilewriter,minfilewriter
            global contentFileWriter,authornameFileWriter
            global labelFileWriter,tmpFileWriter,weekdayFileWriter,sentimentFileWriter

            tweetsFileReader = open(inputdatafile,'r')
            tweetidFileWriter=open(outputdir+'tweet.id','w')
            pubdatefilewriter = open(outputdir+'pub.date.GMT','w')
            yearfilewriter = open(outputdir+'year','w')
            monthfilewriter = open(outputdir+'month','w')
            dayfilewriter = open(outputdir+'day','w')
            hourfilewriter = open(outputdir+'hour','w')
            minfilewriter = open(outputdir+'min','w')
            contentFileWriter = open(outputdir+'content','w')
            authornameFileWriter = open(outputdir+'author.name','w')
            labelFileWriter = open(outputdir+'label','w')
            tmpFileWriter = open(outputdir+'tmp','w')
            weekdayFileWriter = open(outputdir+'weekday','w')
            sentimentFileWriter = open(outputdir + 'sentiment','w')

        except IOError,e:
            print ("读取源数据出现错误",e)
        else:
            for readLine in tweetsFileReader:
                readLineArray = readLine.split("\t")
                position=1
                # negative positive neutral
                for segment in readLineArray:
                    positionAction.get(str(position))(segment)
                    position = position+1


            tweetsFileReader.close()
            tweetidFileWriter.flush(),tweetidFileWriter.close()
            pubdatefilewriter.flush(),pubdatefilewriter.close()
            contentFileWriter.flush(),contentFileWriter.close()
            authornameFileWriter.flush(),authornameFileWriter.close()
            yearfilewriter.flush(),yearfilewriter.close()
            monthfilewriter.flush(),monthfilewriter.close()
            dayfilewriter.flush(),dayfilewriter.close()
            hourfilewriter.flush(),hourfilewriter.close()
            minfilewriter.flush(),minfilewriter.close()
            labelFileWriter.flush(),labelFileWriter.close()
            tmpFileWriter.flush(),tmpFileWriter.close()
            weekdayFileWriter.flush(),weekdayFileWriter.close()
            sentimentFileWriter.flush(),sentimentFileWriter.close()
