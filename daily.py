import random

user_input = input("Enter a string (10 characters long): ")

if len(user_input) < 10:
    print("String not long enough.")
elif len(user_input) > 10:
    print("String too long.")
else:
    print("Perfect string.")

first_character = user_input[0]
last_character = user_input[-1]
print(f"First character: {first_character}")
print(f"Last character: {last_character}")

for character in user_input:
    print(character)

characters = list(user_input)
random.shuffle(characters)
jumbled_string = ''.join(characters)

print("Jumbled string:", jumbled_string)
