# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)
def comparison(a, b, c):
    try:
        if a > b > c or a < b < c:
            print(f'среднее число b = {b}')
        elif b > c > a or b < c < a:
            print(f'среднее число c = {c}')
        elif c > a > b or c < a < b:
            print(f'среднее число a = {a}')
    except ValueError:
        print('ОШИБКА!!!: вводите только числа')


comparison(a=float(input('Введите число a: ')), b=float(input('Введите число b: ')),
           c=float(input('Введите число c: ')))