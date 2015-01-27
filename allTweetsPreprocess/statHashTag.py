# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2015-01-07
# version: 0.1
__author__ = 'lifuxin'
'''
    统计hashtag
'''
wordfredic={}
if __name__ == "__main__":
    inputDataFile = "../all_asc_tweetsOutput/filterData/EmocCloseData"
    outputDataFile = "../all_asc_tweetsOutput/filterData/HashTagStat"
    try:
        global hashtagWriter
        tweetsFileReader = open(inputDataFile,'r')
        hashtagWriter=open(outputDataFile,'w')
    except IOError,e:
        print ("读取源数据出现错误",e)
    else:

        for readLine in tweetsFileReader:
            readLineArray = readLine.strip('\n').split('\t')
            content = readLineArray[4]#.lower()
            #DosPalabras callate gay:D

            if len(content)!=0:
                startpos=content.find('#')
                while startpos!=-1:
                    endpos=content.find(' ',startpos)
                    if endpos!=-1:
                        hashtopic=content[startpos+1:endpos]
                        content=content[endpos:len(content)]
                    else:
                        hashtopic=content[startpos+1:len(content)]
                    if len(hashtopic) !=0:
                        if wordfredic.has_key(hashtopic):
                            wordfredic[hashtopic]=wordfredic[hashtopic]+1
                        else:
                            wordfredic[hashtopic]=1

                    if endpos==-1:
                        break
                    else:
                        startpos=content.find('#')


        # 词典
        hashtopicDicList=sorted(wordfredic.items(),lambda x,y:cmp(x[1],y[1]),reverse=True)

        for key,value in hashtopicDicList:
            hashtagWriter.write(str(key)+"\t"+str(value)+"\n")

        tweetsFileReader.close()
        hashtagWriter.flush(),hashtagWriter.close()