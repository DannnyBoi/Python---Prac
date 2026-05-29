transactions = [
    {"txn_id": "TXN001", "amount": 25000, "sender_account": "12345678901", "receiver_account": "98765432101", "maker_id": "MKR001", "checker_id": "CHK001"},
    {"txn_id": "TXN002", "amount": -500, "sender_account": "12345678901", "receiver_account": "98765432101", "maker_id": "MKR001", "checker_id": "CHK001"},
    {"txn_id": "TXN003", "amount": 25000, "sender_account": "1234567", "receiver_account": "98765432101", "maker_id": "MKR001", "checker_id": "CHK001"},
    {"txn_id": "TXN004", "amount": 25000, "sender_account": "12345678901", "receiver_account": "12345678901", "maker_id": "MKR001", "checker_id": "CHK001"},
    {"txn_id": "TXN005", "amount": 25000, "sender_account": "12345678901", "receiver_account": "98765432101", "maker_id": "", "checker_id": "CHK001"},
    {"txn_id": "TXN006", "amount": 600000, "sender_account": "1234567", "receiver_account": "98765432101", "maker_id": "", "checker_id": ""},
]
def txn_check(tid, amt, sa, ra, mid, cid):
    error = []
    if amt <= 0 or amt > 500000:
        error.append("amount must be between 1 and 500000")
    if len(sa) != 11:
        error.append("sender_account must be 11 characters")
    if len(ra) != 11:
        error.append("receiver_account must be 11 characters")
    if not mid:
        error.append("maker_id must not be empty")
    if not cid:
        error.append("checker_id must not be empty")
    if sa == ra:
        error.append("sender and receiver account must not be the same")
    if error:
        return(tid + " - " + ", ".join(error))
    else:
        return(tid + " - Valid")
for i in transactions:
    print(txn_check(i["txn_id"], i["amount"], i["sender_account"], i["receiver_account"], i["maker_id"], i["checker_id"]))