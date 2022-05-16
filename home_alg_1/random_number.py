# 4. Написать программу, которая генерирует в указанных пользователем границах:
"""случайное целое число; случайное вещественное число; случайный символ."""
import random


# случайное целое число;
def random_number(start, end):
    print(random.randrange(start, end))


random_number(start=int(input('введите начало диапазона: ')), end=int(input('введите конец диапазона: ')))


# случайное вещественное число;
def random_real_number(start, end):
    print(random.uniform(start, end))


random_real_number(start=float(input('введите начало диапазона: ')), end=float(input('введите конец диапазона: ')))


# случайный символ.

def random_symbol(start, end):
    symbol = random.randrange(ord(start), ord(end))
    print(chr(symbol))


random_symbol(start=str(input('введите начало деапазона случайной буквы: ')),
              end=str(input('введите начало деапазона случайной буквы: ')))
