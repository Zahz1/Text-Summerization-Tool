import os, math

dataPath = "Results"
resultPath = "MasterDataFile.csv"

ref = ["Byline", "FirstSentence", "MikeSum", "title"]

SumList = []

Byline = []
FirstSentenceFile = []
MikeSumFile = []
titleFile = []

for filename in os.listdir(dataPath):

    fPath = os.path.join(dataPath, filename)
    if os.path.isfile(fPath):
        file = open(fPath, "r")

        Lines = file.readlines()

        articleName = Lines[0].replace("\n", "")
        SumList = Lines[1].replace("\n", "")

        #line 2 is byline title, line 3 is byline data
        MikeSumData = Lines[3].replace("\n", "").split(",")
        MikeSumData[0] = articleName
        MikeSumFile.append(MikeSumData)

        #line 4 is FirstSentence title, line 5 is FirstSentence data
        titleData = Lines[5].replace("\n", "").split(",")
        titleData[0] = articleName
        titleFile.append(titleData)

        #line 6 is MikeSum title, line 7 is MikeSum data
        bylineData = Lines[7].replace("\n", "").split(",")
        bylineData[0] = articleName
        Byline.append(bylineData)

        #line 8 is title title, line 9 is title data
        FirstSentenceData = Lines[9].replace("\n", "").split(",")
        FirstSentenceData[0] = articleName
        FirstSentenceFile.append(FirstSentenceData)

        file.close()

SumList = SumList.split(",")
print(SumList)


file = open(resultPath, "w")
file.close()

file = open(resultPath, "a")

bylineFirst = SumList
bylineFirst[0] = ref[0]
firstLine = ",".join(bylineFirst) + ","


FirstSentenceFirst = SumList
bylineFirst[0] = ref[1]
firstLine = firstLine + ",".join(FirstSentenceFirst) + ","

MikeSumFirst = SumList
MikeSumFirst[0] = ref[2]
firstLine = firstLine + ",".join(MikeSumFirst) + ","

titleFirst = SumList
titleFirst[0] = ref[3]
firstLine = firstLine + ",".join(titleFirst) + ","

file.write(firstLine + "\n")

for i in range(0,len(Byline)):
    currLine = ",".join(Byline[i]) + "," + ",".join(FirstSentenceFile[i]) + "," + ",".join(MikeSumFile[i]) + "," + ",".join(titleFile[i]) + ",\n"
    file.write(currLine)
