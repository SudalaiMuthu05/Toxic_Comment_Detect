from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import pickle

# Load dataset
df = pd.read_csv("data.csv")

# Create vectorizer
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['text'])

# Save vectorizer
pickle.dump(vectorizer, open("models/vectorizer.pkl", "wb"))
print("✅ Vectorizer created and saved")