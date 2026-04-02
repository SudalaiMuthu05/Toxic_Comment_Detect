import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")
print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())