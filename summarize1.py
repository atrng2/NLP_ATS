#https://www.mygreatlearning.com/blog/text-summarization-in-python/

# importing libraries

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize



with open("sample.txt", "r") as file:
    text = file.read().replace('\n', '')




#tokenizing the text
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

#creating a frequency table to keep the score of each word

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1


#Creating a dictionary to keep the score of each sentence
sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

average = int(sumValues / len(sentenceValue))

#Storing setences into our summary.
summary = ''
for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence

print(summary)