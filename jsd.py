import json

with open('country.json', 'r') as file:
    data = json.load(file)

def find_country_by_name(country_name):
    for country in data["countries"]:
        if country["name"].lower() == country_name.lower():
            return country
    return None

user_input = input("Enter the name of the country: ")

result = find_country_by_name(user_input)
if result:
    print(f"Country found: ID = {result['id']}, Name = {result['name']}")
else:
    print("Country not found.")
