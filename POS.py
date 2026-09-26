import nltk

nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

sentence = input("Enter a sentence: ")
words = nltk.word_tokenize(sentence)

pos_tags = nltk.pos_tag(words)


print("POS Tags:")
for word, tag in pos_tags:
    print(word, "->", tag)