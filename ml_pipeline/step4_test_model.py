from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pandas as pd
import pickle

# Load dataset
df = pd.read_csv("data.csv")

# Load model and vectorizer
model = pickle.load(open("models/toxic_model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

X = vectorizer.transform(df['text'])
y = df['label']

# Make predictions
y_pred = model.predict(X)

# Print metrics
print("✅ Model Test Results:")
print(f"Accuracy: {accuracy_score(y, y_pred):.2f}")
print("
Classification Report:")
print(classification_report(y, y_pred))
print("
Confusion Matrix:")
print(confusion_matrix(y, y_pred))