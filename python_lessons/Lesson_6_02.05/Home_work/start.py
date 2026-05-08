import os
from src.Print import print_people
from src.Retrive import get_data, read_from_csv
from src.Save import save_people_to_csv
from dotenv import load_dotenv

load_dotenv(override=True)

PEOPLE_URL = os.getenv("SWAPI_PEOPLE_URL")
PLANETS_URL = os.getenv("SWAPI_PLANETS_URL")
SPECIES_URL = os.getenv("SWAPI_SPECIES_URL")
VEHICLES_URL = os.getenv("SWAPI_VEHICLES_URL")
STARSHIPS_URL = os.getenv("SWAPI_STARSHIPS_URL")
FILMS_URL = os.getenv("SWAPI_FILMS_URL")

exit = False

while not exit:
    chouce = input(
        "Enter a number to choose an option:\n1. People\n2. Planets\n3. Species\n4. Vehicles\n5. Starships\n6. Films\n7. Read from file\n8. Search\n9. Exit\n-------> ")
    
    if chouce == "1":
        data = get_data(PEOPLE_URL).get('results', [])
        print_people(data)
        save_people_to_csv(data, "people.csv")
    elif chouce == "2":
        data = get_data(PLANETS_URL).get('results', [])
        print_people(data)
        save_people_to_csv(data, "planets.csv")
    elif chouce == "3":
        data = get_data(SPECIES_URL).get('results', [])
        print_people(data)
        save_people_to_csv(data, "species.csv")
    elif chouce == "4":
        data = get_data(VEHICLES_URL).get('results', [])
        print_people(data)
        save_people_to_csv(data, "vehicles.csv")
    elif chouce == "5":
        data = get_data(STARSHIPS_URL).get('results', [])
        print_people(data)
        save_people_to_csv(data, "starships.csv")
    elif chouce == "6":
        data = get_data(FILMS_URL).get('results', [])
        print_people(data)
        save_people_to_csv(data, "films.csv")
    elif chouce == "7":
        filename = input("Enter filename: ")
        data = read_from_csv(filename)
        if data:
            print_people(data)
    elif chouce == "8":
        query = input("Search for: ").lower()
        filename = input("In file: ")
        data = read_from_csv(filename)
        results = [i for i in data if query in i.get('name', '').lower() or query in i.get('title', '').lower()]
        print_people(results)
    elif chouce == "9":
        exit = True
        print("Exiting the program.")