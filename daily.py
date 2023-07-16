# for the bonus
import random

# 1)
user_input = input("Enter a string (10 characters long): ")

if len(user_input) < 10:
    print("String not long enough.")
elif len(user_input) > 10:
    print("String too long.")
else:
    print("Perfect string.")

# 2)
first_character = user_input[0]
last_character = user_input[-1]
print(f"First character: {first_character}")
print(f"Last character: {last_character}")

# 3)
for character in user_input:
    print(character)

# 4)
characters = list(user_input)
random.shuffle(characters)
jumbled_string = ''.join(characters)

print("Jumbled string:", jumbled_string)
