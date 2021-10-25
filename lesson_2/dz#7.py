n = int(input('Введите размер последовательности, для проверки выражения 1+2+...+n = n(n+1)/2: \nn = '))
summa = 0
for i in range(1, n + 1):
    summa += i
if summa == n * (n + 1) / 2:
    print('Выражение верно')
else:
    print('Выражение неверно')

