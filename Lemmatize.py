import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

text= input("Enter a sentence:")
words=nltk.word_tokenize(text)

lemmatizer=WordNetLemmatizer()

lemmatized_words=[]
for word in words:
    lemmatized_words.append(lemmatizer.lemmatize(word))

print("\nOriginal words:", words)
print("\nLemmatized words:", lemmatized_words)
