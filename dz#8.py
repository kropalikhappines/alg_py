year = int(input())

if year % 400 == 0:
    print('Год високосный')
elif year % 100 == 0 and year % 400 != 0:
    print('Невисокосный')
elif year % 4 == 0 and year % 100 != 0:
    print('Високосный')
else:
    print('Невисокосные')
