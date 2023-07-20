import random

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


# ADVANCED

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728


def find_number_of_couples(numbers, target):
    count = 0
    seen = set()

    for num in numbers:
        complement = target - num
        if complement in seen:
            count += 1
        seen.add(num)

    return count


result = find_number_of_couples(list_of_numbers, target_number)
print(f"Number of couples of numbers that sum to {target_number}: {result}")
