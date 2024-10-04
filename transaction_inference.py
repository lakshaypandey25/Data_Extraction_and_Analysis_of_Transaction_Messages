from transaction_entity_extraction import extract_entities
from company_classifier import classify_company
from datetime import datetime

# Initialize a list to hold transaction data
transactions = []

def run_inference(message):
    entities = extract_entities(message)

    if not entities:
        return "Message format not recognized."

    if "company_name" in entities:
        company_category = classify_company(entities["company_name"])
        entities["company_category"] = company_category

    # Extract transaction amount and date from the message
    if "debited" in message:
        transaction_type = "debited"
        amount = float(entities["amount"])
        date = entities["date"]
    elif "credited" in message:
        transaction_type = "credited"
        amount = float(entities["amount"])
        date = entities["date"]
    else:
        return "Transaction type not recognized."

    # Append the transaction data to the list
    transactions.append({
        "date": date,
        "amount": amount,
        "transaction_type": transaction_type,
        "category": entities.get("company_category", "Unknown")
    })

    return entities

if __name__ == "__main__":
    debited_message = "ABC Bank Acct XX123 debited for Rs 1500.50 on 2024-09-30. SuperMarketXYZ credited. UPI: 123456789. Call 1800123456 for dispute."
    credited_message = "Dear Customer, Acct XX456 is credited with Rs 2000.00 on 2024-08-19 from John Doe. UPI: 987654321-XYZ Bank."

    result_debited = run_inference(debited_message)
    print("Result (Debited):", result_debited)

    result_credited = run_inference(credited_message)
    print("Result (Credited):", result_credited)

    # Now you can print or access the transactions for further processing
    print("All Transactions:", transactions)
