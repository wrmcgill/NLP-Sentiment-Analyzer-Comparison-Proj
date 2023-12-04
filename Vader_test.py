from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

obj = SentimentIntensityAnalyzer()

sentence = "Ram is really good"
sentiment_dict = obj.polarity_scores(sentence)
print(sentiment_dict)

sentence = "Rahul is really bad"
sentiment_dict = obj.polarity_scores(sentence)
print(sentiment_dict)