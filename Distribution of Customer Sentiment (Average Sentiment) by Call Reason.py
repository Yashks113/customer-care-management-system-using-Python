plt.figure(figsize=(12, 6))
sns.boxplot(data=merged_df, x='average_sentiment', y='primary_call_reason', palette="coolwarm", order=merged_df['primary_call_reason'].value_counts().index)
plt.title('Customer Sentiment by Primary Call Reason')
plt.xlabel('Average Sentiment')
plt.ylabel('Primary Call Reason')
plt.tight_layout()
plt.show()
