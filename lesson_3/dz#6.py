from random import randint

lst_num = [randint(1, 20) for i in range(20)]

max_idx = 0
min_idx = 0
step = 1
summa = 0

for i in lst_num:
    if lst_num[min_idx] > i:
        min_idx = lst_num.index(i)
    elif lst_num[max_idx] < i:
        max_idx = lst_num.index(i)

if max_idx - min_idx < 0:
    step = -1

for b in lst_num[min_idx + step:max_idx:step]:
    summa += b
print(summa)

print(lst_num)
