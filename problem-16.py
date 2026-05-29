user_profile = {
    "full_name": "Daniel Prakash",
    "age": 25,
    "mobile": "9876543210",
    "email": "daniel@gmail.com",
    "country": "India"
}

def user_profile_validator(fn, age, mob, email, country):
    error = []
    if not fn:
        error.append("full_name must not be empty")
    if age < 18 or age > 60:
        error.append("age must be between 18 and 60")
    if len(mob) != 10:
        error.append("mobile must be a 10-digit number")
    if "@" not in email or "." not in email:
        error.append("email must be a valid email address")
    if country not in ["India", "UAE", "USA", "UK"]:
        error.append("country must be India, UAE, USA, or UK")
    if error:
        return(", ".join(error))
    else:
        return("Valid user profile")

print(user_profile_validator(user_profile["full_name"], user_profile["age"], user_profile["mobile"], user_profile["email"], user_profile["country"]))

"""for i in user_profile:
    print(user_profile_validator(user_profile["full_name"], user_profile["age"], user_profile["mobile"], user_profile["email"], user_profile["country"]))"""