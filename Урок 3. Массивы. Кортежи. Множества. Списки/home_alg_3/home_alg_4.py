# 4. Определить, какое число в массиве встречается чаще всего.
from random import random

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

# Это первая попытка, работает норм, просто не совсем по условиям задачи
# array = [2, 10, 4, 2, 32, 10, 2, 43, 2]
#
# i = 0
# for i in range(len(array)):
#     num = 0
#     for a in range(len(array)):
#         if array[i] == array[a]:
#             num += 1
#
#     print(f'Число {array[i]} встречается в количестве {num} шт.')
# print(array)

