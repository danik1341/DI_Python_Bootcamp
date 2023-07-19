def decrypt_matrix(matrix_str):
    rows = matrix_str.split('\n')
    max_length = max(len(row) for row in rows)

    for i in range(len(rows)):
        rows[i] = rows[i].ljust(max_length)

    message = ""

    for col in range(len(rows[0])):
        for row in rows:
            char = row[col]
            if char.isalpha():
                message += char
            else:
                message += " "

    return message.strip()


matrix = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

decrypted_message = decrypt_matrix(matrix)
print("Decrypted message:", decrypted_message)
