matrix = []

for i in range(4):
    matrix.append([])
    summ = 0

    for n in range(4):
        user_number = int(input(f'Введите число {i+1} и {n+1} столбца: '))
        summ += user_number
        matrix[i].append(user_number)

    matrix[i].append(summ)

for a in matrix:
    print(('{:>4d}' * 5).format(*a))
