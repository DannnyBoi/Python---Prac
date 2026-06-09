transactions = [
    {"transaction_id": "TXN001", "amount": 50000, "transfer_type": "EXPRESS"},
    {"transaction_id": "TXN002", "amount": 30000},
    {"transaction_id": "TXN003", "amount": 20000, "transfer_type": "INVALID"}
]

def calculate_transaction_fee(calc):
    ttype = calc.get("transfer_type", "STANDARD")

    if ttype == "STANDARD":
        fee_amt = (calc["amount"] * 2)/100
        return(calc["transaction_id"] + " : " + ttype + " | Fee amount: " + str(fee_amt))
    elif ttype == "EXPRESS":
        fee_amt = (calc["amount"] * 4)/100
        return(calc["transaction_id"] + " : " + ttype + " | Fee amount: " + str(fee_amt))
    elif ttype == "SAME_DAY":
        fee_amt = (calc["amount"] * 6)/100
        return(calc["transaction_id"] + " : " + ttype + " | Fee amount: " + str(fee_amt))
    else:
        return(calc["transaction_id"] + " : Invalid transfer type")
    
for transfer_check in transactions:
    print(calculate_transaction_fee(transfer_check))


"""Just for my info:
When we give a parameter to a function, it acts like a temp storage while the function runs a loop; after that one run, the parameter gets cleared... 
for example, here when I run the for loop, transfer_check takes the first dict and stores values into calc(the function parameter) and hence we are calling calc throughout the function and not transaction....."""