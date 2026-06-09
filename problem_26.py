transactions = [
    {"transaction_id": "TXN001", "amount": 30000, "account_tier": "BASIC"},
    {"transaction_id": "TXN002", "amount": 80000},
    {"transaction_id": "TXN003", "amount": 150000, "account_tier": "SILVER"},
    {"transaction_id": "TXN004", "amount": 600000, "account_tier": "GOLD"},
    {"transaction_id": "TXN005", "amount": 10000, "account_tier": "PLATINUM"}
]
def validate_transaction_limit(txn):
    tier = txn.get("account_tier", "BASIC")
    if tier not in ("BASIC", "SILVER", "GOLD"):
        return(txn["transaction_id"]+ " : " + tier + " - Unknown Tier")
    if tier == "BASIC" and txn["amount"] <= 50000:
        return(txn["transaction_id"]+ " : " + "Transaction approved - " + tier +", " + str(txn["amount"]))
    elif tier == "SILVER" and txn["amount"] <= 200000:
        return(txn["transaction_id"]+ " : " + "Transaction approved - " + tier +", " + str(txn["amount"]))
    elif tier == "GOLD" and txn["amount"] <= 500000:
        return(txn["transaction_id"]+ " : " + "Transaction approved - " + tier +", " + str(txn["amount"]))
    else:
        return(txn["transaction_id"]+ " : " +"Transaction rejected — limit exceeded - " + tier +", " + str(txn["amount"]))
    
    


    
for txn_loop in transactions:
    print(validate_transaction_limit(txn_loop))