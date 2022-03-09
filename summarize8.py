
from transformers import T5ForConditionalGeneration, T5Tokenizer

# initialize the model architecture and weights
model = T5ForConditionalGeneration.from_pretrained("t5-base")
# initialize the model tokenizer
tokenizer = T5Tokenizer.from_pretrained("t5-base")

with open("sample2.txt", "r") as file:
    article = file.read().replace('\n', '')

article = article[:512]

# encode the text into tensor of integers using the appropriate tokenizer
inputs = tokenizer.encode("summarize: " + article, return_tensors="pt", max_length=512, truncation=True)

outputs = model.generate(
    inputs, 
    #max_length=150, 
    #min_length=40, 
    length_penalty=2.0, 
    num_beams=4, 
    early_stopping=True)
# just for debugging
#print(outputs)

print(tokenizer.decode(outputs[0]))