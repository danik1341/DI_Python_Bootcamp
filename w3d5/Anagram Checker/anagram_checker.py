class AnagramChecker:
    def __init__(self, text_file):
        with open(text_file, 'r') as file:
            self.word_list = set(word.strip().lower() for word in file)

    def is_valid_word(self, word):
        return word.lower() in self.word_list

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        anagrams = [w for w in self.word_list if self.is_anagram(word, w)]
        return anagrams


# c1 = AnagramChecker('w3d5/Anagram Checker/text_file.txt')
# # print(c1.word_list)
# maybe = c1.is_valid_word('COUNTEROFFERS')
# print(maybe)
