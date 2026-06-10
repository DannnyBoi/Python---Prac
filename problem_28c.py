transaction_data = {
    "transaction_id": "TXN003",
    "status": "PENDING",
    "max_attempts": 4
}
def track_failed_attempts(checks):
    failed_attempts=[]
    attempt = 1
    while attempt <= checks["max_attempts"]:
        failed_attempts.append("Attempt " + str(attempt))
        attempt = attempt+1

    if failed_attempts:
         print(", " .join(failed_attempts))
    print(checks["transaction_id"]+ " : Max attempts reached - TIMED_OUT")

track_failed_attempts(transaction_data)