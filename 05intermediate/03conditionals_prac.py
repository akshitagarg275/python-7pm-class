# TODO: Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+)

# age = 15

# if age < 13:
#     print("Child")
# elif age >= 13 and age <= 19:
#     print("Teenager")
# elif age >= 20 and age <= 59:
#     print("Adult")
# elif age >= 60:
#     print("Senior")
# else:
#     print("Please provide a valid age")

# TODO:  Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday

# day = "Wednesday"
# age = 20
# price = 0

# if age>= 18: price = 12
# else: price = 8

# if day == "Wednesday":
#     price-= 2

# print(price)


# TODO: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
# color = "green"

# if color == "green":
#     print("unripe")
# elif color == "yellow":
#     print("ripe")
# elif color == "brown":
#     print("overripe")

# TODO: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman)

# weather = "Sunny"

# if weather == "Sunny":
#     print("Go for a walk")
# elif weather == "Rainy":
#     print("Read a book")
# elif weather == "Snowy":
#     print("Build a snowman")


# TODO:  Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car
# distance = 15

# if distance < 3 and distance > 0:
#     print("Walk")
# elif distance >= 3 and distance <= 15:
#     print("Bike")
# elif distance >15:
#     print("Car")

# TODO: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso

# size = "Small"
# isEspresso = True

# if size =="Small":
#     print(f"Size of coffee: {size} and extra shot required : {isEspresso}")
# elif size == "Medium":
#     print(f"Size of coffee: {size} and extra shot required : {isEspresso}")
# elif size == "Large":
#     print(f"Size of coffee: {size} and extra shot required : {isEspresso}")

# TODO: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong)

# password ="djndfwebjkfbw"

# if len(password) < 6:
#     print("Weak")
# elif len(password) >= 6 and len(password) <= 10:
#     print("Medium")
# elif len(password) > 10:
#     print("Strong")

# TODO: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

# year = 2020

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("It is a leap year")
# else:
#     print("Not a leap year")

# TODO: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).