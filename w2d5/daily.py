# 1)

intput_str = input('Enter comma-separated words: ')
words = intput_str.split(',')

sorted_words = sorted(words)

output_str = ','.join(sorted_words)
print(output_str)

print('/////////////////////////////////////////')


# 2)

def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest
