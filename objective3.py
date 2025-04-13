'''objective 3--distribution of total pay within
different departments and job grades.'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('cleaned_data.csv')

# Strip plot for the distribution of Total Pay across Departments
plt.figure(figsize=(12, 8))
sns.stripplot(data=df, x='department', y='total_pay', jitter=True, palette='Set2')
plt.title('Distribution of Total Pay by Department', fontsize=14)
plt.xlabel('Department', fontsize=12)
plt.ylabel('Total Pay (in currency)', fontsize=12)
plt.xticks(rotation=45)  # Rotate department names for better readability
plt.show()
