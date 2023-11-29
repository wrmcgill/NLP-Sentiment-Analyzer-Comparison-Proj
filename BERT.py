import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import requests
from bs4 import BeautifulSoup
import re

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

file_path = 'Negative_review_data.txt'
max_length = 512
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

tokens = tokenizer.encode(text, max_length=max_length, truncation=True, return_tensors='pt')

result = model(tokens)

print(torch.argmax(result.logits))
