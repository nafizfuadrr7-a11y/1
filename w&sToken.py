import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
paragraph=input("Enter the paragraph:")

sentences=nltk.sent_tokenize(paragraph)
words=nltk.word_tokenize(paragraph)

print("\nSentences:")
for sentence in sentences:
    print(sentence)
    
print("\nWords:", words)
