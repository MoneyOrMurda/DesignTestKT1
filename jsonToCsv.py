import json
import csv

def convert_json_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['name', 'age', 'secretIdentity', 'powers'])

        for member in data['members']:
            writer.writerow([member['name'], member['age'], member['secretIdentity'], ', '.join(member['powers'])])

    print(f"JSON данные успешно преобразованы в CSV. Результат сохранен в {csv_file_path}")

if __name__ == '__main__':
    json_file_path = 'SuperHero.json'
    csv_file_path = 'SuperHero.csv'
    convert_json_to_csv(json_file_path, csv_file_path)