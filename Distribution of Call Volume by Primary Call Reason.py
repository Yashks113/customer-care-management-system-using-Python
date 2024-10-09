#Distribution of Call Volume by Primary Call Reason
plt.figure(figsize=(12, 6))
sns.countplot(data=merged_df, y='primary_call_reason', order=merged.df['primary_call_reason'].value_counts().index, palette="viridis")
plt.title('Distribution of Call Volume by Primary Call Reason')
plt.xlabel('Number of Calls')
plt.ylabel('Primary Call Reason')
plt.tight_layout()
plt.show()
