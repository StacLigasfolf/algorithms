''' Задача № 1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python и разрядность
вашей ОС. '''

''' Версия Python: python 3.10.4 x64
ОС: Windows 10 x64 '''

import sys


def show_size(x, level=0):
    ''' Добавил в функцию сложение всех затрат памяти
        и возврат общей суммы затраченной памяти '''
    size_par = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={size_par}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                size_par = size_par + sys.getsizeof(key)
                show_size(value, level + 1)
                size_par = size_par + sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                size_par = size_par + sys.getsizeof(item)
    return size_par


# Урок 1, задача № 1. Найти сумму и произведение цифр трехзначного
# числа, которое вводит пользователь.

a = input('Введите трехзначное число: ')

x = int(a[0])
y = int(a[1])
z = int(a[2])

sum_l = x + y + z
mult = x * y * z

sum_member = sys.getsizeof(a) + sys.getsizeof(x) + sys.getsizeof(y) + sys.getsizeof(z) + sys.getsizeof(
    sum_l) + sys.getsizeof(mult)
print('В программе задействовано байт памяти: {}'.format(sum_member))

# Результат запуска программы и измерения:
#
# Введите трехзначное число: 999
#
# В программе задействовано байт памяти: 98

# ===============================================

# Урок 2, задача № 3. Сформировать из введенного числа обратное по порядку
# входящих в него цифр и вывести на экран. Например, если введено число 3486,
# то надо вывести число 6843.

new_num = ''
# show_size(new_num)

num = input('Введите число: ')
count = len(num)
k = range(count)

for i in k:
    new_num = new_num + str(int(num) % 10)
    # show_size(new_num)
    num = int(num) // 10
    # show_size(num)
print(new_num)

sum_member2 = show_size(new_num) + show_size(num) + show_size(count) + show_size(k)
print('В программе задействовано байт памяти: {}'.format(sum_member2))

# Результат запуска программы и измерения:
#
# Введите число: 123456
# 654321
# type=<class 'str'>, size=31, object=654321
# type=<class 'int'>, size=12, object=0
# type=<class 'int'>, size=14, object=6
# type=<class 'range'>, size=24, object=range(0, 6)
#	 type=<class 'int'>, size=12, object=0
#	 type=<class 'int'>, size=14, object=1
#	 type=<class 'int'>, size=14, object=2
#	 type=<class 'int'>, size=14, object=3
#	 type=<class 'int'>, size=14, object=4
#	 type=<class 'int'>, size=14, object=5
#
# В программе задействовано байт памяти: 163
#
# ЗАМЕТКА: в программе у нас количество цифр в вводимом числе неограничено, поэтому
# затраты памяти напрямую зависят от того, какой длинны число будет введено (из него формируется список).
# При вводе 0123456789 результат будет: 223 байт.
# При вводе 01234567890123456789 результат будет уже : 373 байт.
# Также следует отметить, что вначале работы программы new_num и num имеют иные размер памяти, но в сумме меньшие, чем в конце.

# ===============================================

# Урок 2, задача № 2. Во втором массиве сохранить индексы четных элементов первого
# массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во
# второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 – если
# индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

g = range(9)

mas_num = [random.randint(1, 100) for n in g]
print('Дан массив элементов: {}'.format(mas_num))

mas_index = [mas_num.index(i) for i in mas_num if i % 2 == 0]
print('Массив индексов четных элементов: {}'.format(mas_index))

sum_member3 = show_size(mas_num) + show_size(num) + show_size(g)
print('В программе задействовано байт памяти: {}'.format(sum_member3))

# Результат запуска программы и измерения:
#
# Дан массив элементов: [75, 16, 100, 43, 76, 49, 25, 34, 83]
# Массив индексов четных элементов: [1, 2, 4, 7]
# type=<class 'list'>, size=100, object=[75, 16, 100, 43, 76, 49, 25, 34, 83]
#	 type=<class 'int'>, size=14, object=75
#	 type=<class 'int'>, size=14, object=16
#	 type=<class 'int'>, size=14, object=100
#	 type=<class 'int'>, size=14, object=43
#	 type=<class 'int'>, size=14, object=76
#	 type=<class 'int'>, size=14, object=49
#	 type=<class 'int'>, size=14, object=25
#	 type=<class 'int'>, size=14, object=34
#	 type=<class 'int'>, size=14, object=83
# type=<class 'int'>, size=12, object=0
# type=<class 'range'>, size=24, object=range(0, 9)
#	 type=<class 'int'>, size=12, object=0
#	 type=<class 'int'>, size=14, object=1
#	 type=<class 'int'>, size=14, object=2
#	 type=<class 'int'>, size=14, object=3
#	 type=<class 'int'>, size=14, object=4
#	 type=<class 'int'>, size=14, object=5
#	 type=<class 'int'>, size=14, object=6
#	 type=<class 'int'>, size=14, object=7
#	 type=<class 'int'>, size=14, object=8
#
# В программе задействовано байт памяти: 386
#
# ЗАМЕТКА: так как в данной программе фиксированные размеры массивов и в массивы не будут попадать нули
# в качестве значений, объем памяти будет всегда одинаковым - 386 байт.

# ===============================================

''' ИТОГ: Судя по данным, программы с наиболее эффективным использованием памяти - это первая и третья,
так как их потребление памяти будет константным и предсказуемым за счет заранее определенных размеров переменных
(в первой - число из трех цифр, во второй - фиксированный размер массива). Менее всего памяти требует первая программа.
Вторая программа целиком зависит от количества цифр, из которых будет состоять введенное число. '''
