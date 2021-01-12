# counter = 0
# my_number = 5

# while (counter < my_number):
#     #print("counter is " + str(counter))
#     print(f"counter is {counter}")
#     counter += 1


# my_number = 5
# value = int(input("What number am I thinking of? "))

# while (value != my_number): 
#     if (value < my_number):
#         print("Too low")
#     else:
#         print("Too high")
#     value = int(input("Try again: "))

# # print("Yes!  You got it!")

# while True:
#     line = input("Type something: ")

#     if line.lower() == "q":
#         break

#     print(f"You typed: {line}")

# Farmer with chickens - wants to find out how many eggs laid

# numbers = [1, 2, 3, 4, 5]
# total = 0

# for number in numbers: 
#     total += number 

# print(total)


chickens = [
  {"name": "Margaret", "age": 2, "eggs": 0},
  {"name": "Hetty", "age": 1, "eggs": 2},
  {"name": "Henrietta", "age": 3, "eggs": 1},
  {"name": "Audrey", "age": 2, "eggs": 0},
  {"name": "Mabel", "age": 5, "eggs": 1},
]

# for chicken in chickens:
#     print(f'{chicken["name"]} is {chicken["age"]}')

total_eggs = 0

for chicken in chickens:
    if (chicken["eggs"] > 0):
        print("Wooooo eggs!")
    total_eggs += chicken["eggs"]
    chicken["eggs"] = 0


print(f"{total_eggs} eggs collected")
print(chickens)
















