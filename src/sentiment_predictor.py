from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.over_sampling import SMOTE
import joblib
import pandas as pd

def train_model(df):
    # Yıldız puanına göre etiketler oluştur
    df['label'] = df['stars'].apply(lambda x: 1 if x > 3 else 0)
    
    # Özellikler ve etiketler
    X = df['text']
    y = df['label']

    # TF-IDF vektörizeri oluştur
    tfidf = TfidfVectorizer()
    X_vectorized = tfidf.fit_transform(X)

    # Veriyi eğitim ve test setlerine ayır
    X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

    # SMOTE ile eğitim setini dengele
    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

    # Modeli eğit
    model = LogisticRegression()
    model.fit(X_train_resampled, y_train_resampled)

    # Model ve TF-IDF'yi kaydet
    joblib.dump(model, 'models/logistic_model.pkl')
    joblib.dump(tfidf, 'models/tfidf_vectorizer.pkl')

    return model, tfidf
