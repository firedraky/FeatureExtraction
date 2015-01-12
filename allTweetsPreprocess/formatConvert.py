# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2015-01-12
# version: 0.1
__author__ = 'lifuxin'
'''
    做格式转换：
        将weka的数据格式转化为spark mllib的格式
    例子：
    weka格式：{7626 0,20010 neutral}
    spark格式：1 7626:0
'''

if __name__ == "__main__":
    # 输入
    inputFile = "../all_asc_tweetsOutput/mixedTopic/DataSet/testFile"
    # 输出
    outputFile = "../all_asc_tweetsOutput/mixedTopic/sparkDataSet/testFile"

    inputFileReader = open(inputFile,'r')
    outputFileWriter = open(outputFile ,'w')

    for readLine in inputFileReader:
        featureVector = readLine.strip("\n")[1:-1]
        featureVector = featureVector.replace("superbowl","1")
        label = -1
        if "positive" in featureVector:
            label = 0
        elif "neutral" in featureVector:
            label = 1
        elif "negative" in featureVector:
            label = 2
        elif "unknown" in featureVector:
            label = 3

        convertedFeature = str(label)
        featureArray = featureVector.split(",")
        for posAndValue in featureArray:
            posAndValueArray = posAndValue.split(" ")
            if posAndValueArray[0] == "20010":
                break
            convertedFeature += " "
            convertedFeature += posAndValueArray[0]
            convertedFeature += ":"
            convertedFeature += posAndValueArray[1]

        outputFileWriter.write(convertedFeature+"\n")

    inputFileReader.close()
    outputFileWriter.flush(),outputFileWriter.close()