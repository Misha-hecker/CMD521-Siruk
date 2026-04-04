# Завдання:
# person_list = [
#     {"Id": 0, "Name": "Bill", "Surname": "Gates", "Age": 65},
#     {"Id": 1, "Name": "Steve", "Surname": "Jobs", "Age": 72},
#     {"Id": 2, "Name": "Steve", "Surname": "Ballmer", "Age": 69}
# ]

# Вивести всіх користувачів (Імена, призвіще
# Додати користувача)
# Видалити користувача
# Редагувати користувача

# Цикли, і ввід з клавіатури


import time

choise = -1
b = True

person_list = [

    {"Id": 0, "Name": "Bill", "Surname": "Gates", "Age": 65},

    {"Id": 1, "Name": "Steve", "Surname": "Jobs", "Age": 72},

    {"Id": 2, "Name": "Steve", "Surname": "Ballmer", "Age": 69}

]

while b == True:
    choise = int (input("\n1. Вивести всіх користувачів (Імена, призвіще)\n 2. Додати користувача\n 3. Видалити користувача\n 4. Редагувати користувача\n 0. Вихід\n Введіть число: "))

    if choise == 1:
        for person in person_list:
            print(f"{person['Id']} : {person['Name']} : {person['Surname']}")


    elif choise == 2:
        name = input("Введіть ім'я користувача:")
        surname = input("Введіть призвіще користувача:")
        age = int(input("Введіть вік користувача:"))
        new_person = {"Id": len(person_list), "Name": name, "Surname": surname, "Age": age}
        person_list.append(new_person)


    elif choise == 3:
        id_delete = int(input("Введіть Id користувача для видалення:"))
        if 0 <= id_delete < len(person_list):
            del person_list[id_delete]
        else:
            print("Невірний Id користувача.")


    elif choise == 4:
        id_edit = int(input("Введіть Id користувача для редагування:"))
        if 0 <= id_edit < len(person_list):
            name = input("Введіть нове ім'я користувача:")
            surname = input("Введіть нове призвіще користувача:")
            age = int(input("Введіть новий вік користувача:"))
            person_list[id_edit] = {"Id": id_edit, "Name": name, "Surname": surname, "Age": age}
        else:
            print("Невірний Id користувача.")


    elif choise == 0:
        time.sleep(3)
        print("Вихід з програми...")
        exit()