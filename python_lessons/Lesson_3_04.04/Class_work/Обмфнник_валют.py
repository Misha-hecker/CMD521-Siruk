# Користувач вводить валютну пару.
# Купити/Продати
# Суму
# у обмінника стандартна база сум для кожної валютної пари євро долар гривня
# зверху виводити курс валют



#-----> Переробити валюти на свої і обмінника i додати elif == 2: і додати змінну API у кожен choise і зробити щоб вигідно було обміннику 


import time
import requests
#My_aluts
uah = 100000
eur = 1000
usd = 1000
#Valuts_obmen
uah_obmen = 1000000
eur_obmen = 100000
usd_obmen = 100000
# Another zminni
choise = -1
a = False
API = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"
 
response = requests.get(API)
data = response.json()
 
 
for item in data:
    print(f"{item["ccy"]}|{item["base_ccy"]} {item["buy"]}|{item["sale"]} ")
while a != True:
    choise = int(input("\n1. Показати всю валюту обмінника\n 2. Показати свою валюту \n3. Додати валюту\n4. Ввести валютну пару\n5. Купити\n6. Продати\n7. Вихід\n ---> "))



    if choise == 1:
        print(f"\nГривні: {uah_obmen}\nЄвро: {eur_obmen}\nДолари: {usd_obmen}")



    elif choise == 2:
        print(f"\nГривні: {uah}\nЄвро: {eur}\nДолари: {usd}")



    elif choise == 3:
        chos = int(input("\n1. Додати гривні\n2. Додати євро\n3. Додати долари\n ---> "))
        if chos == 1:
            uah += int(input("Введіть кількість гривень: "))
        elif chos == 2:
            eur += int(input("Введіть кількість євро: "))
        elif chos == 3:
            usd += int(input("Введіть кількість доларів: "))
    


    elif choise == 4:
        pair = input("Введіть валютну пару EUR,USD,UAH (наприклад, EUR/USD): ")
        if pair == "EUR/USD":
            response = requests.get("https://api.exchangerate-api.com/v4/latest/EUR")
            data = response.json()
            rate = data["rates"]["USD"]
            print(f"Курс EUR/USD: {rate}")
        elif pair == "USD/UAH":
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
            data = response.json()
            rate = data["rates"]["UAH"]
            print(f"Курс USD/UAH: {rate}")
        elif pair == "EUR/UAH":
            response = requests.get("https://api.exchangerate-api.com/v4/latest/EUR")
            data = response.json()
            rate = data["rates"]["UAH"]
            print(f"Курс EUR/UAH: {rate}")
        else:
            print("Невірна валютна пара. Спробуйте ще раз.")
    


    elif choise == 5:
        buy_pair = input("Введіть валютну пару для купівлі EUR,USD,UAH (наприклад, EUR/USD): ")
        amount = float(input("Введіть суму для купівлі: "))
        if buy_pair == "EUR/USD":
            response = requests.get("https://api.exchangerate-api.com/v4/latest/EUR")
            data = response.json()
            rate = data["rates"]["USD"]
            cost = amount * rate
            if cost <= usd:
                usd -= cost
                eur += amount
                print(f"Ви купили {amount} EUR за {cost} USD.")
            else:
                print("Недостатньо доларів для купівлі.")
        elif buy_pair == "USD/UAH":
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
            data = response.json()
            rate = data["rates"]["UAH"]
            cost = amount * rate
            if cost <= uah:
                uah -= cost
                usd += amount
                print(f"Ви купили {amount} USD за {cost} UAH.")
            else:
                print("Недостатньо гривень для купівлі.")
        elif buy_pair == "EUR/UAH":
            response = requests.get("https://api.exchangerate-api.com/v4/latest/EUR")
            data = response.json()
            rate = data["rates"]["UAH"]
            cost = amount * rate
            if cost <= uah:
                uah -= cost
                eur += amount
                print(f"Ви купили {amount} EUR за {cost} UAH.")
            else:
                print("Недостатньо гривень для купівлі.")
        else:
            print("Невірна валютна пара. Спробуйте ще раз.")



    elif choise == 6:
        sell_pair = input("Введіть валютну пару для продажу EUR,USD,UAH (наприклад, EUR/USD): ")
        amount = float(input("Введіть суму для продажу: "))
        if sell_pair == "EUR/USD":
            response = requests.get("https://api.exchangerate-api.com/v4/latest/EUR")
            data = response.json()
            rate = data["rates"]["USD"]
            cost = amount * rate
            if amount <= eur:
                eur -= amount
                usd += cost
                print(f"Ви продали {amount} EUR за {cost} USD.")
            else:
                print("Недостатньо євро для продажу.")
        elif sell_pair == "USD/UAH":
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
            data = response.json()
            rate = data["rates"]["UAH"]
            cost = amount * rate
            if amount <= usd:
                usd -= amount
                uah += cost
                print(f"Ви продали {amount} USD за {cost} UAH.")
            else:
                print("Недостатньо доларів для продажу.")
        elif sell_pair == "EUR/UAH":
            response = requests.get("https://api.exchangerate-api.com/v4/latest/EUR")
            data = response.json()
            rate = data["rates"]["UAH"]
            cost = amount * rate
            if amount <= eur:
                eur -= amount
                uah += cost
                print(f"Ви продали {amount} EUR за {cost} UAH.")
            else:
                print("Недостатньо євро для продажу.")
        else:
            print("Невірна валютна пара. Спробуйте ще раз.")



    elif choise == 7:
        print("Вихід з програми...")
        time.sleep(1)
        a = True
        