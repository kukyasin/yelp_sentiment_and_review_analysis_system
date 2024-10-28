from sklearn.feature_extraction.text import TfidfVectorizer

def get_tfidf_features(corpus, max_features=5000):
    tfidf = TfidfVectorizer(max_features=max_features)
    X = tfidf.fit_transform(corpus)
    return X, tfidf
