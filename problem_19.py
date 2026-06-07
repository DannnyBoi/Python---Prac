fx_rate = [{
    "TXN_ID": "TX001",
    "currency_from": "INR",
    "currency_to": "USD",
    "rate": 83.5,
    "rate_type": "LIVE",
    "provider": "Reuters"
},
{
    "TXN_ID": "TX002",
    "currency_from": "",
    "currency_to": "EUR",
    "rate": 110,
    "rate_type": "Not_fixed",
    "provider": "XE"
},
{
    "TXN_ID": "TX003",
    "currency_from": "",
    "currency_to": "",
    "rate": 0,
    "rate_type": "not_fixed",
    "provider": "NA"
}
]
def validate_fx_rate(fx_rate):
    error = []
    if not fx_rate["currency_from"]:
        error.append("currency_from cannot be empty")
    if not fx_rate["currency_to"]:
        error.append("currency_to cannot be empty")
    if (fx_rate["rate"]) <= 0:
        error.append("rate must be greater than 0")
    if (fx_rate["rate_type"]) not in ("LIVE", "FIXED", "INDICATIVE"):
        error.append("rate_type must be one of — LIVE, FIXED, INDICATIVE")
    if (fx_rate["provider"]) not in ("Reuters", "Bloomberg", "XE"):
        error.append("provider must be one of — Reuters, Bloomberg, XE")
    if error:
        return((fx_rate["TXN_ID"]) + " : " +", ".join(error))
    else:
        return((fx_rate["TXN_ID"]) + " : Valid Fx rate")

for fx_rate_check in fx_rate:
    print(validate_fx_rate(fx_rate_check))
