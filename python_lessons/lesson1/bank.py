PIN = int(input ("print your pin:\n"))
balance = int(1000)
a = 0
if PIN == 1234:
    print("access granted")
    while a != "4":
        choise = input("Choose operation:\n 1 - Check balance\n2 - Deposit\n3 - Withdraw\n4 - Exit\n")
        if choise == "1":
            print("your balance is " + str(balance))
        elif choise == "2":
            deposit = int(input("how much do you want to deposit?\n"))
            balance += deposit
            print("your new balance is " + str(balance))
        elif choise == "3":
            withdraw = int(input("how much do you want to withdraw?\n"))
            if withdraw > balance:
                print("you don't have enough money")
            else:
                balance -= withdraw
                print("your new balance is " + str(balance))
        elif choise == "4":
            print("good bye")
            break
elif PIN < 1234:
    print("PIN is too low")
elif PIN > 1234:
    print("PIN is too high")