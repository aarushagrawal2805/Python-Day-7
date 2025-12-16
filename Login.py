#Simple Login Validation
try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != "admin" or password != "1234":
        raise Exception("Invalid login")
    print("Login successful")
except Exception as e:
    print(e)
