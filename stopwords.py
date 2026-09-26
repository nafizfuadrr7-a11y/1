import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

text=input("Enter a sentence:")
words=nltk.word_tokenize(text)

stop_words= set(stopwords.words('english'))
filter_words=[w for w in words if w.lower() not in stop_words]

print("\nOriginal words:", words)
print("\nAfter removing stopwords:", filter_words)