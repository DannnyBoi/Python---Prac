transactions = [
    {"id": "TXN001", "amount": 5000, "currency": "INR", "status": "PENDING"},
    {"id": "TXN002", "amount": 50, "currency": "USD", "status": "PENDING"},
    {"id": "TXN003", "amount": 150000, "currency": "INR", "status": "COMPLETED"},
    {"id": "TXN004", "amount": 1000, "currency": "", "status": "PENDING"},
    {"id": "TXN005", "amount": 0, "currency": "INR", "status": "PENDING"}
]
def txn(ids, amt, curr, stat):
    if amt <= 0:
        return("FAIL - " + str(ids) + " - Invalid amount")
    elif curr == "":
        return("FAIL - " + str(ids) + " - Currency missing")
    elif stat == "COMPLETED":
        return("SKIP - " + str(ids) + " - Already completed")
    elif curr == "INR" and amt > 100000:
        return("FAIL - " + str(ids) + " - Exceeds INR limit")
    else:
        return("PASS - " + str(ids) + " - Transaction valid")

for transaction in transactions:
    ids = transaction["id"]
    amt = transaction["amount"]
    curr = transaction["currency"]
    stat = transaction["status"]
    print(txn(ids, amt, curr, stat))