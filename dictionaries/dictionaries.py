# meals = ["yoghurt", "roll", "cheese"]

# create dictionary
# meals = {}
# meals_2 = dict([(1, "hello")], (2, "world")])

meals = {
    "breakfast": "yoghurt",
    "lunch": "roll",
    "dinner": "steak"
}

# create new key and value 
meals["super"] = "scone"

# change value 
meals["dinner"] = "pancakes"

# delete key and it's values
del(meals["dinner"])

# print(meals)

# find a value in a dictionary
# print("yoghurt" in meals.values())

# below code prints out a boolean value 
# print("breakfast" in meals)
 # print(meals["breakfast"])

 # list of the keys 
 #print(list(meals))
# prints keys
#print(meals.keys())
# prints values 
# print(meals.values())

# Nested Dictionaries

countries = {
    "uk": {
        "capital": "london",
        "population": 1000
        },
    "germany": {
        "capital": "Berlin",
        "population": 500
    }
}

# 
germany_population = countries["germany"]["population"]
print(germany_population)


