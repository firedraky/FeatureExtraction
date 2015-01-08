# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2015-01-07
# version: 0.1
__author__ = 'lifuxin'
'''
    合并人工标注的数据HumanLabel/humanLabel500 和 通过表情符号标注的数据HumanLabel/EmocCloseDataLabel
'''

if __name__ == "__main__":
    # input
    emocLabelDataFile = "../all_asc_tweetsOutput/filterData/HumanLabel/EmocCloseDataLabel"
    humanLabelDataFile = "../all_asc_tweetsOutput/filterData/HumanLabel/humanLabel500"
    humanLabelNumberFile = "../all_asc_tweetsOutput/filterData/HumanLabel/humanLabelNumber"
    #   output
    mergeLabelFile = "../all_asc_tweetsOutput/filterData/HumanLabel/mergedLabel"
    try:
        emocLabelReader = open(emocLabelDataFile,'r')
        humanLabelReader = open(humanLabelDataFile,'r')
        humanLabelNumberReader = open(humanLabelNumberFile,'r')

        mergeLabelWriter=open(mergeLabelFile,'w')


    except IOError,e:
        print ("读取源数据出现错误",e)
    else:
        tweetId = 1
        number = humanLabelNumberReader.readline().strip("\n")
        humanLabel =  humanLabelReader.readline().strip("\n")
        print int(number)
        for readLine in emocLabelReader:
            emocLabel = readLine.strip("\n")

            if int(number) == tweetId:
                print number
                mergeLabelWriter.write(str(humanLabel)+"\n")
                humanLabel =  humanLabelReader.readline().strip("\n")
                number = humanLabelNumberReader.readline().strip("\n")
                if not humanLabel :
                    number = -1
            else:
                mergeLabelWriter.write(str(emocLabel)+"\n")
            tweetId = tweetId+1


        emocLabelReader.close()
        humanLabelReader.close()
        humanLabelNumberReader.close()

        mergeLabelWriter.flush(),mergeLabelWriter.close()


