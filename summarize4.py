#LSA

# Load Packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer



with open("sample3.txt", "r") as file:
    text = file.read().replace('\n', '')

# Creating text parser using tokenization
parser = PlaintextParser.from_string(text,Tokenizer("english"))

from sumy.summarizers.lsa import LsaSummarizer
summarizer_lsa = LsaSummarizer()

# Summarize using sumy LSA
summary =summarizer_lsa(parser.document,2)

lsa_summary=""
for sentence in summary:
    lsa_summary+=str(sentence)

print(lsa_summary)