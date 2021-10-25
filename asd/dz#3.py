a = input('Введите число: ')
b = []

for i in a:
    b.append(i)
b.reverse()
b = ''.join(b)
print(b)
