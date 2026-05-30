accounts = [
    {"account_no": "1234567890", "balance": 5000, "status": "ACTIVE", "type": "SAVINGS"},
    {"account_no": "987654321", "balance": -100, "status": "ACTIVE", "type": "CURRENT"},
    {"account_no": "", "balance": 10000, "status": "INACTIVE", "type": "SAVINGS"},
    {"account_no": "1122334455", "balance": 0, "status": "ACTIVE", "type": "SAVINGS"},
    {"account_no": "9988776655", "balance": 75000, "status": "BLOCKED", "type": "CURRENT"},
    {"account_no": "5544332211", "balance": 200, "status": "ACTIVE", "type": "SAVINGS"}
]
def validate_account(acc, bal, stat):
    error = []
    if acc == "":
        error.append("Account number missing")
    if len(acc) != 10:
        error.append("Invalid account number")
    if bal < 0:
        error.append("Invalid balance")
    if stat == "INACTIVE":
        error.append("Account inactive")
    if stat == "BLOCKED":
        error.append("Account blocked")
    if error:
        return("FAIL - " + acc + " - " + ", ".join(error))
    else:
        return("PASS - " + acc + " - Account valid")

for account in accounts:
    acc = account["account_no"]
    bal = account["balance"]
    stat = account["status"]
    print(validate_account(acc, bal, stat))