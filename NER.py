import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

text = input("Enter a sentence: ")

words = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(words)

named_entities = nltk.ne_chunk(pos_tags)

print("\nNamed Entity Recognition:")
for entity in named_entities:
    if hasattr(entity, 'label'):
        name = " ".join(word for word, tag in entity.leaves())
        print(name, "->", entity.label())

grammar = "NP: {<JJ>*<NN.*>+}"
chunk_parser = nltk.RegexpParser(grammar)
chunk_tree = chunk_parser.parse(pos_tags)

print("\nChunking:")
print(chunk_tree)