import csv
import json


def normalize_value(value):
    if isinstance(value, list):
        return "; ".join(str(x) for x in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False)
    return value


def save_people_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year',
                      'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow({key: normalize_value(item.get(key, ""))
                            for key in fieldnames})
        print(f"Saved to {filename}")