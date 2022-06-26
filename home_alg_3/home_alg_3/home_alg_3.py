# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

array = []

for i in range(10):
    array.append(random.randrange(1, 100))
print(f'ДО - {array}')
mi = array.index(min(array))
ma = array.index(max(array))
array[mi], array[ma] = array[ma], array[mi]
print(f'ПОСЛЕ - {array}')
