from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

import time
start_time = time.time()

PathData = "data.txt"
PathResults = "Results/Roberta.txt"

fileIn = open(PathData, "r")
src_text = fileIn.read().replace("\n", " ")
fileIn.close()



model_name = 'patrickvonplaten/roberta_shared_bbc_xsum'
device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
batch = tokenizer(src_text, truncation=True, padding='longest', return_tensors="pt").to(device)
translated = model.generate(**batch)
tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
print(tgt_text)

print("--- RobertaTorch %s seconds ---" % (time.time() - start_time))

fileOut = open(PathResults, "w")
fileOut.write(tgt_text[0])
fileOut.close()
