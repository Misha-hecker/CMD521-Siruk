a = input ('what program u want to run: \n 1. cinema \n 2. calculator \n 3. fine \n')


if a == "1":
    age = int(input("what is your age?\n"))
    name = input("what is your name?\n")
    if age >= 60:
        price = 70
    elif age >= 12: 
        price = 100
    else: 
        price = 50
    print("enjoy the movie " + name)
    print("your price is " + str(price))


elif a == "2":
    number1 = int(input("number1:\n"))
    number2 = int(input("number2:\n"))
    if number1 > 0 and number2 > 0:
        print(number1 + number2)
    elif number1 < 0 and number2 < 0:
        print(number1 * number2)
    elif number1 > 0 and number2 < 0:
        print(number1 - number2)
    elif number1 < 0 and number2 > 0:
        print(number1 - number2)
    elif number1 == 0 or number2 == 0:
        print("zero")


elif a == "3":
    fine = float(input("what is your fine?\n"))
    if fine > 10000:
        print ("you would to pay fine " + str(fine * 0.1))
    elif fine >= 10000 and fine < 20000:
        print ("you would to pay fine " + str(fine * 0.15))
    elif fine > 20000:
        print ("you would to pay fine " + str(fine * 0.2))
    print ("Дякуємо що ви вибрали нас")


input("\n press enter to exit \n")
    
    