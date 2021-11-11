num = int(input('Введите число: '))
num_2 = 25
num_3 = 21

if num > num_2 and num < num_3:
    print(f'{num} среднее число')
elif num_2 > num and num_2 < num_3:
    print(f'{num_2} среднее число')
else:
    print(f'{num_3} среднее число')