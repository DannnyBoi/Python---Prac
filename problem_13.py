beneficiaries = [
    {"ben_id": "BEN001", "account_number": "12345678901", "ifsc_code": "HDFC0001234", "bank_name": "HDFC Bank", "transfer_limit": 50000},
    {"ben_id": "BEN002", "account_number": "1234567", "ifsc_code": "HDFC0001234", "bank_name": "HDFC Bank", "transfer_limit": 50000},
    {"ben_id": "BEN003", "account_number": "12345678901", "ifsc_code": "ICIC123", "bank_name": "ICICI Bank", "transfer_limit": 50000},
    {"ben_id": "BEN004", "account_number": "12345678901", "ifsc_code": "AXIS0001234", "bank_name": "", "transfer_limit": 50000},
    {"ben_id": "BEN005", "account_number": "12345678901", "ifsc_code": "SBIN0001234", "bank_name": "SBI", "transfer_limit": 150000},
    {"ben_id": "BEN006", "account_number": "1234567", "ifsc_code": "SBIN123", "bank_name": "", "transfer_limit": 0},
]
def bene_check(bid, acc, ifsc, bn, tl):
    error = []
    if len(acc) != 11:
        error.append("account_number must be 11 characters")
    if len(ifsc) != 11:
        error.append("ifsc_code must be 11 characters")
    if len(bn) == 0:
        error.append("bank_name must not be empty")
    if tl <= 0 or tl > 100000:
        error.append("transfer_limit must be between 1 and 100000")
    if error:
        return(bid + " - " + ", ".join(error))
    else:
        return(bid + " - Valid")
for i in beneficiaries:
    print(bene_check(i["ben_id"], i["account_number"], i["ifsc_code"], i["bank_name"], i["transfer_limit"]))