import csv
import random

restaurant_prefix = [
    "Royal", "Spicy", "Tasty", "Urban", "Golden", "Food", "Taste",
    "Delight", "Magic", "Street", "Hungry", "Flavors"
]

restaurant_suffix = [
    "Kitchen", "Bites", "Corner", "Dhaba", "Cafe",
    "House", "Point", "Restaurant", "Hub"
]

cuisines = [
    "Gujarati", "North Indian", "South Indian",
    "Chinese", "Fast Food", "Pizza", "Burger",
    "Biryani", "Street Food", "Desserts"
]

restaurants = []
restaurant_id = 1

with open("C:\\Users\\DC\\OneDrive\\Desktop\\swiggy-gujarat-data-pipeline\\data\\cities.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        city = row["city"]
        restaurant_count = int(row["restaurant_count"])

        for _ in range(restaurant_count):

            name = random.choice(restaurant_prefix) + " " + random.choice(restaurant_suffix)

            cuisine = random.choice(cuisines)

            rating = round(random.uniform(3.5, 4.9), 1)

            delivery_time = random.randint(20, 50)

            restaurants.append([
                restaurant_id,
                name,
                city,
                cuisine,
                rating,
                delivery_time
            ])

            restaurant_id += 1

with open("C:\\Users\\DC\\OneDrive\\Desktop\\swiggy-gujarat-data-pipeline\\data\\restaurants.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "restaurant_id",
        "restaurant_name",
        "city",
        "cuisine",
        "rating",
        "delivery_time"
    ])

    writer.writerows(restaurants)

print("Restaurants dataset generated successfully!")