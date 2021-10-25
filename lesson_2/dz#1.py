class MyOperator(Exception):
    def __init__(self):
        pass


while True:
    operator = input('Введите оператор("+" "-" "*" "/") или "0" чтобы завершить программу: ')
    try:
        if operator != '-' and operator != '+' and operator != '*' and operator != '/' and operator != '0':
            raise MyOperator
    except MyOperator:
        print('Не верный оператор!')
        continue
    if operator == '0':
        print('Конец!')
        break

    else:
        try:
            num_1, num_2 = input('Введите два числа через пробел: ').split()
        except ValueError:
            print('Два значения через пробел!')
            continue
        try:
            if operator == '+':
                print(int(num_1) + int(num_2))
            elif operator == '-':
                print(int(num_1) - int(num_2))
            elif operator == '*':
                print(int(num_1) * int(num_2))
            elif operator == '/':
                try:
                    print(int(num_1) / int(num_2))
                except ZeroDivisionError:
                    print('На ноль не делится!')
        except ValueError:
            print('Только числа!')
