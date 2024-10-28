import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    # Küçük harfe çevir
    text = text.lower()
    
    # Özel karakterleri ve sayıları kaldır
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Kelimeleri ayır
    words = text.split()
    
    # Stopwords'leri kaldır
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    
    # Kelimeleri lemmatize et
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    # Temizlenmiş metni geri döndür
    return ' '.join(words)
