import requests
 
'''Plus'''
 
 
def Plus(first: int, second: int):
    return first + second
 
 
'''Minus'''

def Minus(first: int, second: int):
    return first - second

'''Multiply'''
def Multiply(first: int, second: int):
    return first * second

'''Divide'''
def Divide(first: int, second: int):
    if second == 0:
        return "На нуль ділити не можна!"
    return first / second


'''Menu'''
# ("\n1. Плюс\n2. Мінус\n3. Множення\n4. Ділення\n0. Вихід\n------>  ")
def Menu():
    print("\n1. Плюс\n2. Мінус\n3. Множення\n4. Ділення\n0. Вихід\n")
    variable = int(input("---->: "))
    return variable