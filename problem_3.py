responses = [
    {"endpoint": "login", "status": 200},
    {"endpoint": "transaction", "status": 500},
    {"endpoint": "kyc", "status": 404},
    {"endpoint": "dashboard", "status": 200},
    {"endpoint": "logout", "status": 401}
]
def test(res_end, res_stat):
    if res_stat == 200:
        return("PASS - " + res_end + " is working")
    else:
        return("FAIL - " + res_end + " has issue")

for api in responses:
    res_end = api["endpoint"]
    res_stat = api["status"]
    print(test(res_end, res_stat))