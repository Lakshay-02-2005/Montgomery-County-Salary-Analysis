import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data.csv")

# Preview the data
print("Original Data Preview:")
print(df.head())

# Standardize column names: lowercase, no spaces
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
print("Cleaned Column Names:", df.columns.tolist())

# Data types and missing values
print("\nData Types and Missing Values:")
print(df.info())

# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing Values per Column:")
print(missing_values)

# Define pay-related columns
pay_cols = ['base_salary', '2024_overtime_pay', '2024_longevity_pay']

# Function to clean and convert to float (e.g., "$45,000" -> 45000.00)
def clean_currency(x):
    if pd.isna(x):
        return 0.0
    return float(str(x).replace(",", "").replace("$", "").strip())

# Apply cleaning function to the salary columns
for col in pay_cols:
    df[col] = df[col].apply(clean_currency)

# Confirm that the columns are now numeric
print("\nData After Cleaning Salary Columns:")
print(df[pay_cols].head())

# Fill missing numeric salary values with 0
df[pay_cols] = df[pay_cols].fillna(0)

# Drop rows where critical columns (department or grade) are missing
df = df.dropna(subset=['department', 'grade'])

# Check if there are any remaining missing values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Create Total Pay column (base salary + overtime pay + longevity pay)
df['total_pay'] = df['base_salary'] + df['2024_overtime_pay'] + df['2024_longevity_pay']

# Create Overtime-to-Base Ratio column (overtime pay as a fraction of base salary)
df['ot_ratio'] = df['2024_overtime_pay'] / df['base_salary'].replace(0, 1)

# Preview new columns
print("\nData with New Columns:")
print(df[['base_salary', '2024_overtime_pay', '2024_longevity_pay', 'total_pay', 'ot_ratio']].head())

# Summary statistics for the cleaned data
print("\nSummary Statistics:")
print(df.describe())

# Check the final shape of the dataset
print("\nFinal Data Shape:", df.shape)

# Preview the cleaned data
print("\nCleaned Data Preview:")
print(df.head())

# Save cleaned data to a new CSV file
df.to_csv("cleaned_data.csv", index=False)

# Sample visualization: Distribution of Total Pay
plt.figure(figsize=(10, 6))
sns.histplot(df['total_pay'], kde=True, color='blue')
plt.title('Distribution of Total Pay')
plt.xlabel('Total Pay')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
