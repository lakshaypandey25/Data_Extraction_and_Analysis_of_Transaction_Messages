import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from transaction_inference import run_inference
from datetime import datetime
from collections import defaultdict

# Initialize a list to hold transaction data
transactions = []

def aggregate_monthly_expenses(transactions):
    monthly_expenses = defaultdict(float)
    
    for transaction in transactions:
        date = datetime.strptime(transaction['date'], '%Y-%m-%d')
        if date.month == datetime.now().month and date.year == datetime.now().year:
            if transaction['transaction_type'] == 'debited':
                category = transaction['category']
                monthly_expenses[category] += transaction['amount']

    return monthly_expenses

def prepare_training_data(monthly_expenses_history):
    X, y = [], []
    
    for i in range(1, len(monthly_expenses_history)):
        X.append(monthly_expenses_history[i-1])
        y.append(monthly_expenses_history[i])
    
    return np.array(X), np.array(y)

def predict_next_month_expenses(monthly_expenses_history):
    categories = list(monthly_expenses_history[0].keys())
    model = LinearRegression()
    
    # Prepare training data
    X, y = prepare_training_data(monthly_expenses_history)
    
    # Fit model for each category
    predictions = {}
    for category in categories:
        model.fit(X, [entry[category] for entry in y])
        last_month_expenses = np.array([monthly_expenses_history[-1][category]]).reshape(1, -1)
        predictions[category] = model.predict(last_month_expenses)[0]

    return predictions

if __name__ == "__main__":
    # Example transaction messages
    debited_message = "ABC Bank Acct XX123 debited for Rs 1500.50 on 2024-09-30. SuperMarketXYZ credited. UPI: 123456789. Call 1800123456 for dispute."
    credited_message = "Dear Customer, Acct XX456 is credited with Rs 2000.00 on 2024-08-19 from John Doe. UPI: 987654321-XYZ Bank."

    # Run inference to extract entities and populate transactions
    result_debited = run_inference(debited_message)
    print("Result (Debited):", result_debited)

    result_credited = run_inference(credited_message)
    print("Result (Credited):", result_credited)

    # Aggregate monthly expenses
    current_month_expenses = aggregate_monthly_expenses(transactions)
    print("Current Month Expenses:", current_month_expenses)

    # Historical monthly expenses data (example)
    monthly_expenses_history = [
        {'Food': 1500, 'Clothes': 800, 'Electric appliances': 200},
        {'Food': 1600, 'Clothes': 900, 'Electric appliances': 250},
        {'Food': 1700, 'Clothes': 950, 'Electric appliances': 300},
        {'Food': 1800, 'Clothes': 1000, 'Electric appliances': 350},
        # Add more historical data as needed
    ]

    # Predict next month's expenses
    next_month_expenses = predict_next_month_expenses(monthly_expenses_history)
    print("Predicted Next Month Expenses:", next_month_expenses)
