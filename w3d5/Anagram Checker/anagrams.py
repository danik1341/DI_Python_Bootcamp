from anagram_checker import AnagramChecker


def get_user_input():
    """
    Get a word from the user and perform data validation.

    Returns:
    str or None: The user's input word, or None if the user chooses to quit.

    """
    while True:
        word = input("Enter a word (or 'q' to quit): ").strip()
        print(word)
        if word.lower() == 'q':
            return None
        if len(word.split()) > 1:
            print("Error: Only a single word is allowed.")
            continue
        if not word.isalpha():
            print("Error: Only alphabetic characters are allowed.")
            continue
        return word


def display_anagrams(anagrams):
    """
    Display the anagrams of a word.

    Parameters:
    anagrams (list): A list of anagrams for the word.
    """
    if anagrams:
        print(f"Anagrams for your word: {', '.join(anagrams)}.")
    else:
        print("No anagrams found for your word.")


def main():
    """
    The main function that handles the user interface for the Anagram Checker.

    The user can input a word and check if it is a valid English word.
    If the word is valid, the program finds and displays all anagrams for that word.
    The program will continue to prompt the user for words until the user chooses to quit.

    """
    word_list_file = 'w3d5/Anagram Checker/text_file.txt'
    anagram_checker = AnagramChecker(word_list_file)

    print("Welcome to the Anagram Checker!")

    while True:
        word = get_user_input()
        if word is None:
            print("Exiting the program. Goodbye!")
            break

        if anagram_checker.is_valid_word(word):
            print(f"Your word: \"{word}\" is a valid English word.")
            anagrams = anagram_checker.get_anagrams(word)
            display_anagrams(anagrams)
        else:
            print(f"Your word: \"{word}\" is NOT a valid English word.")


if __name__ == "__main__":
    main()
