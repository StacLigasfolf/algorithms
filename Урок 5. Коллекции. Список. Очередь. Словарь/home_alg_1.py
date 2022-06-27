# 1  Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна
# определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше
# среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.


amount = int(input('Введите количество предприятий: '))
i = 0
average = 0
generate_key = 0
summ = 0
accounting = {}


# Задаем название компаний и их зароботок за каждый квартал и вычисляем средний за год
while i < amount:
    j = 0
    name = str(input(f'Введите название {i + 1} предприятия: '))
    while j <= 3:
        income = float(input(f'Введите прибыль за {j + 1} квартал для {name}: '))
        summ += income
        j += 1
    i += 1
    average = summ / 4
    accounting.update({name: average})
    average = 0
    summ = 0

# Вычисляем общий средний зароботок всех компаний
for k in accounting:
    generate_key += accounting[k]
average_generate = generate_key / amount
print(f'Список предприятий - {accounting}')
print(f'Средний доход всех предприятий = {average_generate}')

for v in accounting:
    if accounting[v] < average_generate:
        print(f'прибыль {v} = {accounting[v]} ниже чем {average_generate}')

    elif accounting[v] > average_generate:
        print(f'прибыль {v} = {accounting[v]} выше чем {average_generate}')


