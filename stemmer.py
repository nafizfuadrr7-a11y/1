import nltk
from nltk.stem import PorterStemmer

text= input("Enter Words:")
words=nltk.word_tokenize(text)

stemmer=PorterStemmer()

stemmed_words=[]
for word in words:
    stemmed_words.append(stemmer.stem(word))

print("Original words:", words)
print("Stemmed words:", stemmed_words)