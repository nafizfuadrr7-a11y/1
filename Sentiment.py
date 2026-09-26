import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('Vader_lexicon')
text= input("Enter a Sentence: ")

sia= SentimentIntensityAnalyzer()
scores=sia.polarity_scores(text)

compound= scores['compound']
if compound >= 0.05:
    sentiment = "Positive"
elif compound <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print("Sentiment:", sentiment)
print("Scores:", scores)
