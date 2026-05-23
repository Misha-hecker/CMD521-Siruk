from src.functions import get_all_users, add_user, rm_user, change_user, show_user_by_surname

exit = False

while not exit:
    choice = input("\nChoose an option:\n1.Get all users\n2.Show user by surname\n3.Add user\n4.Remove user\n5.Change user\n0.Exit\n-----> ")

    if choice == '1':
        get_all_users()
    elif choice == '2':
        show_user_by_surname()
    elif choice == '3':
        iid = input("Enter ID: ")
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        email = input("Enter email: ")
        country = input("Enter country: ")
        city = input("Enter city: ")
        salary = input("Enter salary: ")
        add_user(iid, name, surname, email, country, city, salary)
    elif choice == '4':
        user_id = input("Enter user ID to remove: ")
        rm_user(user_id)
    elif choice == '5':
        change_user()
    elif choice == '0':
        exit = True
    else:
        print("Invalid choice. Please try again.")