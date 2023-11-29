from newspaper import Article
import nltk
nltk.download('punkt')
from textblob import TextBlob

file_path = "Negative_review_data.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()


blob = TextBlob(text)

sentiment = blob.sentiment.polarity

print(sentiment)
