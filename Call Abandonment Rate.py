#Call Abandonment Rate (Proxy - Based on AST or other wait time proxies, we'll assume AST > 8 seconds might indicate a risk of abandonment)
merged_df['abandoned'] = merged_df['AST'] > 8  # Proxy to identify abandoned calls

# Call abandonment rate by reason
abandonment_rate_by_reason = merged_df.groupby('primary_call_reason')['abandoned'].mean().sort_values(ascending=False)

# Visualizing Call Abandonment Rate by Call Reason
plt.figure(figsize=(12, 6))
sns.barplot(x=abandonment_rate_by_reason.values, y=abandonment_rate_by_reason.index, palette="Reds")
plt.title('Call Abandonment Rate by Call Reason (Proxy)')
plt.xlabel('Abandonment Rate')
plt.ylabel('Primary Call Reason')
plt.tight_layout()
plt.show()

