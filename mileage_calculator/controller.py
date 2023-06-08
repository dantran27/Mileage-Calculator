mileage_chart = {
    "Albany": {
        "Albany": 0,
        "Baker City": 351,
        "Beaverton": 67,
        "Bend": 125,
        "Salem": 25,
    },
    "Baker City": {
        "Albany": 351,
        "Baker City": 0,
        "Beaverton": 312,
        "Bend": 231,
        "Salem": 349, 
    },
    "Beaverton": {
        "Albany": 67,
        "Baker City": 312,
        "Beaverton": 0,
        "Bend": 173,
        "Salem": 43,
    },
    "Bend": {
        "Albany": 125,
        "Baker City": 231,
        "Beaverton": 173,
        "Bend": 0,
        "Salem": 132,
    },
    "Salem":{
        "Albany": 25,
        "Baker City": 349,
        "Beaverton": 43,
        "Bend": 132,
        "Salem": 0,
    }
    
}

def get_miles(city1, city2):
    miles = mileage_chart[city1][city2]
    return miles


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