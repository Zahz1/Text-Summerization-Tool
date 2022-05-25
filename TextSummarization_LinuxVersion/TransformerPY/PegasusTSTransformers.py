#PathData = "..//..//data.txt"
#PathResults = "..//..//Results//TF//PegasusTS.txt"

PathData = "data.txt"
PathResults = "Results/Pegasus.txt"

fileIn = open(PathData, "r")
src_text = fileIn.read().replace("\n", " ")
fileIn.close()

from transformers import PegasusTokenizer, TFPegasusModel, PegasusModel, TFPegasusForConditionalGeneration
import tensorflow as tf

import time
start_time = time.time()

modelName = 'google/pegasus-xsum'
tokenizer = PegasusTokenizer.from_pretrained(modelName)
model = TFPegasusForConditionalGeneration.from_pretrained(modelName)

inputs = tokenizer(src_text, truncation=True, padding='longest', return_tensors="tf", )
translated = model.generate(**inputs)
tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
print(tgt_text)

print("--- PegasusTS %s seconds ---" % (time.time() - start_time))

fileOut = open(PathResults, "w")
fileOut.write(tgt_text[0])
fileOut.close()
