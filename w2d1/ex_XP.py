# Ex XP

# 1)

world = 'Hello world\n'
print(world * 4)

# 2)

result = (99 ** 3)*8
print(result)

# 3)

# 1. false
# 2. true
# 3. false
# 4. string and int can not be compared like so
# 5. false

# 4)

computer_brand = 'custom made'
print(f"I've a {computer_brand} computer")

# 5)

name = 'Daniel'
age = 25
shoe_size = 43
info = f"Hello, my name is {name}, I'm {age} years old, and my shoe size is {shoe_size}."
print(info)

# 6)

a = input('Give me the first num, please ')
b = input('Give me the second num, please ')
if (a > b):
    {
        print('Hello World')
    }

# 7)

odd_even = input('Please provide me with a number ')
if (int(odd_even) % 2 == 0):
    {
        print('The number you have provided is an even number')
    }
else:
    {
        print('The number you have provided is an odd number')
    }

# 8)

stranger_name = input('Please tell me your name? ')

if (name != stranger_name):
    {
        print(
            f'Your name is {stranger_name} wha.... No no no This is Patrick, please do call me again')
    }
else:
    {
        print(f'Ehhh yoooo how do you do {name}?')
    }

# 9)

stranger_height = input('Please provide your height in inches ')

if (int(stranger_height) * 2.54 > 145):
    {
        print('Welcome to the ride of hell, please dont puke all over the seats')
    }
else:
    {
        print('Bounce shorty')
    }


# EX XP GOLD

# 1)

for _ in range(4):
    print("Hello world")
for _ in range(4):
    print("I love python")

# 2)

month = int(input("Enter a month (1 to 12): "))

if month >= 3 and month <= 5:
    season = "Spring"
elif month >= 6 and month <= 8:
    season = "Summer"
elif month >= 9 and month <= 11:
    season = "Autumn"
else:
    season = "Winter"

print(f"The season of month {month} is {season}.")


# EX XP Ninja

# 3)

# true
# true
# false
# false
# true
# false

x = (1 == True)  # print("x is", x) - true
y = (1 == False)  # print("y is", y) - false
a = True + 4  # a = (True + 4) - 5
b = False + 10  # print("b:", b) - 10

# 4)

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

character_count = len(my_text)
print("Number of characters:", character_count)

# 5)

longest_sentence = ""
while True:
    sentence = input("Enter the longest sentence without the letter 'A': ")
    if 'A' in sentence:
        print("Sorry, the sentence contains the letter 'A'. Try again.")
    elif len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("Congratulations! You've set a new longest sentence.")
    else:
        print("Not long enough. Try again.")

    play_again = input("Do you want to continue? (yes/no): ")
    if play_again.lower() != "yes":
        break

print("Thank you for playing!")
