num = input('Введите трехзначное число: ')
# Тут использование цикла for

sum = 0
proiz = 1

for i in num:
    sum += int(i)
    proiz *= int(i)

print(f'Сумма чисел {sum} и произвидение чисел {proiz}')
# Не используя цикл, линейный алгоритм
a = int(num) // 100
b = int(num) // 10 % 10
c = int(num) % 10

print(f'Сумма чисел {num}: {a + b + c}, произведение чисел {num}: {a * b * c}')