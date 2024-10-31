import joblib

# Modeli ve TF-IDF vektörizeri yükleyin
model = joblib.load('models/logistic_model.pkl')
tfidf_vectorizer = joblib.load('models/tfidf_vectorizer.pkl')

# Yeni bir metni dönüştür ve tahmin yap
sample_text = "Service was crappy,"
sample_text_features = tfidf_vectorizer.transform([sample_text])
prediction = model.predict(sample_text_features)

print("Predicted Sentiment:", prediction)
