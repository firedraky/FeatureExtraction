# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2015-01-08
# version: 0.1
__author__ = 'lifuxin'


if __name__ == "__main__":

    #   output
    attPrefixFile = "../all_asc_tweetsOutput/attPrefix"
    attPrefieWriter = open(attPrefixFile,'w')

    attNo = 1
    while attNo < 20000:
        #@attribute Att_1 numeric
        attPrefieWriter.write("@attribute Att"+str(attNo)+" numeric\n")
        attNo = attNo + 1
    attPrefieWriter.flush(),attPrefieWriter.close()


