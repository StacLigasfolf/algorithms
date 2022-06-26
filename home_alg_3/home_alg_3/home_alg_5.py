# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random
# Возможно перемудрил с заполнением массива но все работает как надо:/
array = [(-1) ** random.randint(1, 2) * random.randint(1, 100) for i in range(10)]

index = -1
i = 0
while i < len(array):
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array[i] > array[index]:
        index = i
    i += 1
print(array)
print(f'место: {index + 1} - число: {array[index]}')
