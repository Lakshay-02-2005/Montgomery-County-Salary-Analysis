#objective  Analyze overtime pay distribution across departments
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_data.csv')

df_ot = df[df['2024_overtime_pay'] > 0]
dept_ot = df_ot.groupby('department')['2024_overtime_pay'].mean().reset_index()
dept_ot_pivot = dept_ot.pivot_table(index='department', values='2024_overtime_pay')
#plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(dept_ot_pivot, annot=True, fmt=".0f", cmap='YlGnBu', cbar_kws={'label': 'Avg Overtime Pay'})
plt.title('Average Overtime Pay by Department', fontsize=14)
plt.xlabel('')
plt.ylabel('Department', fontsize=12)
plt.tight_layout()
plt.show()
