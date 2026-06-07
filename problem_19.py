fx_rate = {
    "TXN_ID": "TX001",
    "currency_from": "INR",
    "currency_to": "USD",
    "rate": 83.5,
    "rate_type": "LIVE",
    "provider": "Reuters"
}

def validate_fx_rate(fx_rate):
    error = []
    if not len(fx_rate["currency_from"]):
        error.append("currency_from cannot be empty")
    if not len(fx_rate["currency_to"]):
        error.append("currency_to cannot be empty")
    if (fx_rate["rate"]) <= 0:
        error.append("rate must be greater than 0")
    if (fx_rate["rate_type"]) not in ("LIVE", "FIXED", "INDICATIVE"):
        error.append("rate_type must be one of — LIVE, FIXED, INDICATIVE")
    if (fx_rate["provider"]) not in ("Reuters", "Bloomberg", "XE"):
        error.append("provider must be one of — Reuters, Bloomberg, XE")
    if error:
        return((fx_rate["TXN_ID"]) + " : " ", ".join(error))
    else:
        return("Valid Fx rate")

"""for fx_rate_check in fx_rate:
    print(fx_rate_checker(validate_fx_rate))"""

print(validate_fx_rate(fx_rate))