# Problem 11 - Forex transaction batch validator

transactions = [
    {"transaction_id": "TXN001", "amount": 500, "currency": "USD", "status": "PENDING"},
    {"transaction_id": "TXN002", "amount": -100, "currency": "USD", "status": "PENDING"},
    {"transaction_id": "TXN003", "amount": 200, "currency": "YEN", "status": "PENDING"},
    {"transaction_id": "TXN004", "amount": 300, "currency": "GBP", "status": "COMPLETED"},
    {"transaction_id": "TXN005", "amount": 0, "currency": "EUR", "status": "PENDING"},
]
def func(txn, amt, curr, stat):
    error = []
    if amt <= 0:
        error.append("amount must be greater than 0")
    if curr not in ["USD", "GBP", "EUR"]:
        error.append("currency must be USD, GBP, or EUR")
    if stat != "PENDING":
        error.append("status must be PENDING")
    if error:
        return(txn + " - " + ", ".join(error))
    else:
        return(txn + " - No error")
for i in transactions:
    print(func(i["transaction_id"], i["amount"], i["currency"], i["status"]))