# Алгоритмы и структуры данных на Python. Базовый курс
Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# Урок 2. Циклы. Рекурсия. Функции.
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
# Урок 3. Массивы. Кортежи. Множества. Списки.
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
4. Определить, какое число в массиве встречается чаще всего.
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Урок 4. Эмпирическая оценка алгоритмов на Python
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
# Урок 5. Коллекции. Список. Очередь. Словарь.
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Урок 6. Работа с динамической памятью
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.
# Урок 7. Алгоритмы сортировки
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
# Урок 8. Деревья. Хэш-функция
1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
