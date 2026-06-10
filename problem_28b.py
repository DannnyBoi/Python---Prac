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
