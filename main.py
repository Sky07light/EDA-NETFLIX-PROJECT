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
