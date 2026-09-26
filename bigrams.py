import nltk

text = input("Enter a text: ")
words = nltk.word_tokenize(text)

bigrams = list(nltk.bigrams(words))

print("Bigrams:")

for bigram in bigrams:
    print(bigram)