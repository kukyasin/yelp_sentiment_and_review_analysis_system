import pandas as pd
from src.sentiment_predictor import train_model

# Yelp yorumlarını JSON dosyasından yükle
df = pd.read_json('data/yelp_reviews.json')

# Modeli eğit
model, tfidf = train_model(df)

print("Model eğitimi tamamlandı.")
