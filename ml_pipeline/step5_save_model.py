from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import pickle

# Load dataset
df = pd.read_csv("data.csv")

# Create vectorizer
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model
pickle.dump(model, open("models/toxic_model.pkl", "wb"))
pickle.dump(vectorizer, open("models/vectorizer.pkl", "wb"))

print("✅ Model and vectorizer saved successfully")
print("Files created: toxic_model.pkl, vectorizer.pkl")