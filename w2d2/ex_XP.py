# Ex XP

# 1)

my_fav_numbers = {1, 3, 4, 420}
my_fav_numbers.add(10)
my_fav_numbers.add(42)
my_fav_numbers.remove(42)

friend_fav_numbers = {3, 8, 12}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print("My favorite numbers:", my_fav_numbers)
print("Friend's favorite numbers:", friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)

print('/////////////////////////////////////////')

# 2)

# tuples are immutable, which means you cannot modify them after they are created.
# This includes adding, removing, or modifying elements.
# Therefore, you cannot directly add more integers to an existing tuple.
# However, you can create a new tuple by concatenating two tuples together,
# including the existing tuple and the additional integers you want to include.

my_tuple = (1, 2, 3)
additional_integers = (4, 5)

new_tuple = my_tuple + additional_integers

print("Original tuple:", my_tuple)
print("Additional integers:", additional_integers)
print("New tuple:", new_tuple)

print('/////////////////////////////////////////')

# 3)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")

basket.append("Kiwi")
basket.insert(0, "Apples")

apple_count = basket.count("Apples")

basket.clear()

print(basket)

print('/////////////////////////////////////////')

# 4)

# The difference between an integer and a float lies in the way they represent numbers.
# An integer is a whole number without a decimal point, such as 1, -5, or 100.
# In contrast, a float allows for decimal points and fractional parts, such as 3.14 or -2.5.

# To generate a sequence of floats, you can use various methods,
# such as using a loop to increment or decrement a starting value by a fixed step size or
# using built-in functions like range() in combination with division or multiplication.

start = 1.5
step = 0.5
count = 8

sequence = [start + step * i for i in range(count)]
print(sequence)

print('/////////////////////////////////////////')

# 5)

for num in range(1, 21):
    print(num)

print("--------")

for index in range(1, 21):
    if index % 2 == 0:
        print(index)

print('/////////////////////////////////////////')

# 6)

my_name = "Daniel"

name = input("Enter your name: ")

while name != my_name:
    name = input("Enter your name: ")

print(f"Hello {name}, I'm {my_name}")

print('/////////////////////////////////////////')

# 7)

favorite_fruits = input(
    "Enter your favorite fruit(s), separated by a single space: ").split()

chosen_fruit = input("Enter a fruit name: ")

if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy!")

print('/////////////////////////////////////////')

# 8)

toppings = []
price_per_topping = 2.5

while True:
    topping = input("Enter a pizza topping (or 'quit' to exit): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_price = 10 + (len(toppings) * price_per_topping)

print("Toppings on your pizza:", toppings)
print("Total price:", total_price)

print('/////////////////////////////////////////')

# 9)

ticket_price_under_3 = 0
ticket_price_3_to_12 = 10
ticket_price_over_12 = 15

total_cost = 0

family_size = int(input("Enter the number of people in the family: "))

for _ in range(family_size):
    age = int(input("Enter the age of a family member: "))

    if age < 3:
        ticket_cost = ticket_price_under_3
    elif age >= 3 and age <= 12:
        ticket_cost = ticket_price_3_to_12
    else:
        ticket_cost = ticket_price_over_12

    total_cost += ticket_cost

print("Total cost of family tickets:", total_cost)

teenagers = ["John", "Jane", "Michael", "Emily", "David"]
eligible_teenagers = []

for teenager in teenagers:
    age = int(input(f"Enter the age of {teenager}: "))

    if age >= 16 and age <= 21:
        eligible_teenagers.append(teenager)

print("Eligible teenagers to watch the movie:", eligible_teenagers)

print('/////////////////////////////////////////')

# 10)

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
                   "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print("I made your", sandwich.lower())

print("All sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
