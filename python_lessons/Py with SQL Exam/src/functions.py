import pyodbc
import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

# Define connection parameters
server = os.getenv('SERVER')
database = os.getenv('DATABASE')
username = os.getenv('DB_USERNAME') or os.getenv('USERNAME')
password = os.getenv('DB_PASSWORD') or os.getenv('PASSWORD')
encrypt = os.getenv('ENCRYPT', 'yes')
trust_server_certificate = os.getenv('TRUST_SERVER_CERTIFICATE', 'yes')


# For Windows Authentication, use: Trusted_Connection=yes;
CONNECTION_STRING = (
    f'DRIVER={{ODBC Driver 18 for SQL Server}};'
    f'SERVER={server};DATABASE={database};UID={username};PWD={password};'
    'TrustServerCertificate=yes;Encrypt=yes'
)


def _fetch_swapi(url):
    """Generator that fetches paginated SWAPI-like endpoints and yields results."""
    while url:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        data = resp.json()

        if isinstance(data, list):
            for item in data:
                yield item
            break

        if isinstance(data, dict):
            results = (
                data.get('results')
                or data.get('docs')
                or data.get('films')
                or data.get('people')
                or data.get('items')
                or data.get('data')
            )

            if isinstance(results, list):
                for item in results:
                    yield item
            elif isinstance(data, dict) and not results:
                yield data

            url = data.get('next') or data.get('nextPage') or data.get('next_url')
            continue

        break


def _ensure_people_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'People')
    CREATE TABLE People (
        name NVARCHAR(255) PRIMARY KEY,
        height NVARCHAR(50),
        mass NVARCHAR(50),
        gender NVARCHAR(50)
    )
    """)
    conn.commit()


def _ensure_films_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Films')
    CREATE TABLE Films (
        title NVARCHAR(255) PRIMARY KEY,
        director NVARCHAR(255),
        release_date NVARCHAR(50)
    )
    """)
    conn.commit()


def import_people(url="https://swapi.info/api/people"):
    """Import people from SWAPI-style endpoint. Writes only name, height, mass, gender.
    Skips rows where a person with same name already exists.
    """
    try:
        with pyodbc.connect(CONNECTION_STRING) as conn:
            _ensure_people_table(conn)
            cursor = conn.cursor()

            added = 0
            for person in _fetch_swapi(url):
                if not isinstance(person, dict):
                    continue

                name = person.get('name')
                height = person.get('height')
                mass = person.get('mass')
                gender = person.get('gender')

                if not name:
                    continue

                cursor.execute("SELECT 1 FROM People WHERE name = ?", (name,))
                if cursor.fetchone():
                    continue

                cursor.execute(
                    "INSERT INTO People (name, height, mass, gender) VALUES (?, ?, ?, ?)",
                    (name, height, mass, gender),
                )
                added += 1

            conn.commit()
            print(f"Imported people: {added}")

    except Exception as e:
        print(f"Error importing people: {e}")


def import_films(url="https://swapi.info/api/films"):
    try:
        with pyodbc.connect(CONNECTION_STRING) as conn:
            _ensure_films_table(conn)
            cursor = conn.cursor()

            added = 0
            for film in _fetch_swapi(url):
                if not isinstance(film, dict):
                    continue

                title = film.get('title') or film.get('name')
                director = film.get('director')
                release = film.get('release_date') or film.get('release')

                if not title:
                    continue

                cursor.execute("SELECT 1 FROM Films WHERE title = ?", (title,))
                if cursor.fetchone():
                    continue

                cursor.execute(
                    "INSERT INTO Films (title, director, release_date) VALUES (?, ?, ?)",
                    (title, director, release),
                )
                added += 1

            conn.commit()
            print(f"Imported films: {added}")

    except Exception as e:
        print(f"Error importing films: {e}")


def show_table(table_name):
    try:
        with pyodbc.connect(CONNECTION_STRING) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            if not rows:
                print(f"No rows in {table_name}")
                return
            for r in rows:
                print(r)

    except Exception as e:
        print(f"Error reading {table_name}: {e}")


def get_all_users():
    try:
        # Establish connection
        with pyodbc.connect(CONNECTION_STRING) as conn:
            cursor = conn.cursor()
            # Execute a query
            cursor.execute(
                "SELECT name, surname, email, country, city, salary FROM Users")

            # Fetch results
            for row in cursor.fetchall():
                print(row)

    except Exception as e:
        print(f"Error: {e}")