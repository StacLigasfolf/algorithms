while True:
    try:
        n = int(input('введите количество чисел: '))
        if n == 0000:
            print('завершение работы')
            break
        else:
            i = 0
            a = 1
            sum = 0
            while i < n:
                sum += a
                a /= -2
                i += 1
            print(sum)
    except ValueError:
        print('ОШИБКА!!! ИСПОЛЬЗУЙТЕ ТОЛЬКО НАТУРАЛЬНЫЕ ЧИСЛА')
