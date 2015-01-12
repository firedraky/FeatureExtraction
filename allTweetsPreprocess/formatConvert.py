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
    inputFile = "../all_asc_tweetsOutput/mixedTopic/DataSet/trainFile"
    # 输出
    outputFile = "../all_asc_tweetsOutput/mixedTopic/sparkDataSet/trainFile"

    inputFileReader = open(inputFile,'r')
    outputFileWriter = open(outputFile ,'w')

    # 离散数据归一化 rg(x_i) = (x_i - min(i)) / (max(i)-min(i))
    emoMin = 0 ; emoMax = 0
    negMin = 0 ; negMax = 0
    yearMin = 0 ; yearMax = 0
    monthMin = 0; monthMax = 0
    dayMin = 0; dayMax = 0
    hourMin = 0; hourMax = 0
    minMin = 0; minMax = 0
    parentMin =0; parentMax =0
    childMin = 0; childMax =0
    # topicMin = 0;topicMax = 0
    for readLine in inputFileReader:
        featureVector = readLine.strip("\n")[1:-1]
        featureVector = featureVector.replace("superbowl","1")
        featureVector = featureVector.replace("positive","0")
        featureVector = featureVector.replace("neutral","1")
        featureVector = featureVector.replace("negative","2")
        featureVector = featureVector.replace("unknown","3")
        featureArray = featureVector.split(",")
        for posAndValue in featureArray:
            posAndValueArray = posAndValue.split(" ")
            pos = posAndValueArray[0]
            value = float(posAndValueArray[1])
            if pos == "20000":
                emoMin = min(emoMin,value)
                emoMax = max(emoMax,value)
            elif pos == "20001":
                negMin = min(negMin,value)
                negMax = max(negMax,value)
            elif pos == "20002":
                yearMin = min(yearMin,value)
                yearMax = max(yearMax,value)
            elif pos == "20003":
                monthMin = min(monthMin,value)
                monthMax = max(monthMax,value)
            elif pos == "20004":
                dayMin = min(dayMin,value)
                dayMax = max(dayMax,value)
            elif pos == "20005":
                hourMin = min(hourMin,value)
                hourMax = max(hourMax,value)
            elif pos == "20006":
                minMin = min(minMin,value)
                minMax = max(minMax,value)
            elif pos == "20007":
                parentMin = min(parentMin,value)
                parentMax = max(parentMax,value)
            elif pos == "20008":
                childMin = min(childMin,value)
                childMax = max(childMax,value)
    inputFileReader.close()

    inputFileReader = open(inputFile,'r')
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
        featureVector = featureVector.replace("positive","0")
        featureVector = featureVector.replace("neutral","1")
        featureVector = featureVector.replace("negative","2")
        featureVector = featureVector.replace("unknown","3")
        convertedFeature = str(label)
        featureArray = featureVector.split(",")
        for posAndValue in featureArray:
            posAndValueArray = posAndValue.split(" ")
            pos = posAndValueArray[0]
            value = float(posAndValueArray[1])
            if pos == "20010":
                break
            if pos == "20000":
                value = (value - emoMin)/(emoMax-emoMin)
            elif pos == "20001":
                value = (value - negMin)/(negMax-negMin)
            elif pos == "20002":
                value = (value - yearMin)/(yearMax-yearMin)
            elif pos == "20003":
                value = (value - monthMin)/(monthMax-monthMin)
            elif pos == "20004":
                value = (value - dayMin)/(dayMax-dayMin)
            elif pos == "20005":
                value = (value - hourMin)/(hourMax-hourMin)
            elif pos == "20006":
                value = (value - minMin)/(minMax-minMin)
            elif pos == "20007":
                value = (value - parentMin)/(parentMax-parentMin)
            elif pos == "20008":
                value = (value - childMin)/(childMax-childMin)
            convertedFeature += " "
            convertedFeature += pos
            convertedFeature += ":"
            convertedFeature += str(value)

        outputFileWriter.write(convertedFeature+"\n")

    inputFileReader.close()
    outputFileWriter.flush(),outputFileWriter.close()