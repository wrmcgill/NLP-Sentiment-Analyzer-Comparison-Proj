from newspaper import Article
import nltk
nltk.download('punkt')
from textblob import TextBlob

url = "https://en.wikipedia.org/wiki/Donald_A._Morgan"

article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary

blob = TextBlob(text)

sentiment = blob.sentiment.polarity

print(sentiment)
