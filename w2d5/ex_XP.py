import math

# Challenge 1

# 1)


def insert_item_at_index(lst, item, index):
    lst.insert(index, item)
    return lst

# 2)


def count_spaces(input_string):
    space_count = 0
    for char in input_string:
        if char == ' ':
            space_count += 1
    return space_count

# 3)


def count_upper_lower(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count


# 4)

def my_sum(arr):
    total_sum = 0

    for num in arr:
        total_sum += num

    return total_sum


# 5)

def find_max(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num

    return max_num

# 6)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 7)


def list_count(lst, target):
    count = 0
    for element in lst:
        if element == target:
            count += 1
    return count


# 8)

def norm(lst):
    sum_of_squares = sum(x ** 2 for x in lst)
    return math.sqrt(sum_of_squares)

# 9)


def is_mono(arr):
    is_ascending = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    if is_ascending:
        return True

    is_descending = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
    if is_descending:
        return True

    return False

# 10)


def longest_word(word_list):
    if not word_list:
        print("The list is empty.")
        return

    longest = word_list[0]
    for word in word_list:
        if len(word) > len(longest):
            longest = word

    print("The longest word is:", longest)


# 11)
