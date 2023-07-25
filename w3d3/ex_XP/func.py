import random
import string
import datetime
from faker import Faker

# EX XP 2)


def add_two_numbers(num1, num2):
    result = num1 + num2
    print(f"The result of adding {num1} and {num2} is: {result}")


# EX XP 3)

def roll_and_check(user_num):
    if not isinstance(user_num, int) or user_num < 1 or user_num > 100:
        raise print("Please enter a valid number between 1 and 100.")

    random_num = random.randint(1, 100)
    print(f"You rolled: {random_num}")

    if user_num == random_num:
        print("Congratulations! It's a match!")
    else:
        print("Better luck next time!")


# EX XP 4)

def generate_random_string(length):
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))


# EX XP 5)

def display_current_date():
    current_date = datetime.date.today()
    print(current_date)


# EX XP 6)

def time_left_until_jan_1st():
    today = datetime.date.today()
    jan_1st = datetime.date(today.year + 1, 1, 1)

    timeleft = jan_1st - today
    days_left = timeleft.days
    hours_left = timeleft.seconds // 3600
    minutes_left = (timeleft.seconds // 60) % 60
    seconds_left = timeleft.seconds % 60

    print(
        f"The 1st of January is in {days_left} days and {hours_left:02}:{minutes_left:02}:{seconds_left:02} hours.")


# EX XP 7)

def minutes_lived(birthdate):
    current_datetime = datetime.datetime.now()

    try:
        birth_datetime = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
    except ValueError:
        raise ValueError(
            "Invalid birthdate format. Please use the format 'YYYY-MM-DD'.")

    time_lived = current_datetime - birth_datetime
    minutes_lived = time_lived.total_seconds() / 60

    return minutes_lived

# EX XP 8)


faker = Faker()

users = []


def add_user():
    name = faker.name()
    address = faker.address()
    language_code = faker.language_code()

    user = {
        'name': name,
        'address': address,
        'language_code': language_code
    }

    users.append(user)
