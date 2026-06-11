def attempt_transaction(transaction_data, user_input):
    try:
        user = transaction_data["user_id"]
        amount = float(user_input)
        print("Transaction processed successfully for " + user + " — Amount: " + str(amount))
    except ValueError:
        print("Invalid amount entered")
    except KeyError:
        print("Missing user ID in transaction data")
    finally:
        print("Transaction attempt logged for audit")

attempt_transaction({"user_id": "USR001"}, "7500")
attempt_transaction({"user_id": "USR001"}, "xyz")
attempt_transaction({}, "7500")
    