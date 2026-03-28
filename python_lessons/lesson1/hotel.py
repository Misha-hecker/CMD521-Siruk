

usernames = []
passwords = []
for i in range (3):
    login = input ("What is yout name?\n")
    if login == "":
        print ("Login cant be void")
        ex = input ("press ENTER to exit")
        exit()
    passw = int (input ("Write your password\n"))
    if passw < 1000:
        print ("password too small")
        ex = input ("press ENTER to exit")
        exit()
    elif passw >9999:
        print ("pasword too large")
        ex = input ("press ENTER to exit")
        exit()
    usernames.append (login)
    passwords.append (passw)

a = 0
while a == 0:
    login_user = input ("Write ypur login\n") 
    if login_user in usernames:
        index = usernames.index(login_user)
        correkt_password= passwords[index]
        if correkt_password in passwords:
            pasw_user = int( input ("Write your password:\n") )

            if pasw_user == correkt_password:
                print ("Login succes\n Welcome")
    else:
        print ("Login Eror")
