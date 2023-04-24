destinations = {
    "Seattle": 189,
    "Spokane": 375}

cities = list(destinations.keys())
print(cities)
print(destinations.values())
to_seattle = destinations["Seattle"]
print(f"the distance from Portland to Seattle is {to_seattle} miles.")