import datetime  # USED IN GOLD CHALLANGE

# 1)

number = int(input("Enter a number: "))
length = int(input("Enter the desired length: "))

multiples = []
count = 0

while len(multiples) < length:
    count += 1
    multiple = number * count
    multiples.append(multiple)

print("Multiples of", number, "until length", length, ":", multiples)

print('/////////////////////////////////////////')

# 2)

user_word = input("Enter a word: ")
result = ""

for i in range(len(user_word)):
    if i == 0 or user_word[i] != user_word[i - 1]:
        result += user_word[i]

print("Modified word:", result)

print('/////////////////////////////////////////')


# GOLD

birthdate = input("Enter your birthdate (DD/MM/YYYY): ")
day, month, year = birthdate.split('/')

is_leap_year = False
try:
    birth_date = datetime.date(int(year), int(month), int(day))
    if (birth_date.year % 4 == 0 and birth_date.year % 100 != 0) or birth_date.year % 400 == 0:
        is_leap_year = True
except ValueError:
    print("Invalid birthdate entered.")
    exit()

current_date = datetime.date.today()

if (birth_date.month, birth_date.day) == (2, 29) and not is_leap_year:
    print("Invalid birthdate entered.")
    exit()

age = current_date.year - birth_date.year
if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
    age -= 1

num_candles = age % 10

top_layer = ":" + ":H:a:p:p:y:" + ":"
body_layer = "^" * (num_candles + 8)
bottom_layer = ":" + ":B:i:r:t:h:d:a:y:" + ":"

top_layer_width = len(top_layer) + 2
bottom_layer_width = len(bottom_layer) + 2

cake = f'''
       ___{'i' * num_candles}___
      |{top_layer:^{top_layer_width}}|
   {'__|' + '_' * (top_layer_width - 5) + '|__'}
   |{body_layer:^{top_layer_width}}|
   |{bottom_layer:^{bottom_layer_width}}|
   {'~' * (top_layer_width + 2)}
'''

print(cake)
print(f"Number of candles: {num_candles}")
print(f"{'-' * 20}")

if is_leap_year:
    print("It's a leap year! Here's an extra cake:")
    print(cake)
    print(
        f"Number of candles: {num_candles}. But now its a leap year with EXTRA CAKE!!!!")
    print(f"{'-' * 20}")
