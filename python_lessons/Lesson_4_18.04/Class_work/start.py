# import requests

# API = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"
# API2 = "https://api.privatbank.ua/p24api/exchange_rates?date=01.12.2014"

# def get_data(API):

#     data = requests.get(API).json()
#     return data


# currancy = get_data(API)
# print(currancy)
# print("==============================")
# archive = get_data(API2)
# print(archive)


from function import Plus, Minus, Multiply, Divide, Menu
variable = -1
a = False
while a == False:
    
    variable = Menu()

    if variable == 1:
        first = int(input("Введіть перше число: "))
        second = int(input("Введіть друге число: "))
        print(Plus(first, second))
    elif variable == 2:
        first = int(input("Введіть перше число: "))
        second = int(input("Введіть друге число: "))
        print(Minus(first, second))
    elif variable == 3:
        first = int(input("Введіть перше число: "))
        second = int(input("Введіть друге число: "))
        print(Multiply(first, second))
    elif variable == 4:
        first = int(input("Введіть перше число: "))
        second = int(input("Введіть друге число: "))
        print(Divide(first, second))
    elif variable == 0:
        a = True
    else:
        print("Невірний вибір. Спробуйте ще раз.")