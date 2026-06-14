# Problem 33 - Remit4Me KYC Retry System

test_inputs = ["abc", "KYC001", "xyz"]

def kyc_retry(inp, max_attempts=3):
    attempt = 1
    success = False

    while attempt <= max_attempts:
        try:
            if not inp[attempt - 1].isdigit():
                raise ValueError("Invalid KYC ID")
            print("KYC verified on attempt " + str(attempt))
            success = True
            break
        except ValueError:
            print("Attempt " + str(attempt) + " failed")
        attempt = attempt + 1

    if success == False:
        print("KYC verification failed — max attempts reached")

kyc_retry(test_inputs)