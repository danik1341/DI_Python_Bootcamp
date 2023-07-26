import random


def get_words_from_file():
    try:
        with open('w3d4/words.txt', 'r') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print("Error: The words.txt file is missing. Make sure to download and save it in the correct directory.")
        return []


def get_random_sentence(length):
    words = get_words_from_file()
    if not words:
        return "Unable to generate a sentence. Please check the words.txt file."

    random_words = random.sample(words, length)
    sentence = ' '.join(random_words).lower() + '.'
    return sentence


def main():
    print("Welcome to the Random Sentence Generator!")
    print("Please enter a sentence length (between 2 and 20):")

    try:
        length = int(input())
        if length < 2 or length > 20:
            raise ValueError()

        sentence = get_random_sentence(length)
        print("Generated Sentence:", sentence)

    except ValueError:
        print("Error: Invalid input. Please enter an integer between 2 and 20.")
        return


if __name__ == "__main__":
    main()
