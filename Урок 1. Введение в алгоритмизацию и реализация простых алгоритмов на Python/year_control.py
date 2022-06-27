# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
def year_control(year):
    if year % 4 != 0:
        print("Обычный")

    elif year % 100 == 0:
        if year % 400 == 0:
            print("Високосный")
        else:
            print("Обычный")
    else:
        print("Високосный")


year_control(year=int(input('введите год: ')))