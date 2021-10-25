length = int(input('Введите длину последовательности: '))
summa = 0
for i in range(length):
    summa += 1 / (-2) ** i
    print(summa)
print(f'Сумма последовательности = {summa}')
