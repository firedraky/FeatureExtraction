# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2015-01-08
# version: 0.1
__author__ = 'lifuxin'
'''
    标注EmocCloseData中的正／负
    选择部分unknown数据，进行中性标注
'''
positiveEmoc = {":)",";)",":-)","^_^","^^",":-)","-)",":D",";]",":]",":P",";P",":p",";p","-__-","-_-"}
negativeEmoc ={":(",":-(",":["}

if __name__ == "__main__":
    # input
    inputDataFile = "../all_asc_tweetsOutput/filterData/EmocCloseData"
    #   output
    LabelFile = "../all_asc_tweetsOutput/filterData/HumanLabel/EmocCloseDataLabel"
    humanLabelContentFile = "../all_asc_tweetsOutput/filterData/HumanLabel/humanLabelContent"
    humanLabelNumberFile = "../all_asc_tweetsOutput/filterData/HumanLabel/humanLabelNumber"
    try:
        EmocCloseDataReader = open(inputDataFile,'r')
        LabelWriter=open(LabelFile,'w')
        humanLabelContentWriter=open(humanLabelContentFile,'w')
        humanLabelNumberWriter=open(humanLabelNumberFile,'w')


    except IOError,e:
        print ("读取源数据出现错误",e)
    else:
        tweetId = 1
        for readLine in EmocCloseDataReader:
            readLineArray = readLine.strip("\n").split("\t")
            content = readLineArray[4]
             # label = "neutral"
            label = "unknown"
            #contentfilewriter.write(str(content).lower())
            numPositive = 0
            numNegative = 0
            for emoc in positiveEmoc:
                if emoc in content:
                    numPositive = numPositive+1

            for emoc in negativeEmoc:
                if emoc in content:
                    numNegative = numNegative +1
            if numPositive > numNegative:
                label = "positive"
            if numPositive < numNegative:
                label = "negative"

            LabelWriter.write(str(label)+"\n")

            if label == "unknown":
                humanLabelContentWriter.write(str(content)+"\n")
                humanLabelNumberWriter.write(str(tweetId)+"\n")

            tweetId = tweetId+1


        EmocCloseDataReader.close()
        LabelWriter.flush(),LabelWriter.close()
        humanLabelContentWriter.flush(),humanLabelContentWriter.close()
        humanLabelNumberWriter.flush(),humanLabelNumberWriter.close()