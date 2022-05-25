def runSum():
    os.system('python3 SMMRY/runSMMRY.py')
    os.system('python3 Sumy/runSumy.py')
    os.system('python3 textteaser/runTextTeaser.py')
    os.system('python3 Bert_extractive/runBertExtractive.py')
    os.system('python3 TransformerPY/RobertaTorchTransformer.py')
    os.system('python3 TransformerPY/PegasusTSTransformers.py')
    os.system('python3 TransformerPY/distilbartTSTransformers.py')
    os.system('python3 TransformerPY/BartTSTransformers.py')

def moveFiles():
    try:
        shutil.move("Results/Bart.txt", pathDir + "/Bart.txt" )
    except:
        print("ERROR MOVING FILES Bart.txt")
    try:
        shutil.move("Results/Bert.txt", pathDir + "/Bert.txt" )
    except:
        print("ERROR MOVING FILES Bert.txt")
    try:
        shutil.move("Results/distilbart.txt", pathDir + "/distilbart.txt" )
    except:
        print("ERROR MOVING FILES distilbart.txt")
    try:
        shutil.move("Results/Pegasus.txt", pathDir + "/Pegasus.txt" )
    except:
        print("ERROR MOVING FILES Pegasus.txt")
    try:
        shutil.move("Results/Roberta.txt", pathDir + "/Roberta.txt" )
    except:
        print("ERROR MOVING FILES Roberta.txt")
    try:
        shutil.move("Results/Sumy.txt", pathDir + "/Sumy.txt" )
    except:
        print("ERROR MOVING FILES Sumy.txt")
    try:
        shutil.move("Results/TextTeaser.txt", pathDir + "/TextTeaser.txt" )
    except:
        print("ERROR MOVING FILES TextTeaser.txt")
    try:
        shutil.move("Results/SMMRY.txt", pathDir + "/SMMRY.txt" )
    except:
        print("ERROR MOVING FILES SMMRY.txt")



import os
import shutil
import preProssessing


preProssessing.preProc()

dataPath = "ArticleTexts"
parent_dir = "Results"

for filename in os.listdir(dataPath):

    fPath = os.path.join(dataPath, filename)
    if os.path.isfile(fPath):

        print(filename)

        #move data into data.txt
        file = open(fPath, "r")
        fileText = file.read()
        file.close()

        fileData = open("data.txt", "w")
        fileData.write(fileText)
        fileData.close()

        #run all 8 summaries
        runSum()

        #set up paths and dir
        directory = filename[0:len(filename)-4]
        pathDir = os.path.join(parent_dir, directory)
        try:
            os.mkdir(pathDir)
        except:
            print(directory + " file exists in " + pathDir + " directory.")

        #move files to the write spot
        moveFiles()
