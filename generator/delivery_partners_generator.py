import csv
import random
from faker import Faker

fake = Faker()

partners = []

cities = []

# read cities
with open("C:\\Users\\DC\\OneDrive\\Desktop\\swiggy-gujarat-data-pipeline\\data\\cities.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cities.append(row["city"])

vehicle_types = [
    "bike",
    "scooter",
    "bicycle"
]

partner_id = 1

TOTAL_PARTNERS = 5000

for _ in range(TOTAL_PARTNERS):

    name = fake.name()

    city = random.choice(cities)

    vehicle = random.choice(vehicle_types)

    rating = round(random.uniform(3.5, 4.9), 1)

    partners.append([
        partner_id,
        name,
        city,
        vehicle,
        rating
    ])

    partner_id += 1


with open("C:\\Users\\DC\\OneDrive\\Desktop\\swiggy-gujarat-data-pipeline\\data\\delivery_partners.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "delivery_partner_id",
        "name",
        "city",
        "vehicle_type",
        "rating"
    ])

    writer.writerows(partners)


print("Delivery partners dataset generated successfully!")