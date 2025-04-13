#Objective 2-- Analyze Overtime Pay by Department and Grade

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

df = pd.read_csv("cleaned_data.csv")

df = df[df['2024_overtime_pay'] > 0]

top_departments = df['department_name'].value_counts().head(10).index.tolist()
filtered_df = df[df['department_name'].isin(top_departments)]

top_grades = df['grade'].value_counts().head(10).index.tolist()
filtered_df = filtered_df[filtered_df['grade'].isin(top_grades)]

plt.figure(figsize=(14, 8))
sns.boxplot(
    data=filtered_df,
    x='2024_overtime_pay',
    y='grade',
    hue='grade',
    palette='Set2',
    legend=False
)

plt.title("Overtime Pay by Grade (Top 10 Job Grades)", fontsize=14)
plt.xlabel("Overtime Pay ($)")
plt.ylabel("Job Grade")
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
