#using sumy
#requires numpy, sumy

# Load Packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

#text
#text = "Some of the earliest evidence of salt processing dates to around 6,000 BC, when people living in the area of present-day Romania boiled spring water to extract salts; a salt-works in China dates to approximately the same period. Salt was also prized by the ancient Hebrews, the Greeks, the Romans, the Byzantines, the Hittites, Egyptians, and the Indians. Salt became an important article of trade and was transported by boat across the Mediterranean Sea, along specially built salt roads, and across the Sahara on camel caravans. The scarcity and universal need for salt have led nations to go to war over it and use it to raise tax revenues. Salt is used in religious ceremonies and has other cultural and traditional significance."
#text = "I AM SAM. I AM SAM. SAM I AM.THAT SAM-I-AM! THAT SAM-I-AM! I DO NOT LIKE THAT SAM-I-AM!DO WOULD YOU LIKE GREEN EGGS AND HAM?I DO NOT LIKE THEM,SAM-I-AM.I DO NOT LIKE GREEN EGGS AND HAM.WOULD YOU LIKE THEM HERE OR THERE?I WOULD NOT LIKE THEM HERE OR THERE.I WOULD NOT LIKE THEM ANYWHERE.I DO NOT LIKE GREEN EGGS AND HAM.I DO NOT LIKE THEM, SAM-I-AM.WOULD YOU LIKE THEM IN A HOUSE?WOULD YOU LIKE THEN WITH A MOUSE?I DO NOT LIKE THEM IN A HOUSE.I DO NOT LIKE THEM WITH A MOUSE.I DO NOT LIKE THEM HERE OR THERE.I DO NOT LIKE THEM ANYWHERE.I DO NOT LIKE GREEN EGGS AND HAM.I DO NOT LIKE THEM, SAM-I-AM.WOULD YOU EAT THEM IN A BOX?WOULD YOU EAT THEM WITH A FOX?"
text = "The sun did not shine. It was too wet to play. So we sat in the houseAll that cold, cold, wet day. I sat there with Sally. We sat there, we two. And I said, 'How I wish We had something to do!' Too wet to go out And too cold to play ball. So we sat in the house. We did nothing at all. So all we could do was to. Sit! Sit! Sit! Sit! And we did not like it. Not one little bit. BUMP! And then something went BUMP! How that bump made us jump! We looked! Then we saw him step in on the mat! We looked! And we saw him! The Cat in the Hat! And he said to us, 'Why do you sit there like that?' 'I know it is wet. And the sun is not sunny. But we can have Lots of good fun that is funny!' "

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