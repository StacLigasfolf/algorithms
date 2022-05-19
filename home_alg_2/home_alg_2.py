# 2.
while True:
    try:
        user_number = int(input('Введите натуральное число: '))
        if user_number == 's':
            print('завершение работы')
            break
        even = odd = 0
        while user_number > 0:
            if user_number % 2 == 0:
                even += 1
            else:
                odd += 1
            user_number = user_number // 10
        print("четных - %d, нечетных - %d" % (even, odd))
    except ValueError:
        print('ОЩИБКА!!! ИСПОЛЬЗУЙТЕ ТОЛЬКО НАТУРАЛЬНЫЕ ЧИСЛА')
