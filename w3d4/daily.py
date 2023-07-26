import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Text:
    def __init__(self, text):
        self.text = text

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
        return cls(text)

    def word_frequency(self, word):
        words_list = self.text.split()
        word_count = words_list.count(word)
        if word_count == 0:
            return None
        else:
            return f"The word '{word}' appears {word_count} time(s) in the text."

    def most_common_word(self):
        words_list = self.text.split()
        word_counts = {}
        for word in words_list:
            word_counts[word] = word_counts.get(word, 0)
        if not word_counts:
            return None
        most_common_word = max(word_counts, key=word_counts.get)
        return f"The most common word in the text is '{most_common_word}'."

    def unique_words(self):
        words_list = self.text.split()
        unique_words_set = set(words_list)
        return list(unique_words_set)


class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)
        self.punctuation = set(string.punctuation)
        self.stop_words = set(stopwords.words('english'))

    def remove_punctuation(self):
        no_punct_text = ''.join(
            char for char in self.text if char not in self.punctuation)
        return no_punct_text

    def remove_special_characters(self):
        special_chars = set(string.punctuation).union(
            set(string.digits)).union(set(string.whitespace))
        no_special_text = ''.join(
            char for char in self.text if char not in special_chars)
        return no_special_text


text_obj = Text.from_file('w3d4/words.txt')

# Test word_frequency method
# Output: The word 'meursault' appears 84 time(s) in the text.
print(text_obj.word_frequency("meursault"))
# Output: The word 'stranger' appears 21 time(s) in the text.
print(text_obj.word_frequency("stranger"))

# Test most_common_word method
# Output: The most common word in the text is 'the'.
print(text_obj.most_common_word())

# Test unique_words method
print(text_obj.unique_words())  # Output: List of unique words in the text.

text_obj = TextModification.from_file('w3d4/words.txt')

# Test remove_punctuation method
print(text_obj.remove_punctuation())

# Test remove_stop_words method
print(text_obj.remove_stop_words())

# Test remove_special_characters method
print(text_obj.remove_special_characters())
