import csv
import random

food_items = [
    "Paneer Butter Masala",
    "Veg Biryani",
    "Chicken Biryani",
    "Masala Dosa",
    "Idli Sambar",
    "Pav Bhaji",
    "Vada Pav",
    "Paneer Tikka",
    "Hakka Noodles",
    "Manchurian",
    "Veg Pizza",
    "Burger",
    "Fries",
    "Cold Coffee",
    "Chocolate Shake",
    "Gulab Jamun",
    "Rasgulla",
    "Dal Tadka",
    "Butter Naan",
    "Jeera Rice",
    "Kadhi Khichdi",
    "Gujarati Thali"
]

menus = []
menu_id = 1

with open("C:\\Users\\DC\\OneDrive\\Desktop\\swiggy-gujarat-data-pipeline\\data\\restaurants.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        restaurant_id = row["restaurant_id"]

        # each restaurant gets 20 menu items
        selected_items = random.sample(food_items, 20)

        for item in selected_items:

            price = random.randint(80, 400)

            veg = random.choice(["Yes", "No"])

            menus.append([
                menu_id,
                restaurant_id,
                item,
                price,
                veg
            ])

            menu_id += 1


with open("C:\\Users\\DC\\OneDrive\\Desktop\\swiggy-gujarat-data-pipeline\\data\\menus.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "menu_id",
        "restaurant_id",
        "item_name",
        "price",
        "veg"
    ])

    writer.writerows(menus)

print("Menu dataset generated successfully!")