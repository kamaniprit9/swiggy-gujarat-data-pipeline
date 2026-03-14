import csv

cities = [
    # Mega Cities
    ("Ahmedabad", "mega", 200),
    ("Surat", "mega", 200),
    ("Vadodara", "mega", 200),
    ("Rajkot", "mega", 200),

    # Large Cities
    ("Bhavnagar", "mid", 120),
    ("Jamnagar", "mid", 120),
    ("Junagadh", "mid", 120),
    ("Gandhinagar", "mid", 120),
    ("Anand", "mid", 120),
    ("Nadiad", "mid", 120),
    ("Mehsana", "mid", 120),
    ("Morbi", "mid", 120),

    # Medium Cities
    ("Surendranagar", "small", 80),
    ("Porbandar", "small", 80),
    ("Navsari", "small", 80),
    ("Bharuch", "small", 80),
    ("Palanpur", "small", 80),
    ("Valsad", "small", 80),
    ("Godhra", "small", 80),
    ("Patan", "small", 80),
    ("Dahod", "small", 80),
    ("Amreli", "small", 80),

    # Smaller Cities
    ("Botad", "small", 50),
    ("Veraval", "small", 50),
    ("Vyara", "small", 50),
    ("Vapi", "small", 50),
    ("Ankleshwar", "small", 50),
    ("Kalol", "small", 50),
    ("Deesa", "small", 50),
    ("Modasa", "small", 50),
    ("Himmatnagar", "small", 50)
]

with open("C:\\Users\\DC\\OneDrive\\Desktop\\swiggy-gujarat-data-pipeline\\data\\cities.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["city", "tier", "restaurant_count"])
    writer.writerows(cities)

print("Cities dataset generated successfully!")