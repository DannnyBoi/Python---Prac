sender = [{
    "sender_id": "SND001",
    "full_name": "Daniel Prakash",
    "dob": "2002-07-11",
    "nationality": "Indian",
    "account_status": "ACTIVE",
    "kyc_verified": True
},
{
    "sender_id": "SND002",
    "full_name": "",
    "dob": "2002-07-11",
    "nationality": "Indian",
    "account_status": "NA",
    "kyc_verified": True
},
{
    "sender_id": "",
    "full_name": "",
    "dob": "2002-07-11",
    "nationality": "NA",
    "account_status": "NA",
    "kyc_verified": False
}
]

def sender_validator(sender):
    error = []
    if sender["sender_id"]:
        send_id = sender["sender_id"]
    else:
        send_id = "UNKNOWN"
    
    if not sender["sender_id"]:
        error.append("sender_id cannot be empty")
    if not sender["full_name"]:
        error.append("full_name cannot be empty")
    if sender["nationality"] not in ("Indian", "American", "British", "Emirati"):
        error.append("nationality must be one of — Indian, American, British, Emirati")
    if sender["account_status"] not in ("ACTIVE", "SUSPENDED", "CLOSED"):
        error.append("account_status must be one of — ACTIVE, SUSPENDED, CLOSED")
    if not sender["kyc_verified"]:
        error.append("sender cannot transact")
    if error:
        return(send_id + " : " + ", ".join(error))
    else:
        return(send_id + " : Valid sender")

for sender_loop in sender:
    print(sender_validator(sender_loop))