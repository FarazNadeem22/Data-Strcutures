import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.probability import FreqDist
import os

# Download necessary NLTK resources (if not already downloaded)
try:
    nltk.data.find('vader_lexicon')
    nltk.data.find('stopwords')
    nltk.data.find('wordnet')
except LookupError:
    nltk.download('vader_lexicon')
    nltk.download('stopwords')
    nltk.download('wordnet')
def read_csv_to_dataframe(filepath):
    try:
        df = pd.read_csv(filepath)
        if 'Text' not in df.columns:
            raise ValueError("'Text' column not found in CSV.")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None

sia = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
sentimental_words = []

for text in df['Text']:
    tokens = word_tokenize(str(text).lower())
    tags = nltk.pos_tag(tokens)

    for word, tag in tags:
        if tag.startswith('JJ') or tag.startswith('RB'):
            if word not in stop_words:
                sentiment = sia.polarity_scores(word)
                if sentiment['compound'] != 0:
                    stemmed_word = stemmer.stem(word)
                    lemma_word = lemmatizer.lemmatize(stemmed_word)
                    sentimental_words.append(lemma_word)

freq_dist = FreqDist(sentimental_words)
word_counts = pd.DataFrame(freq_dist.most_common(), columns=['Word', 'Count'])
