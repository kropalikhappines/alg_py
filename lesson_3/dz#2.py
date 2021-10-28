from random import randint

lst_num = []

for i in range(1, 100):
    lst_num.append(randint(1, 100))

num = [i for i, e in enumerate(lst_num) if e % 2 == 0]
print(num)
print(lst_num)
