# def greet():
#     return("Hey")

# greeting = greet()
# print(greeting)

# def greet(name):
#     return "Hey " + name

# greeting = greet("Jenny")
# print(greeting)

# def greet(name, time_of_day):
#     return "Good " + time_of_day + ", " + name 

# greeting = greet('Jenny', 'evening')
# print(greeting)

# def greet (name, time_of_day):
#     return "Good " + time_of_day + ", " + name

# name_1 = "Bob"
# time_of_day_1 = "evening"
# greeting = greet(name_1, time_of_day_1)
# print(greeting)

# name_2 = "Anna"
# time_of_day_2 = "morning"
# greeting = greet(name_2, time_of_day_2)
# print(greeting)

# chickens = [
#   { "name": "Margaret", "age": 2, "eggs": 0 },
#   { "name": "Hetty", "age": 1, "eggs": 2 },
#   { "name": "Henrietta", "age": 3, "eggs": 1 },
#   { "name": "Audrey", "age": 2, "eggs": 0 },
#   { "name": "Mabel", "age": 5, "eggs": 1 },
# ]

# total_eggs = 0

# for chicken in chickens:
#     total_eggs += chicken["eggs"]
#     chicken["eggs"] = 0 # eggs have been collected

# print(f"{total_eggs} eggs collected")

chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

def count_eggs( list ):
    total_eggs = 0

    for bird in list:
        total_eggs += bird["eggs"]
        bird["eggs"] = 0 # eggs have been collected

    return f"{total_eggs} eggs collected"

print(count_eggs(chickens))

#practise comment 














