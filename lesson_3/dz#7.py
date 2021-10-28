from random import randint

lst_num = [randint(1, 20) for i in range(20)]
print(lst_num)


def func_min_num(lst):
    min_num = lst[0]

    for i in lst:
        if i < min_num:
            min_num = i
    return lst.index(min_num)


num_1 = lst_num.pop(func_min_num(lst_num))
num_2 = lst_num.pop(func_min_num(lst_num))
print(f'Минимальные числа {num_1, num_2}')
