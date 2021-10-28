from random import randint

lst_num = [randint(1, 10) for i in range(20)]

print(lst_num)

num_dict = dict.fromkeys(lst_num, 0)

for i in lst_num:
    num_dict[i] += 1

max_count = 0

for a in num_dict:
    if num_dict[a] > max_count:
        max_count = num_dict[a]
        key_num = a

print(key_num, max_count)
