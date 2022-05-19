# 6.
import random

number = random.randrange(1, 101)
i = 10
try:
    while i > 0:
        user = int(input(f'Угадайте число осталось {i} попыток: '))
        if user < number:
            print('Загаданное число больше')
        elif user > number:
            print('Загаданное число меньше')
        else:
            print(f'Вы угадали это было число - {number}')
            break
        if i == 1:
            print(f'Вы не смогли угадать загаданное число за 10 попыток - {number}')
            break
        i -= 1
except ValueError:
    print('ОШИБКА!!! ПОЖАЛУЙСТА ИСПОЛЬЗУЙТЕ ТОЛЬКО НАТУРАЛЬНЫЕ ЧИСЛА')
