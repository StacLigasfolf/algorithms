# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
import string


def alf_choose(start, end):
    try:
        alf = []
        for i in string.ascii_lowercase:
            alf.append(i)
        print(f'Место первой буквы в алфавите: {alf.index(start) + 1}')
        print(f'Место второй буквы в алфавите: {alf.index(end) + 1}')
        print(f'Количество символов между этими буквами: {alf.index(end) - alf.index(start)}')
    except ValueError:
        print('ОШИБКА!!!: используйте только 1 латинскую букву на диапазон и в нижнем регистре')


alf_choose(start=str(input('введите букву: ')), end=str(input('введите букву: ')))