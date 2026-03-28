
usernames = []
passwords = []

print("Write 3 users")

for i in range(3):
    login = input("Print login")
    i+1
    
    if login == "":
        print("Username cannot be empty")
        input("Press ENTER for exit")
        exit()

    passw = int(input("Write password: \n(1000-9999)\n "))
    
    if passw < 1000:
        print("password too small")
        input("Press ENTER for exit")
        exit()
    elif passw > 9999:
        print("Password too large")
        input("Press ENTER for exit")
        exit()
        
    usernames.append(login)
    passwords.append(passw)
    print("Login succes\n")

access_granted = 0

while not access_granted:
    login_user = input("write your login")
    
    if login_user in usernames:
        index = usernames.index(login_user)
        correct_password = passwords[index]
        passw_user = int(input("write your password: "))
            
        if passw_user == correct_password:
            print("Login successful\nWelcome!")
            access_granted = 1
        elif passw_user > correct_password:
            print("Password too large")
        else:
            print("Password too small")
            
    else:
        print("User not found")

        