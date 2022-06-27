# 7.
n = int(input('Введите число n = '))
array = []
nf = (n * (n + 1)) / 2
while n > 0:
    array.append(n)
    n -= 1
print(f'Сумма последовательных чисел 1 + 2 + 3 + ...n = {sum(array)}')
print(f'Сумма чисел по формуле n(n+1)/2 = {nf}')
