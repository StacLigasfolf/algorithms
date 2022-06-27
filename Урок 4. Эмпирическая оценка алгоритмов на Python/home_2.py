import cProfile


# Решето Эратосфена
def sieve_of_Eratosthenes(n):
    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)


# Решето Сундарама
def sieve_of_Sundaram(n):
    b = list()
    a = [0] * n

    i = k = j = 0
    while 3 * i + 1 < n:
        while k < n and j <= i:
            a[k] = 1
            j += 1
            k = i + j + 2 * i * j
        i += 1
        k = j = 0

    for i in range(1, n):
        if a[i] == 0:
            b.append(2 * i + 1)

    return b


'''Я убрал вывод простых чисел чтобы не засорять консоль, но на этом примере вижно что Решето Эратосфена работает быстрее
чем Решето Сундарама'''
if __name__ == '__main__':
    print('С помощю "Решето Эратосфена"')
    cProfile.run('sieve_of_Eratosthenes(n=150000)')
    print('C помощю "Решето Сундарама"')
    cProfile.run('sieve_of_Sundaram(n=150000)')
