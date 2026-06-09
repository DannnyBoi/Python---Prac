transactions = [
    {"transaction_id": "TXN001", "purpose": "Medical"},
    {"transaction_id": "TXN002"},
    {"transaction_id": "TXN003", "purpose": "Tourism"}
]

def validate_transfer_purpose(transactions):
    purpose = transactions.get("purpose", "Family Remittance")

    if purpose not in ("Family Remittance", "Medical", "Education", "Business"):
        return (transactions["transaction_id"] + " - " + purpose + " : Invalid purpose code")
    else:
        return(transactions["transaction_id"] + " - " + purpose + " : Valid purpose code")

for txn in transactions:
    print(validate_transfer_purpose(txn))