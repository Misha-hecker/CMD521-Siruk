a = input("what program u want to run? \n 1. calculator \n 2. who older \n 3. positive/negative \n 4 Hello user \n 5. запитує 2 числа -якщо перше число більше другого → вивести їх суму -якщо менше → вивести різницю -якщо рівні → вивести 'Numbers are equal'")
if a == "1":
    index = input("+ - * /:\n")
    nuber1 = int(input("number1:\n"))
    nuber2 = int(input("number2:\n"))
    if index == "+":
        print(nuber1 + nuber2)
    elif index == "-":
        print(nuber1 - nuber2)
    elif index == "*":
        print(nuber1 * nuber2)
    elif index == "/":
        print(nuber1 / nuber2)
    else:
        print("wrong syntax")
elif a == "2":
    age1 = int(input("age1:\n"))
    age2 = int(input("age2:\n"))
    if age1 > age2:
        print("age1 is older")
    elif age1 < age2:
        print("age2 is older")
    else:
        print("they are the same age")
elif a == "3":
    number = int(input("number:\n"))
    if number > 0:
        print("positive")
    elif number < 0:
        print("negative")
    else:
        print("zero")
elif a == "4":
    name = input("what is your name?\n")
    old = input("what is your age?\n")
    print("hello " + name + " you are " + old + " years old")
elif a == "5":
    number1 = int(input("number1:\n"))
    number2 = int(input("number2:\n"))
    if number1 > number2:
        print(number1 + number2)
    elif number1 < number2:
        print(number1 - number2)
    else:
        print("Numbers are equal")
input("press enter to exit")