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
