kyc_records = [
    {"name": "Danny", "pan": "ABCDE1234F", "aadhaar": "123456789012", "age": 25},
    {"name": "Sarah", "pan": "", "aadhaar": "987654321012", "age": 22},
    {"name": "Mike", "pan": "XYZAB5678K", "aadhaar": "", "age": 17},
    {"name": "John", "pan": "PQRST9876L", "aadhaar": "456789123456", "age": 30},
    {"name": "Priya", "pan": "LMNOP4321Z", "aadhaar": "111222333444", "age": 16}
]
def func(na, pa, aad, age):
    if pa == "":
        return("FAIL - " + str(na) + " - PAN missing")
    elif len(pa) != 10:
        return("FAIL - " + str(na) + " - Invalid PAN format")
    elif aad == "":
        return("FAIL - " + str(na) + " - Aadhaar missing")
    elif len(aad) != 12:
        return("FAIL - " + str(na) + " - Invalid Aadhaar format")
    elif age < 18:
        return("FAIL - " + str(na) + " - Underage")
    else:
        return("PASS - " + str(na) + " - KYC Verified")

for record in kyc_records:
    na = record["name"]
    pa = record["pan"]
    aad = record["aadhaar"]
    age = record["age"]
    print(func(na, pa, aad, age))