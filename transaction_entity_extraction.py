import re

# Define regex patterns for debited and credited messages
debited_pattern = re.compile(
    r'(?P<bank_name>\w+) Bank Acct XX(?P<account_number>\d{3}) debited for Rs (?P<amount>[\d.]+) on (?P<date>\d{4}-\d{2}-\d{2}). (?P<company_name>[\w\s]+) credited. UPI: (?P<upi_number>\d+). Call (?P<helpline_number>\d+) for dispute.'
)

credited_pattern = re.compile(
    r'Dear Customer, Acct XX(?P<account_number>\d{3}) is credited with Rs (?P<amount>[\d.]+) on (?P<date>\d{4}-\d{2}-\d{2}) from (?P<account_name>[\w\s]+). UPI: (?P<upi_number>\d+)-(?P<bank_name>\w+) Bank.'
)

def extract_entities(message):
    # Try debited message pattern
    debited_match = debited_pattern.search(message)
    if debited_match:
        return debited_match.groupdict()

    # Try credited message pattern
    credited_match = credited_pattern.search(message)
    if credited_match:
        return credited_match.groupdict()

    return None

if __name__ == "__main__":
    # Example debited and credited messages
    debited_message = "ABC Bank Acct XX123 debited for Rs 1500.50 on 2024-09-30. SuperMarketXYZ credited. UPI: 123456789. Call 1800123456 for dispute."
    credited_message = "Dear Customer, Acct XX456 is credited with Rs 2000.00 on 2024-08-19 from John Doe. UPI: 987654321-XYZ Bank."

    # Extract entities
    debited_entities = extract_entities(debited_message)
    credited_entities = extract_entities(credited_message)

    print("Debited Entities:", debited_entities)
    print("Credited Entities:", credited_entities)
