users = [
    {"user_id": "USR001", "pan_number": "ABCDE1234F", "aadhaar_number": "123456789012", "kyc_status": "VERIFIED"},
    {"user_id": "USR002", "pan_number": "ABCDE123", "aadhaar_number": "123456789012", "kyc_status": "VERIFIED"},
    {"user_id": "USR003", "pan_number": "ABCDE1234F", "aadhaar_number": "12345678", "kyc_status": "VERIFIED"},
    {"user_id": "USR004", "pan_number": "ABCDE1234F", "aadhaar_number": "123456789012", "kyc_status": "PENDING"},
    {"user_id": "USR005", "pan_number": "XY1", "aadhaar_number": "9999", "kyc_status": "VERIFIED"},
]
def kyc_validator(us, pan, aad, kyc):
    error = []
    if len(pan) != 10:
        error.append("pan_number must be 10 characters")
    if len(aad) != 12:
        error.append("aadhaar_number must be 12 characters")
    if kyc != "VERIFIED":
        error.append("kyc_status must be VERIFIED")
    if error:
        return(us + " - " + ", ".join(error))
    else:
        return(us + " - Valid KYC")
for i in users:
    print(kyc_validator(i["user_id"], i["pan_number"], i["aadhaar_number"], i["kyc_status"]))