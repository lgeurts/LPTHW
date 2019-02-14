# Exercise 5: More Variables and Printing

my_name = 'Luc Geurts'
my_age = 34 # Is a lie.
my_height = 164 # Centimeters. Not a lie.
my_weight = 68 # Kilograms.
my_eyes = 'green-blue'
my_teeth = 'white'
my_hair = 'brown'
my_posture = 'muscular'
my_nationality = 'Irish, Belgian'

# Little f before " and {} characters tells Python the string needs formatting.
# Like "Put these vatables in there!"
print(f"Let's talk about {my_name}." )
print(f"His supposed age is {my_age}.")
print(f"He weighs {my_weight} kilograms.")
print("Actually that is not too heavy.")
print(f"He has beautiful {my_eyes} eyes and his hair is {my_hair}.")
print(f"He likes to flash his {my_teeth} teeth.")
print(f"His posture is really {my_posture}.")
print(f"His nationality is {my_nationality}.")

# This line is tricky, try to get it right.
total = my_weight / my_height
print(f"If I divide {my_weight} kilogram by {my_height}, I weigh {total} grams per cm.")
