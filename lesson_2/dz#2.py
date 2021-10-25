a = input('Введите число: ')
even = []
uneven = []
count_even = 0
count_uneven = 0
for i in a:
    try:
        i = int(i)
    except ValueError:
        print('Нужно цифры')
        pass
    if i % 2 == 0:
        even.append(i)
        count_even += 1
    else:
        uneven.append(i)
        count_uneven += 1

print(f'В числе {a}, {count_even} четных чисел {even} и {count_uneven} нечетных числа {uneven}')
