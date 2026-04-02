# This script will be used to train the model for toxic comment detection.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load your dataset
# df = pd.read_csv('path_to_your_data.csv')
# X = df['comment']  # Features (toxic comments)
# y = df['label']    # Target (labels)

# Example dataset initialization (to be replaced with actual data)
data = {'comment': ['Example comment 1', 'Example comment 2'], 'label': [0, 1]}
df = pd.DataFrame(data)
X = df['comment']
y = df['label']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))
