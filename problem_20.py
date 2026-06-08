kyc_record = [{
    "user_id": "USR001",
    "pan_status": "VERIFIED",
    "aadhaar_status": "PENDING",
    "selfie_status": "VERIFIED",
    "overall_status": "INCOMPLETE"
},
{
    "user_id": "USR002",
    "pan_status": "VERIFIED",
    "aadhaar_status": "NA",
    "selfie_status": "VERIFIED",
    "overall_status": "NA"
},
{ "user_id": "",
    "pan_status": "NA",
    "aadhaar_status": "NA",
    "selfie_status": "NA",
    "overall_status": "NA"
}
]
def validate_kyc(kyc_record):
    error = []
    if kyc_record["user_id"]:
        user_display = kyc_record["user_id"]
    else:
        user_display = "UNKNOWN"

    if not kyc_record["user_id"]:
        error.append("user_id cannot be empty")
    if kyc_record["pan_status"] not in ("VERIFIED", "PENDING", "REJECTED"):
        error.append("pan_status must be one of — VERIFIED, PENDING, REJECTED")
    if kyc_record["aadhaar_status"] not in ("VERIFIED", "PENDING", "REJECTED"):
        error.append("aadhaar_status must be one of — VERIFIED, PENDING, REJECTED")
    if kyc_record["selfie_status"] not in ("VERIFIED", "PENDING", "REJECTED"):
        error.append("selfie_status must be one of — VERIFIED, PENDING, REJECTED")
    if kyc_record["overall_status"] not in ("COMPLETE", "INCOMPLETE", "UNDER_REVIEW"):
        error.append("overall_status must be one of — COMPLETE, INCOMPLETE, UNDER_REVIEW")
    
    if error:
        return(user_display + " : " + ", ".join(error))
    else:
        return(user_display + " : Valid KYC")

for kyc_check in kyc_record:
    print(validate_kyc(kyc_check))