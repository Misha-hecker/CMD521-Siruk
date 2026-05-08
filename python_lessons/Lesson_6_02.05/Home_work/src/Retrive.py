import requests
import csv

def get_data(URL):
    data = requests.get(URL, verify=False)
    return data.json()

def read_from_csv(filename):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []