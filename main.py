import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')
plt.style.use('seaborn-v0_8-muted')

# Load Dataset
df = pd.read_csv(r"D:\\PythonPr\\netflix_titles.csv")

# Head of dataset
print("First 5 Rows:")
print(df.head())

# Basic info
print("Info:")
print(df.info())

# Summary stats
print("Description of numerical columns:")
print(df.describe())

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Check for missing values
print("Missing Values:")
print(df.isnull().sum())

# Fill missing values (No inplace to avoid FutureWarnings)
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
df['rating'] = df['rating'].fillna("Unknown")
df['duration'] = df['duration'].fillna("Unknown")
