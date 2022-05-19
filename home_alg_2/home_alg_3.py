# 3.
while True:
    try:
        user_number = int(input('Введите натуральное число: '))
        un_2 = 0
        if user_number == '0000':
            break
        while user_number > 0:
            un_r = user_number % 10
            user_number = user_number // 10
            un_2 = un_2 * 10
            un_2 = un_2 + un_r
        print(f'Число наоборот : {un_2}')
    except ValueError:
        print('ОШИБКА!!! ИСПОЛЬЗУЙТЕ ТОЛЬКО НАТУРАЛЬНЫЕ ЧИСЛА')

