import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import functions


def main():
    with functions.pyodbc.connect(functions.conn_str) as conn:
        functions._ensure_people_table(conn)
        functions._ensure_films_table(conn)
    print('Database initialized: People and Films tables are ready.')


if __name__ == '__main__':
    main()
