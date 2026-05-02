import requests


def get_data(URL):
    data = requests.get(URL, verify=False)
    return data.json()
