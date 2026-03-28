username = input("Enter your name: ")

if username == "":
    print("Username cannot be empty")
    exit()

password = int(input("Enter your password (number): "))

if password < 1000:
    print("Weak password")
    exit()

login_username = input("Enter your name to login: ")

if login_username == "":
    print("Username cannot be empty")
    exit()

login_password = int(input("Enter your password to login: "))

if login_username != username:
    print("User not found")
elif login_password == password:
    print("Login successful")
elif login_password > password:
    print("Password too large")
else:
    print("Password too small")
