apartments = []
do = -1
while do != 0:
    do = int(input( " \n\n\n 1. Додати квартиу \n 2. Видалити квартиру \n 3. Редагувати квартиру \n 4. Показати всі квартири \n 5. Показати найдешевшу \n 6. Показати найдорощу \n 7. Сортувати від найдешевшої до найдорощої \n 8. Сортувати від найдорощої до найдешевшої\n 0. Вихід \n"))


    if do == 1:
        kv = str(input ("Введіть назву квартири: "))
        zn = int(input ("Введіть ціну квартири: "))
        apartments.append ([kv,zn])
        print (apartments)


    elif do == 2:
        kv = str(input ("Введіть назву квартири для видалення: "))
        found = False
        for item in apartments:
            if item[0] == kv:
                apartments.remove(item)
                found = True
                print(f"Квартира {kv} була видалена")
                break
        if not found:
            print ("Такої квартири не істує")
            print (apartments)


    elif do == 3:
        target = input("Введіть назву для редагування: ")
        found = False
        for item in apartments:
            if item[0] == target:
                found = True
                ins = int(input("Що ви бажаєте змінити? \n 1.Ціну \n 2.Назву \n"))
                if ins == 1:
                    price = int(input("Введіть нову ціну: "))
                    item[1] = price
                    print("Wsye pvsytyj")
                elif ins == 2:
                    name = input("Введіть нову назву: ")
                    item[0] = name
                    print("Назву змінено")
                break 
        if not found:
            print("Квартиру не знайдено")


    elif do == 4:
        if not apartments:
            print("Список порожній")
        else:
            for item in apartments:
                print (f"{item[0]}")


    elif do == 5:
        if not apartments:
            print("Список порожній")
        else:
                cheap = min(apartments, key=lambda x: x[1])
                print (f"Найдешевша кваритра:{cheap[0]},{cheap[1]}")
    

    elif do == 6:
        if not apartments:
            print("Список порожній")
        else:
            cheap = max(apartments, key=lambda x: x[1])
            print (f"Найдорожча кваритра:{cheap[0]},{cheap[1]}")
    

    elif do == 7:
        if not apartments:
            print("Список порожній")
        else:
            apartments.sort(key=lambda x: x[1])
            for item in apartments:
                print(f"{item[0]}:{item[1]}")


    elif do == 8:
        if not apartments:
            print("Список поророжній")
        else:
            apartments.sort(key=lambda x: x[1], reverse=True)
            for item in apartments:
                print(f"{item[0]}:{item[1]}")
