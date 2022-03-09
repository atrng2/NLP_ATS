#https://www.thepythoncode.com/article/text-summarization-using-huggingface-transformers-python
#pip3 install transformers torch sentencepiece


from transformers import pipeline

# using pipeline API for summarization task
summarization = pipeline("summarization")

with open("sample1.txt", "r") as file:
    original_text = file.read().replace('\n', '')

original_text = original_text[:1024]

summary_text = summarization(original_text)[0]['summary_text']
print("Summary:", summary_text)