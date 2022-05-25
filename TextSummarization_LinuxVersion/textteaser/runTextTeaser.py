from textteaser import TextTeaser

# article source: https://blogs.dropbox.com/developers/2015/03/limitations-of-the-get-method-in-http/
# title = "Limitations of the GET method in HTTP"


PathData = "data.txt"
PathResults = "Results/TextTeaser.txt"

fileIn = open(PathData, "r")
title = text = fileIn.read().replace("\n", " ")
fileIn.close()

tt = TextTeaser()

sentences = tt.summarize(title, text)

sentenceCount = 1

output = ""
for i in range(sentenceCount):
    output = output + " " + sentences[i]

print(output)
fileOut = open(PathResults, "w")
fileOut.write(output)
fileOut.close()
