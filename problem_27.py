transaction_data = {
    "transaction_id": "TXN001",
    "status": "PENDING",
    "max_attempts": 3
}

def check_attempts(txn):
    attempts = 1

    while attempts <= txn["max_attempts"]:
        print("Number of attempts : " + str(attempts) + " - " + txn["transaction_id"] + " , " + txn["status"])
        attempts = attempts + 1
    print(txn["transaction_id"] + " — Maximum attempts reached — Transaction TIMED_OUT")
(check_attempts(transaction_data))