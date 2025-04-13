#Objective 1: Department-level Salary Summary
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
df = pd.read_csv("cleaned_data.csv")

def clean_currency(col):
    return (
        col.replace('[\$,₹,€,£]', '', regex=True)
           .replace(',', '', regex=False)
           .astype(float)
    )

cols_to_clean = ['base_salary', 'total_pay', '2024_overtime_pay', '2024_longevity_pay']
for col in cols_to_clean:
    if col in df.columns:
        df[col] = clean_currency(df[col])
group_column = 'department_name' if 'department_name' in df.columns else 'department'

dept_summary = df.groupby(group_column).agg(
    employee_count=('base_salary', 'count'),
    avg_base_salary=('base_salary', 'mean'),
    avg_total_pay=('total_pay', 'mean')
).sort_values(by='avg_total_pay', ascending=False).round(2)

print("🔍 Top 10 departments by average total pay:")
print(dept_summary.head(10))
# 5. Bar Plot - Avg Total Pay
plt.figure(figsize=(14, 6))
sns.barplot(
    data=dept_summary.reset_index(),
    x=group_column,
    y='avg_total_pay',
    palette='viridis',
    hue=group_column,
    legend=False
)
plt.xticks(rotation=90)
plt.title('Average Total Pay by Department (2024)', fontsize=14)
plt.ylabel('Avg Total Pay ($)')
plt.xlabel('Department')
plt.tight_layout()
plt.show()
