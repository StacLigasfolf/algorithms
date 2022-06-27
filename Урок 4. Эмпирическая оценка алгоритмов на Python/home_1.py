# 1 Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
import cProfile
from random import random

'''по условию ДЗ нужно было взять с предыдущих заданий, но у меня везде получается 0, вывод: алгоритмы слишком маленькие'''


def max():
    N = 15
    arr = [0] * N
    for i in range(N):
        arr[i] = int(random() * 20)
    print(arr)

    num = arr[0]
    max_frq = 1
    for i in range(N - 1):
        frq = 1
        for k in range(i + 1, N):
            if arr[i] == arr[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = arr[i]

    if max_frq > 1:
        print(max_frq, 'раз(а) встречается число', num)
    else:
        print('Все элементы уникальны')


def max_once():
    array = [2, 10, 4, 2, 32, 10, 2, 43, 2]
    print(array)
    i = 0
    for i in range(len(array)):
        num = 0
        for a in range(len(array)):
            if array[i] == array[a]:
                num += 1

        print(f'Число {array[i]} встречается в количестве {num} шт.')


if __name__ == '__main__':
    max_once()
    cProfile.run('max_once')
    max()
    cProfile.run('max()')
