import random  # FOR EX

# EX XP

# 1)


def display_message() -> str:
    return 'Im learning Full Stack Web Development with Python included'


print(display_message())

# 2)
# Made it more fun dont judge me.... pretty please :)


def favorite_book(title) -> str:
    if (title != 'The Way of Kings' and title != 'Stormlight Archive' and title != 'Stormlight Archive The Way of Kings' and title != 'TWoK'):
        return 'You are reading the wrong books! Go and read TWoK NOW!'
    else:
        return 'Speak Again The Hallowed Oaths\nLife Before Death\nStrength Before Weakness\nJourney Before Destination'


print(favorite_book(input('Enter the title of your favorite book: ')))

print('/////////////////////////////////////////')

# 3)


def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}")


describe_city("Paris")
describe_city("Mahachkala", "Russia")

print('/////////////////////////////////////////')

# 4)


def one_to_hundred(num) -> str:
    num = int(num)
    while (num < 1 or num > 100):
        num = int(input(
            'No.... The number needs to be between One and a Hundred (1-100). Enter a valid number: '))

    random_num = random.randint(1, 100)
    print(f'The random number is: {random_num}')

    if num == random_num:
        return 'Great success!'
    else:
        return 'No luck try again next time. Goodbye!'


print(one_to_hundred(input('Enter a number between 1 and 100: ')))

print('/////////////////////////////////////////')

# 5)


def make_shirt(size=None, text=None) -> str:
    if size is None:
        size = 'large'
    if text is None:
        text = 'I love Python'
    return f'The size of the shirt is {size} and the text is "{text}"'


print(make_shirt(input('What is the size of the shirt(large by default): ') or None,
                 input('What is the text you want on the shirt(says "I love Python" by default): ') or None))

print(make_shirt())
print(make_shirt(size='medium'))
print(make_shirt(size='large'))

print('/////////////////////////////////////////')

# 6)

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians(list) -> None:
    for name in list:
        print(name)


show_magicians(magician_names)


def make_great(list) -> None:
    for i in range(len(list)):
        list[i] = list[i] + ' The Great'


make_great(magician_names)

show_magicians(magician_names)

print('/////////////////////////////////////////')

# 7)


def get_random_temp(season) -> float:
    if (season.lower() == 'winter'):
        return round(random.uniform(-10, 16), 1)
    elif season.lower() == 'spring':
        return round(random.uniform(0, 23), 1)
    elif season.lower() == 'summer':
        return round(random.uniform(32, 40), 1)
    elif season.lower() == 'autumn' or season.lower() == 'fall':
        return round(random.uniform(23, 32), 1)
    else:
        raise ValueError(
            "Invalid season. Please choose 'winter', 'spring', 'summer', or 'autumn/fall' or a valid month number.")


print(get_random_temp('Summer'))


def main():
    season = input(
        'Please provide the season you are in or the num of the month: ')
    if (len(season) <= 2):
        month = int(season)
        if (3 <= month <= 5):
            season = 'Spring'
        elif (6 <= month <= 8):
            season = 'Summer'
        elif (9 <= month <= 11):
            season = 'Fall'
        else:
            season = 'Winter'
    temp = get_random_temp(season)
    if (temp < 0):
        return f'Brrr, thats freezing! Wear some extra layers today. Its {temp} degrees'
    if (0 < temp < 16):
        return f'Quite chilly! Dont forget your coat. Its {temp} degrees'
    if (16 < temp < 23):
        return f'Its chilly but aint that bad. Its {temp} degrees'
    if (24 < temp < 32):
        return f'Ok we getting to home temps over here. Its {temp} degrees'
    if (32 < temp < 40):
        return f'Yep... Welcome to Israel. Its {temp} degrees'


print(main())

print('/////////////////////////////////////////')

# 8)

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


def ask_questions(data):
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    for question_data in data:
        question = question_data["question"]
        correct_answer = question_data["answer"]

        user_answer = input(question + " ")

        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}\n")
            incorrect_answers += 1
            wrong_answers.append(
                {"question": question, "user_answer": user_answer, "correct_answer": correct_answer})

    return correct_answers, incorrect_answers, wrong_answers


def show_results(correct, incorrect, wrong_answers):
    print(f"Number of correct answers: {correct}")
    print(f"Number of incorrect answers: {incorrect}")

    if incorrect > 0:
        print("Questions you answered incorrectly:")
        for answer in wrong_answers:
            print(f"Question: {answer['question']}")
            print(f"Your answer: {answer['user_answer']}")
            print(f"Correct answer: {answer['correct_answer']}")
            print()


def game():
    play_again = True

    while play_again:
        correct, incorrect, wrong_answers = ask_questions(data)
        show_results(correct, incorrect, wrong_answers)

        if incorrect > 3:
            play_again_input = input(
                "You had more than 3 wrong answers. Do you want to play again? (yes/no): ")
            play_again = play_again_input.lower() == "yes"
        else:
            play_again = False


game()
