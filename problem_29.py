def validate_amount(check):
    try:
        amount = float(check)
        print("Valid amount: " + str(amount))
    except:
        print("Invalid input — please enter a numeric amount")

validate_amount("5000")
validate_amount("abc")
validate_amount("")