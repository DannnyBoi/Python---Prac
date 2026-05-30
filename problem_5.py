attempts = [
    {"username": "admin", "password": "Admin@1234", "attempts": 1},
    {"username": "maker", "password": "", "attempts": 2},
    {"username": "", "password": "Test@123", "attempts": 3},
    {"username": "checker", "password": "Check@123", "attempts": 6},
    {"username": "admin", "password": "wrongpass", "attempts": 4}
]
def check(us, passw, att):
    if us == "":
        return("FAIL - Username cannot be empty")
    elif passw == "":
        return("FAIL - Password cannot be empty")
    elif att > 5:
        return("FAIL - Account locked")
    else:
        return("PASS - " + str(us) + " logged in successfully")

for attempt in attempts:
    us = attempt["username"]
    passw = attempt["password"]
    att = attempt["attempts"]
    print(check(us, passw, att))