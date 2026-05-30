import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
import functions


def main():
    while True:
        choice = int(input('\nChoose an option \n 1. Import films \n 2. Import people \n 3. Show films \n 4. Show people \n 5. Show users (example) \n 6. Exit \n ----->'))
        if choice == 1:
            functions.import_films()
        elif choice == 2:
            functions.import_people()
        elif choice == 3:
            functions.show_table('Films')
        elif choice == 4:
            functions.show_table('People')
        elif choice == 5:
            functions.get_all_users()
        elif choice == 6:
            break
        else:
            print('Unknown option')


if __name__ == '__main__':
    main()