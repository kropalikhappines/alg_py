letter = int(input('Введите номер буквы: '))
alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
index_letter = alphabet[letter - 1]
print(index_letter)
