from random import randint

lst_num = [randint(-20, -5) for i in range(20)]

max_num = 0

for i in lst_num:
    if i < max_num:
        max_num = i

print(max_num)
