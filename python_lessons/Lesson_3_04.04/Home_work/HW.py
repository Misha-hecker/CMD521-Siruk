import time
import requests

# Баланс користувача
uah = 100000.0
eur = 1000.0
usd = 1000.0

# Баланс обмінника
uah_obmen = 1000000.0
eur_obmen = 100000.0
usd_obmen = 100000.0

API = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"
current_api = API
a = False
res = []

try:
    response = requests.get(current_api)
    res = response.json()
    print("--- КУРС ВАЛЮТ ВІД ПРИВАТБАНКУ ---")
    for item in res:
        print(f"{item['ccy']}/{item['base_ccy']} | Купівля: {item['buy']} | Продаж: {item['sale']}")
except Exception as e:
    print(f"Помилка підключення до API: {e}")

while a != True:
    choice = int(input("\n1.Валюта обмінника\n2.Валюта користувача\n3. Нарахувати собі валюту\n4. Переглянути курс конкретної пари\n5. Купити у обмінника\n6. Продати обміннику\n7. Вихід\n ---> "))
    
    if choice == 1:
        print(f"\n[ОБМІННИК]\n Гривні: {uah_obmen} \n Євро: {eur_obmen} \n Долари: {usd_obmen}")

    elif choice == 2:
        print(f"\n[МІЙ ГАМАНЕЦЬ]\n Гривні: {uah} \n Євро: {eur} \n Долари: {usd}")

    elif choice == 3:
        print("\n1. Гривні\n2. Євро\n3. Долари")
        chos = int(input(" ---> "))
        amount_to_add = float(input("Введіть суму: "))
        if chos == 1: uah += amount_to_add
        elif chos == 2: eur += amount_to_add
        elif chos == 3: usd += amount_to_add

    elif choice == 4:
        pair = input("Яка валюта цікавить? (USD/EUR): ").upper()
        found = False
        for item in res:
            if item['ccy'] == pair:
                print(f"Курс {item['ccy']}: Ви купуєте за {item['sale']}, Ви продаєте за {item['buy']}")
                found = True
        if not found: print("Валюту не знайдено.")

    elif choice == 5:
        buy_val = input("Яку валюту хочете купити? (USD/EUR): ").upper()
        amount = float(input(f"Скільки {buy_val} купуєте? "))
        
        for item in res:
            if item['ccy'] == buy_val:
                rate = float(item['sale'])
                cost = amount * rate
                
                if uah >= cost:
                    if buy_val == "USD" and usd_obmen >= amount:
                        uah -= cost; uah_obmen += cost
                        usd += amount; usd_obmen -= amount
                        print(f"Успішно! Куплено {amount} USD за {cost:.2f} UAH")
                    elif buy_val == "EUR" and eur_obmen >= amount:
                        uah -= cost; uah_obmen += cost
                        eur += amount; eur_obmen -= amount
                        print(f"Успішно! Куплено {amount} EUR за {cost:.2f} UAH")
                    else:
                        print("В обміннику немає стільки валюти!")
                else:
                    print(f"У вас недостатньо гривень! Треба {cost:.2f} UAH")

    elif choice == 6:
        sell_val = input("Яку валюту хочете продати? (USD/EUR): ").upper()
        amount = float(input(f"Скільки {sell_val} продаєте? "))
        
        for item in res:
            if item['ccy'] == sell_val:
                rate = float(item['buy'])
                total_receive = amount * rate
                
                if sell_val == "USD" and usd >= amount:
                    if uah_obmen >= total_receive:
                        usd -= amount; usd_obmen += amount
                        uah += total_receive; uah_obmen -= total_receive
                        print(f"Успішно! Продано {amount} USD, отримано {total_receive:.2f} UAH")
                elif sell_val == "EUR" and eur >= amount:
                    if uah_obmen >= total_receive:
                        eur -= amount; eur_obmen += amount
                        uah += total_receive; uah_obmen -= total_receive
                        print(f"Успішно! Продано {amount} EUR, отримано {total_receive:.2f} UAH")
                else:
                    print("Недостатньо валюти у вас або гривень в обміннику!")

    elif choice == 7:
        print("Вихід...")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        a = True