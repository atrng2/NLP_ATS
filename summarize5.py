#https://avinashnavlani.medium.com/text-summarization-using-python-773e064377eb
#KL Divergence

# Load Packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

with open("sample3.txt", "r") as file:
    text = file.read().replace('\n', '')

# Creating text parser using tokenization
parser = PlaintextParser.from_string(text,Tokenizer("english"))

from sumy.summarizers.kl import KLSummarizer

summarizer_kl = KLSummarizer()

# Summarize using sumy KL Divergence
summary =summarizer_kl(parser.document,2)

kl_summary=""
for sentence in summary:
    kl_summary+=str(sentence)  
print(kl_summary)