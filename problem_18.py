bene = [{
    "name": "John Doe",
    "account_number": "12345678901",
    "ifsc_code": "HDFC0001234",
    "bank_name": "HDFC Bank",
    "account_type": "SAVINGS"
},
{"name": "Jane Doe", "account_number": "1234567", "ifsc_code": "HDFC0001234", "bank_name": "HDFC Bank", "account_type": "CURRENT"},
{"name": "Alice", "account_number": "12345678901", "ifsc_code": "ICIC123", "bank_name": "ICICI Bank", "account_type": "NRE"},]

def bene_validator(bene):
    error=[]
    if not bene["name"]:
        error.append("name cannot be empty")
    if len(bene["account_number"]) !=11:
        error.append("account number must be 11 digits")
    if len(bene["ifsc_code"]) !=11:
        error.append("IFSC code must be 11 characters")
    if not bene["bank_name"]:
        error.append("bank name cannot be empty")
    if bene["account_type"] not in ["SAVINGS", "CURRENT", "NRE", "NRO"]:
        error.append("account type must be SAVINGS, CURRENT, NRE, or NRO")
    if error:
        return("ERROR: " + ", ".join(error))
    else:
        return("Beneficiary details are valid")
    
for bene_list in bene:
    print(bene_validator(bene_list))