from summarizer import Summarizer
import time
start_time = time.time()

#PathData = "//home//mfoley//TextSummarization_LinuxVersion//data.txt"
#PathResults = "//home//mfoley//TextSummarization_LinuxVersion//Results//Bert.txt"

PathData = "data.txt"
PathResults = "Results/Bert.txt"


fileIn = open(PathData, "r")
body = fileIn.read().replace("\n", " ")
fileIn.close()


model = Summarizer()
result = model(body, num_sentences = 0)
full = ''.join(result)
print(full)

fileOut = open(PathResults, "w")
fileOut.write(full)
fileOut.close()

print("--- Bert %s seconds ---" % (time.time() - start_time))
