# import requests
 
# '''Plus'''
 
 
# def Plus(first: int, second: int):
#     return first + second
 
 
# '''Minus'''

# def Minus(first: int, second: int):
#     return first - second

# '''Multiply'''
# def Multiply(first: int, second: int):
#     return first * second

# '''Divide'''
# def Divide(first: int, second: int):
#     if second == 0:
#         return "На нуль ділити не можна!"
#     return first / second


# '''Menu'''
# # ("\n1. Плюс\n2. Мінус\n3. Множення\n4. Ділення\n0. Вихід\n------>  ")
# def Menu():
#     print("\n1. Плюс\n2. Мінус\n3. Множення\n4. Ділення\n0. Вихід\n")
#     variable = int(input("---->: "))
#     return variable

import requests

def Menu():
    print("\n" + "="*30)
    print("      USER MANAGER")
    print("="*30)
    print("1. Показати всіх користувачів")
    print("2. Додати нового")
    print("3. Редагувати користувача")
    print("4. Видалити користувача")
    print("5. Знайти за ID")
    print("6. Знайти найстаршого")
    print("7. Знайти найбільшу ЗП")
    print("0. Вихід")
    
    try:
        return int(input("\nОберіть дію: "))
    except ValueError:
        return -1

def users_id():
    try:
        return int(input("Введіть ID користувача: "))
    except ValueError:
        print("Помилка: ID має бути числом!")
        return -1