from translate import Translator


def translate_to_english(french_words):
    translator = Translator(from_lang='fr', to_lang='en')
    translations = {}

    for word in french_words:
        english_word = translator.translate(word)
        translations[word] = english_word

    return translations


french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translations = translate_to_english(french_words)

print(translations)
