import pandas as pd
import joblib
from src.data_preprocessing import preprocess_text

# Yelp yorumlarını JSON dosyasından yükle
df = pd.read_json('data/yelp_reviews.json')

# Model ve TF-IDF vektörizerini yükle
tfidf = joblib.load('models/tfidf_vectorizer.pkl')
model = joblib.load('models/logistic_model.pkl')

def predict_sentiment(text, tfidf, model):
    cleaned_text = preprocess_text(text)  # Yorum metnini temizle
    vectorized_text = tfidf.transform([cleaned_text])  # TF-IDF ile vektörize et
    prediction = model.predict(vectorized_text)  # Model ile tahmin yap
    return "Olumlu" if prediction == 1 else "Olumsuz"  # Tahmin sonucunu döndür

# Yorumları ve ilgili bilgileri yazdır
for index, row in df.iterrows():
    review_text = row['text']
    stars = row['stars']
    
    # Tahmin yap
    sentiment = predict_sentiment(review_text, tfidf, model)
    
    # Sonuçları yazdır
    #print(f"Yorum ID: {row['review_id']}")
    #print(f"Kullanıcı ID: {row['user_id']}")
    #print(f"İşletme ID: {row['business_id']}")
    print(f"Yıldız: {stars}")
    print(f"Yorum: {review_text}")
    print(f"Tahmin Edilen Duygu: {sentiment}")
    print(f"Tahmin ile Yıldız Puanı: {'Olumlu' if stars > 3 else 'Olumsuz'}")
    print("-" * 80)
