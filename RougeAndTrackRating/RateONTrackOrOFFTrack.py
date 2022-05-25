import os
import csv
from os import system, name

dataPath = "Articles"
sysPath = "system_sum"
refPath = "reference_sum"
ref_sum_MikeSum = "MikeSum.txt"

finalData = [[]]

fileNames = []

listF = os.listdir(dataPath)

listTemp = [listF[0], listF[1]]

print(listTemp)

for dirName in listF:
    dPath = os.path.join(dataPath, dirName)

    rPath = os.path.join(dPath, refPath)
    rPath = os.path.join(rPath, ref_sum_MikeSum)

    dPath = os.path.join(dPath, sysPath)

    file = open(rPath, "r")
    refFileText = file.read().replace("\n"," ")
    file.close()

    fileNames = os.listdir(dPath)
    finalData[0] = fileNames

    currData = [dirName]

    for file in fileNames:
        fPath = os.path.join(dPath, file)
        file = open(fPath, "r")
        fileText = file.read().replace("\n"," ")
        file.close()

        # for windows
        if name == 'nt':
            _ = system('cls')

            # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

        print("-"*15 + "Title" + "-"*15)
        print(dirName)
        print("\n")
        print("-"*15 + "ref_sum_MikeSum" + "-"*15)
        print(refFileText)
        print("\n")
        print("-"*15 + "system_sum" + "-"*15)
        print(fileText)
        print("\n")
        print(currData)
        print("\n")

        while(True):
            userInput = input("Enter Rating: ")
            try:
                userInput = int(userInput)
            except:
                userInput = userInput

            if userInput == 1 or userInput == 0:
                currData.append(str(userInput))
                break
            else:
                print("Wrong input try again!")

    finalData.append(currData)

output = open("outputFile.csv", "w")

outputList = [""]
finalData[0] = outputList + finalData[0]

print(finalData[0])
for list in finalData:
    outputText = ",".join(list) + ",\n"
    output.write(outputText)
