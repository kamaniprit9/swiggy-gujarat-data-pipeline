import csv
import random
from faker import Faker

fake = Faker()

users = []

cities = []

# read cities
with open("C:\\Users\\DC\\OneDrive\\Desktop\\swiggy-gujarat-data-pipeline\\data\\cities.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cities.append(row["city"])

user_id = 1

TOTAL_USERS = 50000

for _ in range(TOTAL_USERS):

    name = fake.name()

    city = random.choice(cities)

    signup_date = fake.date_between(start_date='-2y', end_date='today')

    users.append([
        user_id,
        name,
        city,
        signup_date
    ])

    user_id += 1


with open("C:\\Users\\DC\\OneDrive\\Desktop\\swiggy-gujarat-data-pipeline\\data\\users.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "user_id",
        "name",
        "city",
        "signup_date"
    ])

    writer.writerows(users)


print("Users dataset generated successfully!")