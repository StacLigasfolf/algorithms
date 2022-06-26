# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
import random

array = []
for i in range(10):
    array.append(random.randrange(1, 100))

mi = array.index(min(array))
ma = array.index(max(array))
print(array)
i = 0
if mi < ma:
    print(f'min = {min(array)}, max = {max(array)}, Сумма = {sum(array[mi + 1:ma])}')
else:
    print(f'min = {min(array)}, max = {max(array)}, Сумма = {sum(array[ma + 1:mi])}')
