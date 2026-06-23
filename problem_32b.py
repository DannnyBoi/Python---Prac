print("Self trial")

test_inputs = ["abcd", "xyz", "5000"]

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
