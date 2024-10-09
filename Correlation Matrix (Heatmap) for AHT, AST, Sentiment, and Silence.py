plt.figure(figsize=(10, 6))

correlation_matrix = merged_df[['AHT', 'AST', 'average_sentiment', 'silence_percent_average']].corr()

sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5, vmin=-1, vmax=1)

plt.title('Correlation Matrix (AHT, AST, Sentiment, Silence)')

plt.tight_layout()

plt.show()
