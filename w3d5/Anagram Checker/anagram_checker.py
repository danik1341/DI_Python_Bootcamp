class AnagramChecker:
    def __init__(self, text_file):
        """
        Initialize the AnagramChecker instance with a text file containing valid English words.

        Parameters:
        text_file (str): The path to the text file containing the list of valid English words.

        Attributes:
        word_list (set): A set containing valid English words read from the text file.

        """
        with open(text_file, 'r') as file:
            self.word_list = set(word.strip().lower() for word in file)

    def is_valid_word(self, word):
        """
        Check if a given word is a valid English word.

        Parameters:
        word (str): The word to be checked.

        Returns:
        bool: True if the word is a valid English word, False otherwise.

        """
        return word.lower() in self.word_list

    def is_anagram(self, word1, word2):
        """
        Check if two words are anagrams of each other.

        Parameters:
        word1 (str): The first word to be compared.
        word2 (str): The second word to be compared.

        Returns:
        bool: True if the words are anagrams, False otherwise.

        """
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        """
        Find all anagrams for a given word.

        Parameters:
        word (str): The word to find anagrams for.

        Returns:
        list: A list containing all anagrams of the given word.

        """
        anagrams = [w for w in self.word_list if self.is_anagram(word, w)]
        return anagrams
