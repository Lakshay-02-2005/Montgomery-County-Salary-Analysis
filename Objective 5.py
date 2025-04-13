#Objective 5: Identify trends in longevity pay across different grades or departments.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_data.csv')
df_longevity = df[df['2024_longevity_pay'] > 0]
longevity_by_grade = df_longevity.groupby('grade')['2024_longevity_pay'].mean().reset_index()
longevity_by_grade = longevity_by_grade.sort_values(by='grade')

# Plot bar plot
plt.figure(figsize=(12, 6))
sns.barplot(data=longevity_by_grade, x='grade', y='2024_longevity_pay', palette='coolwarm')
plt.title('Average Longevity Pay by Grade (2024)', fontsize=14)
plt.xlabel('Job Grade', fontsize=12)
plt.ylabel('Avg Longevity Pay', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
