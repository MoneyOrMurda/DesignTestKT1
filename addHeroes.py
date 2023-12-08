import json
import csv

with open('SuperHero.json', 'r') as json_file:
    data = json.load(json_file)

new_heroes = [
    {
        "name": "Captain America",
        "age": 35,
        "secretIdentity": "Steve Rogers",
        "powers": ["Superhuman strength", "Shield throwing"]
    },
    {
        "name": "Spider-Man",
        "age": 22,
        "secretIdentity": "Peter Parker",
        "powers": ["Wall-crawling", "Web-slinging"]
    }
]

updated_data = data.copy()
updated_data['members'].extend(new_heroes)

with open('SuperHeroUpdated.json', 'w') as json_file:
    json.dump(updated_data, json_file, indent=2)

with open('SuperHeroUpdated.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(['name', 'age', 'secretIdentity', 'powers'])

    for member in updated_data['members']:
        writer.writerow([member['name'], member['age'], member['secretIdentity'], ', '.join(member['powers'])])

print("Новые герои успешно добавлены в JSON файл и создан CSV файл с обновленными данными.")