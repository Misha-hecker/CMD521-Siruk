import pyodbc
import os
from dotenv import load_dotenv

load_dotenv(override=True)

# Define connection parameters
server = os.getenv('SERVER')
database = os.getenv('DATABASE')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')


# Create the connection string
# For Windows Authentication, use: Trusted_Connection=yes;
conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;'

def get_all_users():
    try:
        # Establish connection
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            # Execute a query
            cursor.execute(
                "SELECT ID, name, surname, email, country, city, salary FROM Users")

            # Fetch results
            for row in cursor.fetchall():
                print(row)

    except Exception as e:
        print(f"Error: {e}")

def add_user(name, surname, email, country, city, salary):
    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Users (name, surname, email, country, city, salary)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, surname, email, country, city, salary))
            conn.commit()
            print("User added successfully.")
    except Exception as e:
        print(f"Error: {e}")

def rm_user(ID):
    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Users WHERE ID = ?", (ID,))
            conn.commit()
            print("User removed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def change_user():
    a = input("Enter the ID of the user you want to change: ")
    b = input("What do you want to change?\n (1:name, 2:surname, 3:email, 4:country, 5:city, 6:salary)\n ----->")
    if b == '1':
        c = input("Enter the new name: ")
        try:
            with pyodbc.connect(conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE Users SET name = ? WHERE ID = ?", (c, a))
                conn.commit()
                print("User updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
    elif b == '2':
        c = input("Enter the new surname: ")
        try:
            with pyodbc.connect(conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE Users SET surname = ? WHERE ID = ?", (c, a))
                conn.commit()
                print("User updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
    elif b == '3':
        c = input("Enter the new email: ")
        try:
            with pyodbc.connect(conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE Users SET email = ? WHERE ID = ?", (c, a))
                conn.commit()
                print("User updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
    elif b == '4':
        c = input("Enter the new country: ")
        try:
            with pyodbc.connect(conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE Users SET country = ? WHERE ID = ?", (c, a))
                conn.commit()
                print("User updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
    elif b == '5':
        c = input("Enter the new city: ")
        try:
            with pyodbc.connect(conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE Users SET city = ? WHERE ID = ?", (c, a))
                conn.commit()
                print("User updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
    elif b == '6':
        c = input("Enter the new salary: ")
        try:
            with pyodbc.connect(conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE Users SET salary = ? WHERE ID = ?", (c, a))
                conn.commit()
                print("User updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid choice. Please try again.")


def show_user_by_surname():
    surname = input("Enter the surname of the user you want to show: ")
    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT ID, name, surname, email, country, city, salary FROM Users WHERE surname = ?", (surname,))
            for row in cursor.fetchall():
                print(row)
    except Exception as e:
        print(f"Error: {e}")
