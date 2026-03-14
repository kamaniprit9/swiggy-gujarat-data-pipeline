import json
import random
import csv
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    api_version=(3, 9, 0)
)

users = []
restaurants = []
partners = []

with open("C:\\Users\\DC\\OneDrive\\Desktop\\swiggy-gujarat-data-pipeline\\data\\users.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        users.append(row)

with open("C:\\Users\\DC\\OneDrive\\Desktop\\swiggy-gujarat-data-pipeline\\data\\restaurants.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        restaurants.append(row)

with open("C:\\Users\\DC\\OneDrive\\Desktop\\swiggy-gujarat-data-pipeline\\data\\delivery_partners.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        partners.append(row)

while True:

    user = random.choice(users)
    restaurant = random.choice(restaurants)

    order_value = random.randint(100, 600)

    order_event = {
        "event_type": "order_created",
        "user_id": user["user_id"],
        "restaurant_id": restaurant["restaurant_id"],
        "city": restaurant["city"],
        "order_value": order_value
    }

    producer.send("order-events", order_event)
    # producer.flush()

    print("Sent event:", order_event)

    time.sleep(2)