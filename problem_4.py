users = [
    {"name": "Danny", "age": 25, "email": "danny@gmail.com"},
    {"name": "", "age": 17, "email": "test@gmail.com"},
    {"name": "John", "age": 30, "email": ""},
    {"name": "Sarah", "age": 22, "email": "sarah@gmail.com"},
    {"name": "Mike", "age": 15, "email": "mike@gmail.com"}
]
def valid(u_name, u_age, u_mail):
    if u_name == "":
        return("FAIL - Name cannot be empty")
    elif u_age < 18:
        return("FAIL - User is underage")
    elif u_mail == "":
        return("FAIL - Email cannot be empty")
    else:
        return("PASS - " + str(u_name) + " is registered")

for user in users:
    u_name = user["name"]
    u_age = user["age"]
    u_mail = user["email"]
    print(valid(u_name, u_age, u_mail))