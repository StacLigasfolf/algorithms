#  9.
while True:
    try:
        n = int(input('Введите число ("0" - stop): '))
        if n == 0:
            print('Завершение работы')
            break
        max_s = 0
        max_m = 0
        while n != 0:
            m = n
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            if s > max_s:
                max_s = s
                max_m = m
            n = int(input(f'Введите число ("0" - stop): '))
        print('Число', max_m, 'имеет максимальную сумму цифр:', max_s)
    except ValueError:
        print('ОШИБКА!!! ИСПОЛЬЗУЙТЕ ТОЛЬКО НАТУРАЛЬНЫЕ ЧИСЛА')
