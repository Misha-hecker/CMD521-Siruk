import os
from src.Print import print_people
from src.Retrive import get_data
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
        "Enter a number to choose an option:\n1. People\n2. Planets\n3. Species\n4. Vehicles\n5. Starships\n6. Films\n7. Exit\n-------> ")
    if chouce == "7":
        exit = True
        print("Exiting the program.")
    elif chouce == "1":
        data = get_data(PEOPLE_URL)
        print_people(data)
        save_people_to_csv(data, "people.csv")
    elif chouce == "2":
        data = get_data(PLANETS_URL)
        print_people(data)
        save_people_to_csv(data, "planets.csv")
    elif chouce == "3":
        data = get_data(SPECIES_URL)
        print_people(data)
        save_people_to_csv(data, "species.csv")
    elif chouce == "4":
        data = get_data(VEHICLES_URL)
        print_people(data)
        save_people_to_csv(data, "vehicles.csv")
    elif chouce == "5":
        data = get_data(STARSHIPS_URL)
        print_people(data)
        save_people_to_csv(data, "starships.csv")
    elif chouce == "6":
        data = get_data(FILMS_URL)
        print_people(data)
        save_people_to_csv(data, "films.csv")