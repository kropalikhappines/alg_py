import random
num = random.randint(1, 100)
print(num)
count = 0
user_count = 10

while count != user_count:
    print(f'Попытка №{count + 1} из {user_count}')

    user_inp = int(input())

    if num > user_inp:
        print('Введите больше')
    elif num < user_inp:
        print('Введите меньше')

    count += 1

    if num == user_inp:
        print('Угаданно')
    elif count == user_count:
        print(f'Попытки исчерпаны, загаданное число {num}')
