transaction_fee = {
    "txn_id": "TX001",
    "txn_amount": 50000,
    "fee_percentage": 1.5,
    "fee_amount": 750.0,
    "fee_type": "FIXED"
}

def txn_fee_validator(transaction_fee):
    error = []
    if transaction_fee["txn_id"]:
        id = transaction_fee["txn_id"]
    else:
        id = "UNKNOWN"
    
    if not transaction_fee["txn_id"]:
        error.append("txn_id cannot be empty")
    if transaction_fee["txn_amount"] <= 0:
        error.append("txn_amount must be greater than 0")
    if transaction_fee["fee_percentage"] <= 0.1 and transaction_fee["fee_percentage"] >= 5:
        error.append("fee_percentage must be between 0.1 and 5.0")
    if transaction_fee["fee_amount"] != (transaction_fee["txn_amount"] * transaction_fee["fee_percentage"])/100:
        error.append("fee_amount must equal txn_amount multiplied by fee_percentage divided by 100")
    if transaction_fee["fee_type"] not in ("FIXED", "PERCENTAGE", "HYBRID"):
        error.append("fee_type must be one of — FIXED, PERCENTAGE, HYBRID")
    if error:
        return(id + " : " + "; ".join(error))
    else:
        return(id + " : Valid fee")

print(txn_fee_validator(transaction_fee))