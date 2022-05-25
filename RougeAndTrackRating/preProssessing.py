import os

dataPath = "Articles"
sysPath = "system_sum"
refPath = "reference_sum"
ref_sum_MikeSum = "MikeSum.txt"



print("Preprocessing Starting...")

listF = os.listdir(dataPath)

for dirName in listF:
    dPath = os.path.join(dataPath, dirName)
    dPath = os.path.join(dPath, sysPath)

    fileNames = os.listdir(dPath)

    for file in fileNames:
        fPath = os.path.join(dPath, file)

        #file = open(fPath, "r")
        #fileText = file.read().replace("\n"," ")
        #file.close()

        if os.path.isfile(fPath):
            file = open(fPath, "rb")

            filetext = file.read()

            #"
            replaceQuote = [b'\xe2\x80\x9c', b'\xe2\x80\x9d', b'\xe2\x80\x9f', b'\xe2\x80\xb3', b'\xe2\x80\xb6']
            #'
            replaceQuoteSingle = [b'\xe2\x80\x99', b'\xe2\x80\xb2', b'\xe2\x80\xb5']
            #-
            replaceDash = [b'\xe2\x80\x94',b'\xe2\x80\x90',b'\xe2\x80\x91', b'\xe2\x80\x92', b'\xe2\x80\x93', b'\xe2\x80\x95']

            for i in replaceQuote:
                filetext = filetext.replace(i,b'"')

            for i in replaceQuoteSingle:
                filetext = filetext.replace(i,b"'")

            for i in replaceDash:
                filetext = filetext.replace(i,b'-')

                file.close()

                file = open(fPath, "wb")

                file.write(filetext)

print("Preprocessing Done")
