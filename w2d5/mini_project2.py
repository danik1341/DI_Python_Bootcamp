# Hangman game

import random


def choose_random_word():
    '''
        Function to choose a random word from a list of words.

        Returns:
        str: A random word from the wordslist.
    '''

    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive',
                 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
    return random.choice(wordslist)


def display_word(word, guessed_letters):
    '''
        Function to display the word with stars for letters that have not been guessed.

        Parameters:
        word (str): The target word.
        guessed_letters (set): A set containing the letters guessed by the player.

        Returns:
        str: The word with stars for unguessed letters.
    '''

    display = ""
    for letter in word:
        if letter.lower() in guessed_letters:
            display += letter + " "
        else:
            display += "* "
    return display


def hangman():
    '''
        Main function to run the Hangman game.

        It initializes the game, gets user input, checks the guesses, and displays the results.
    '''

    word = choose_random_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word.lower():
            print("Correct guess!")
        else:
            attempts -= 1
            print(f"Incorrect guess! You have {attempts} attempts left.")

        display = display_word(word, guessed_letters)
        print(display)

        if "*" not in display:
            print("Congratulations! You've guessed the word.")
            break

    if attempts == 0:
        print(f"Game Over! The word was '{word}'.")


if __name__ == "__main__":
    hangman()
