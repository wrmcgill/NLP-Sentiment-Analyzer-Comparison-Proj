from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk

# Initialize the VADER sentiment intensity analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment of a sentence
def analyze_sentiment(sentence):
    sentiment_dict = analyzer.polarity_scores(sentence)
    print(f"{sentence} - {sentiment_dict}")

# Read the text file and analyze each sentence
with open('Neutral_study_data.txt', 'r') as file:
        analyze_sentiment(line.strip())  # Stripping to remove leading/trailing whitespace
        
        