#PathData = "..//..//data.txt"
#PathResults = "..//..//Results//TF//distilbartTS.txt"

PathData = "data.txt"
PathResults = "Results/distilbart.txt"

fileIn = open(PathData, "r")
src_text = fileIn.read().replace("\n", " ")
fileIn.close()

from transformers import BartTokenizer, TFBartModel, BartModel, TFBartForConditionalGeneration
import tensorflow as tf

import time
start_time = time.time()

modelName = 'sshleifer/distilbart-xsum-1-1'
tokenizer = BartTokenizer.from_pretrained(modelName)
model = TFBartForConditionalGeneration.from_pretrained(modelName)

inputs = tokenizer(src_text, truncation=True, padding='longest', return_tensors="tf")
translated = model.generate(inputs['input_ids'],
                                    num_beams=4,
                                    no_repeat_ngram_size=2,
                                    min_length=30,
                                    max_length=100,
                                    early_stopping=True)

tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
print(tgt_text)

print("--- distilbartTS %s seconds ---" % (time.time() - start_time))

fileOut = open(PathResults, "w")
fileOut.write(tgt_text[0])
fileOut.close()
