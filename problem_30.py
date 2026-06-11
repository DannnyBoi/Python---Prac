def process_transaction(transaction_data, user_input):
    try:
        amt = float(user_input)
        uid = transaction_data["user_id"]
        print("Processing transaction for " + uid + " : " + str(amt))
    except ValueError:
        print("Invalid amount — please enter a numeric value")
    except KeyError:
        print("Transaction data missing user ID")
process_transaction({"user_id": "USR001"}, "5000")
process_transaction({"user_id": "USR001"}, "abc")
process_transaction({}, "5000")