import pandas as pd
import matplotlib.pyplot as plt
from transaction_inference import transactions  # Import the transactions list from inference.py

# Create a DataFrame from the transactions list
df = pd.DataFrame(transactions)

# Convert the date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Group by date and transaction type, summing the amounts
daily_totals = df.groupby(['date', 'transaction_type']).sum().reset_index()

# Create separate DataFrames for debited and credited transactions
debited_totals = daily_totals[daily_totals['transaction_type'] == 'debited']
credited_totals = daily_totals[daily_totals['transaction_type'] == 'credited']

# Plotting the line graph
plt.figure(figsize=(10, 6))
plt.plot(debited_totals['date'], debited_totals['amount'], label='Debited Amount', marker='o')
plt.plot(credited_totals['date'], credited_totals['amount'], label='Credited Amount', marker='o')
plt.title('Debited and Credited Amounts vs Date')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.xticks(rotation=45)
plt.legend(title='Transaction Type')
plt.tight_layout()
plt.savefig("debited_credited_amounts_vs_date.png")
plt.show()
