# 1.
while True:
    try:
        sign = input('Выберите знак (+, -, *, /): ')
        if sign == '0':
            print('завершение работы')
            break
        if sign in ('+', '-', '*', '/'):
            a = float(input('Введите а = '))
            b = float(input('Введите b = '))
            if sign == '+':
                print(a + b)
            elif sign == '-':
                print(a - b)
            elif sign == '*':
                print(a * b)
            else:
                print(a / b)
        else:
            print('Пожалуйста используйте токлько эти знаки (+, -, *, /)')
    except ZeroDivisionError:
        print('Ошибка!!! ДЕЛЕНИЕ НА 0 НЕВОЗМОЖНО')
    except ValueError:
        print('ОШИБКА!!! ИСПОЛЬЗУЙТЕ ЦИФРЫ В КАЧЕСТВЕ (a, b)')
