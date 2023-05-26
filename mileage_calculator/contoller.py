mileage_chart = {
    "Albany": {
        "Albany": 0,
        "Baker City": 351,
        "Beaverton": 67,
    },
    "Baker City": {
        "Albany": 351,
        "Baker City": 0,
        "Beaverton": 312,
    },
    "Beaverton": {
        "Albany": 67,
        "Baker City": 312,
        "Beaverton": 0,
    }
}

def get_miles(city1, city2):
    miles = mileage_chart[city1][city2]


if __name__ == "__main__":
    destinations = {
        "Seattle": 189,
        "Spokane": 375}

    cities = list(destinations.keys())
    print(cities)
    print(destinations.values())
    to_seattle = destinations["Seattle"]
    print(f"the distance from Portland to Seattle is {to_seattle} miles.")



    albany_to_baker = mileage_chart["Albany"]["Baker City"]
    print(albany_to_baker)