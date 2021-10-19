import random

what = input('Что хотите получить: "Число", "Вещественное", "Символ": ').capitalize()
if what == 'число':
    user_input = int(input())
    user_input_2 = int(input())
elif what == 'Вещественное':
    user_input = float(input())
    user_input_2 = float(input())
elif what == 'Символ':
    user_input = input()
    user_input_2 = input()

if isinstance(user_input and user_input_2, int):
    print(random.randint(user_input, user_input_2))
elif isinstance(user_input and user_input_2, float):
    print(random.uniform(user_input, user_input_2))
elif isinstance(user_input and user_input_2, str):
    print(chr(random.randint(ord(user_input.upper()), ord(user_input_2.upper()))))
