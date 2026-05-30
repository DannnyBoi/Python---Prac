otp_attempts = [
    {"user": "Danny", "otp_entered": "123456", "otp_actual": "123456", "attempts": 1},
    {"user": "Sarah", "otp_entered": "654321", "otp_actual": "123456", "attempts": 2},
    {"user": "Mike", "otp_entered": "111111", "otp_actual": "111111", "attempts": 6},
    {"user": "John", "otp_entered": "", "otp_actual": "789456", "attempts": 1},
    {"user": "Priya", "otp_entered": "12345", "otp_actual": "123456", "attempts": 3}
]
def validate_otp(us, ota, ote, at):
    error = []
    if ote == "":
        error.append("OTP cannot be empty")
    if len(ote) != 6:
        error.append("Invalid OTP format")
    if at > 5:
        error.append("Account locked — too many attempts")
    if ota != ote:
        error.append("OTP mismatch")
    if error:
        return("FAIL - " + us + " - " + ", ".join(error))
    else:
        return("PASS - " + us + " - OTP verified successfully")

for attempt in otp_attempts:
    print(validate_otp(attempt["user"], attempt["otp_actual"], attempt["otp_entered"], attempt["attempts"]))