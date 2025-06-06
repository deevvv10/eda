# -*- coding: utf-8 -*-
"""eda_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16_EEam13hXO1j9L0ufmUng10Ltt0Rm1h
"""

import pandas as pd

# Load the dataset
dataset_url = "https://raw.githubusercontent.com/salemprakash/EDA/main/Data/Fertility2.csv"
data = pd.read_csv(dataset_url)

# Dimensions of the dataset
print(f"Dimensions of dataset: {data.shape}")

# Display basic information about the dataset
print("Dataset Info:")
print(data.info())

# Data types of each column
print("\nData types:")
print(data.dtypes)

# Basic information of the dataset
print("\nDataset Information:")
data.info()

# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Convert categorical columns to appropriate types
# Assuming the actual column names in the dataframe might have leading or trailing spaces
# Use str.strip() to trim whitespace
categorical_columns = ['Class', 'Sex']
categorical_columns_cleaned = [col.strip() for col in data.columns if any(col.strip() == desired_col for desired_col in categorical_columns)]

for column in categorical_columns_cleaned:
    data[column] = data[column].astype('category')

# Display the updated data types
print("\nUpdated Data Types after conversion:")
print(data.dtypes)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Check the actual column names in your DataFrame
print(data.columns)

# Replace 'Season' with the correct column name (e.g., 'age')
plt.figure(figsize=(8, 6))
sns.histplot(data['age'], kde=True, bins=10)  # Replace 'age' with the correct column if needed
plt.title('Distribution of Age')  # Adjust title based on the column
plt.show()

# Countplot for 'gender1' (or any other categorical column in your dataset)
plt.figure(figsize=(8, 6))
sns.countplot(x='gender1', data=data)  # Replace 'gender1' with any relevant column name
plt.title('Count of Gender Categories')  # Update title if needed
plt.show()

# Step 7: Bivariate Analysis - Correlation Heatmap

# Select numeric columns from your dataset
numeric_data = data.select_dtypes(include=['float64', 'int64'])  # Ensure only numeric columns are selected

# Plot correlation heatmap for the numeric features
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Step 8: Multivariate Analysis - Pairplot and Barplot

# Pairplot for analyzing interactions between numerical features, using 'gender1' as the hue
sns.pairplot(data, hue='gender1', diag_kind='kde')
plt.show()

# Barplot for 'age' by 'gender1'
plt.figure(figsize=(10, 6))
sns.barplot(x='gender1', y='age', data=data)
plt.title('Age by Gender1')
plt.show()