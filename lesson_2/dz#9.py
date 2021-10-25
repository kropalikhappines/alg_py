a = '45672 5791237 824021 3218472838 2145263'.split()

def sum_num(num):
    summ = 0
    for i in num:
        summ += int(i)
    return summ
max_number = 0
max_summ = 0

for i in a:
    if sum_num(i) > max_summ:
        max_number = i
        max_summ = sum_num(i)

print(f'У числа {max_number} самая большая максимальная сумма {max_summ}')
