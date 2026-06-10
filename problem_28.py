"""transaction_data = {
    "transaction_id": "TXN001",
    "status": "PENDING",
    "max_attempts": 1
}

def poll_transaction_status(txn_data):
    attempt = 1
    status = txn_data["status"]

    while attempt <= txn_data["max_attempts"]:
        if attempt == 2:
            status = "COMPLETED"
            print(status + " : Transaction completed Successfully")
            break
        attempt = attempt + 1

    if status == "COMPLETED":
        pass
    else:
        print("Max attempts reached — Transaction TIMED_OUT")
    

poll_transaction_status(transaction_data)"""

















transaction_data = {
    "transaction_id": "TXN002",
    "status": "PENDING",
    "max_attempts": 2
}

def checker(check):
    attempt = 1
    status = check["status"]
    while attempt <= check["max_attempts"]:
        if attempt == 3:
            status = "COMPLETED"
            print("Transaction Completed")
            break
        attempt = attempt+1
    
    if status == "COMPLETED":
        pass
    else:
        print("Max attempts reached")

checker(transaction_data)


