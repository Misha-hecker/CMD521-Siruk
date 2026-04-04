# # --- РОБОТА ЗІ СПИСКОМ (LIST) ---
# # Списки створюються за допомогою квадратних дужок []. Вони є змінюваними (mutable).
# programming_lang = ["Python", "C++", "Java"]

# # Метод .insert(індекс, значення) додає елемент у вказану позицію.
# # Додаємо "TypeSctipt" на позицію з індексом 1 (друге місце).
# programming_lang.insert(1, "TypeSctipt")

# # Додаємо "C++" на позицію з індексом 0 (самий початок).
# programming_lang.insert(0, "C++")

# # Індекс [-1] звертається до останнього елемента списку.
# # Тут ми замінюємо останній елемент ("Java") на рядок "Test".
# programming_lang[-1] = "Test"

# # Виводимо вміст списку та його тип (<class 'list'>).
# print(programming_lang, type(programming_lang))


# # --- РОБОТА З КОРТЕЖЕМ (TUPLE) ---
# # Кортежі створюються за допомогою круглих дужок (). Вони незмінювані (immutable).
# prog_lang = ("Python", "C++", "Java")

# # Наступний рядок закоментований, бо він викличе помилку TypeError.
# # Елементи кортежу не можна змінювати або перепризначати після створення.
# # prog_lang(0) = "TypeScript" 

# # Виводимо вміст кортежу та його тип (<class 'tuple'>).
# print(prog_lang, type(prog_lang))






# # --- РОБОТА З словником даних ---
# # Створюємо список, що містить словники з даними про користувачів
# person_list = [
#     {
#         "Id": 1,
#         "Name": "Stive",
#         "Surname": "Jobs",
#         "Age": 'N/A',
#     },
#     {
#         "Id": 2,
#         "Name": "Stive",
#         "Surname": "Balbor",
#         "Age": 69,
#     }
# ]

# # Цикл for проходить по кожному словнику (person) у списку person_list
# for person in person_list:
#     # Виводимо Id та Ім'я за допомогою f-рядка
#     # Зверніть увагу: ми звертаємося до значень за ключами "Id" та "Name"
#     print(f"{person['Id']} : {person['Name']} ")

# # Запитуємо у користувача Id, конвертуючи введене значення в ціле число (int)
# choice = int(input("Enter user Id: "))

# # Виводимо дані про користувача за індексом, який ввів користувач
# # ВАЖЛИВО: У програмуванні індексація починається з 0, тому:
# # Якщо ввести 0 — отримаєте Стіва Джобса (Id: 1)
# # Якщо ввести 1 — отримаєте Стіва Балбора (Id: 2)
# print(person_list[choice])




# programming_lang = ["Python", "C++", "Java"]
# programming_lang.insert(1, "TypeSctipt")
# programming_lang.insert(0, "C++")
# programming_lang[-1] = "Test"
# print(programming_lang, type(programming_lang))
# prog_lang = ("Python", "C++", "Java", "Python")
# print(prog_lang, type(prog_lang))
# person = {
#     "Name": "Bill",
#     "Surname": "Gates",
#     "Age": 65,
# }
# print(f"{person['Name']} : {person["Surname"]} : {person["Age"]} ")
# person['Age'] = 66
# print(f"{person['Name']} : {person["Surname"]} : {person["Age"]} ")
# print(type(person))

# # person_list = [
# #     {
# #         "Id": 0,
# #         "Name": "Bill",
# #         "Surname": "Gates",
# #         "Age": 65,
# #     },
# #     {
# #         "Id": 1,
# #         "Name": "Stive",
# #         "Surname": "Jobs",
# #         "Age": 'N/A',
# #     },
# #     {
# #         "Id": 2,
# #         "Name": "Stive",
# #         "Surname": "Balbor",
# #         "Age": 69,
# #     }
# # ]

# # for person in person_list:
# #     print(f"{person["Id"]} : {person["Name"]} ")

# # choice = int(input("Enter user Id: "))
# # print(person_list[choice]["Name"], person_list[choice]["Surname"])