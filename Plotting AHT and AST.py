# Plotting AHT and AST by Call Reason, Time of Day, and Day of the Week
fig, axes = plt.subplots(1, 2, figsize=(14, 6))



#AHT and AST by Call Reason
aht_ast_by_reason[['AHT', 'AST']].plot(kind='bar', ax=axes[0], color=['#3498db', '#e74c3c'])
axes[0].set_title('AHT and AST by Call Reason')
axes[0].set_xlabel('Primary Call Reason')
axes[0].set_ylabel('Time (Minutes for AHT / Seconds for AST)')
axes[0].legend(['AHT', 'AST'])
axes[0].tick_params(axis='x', rotation=90)

#AHT and AST by Time of Day
aht_ast_by_hour.plot(ax=axes[1], color=['#2ecc71', '#e67e22'], marker='o')
axes[1].set_title('AHT and AST by Time of Day')
axes[1].set_xlabel('Hour of Day')
axes[1].set_ylabel('Time (Minutes for AHT / Seconds for AST)')
axes[1].legend(['AHT', 'AST'])

plt.tight_layout()
plt.show()
