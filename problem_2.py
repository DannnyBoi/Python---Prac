HTTP_status_code = [200, 404, 500, 600]
for i in HTTP_status_code:
    if i == 200:
        print("API test passed")
    elif i == 404:
        print("Page not found")
    elif i == 500:
        print("Server Error - Raising bug")
    else:
        print("Unknown status code")