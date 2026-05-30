transaction = [{
    "sender": "Daniel Prakash",
    "amount": 50000,
    "currency": "USD",
    "transaction_type": "WIRE"
},
{"sender": "Pramoth", "amount": 500, "currency": "USD", "transaction_type": "WIRE"},
{"sender": "Deepsiksh", "amount": 250000, "currency": "AED", "transaction_type": "SWIFT"},
{"sender": "", "amount": 150000, "currency": "EUR", "transaction_type": "NEFT"},
{"sender": "John Doe", "amount": 50000, "currency": "GBP", "transaction_type": "RTGS"},
{"sender": "Jane Doe", "amount": 200000, "currency": "USD", "transaction_type": "WIRE"},
]
def limit_validator(transaction):
    error = []
    if not transaction["sender"]:
        error.append("sender must not be empty")
    if transaction["amount"] < 1000 or transaction["amount"] > 200000:
        error.append("amount must be between 1000 and 200000")
    if transaction["currency"] not in ["USD", "AED", "EUR", "GBP"]:
        error.append("currency must be USD, AED, EUR, or GBP")
    if transaction["transaction_type"] not in ["WIRE", "SWIFT", "NEFT","RTGS"]:
        error.append("transaction_type must be WIRE, SWIFT, NEFT, or RTGS")
    if error:
        return(transaction["sender"] + " - " + ", ".join(error))
    else:
        return(transaction["sender"]    + " - Transaction is valid")

for txn in transaction:
    print(limit_validator(txn))


