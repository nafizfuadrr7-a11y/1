import string
text=input("Enter the text:")
text= text.lower()
text=text.translate(str.maketrans('', '', string.punctuation))
print("Processed text:", text)