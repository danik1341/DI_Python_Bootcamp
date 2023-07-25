from func import *
# EX XP

# 1)


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}'

    def __int__(self):
        return int(self.amount)

    def __repr__(self) -> str:
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, Currency) and self.currency != other.currency:
            raise TypeError(
                f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        elif isinstance(other, Currency):
            return self.amount + other.amount
        else:
            return self.amount + other

    def __iadd__(self, other):
        if isinstance(other, Currency) and self.currency != other.currency:
            raise TypeError(
                f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        elif isinstance(other, Currency):
            self.amount += other.amount
        else:
            self.amount += other

        return self


# Test cases
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))  # Output: '5 dollars'
print(int(c1))  # Output: 5
print(repr(c1))  # Output: '5 dollars'

print(c1 + 5)  # Output: 10
print(c1 + c2)  # Output: 15

print(c1)  # Output: 5 dollars

c1 += 5
print(c1)  # Output: 10 dollars

c1 += c2
print(c1)  # Output: 20 dollars

# Output: TypeError: Cannot add between Currency type <dollar> and <shekel>
# Uncomment the following line in order to test the func afterwards recomment it as the code wont continue with it
# print(c1 + c3)

print('/////////////////////////////////////////')

# 2)
# from func import add_two_numbers || Imported at the top

add_two_numbers(5, 7)

print('/////////////////////////////////////////')

# 3)

# from func import roll_and_check || Imported at the top

user_input = int(input("Enter a number between 1 and 100: "))
roll_and_check(user_input)

print('/////////////////////////////////////////')


# 4)

# from func import generate_random_string || Imported at the top

random_string = generate_random_string(5)
print(random_string)

print('/////////////////////////////////////////')

# 5)

# from func import display_current_date || Imported at the top

display_current_date()

print('/////////////////////////////////////////')

# 6)

# from func import time_left_until_jan_1st || Imported at the top

time_left_until_jan_1st()

print('/////////////////////////////////////////')


# 7)

# from func import minutes_lived || Imported at the top

birthdate_input = "1998-01-08"
minutes = minutes_lived(birthdate_input)
print(f"You have lived approximately {minutes:.2f} minutes.")

print('/////////////////////////////////////////')

# 8)

# from func import add_user || Imported at the top

add_user()
add_user()
add_user()

print(users)
