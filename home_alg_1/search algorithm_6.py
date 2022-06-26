# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import string


def alf_rechoose(symbol):
    try:
        alf = []
        for i in string.ascii_lowercase:
            alf.append(i)
        print(alf[symbol - 1])
    except ValueError:
        print('ОШИБКА!!!: используйте только целые числа')


alf_rechoose(symbol=int(input('введите номер буквы в алфавите: ')))
