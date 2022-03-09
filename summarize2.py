#https://avinashnavlani.medium.com/text-summarization-using-python-773e064377eb
#using sumy
#requires numpy, sumy

# Load Packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer



with open("sample3.txt", "r") as file:
    text = file.read().replace('\n', '')

# Creating text parser using tokenization
parser = PlaintextParser.from_string(text,Tokenizer("english"))

from sumy.summarizers.text_rank import TextRankSummarizer

# Summarize using sumy TextRank
summarizer = TextRankSummarizer()
summary = summarizer(parser.document,2)

text_summary=""
for sentence in summary:
    text_summary+=str(sentence)

print(text_summary)