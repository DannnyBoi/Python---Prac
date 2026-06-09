users = [
    {"user_id": "USR001", "full_name": "Arjun Mehta", "kyc_status": "VERIFIED"},
    {"user_id": "USR002", "full_name": "Priya Nair"},
    {"user_id": "USR003", "full_name": "Ravi Kumar", "kyc_status": "REJECTED"},
    {"user_id": "USR004", "full_name": "Sneha Das", "kyc_status": "UNKNOWN"}
]

def validate_kyc_status(user_check):
    kyc = user_check.get("kyc_status", "PENDING")
    if kyc == "VERIFIED":
        return (user_check["user_id"] + " - " + user_check["full_name"] + " : " + kyc + " - Transfer allowed")
    if kyc == "PENDING":
        return (user_check["user_id"] + " - " + user_check["full_name"] + " : " + kyc + " - Transfer blocked — KYC pending")
    if kyc == "REJECTED":
        return (user_check["user_id"] + " - " + user_check["full_name"] + " : " + kyc + " - Transfer blocked — KYC rejected")
    else: 
        return(user_check["user_id"] + " - " + user_check["full_name"] + " : " + kyc + " - INVALID KYC STATUS")

for users_looped in users:
    print(validate_kyc_status(users_looped))