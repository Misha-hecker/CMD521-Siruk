from function import Menu, users_id

people_list = [
    {"id": 1, "name": "Bart", "surname": "Simpson", "age": 32, "role": "C++ Developer", "salary": 100500},
    {"id": 2, "name": "Homer", "surname": "Simpson", "age": 42, "role": "Software Engineer", "salary": 120000},
    {"id": 3, "name": "Lisa", "surname": "Simpson", "age": 10, "role": "Data Scientist", "salary": 90000},
    {"id": 4, "name": "Marge", "surname": "Simpson", "age": 38, "role": "Project Manager", "salary": 110000},
    {"id": 5, "name": "Maggie", "surname": "Simpson", "age": 2, "role": "Hacker-kid", "salary": 50000}
]

while True:
    variable = Menu()
    
    if variable == 1:
        print("\n--- Список всіх користувачів ---")
        for user in people_list:
            print(user)

    elif variable == 2:
        new_id = max([u["id"] for u in people_list], default=0) + 1
        new_user = {
            "id": new_id,
            "name": input("Введіть ім'я: "),
            "surname": input("Введіть прізвище: "),
            "age": int(input("Введіть вік: ")),
            "role": input("Введіть роль: "),
            "salary": int(input("Введіть зарплату: "))
        }
        people_list.append(new_user)
        print("Користувач доданий успішно!")

    elif variable == 3:
        user_id = users_id()
        for user in people_list:
            if user["id"] == user_id:
                user["name"] = input(f"Нове ім'я ({user['name']}): ")
                user["surname"] = input(f"Нове прізвище ({user['surname']}): ")
                user["age"] = int(input(f"Новий вік ({user['age']}): "))
                user["role"] = input(f"Нова роль ({user['role']}): ")
                user["salary"] = int(input(f"Нова зарплата ({user['salary']}): "))
                print("Дані оновлено!")
                break
        else:
            print("Користувач не знайдений.")

    elif variable == 4:
        user_id = users_id()
        for user in people_list:
            if user["id"] == user_id:
                people_list.remove(user)
                print("Користувача видалено.")
                break
        else:
            print("Користувач не знайдений.")
            
    elif variable == 5:
        user_id = users_id()
        found = False
        for user in people_list:
            if user["id"] == user_id:
                print(f"\nЗнайдено: {user}")
                found = True
                break
        if not found: print("Користувач не знайдений.")

    elif variable == 6:
        if people_list:
            oldest = max(people_list, key=lambda x: x['age'])
            print(f"\nНайстарший користувач: {oldest['name']} {oldest['surname']}, вік: {oldest['age']}")
        else:
            print("Список порожній.")

    elif variable == 7:
        if people_list:
            rich_user = max(people_list, key=lambda x: x['salary'])
            print(f"\nНайбільша ЗП: {rich_user['name']} {rich_user['surname']}, сума: {rich_user['salary']}")
        else:
            print("Список порожній.")

    elif variable == 0:
        print("Вихід з програми. Бувай!")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")