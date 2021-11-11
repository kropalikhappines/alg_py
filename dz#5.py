letter = input('Введите первую букву: ').upper()
letter_1 = input('Введите вторую букву: ').upper()
alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
index_letter = alphabet.index(letter) + 1
index_letter_1 = alphabet.index(letter_1) + 1
print(f'Буква {letter} стоит на {index_letter}, буква {letter_1} стоит на {index_letter_1}')
print(f'Между ними {abs(index_letter - index_letter_1) - 1} букв')
