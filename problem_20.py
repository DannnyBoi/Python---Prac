kyc_record = {
    "user_id": "USR001",
    "pan_status": "VERIFIED",
    "aadhaar_status": "PENDING",
    "selfie_status": "VERIFIED",
    "overall_status": "INCOMPLETE"
}

def validate_kyc(kyc_record):
    error = []
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
        return(kyc_record["user_id"] + " : " + ", ".join(error))
    else:
        return(kyc_record["user_id"] + " : Valid KYC")

print(validate_kyc(kyc_record))