

import requests


def get_info(id, key):
    url = f"https://swapi.dev/api/people/{id}/"
    r = requests.get(url)
    data = r.json()
    return data[key]


def get_name(id):
    return get_info(id, "name")