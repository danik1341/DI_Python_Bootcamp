# EX XP

# 1)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result_dict = dict(zip(keys, values))
print(result_dict)

print('/////////////////////////////////////////')

# 2)

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for member, age in family.items():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15

    print(f'{member} has to pay ${cost}')
    total_cost += cost

print('Total cost for the movies:', total_cost)

print('//////////////  BONUS  ///////////////')

blank_family = {}

total_cost = 0

num_family_memebers = int(input("Please provide the number of watchers: "))

for _ in range(num_family_memebers):
    name = input("Please provide the name: ")
    age = int(input(f'Please provide the age of {name}: '))
    blank_family[name] = age

for member, age in blank_family.items():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15

    print(f'{member} has to pay ${cost}')
    total_cost += cost

print('Total cost for the movies:', total_cost)

print('/////////////////////////////////////////')

# 3)


brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton '],
    'number_stores': 7000,
    'major_color': {
        'France': ['blue'],
        'Spain': ['red'],
        'US': ['pink', 'green']
    },
}

brand['number_stores'] = 2

print("Zara's clients include men, women, children, and home shoppers.")

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print("Last international competitor:", brand["international_competitors"][-1])

print("Major clothes colors in the US:", brand["major_color"]["US"])

print("Number of key-value pairs:", len(brand))

print("Keys of the dictionary:", list(brand.keys()))

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

brand.update(more_on_zara)

print("Value of the key number_stores:", brand["number_stores"])

# When printing the value of the key "number_stores" after using the update() method to add the information from the more_on_zara dictionary,
# you will see that the value has changed to 10000.
# The update() method updates the existing keys in the brand dictionary with the corresponding keys and values from the more_on_zara dictionary.
# In this case, the value of the key "number_stores" was changed from 2 to 10000.

print('/////////////////////////////////////////')


# 4)

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

disney_users_A = {}
disney_users_A_i = {}
disney_users_A_MnP = {}
disney_users_B = {}
disney_users_C = {}

for index, user in enumerate(users):
    disney_users_A[user] = index

print(disney_users_A)

for index, user in enumerate(users):
    disney_users_B[index] = user

print(disney_users_B)

for index, user in enumerate(sorted(users)):
    disney_users_C[user] = index

print(disney_users_C)

disney_users_A.clear()
for index, user in enumerate(users):
    if "i" in user:
        disney_users_A[user] = index
print('The Is')
print(disney_users_A)

disney_users_A.clear()
for index, user in enumerate(users):
    if user.startswith("M") or user.startswith("P"):
        disney_users_A[user] = index
print('The Ps and Ms')
print(disney_users_A)
