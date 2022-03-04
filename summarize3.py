#lex rank

# Load Packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer



with open("sample.txt", "r") as file:
    text = file.read().replace('\n', '')

# Creating text parser using tokenization
parser = PlaintextParser.from_string(text,Tokenizer("english"))

from sumy.summarizers.lex_rank import LexRankSummarizer
summarizer_lex = LexRankSummarizer()

# Summarize using sumy LexRank
summary= summarizer_lex(parser.document, 2)
lex_summary=""

for sentence in summary:
    lex_summary+=str(sentence)  
print(lex_summary)