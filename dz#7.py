a = int(input('Введите первую сторону: '))
b = int(input('Введите вторую сторону: '))
c = int(input('Введите третью сторону: '))

if a < b + c and b < c + a and c < b + a:
    if a == b and b == c:
        print('Равносторонний')
    elif a == b or b == c or c == a:
        print('Равнобедренный')
    else:
        print('Разносторонний')
else:
    raise 'Вырожденный'
