# 1)

number = int(input("Enter a number: "))
length = int(input("Enter the desired length: "))

multiples = []
count = 0

while len(multiples) < length:
    count += 1
    multiple = number * count
    multiples.append(multiple)

print("Multiples of", number, "until length", length, ":", multiples)

print('/////////////////////////////////////////')

# 2)

user_word = input("Enter a word: ")
result = ""

for i in range(len(user_word)):
    if i == 0 or user_word[i] != user_word[i - 1]:
        result += user_word[i]

print("Modified word:", result)
