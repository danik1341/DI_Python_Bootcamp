# 1)

word = input("Enter a word: ")
letter_indexes = {}

for index, letter in enumerate(word):
    if letter in letter_indexes:
        letter_indexes[letter].append(index)
    else:
        letter_indexes[letter] = [index]

print(letter_indexes)

# 2)

items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20",
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2",
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200"
}

wallet = input("Enter the amount of money in your wallet: ")

affordable_items = []

for item, price in items_purchase.items():
    item_price = int(price.strip("$").replace(",", ""))
    if item_price <= int(wallet.strip("$")):
        affordable_items.append(item)

if affordable_items:
    affordable_items.sort()
    print(affordable_items)
else:
    print("Nothing")
