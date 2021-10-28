from random import randint

lst_num = [randint(1, 100) for i in range(21)]

print(lst_num)

min_num = lst_num[0]
max_num = lst_num[1]

for idx, i in enumerate(lst_num):
    if i > max_num:
        max_num = i
        max_id = idx
    elif i < min_num:
        min_num = i
        min_id = idx


lst_num[min_id] = max_num
lst_num[max_id] = min_num

print(lst_num)
