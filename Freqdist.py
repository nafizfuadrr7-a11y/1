import nltk
from nltk.probability import FreqDist


text = input("Enter a text: ")
words = nltk.word_tokenize(text)

fdist = FreqDist(words)

print("Most frequent words:")
for word, frequency in fdist.most_common():
    print(word, "->", frequency)