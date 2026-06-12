test_inputs = ["abc", "xyz", "5000"]

def retry_transfer(inp):
    max_attempt = 3
    attempt = 1
    success = False

    while attempt <= max_attempt:
        try:
            conv = float(inp[attempt - 1])
            print("Success")
            success = True
            break
        except:
            print("Attempt " + str(attempt) + " failed")
        attempt = attempt + 1

    if success == False:
        print("Transfer failed — max attempts reached")

retry_transfer(test_inputs)
















test_inputs = ["abc", "xyz", "5000"]

def xyz(inp):
    attempt = 1
    max_attempt = 3
    success = False
    while attempt <= max_attempt:
        try:
            conv = float(inp[attempt -1])
            print("Successful conversion on attempt " + str(attempt))
            success = True
            break
        except:
            print("Failed to convert on attempt " + str(attempt))
            attempt = attempt+1
        
    if success == False:
        print("Failed to convert")
xyz(test_inputs)




