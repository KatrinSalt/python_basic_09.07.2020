"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.

Выполнено Салтыковой Екатериной.
19.07.20.
"""
Решение 1
user_val = []

while True:
    user_val = input('Введите три числа через пробел:\n').split()
    # проверка ввода числа, но таким образом не включаются отрицательные числа
    user_val = [int(value) for value in user_val if value.isdigit()]
    if len(user_val) != 3:
        print('Вы ввели недостаточно чисел.')
        continue
    break


def my_min(values):
    min_v = values[0]
    for val in values:
        if val <= min_v:
            min_v = val
    return min_v


def my_func(my_list):
    min_v = my_min(my_list)
    my_sum = 0
    for val in my_list:
        my_sum += val
    return my_sum - min_v


print(f'Сумма наибольших двух аргументов равна: {my_func(user_val)}')

print('#' * 30)
# Решение 2

val_1, val_2, val_3 = [int(x) for x in input('Введите три числа через пробел:\n').split()]


def my_min_2(a, b, c):
    """
    Функция возвращает минимальное значение среди трех позиционных аргументов
    :param a: int
    :param b: int
    :param c: int
    :return: int
    """
    min_v = a
    if min_v >= b:
        min_v = b
    if min_v >= c:
        min_v = c
    return min_v


def my_func_2(x, y, z):
    """
    Функция возвращает сумму двух наибольших позиционных аргументов
    :param x: int
    :param y: int
    :param z: int
    :return: int
    """
    min_v = my_min_2(x, y, z)
    my_sum = (x + y + z) - min_v
    return my_sum


print(f'Сумма наибольших двух аргументов равна: {my_func_2(val_1, val_2, val_3)}')


print('#' * 30)
# Решение 3: встроенные функции

val1, val2, val3 = [int(x) for x in input('Введите три числа через пробел:\n').split()]


def my_func_3(a, b, c):
    """
    Функция возвращает сумму двух наибольших позиционных аргументов
    :param a: int
    :param b: int
    :param c: int
    :return: int
    """
    min_v = min(a, b, c)
    numbers = [a, b, c]
    my_sum = sum(numbers) - min_v
    return my_sum


print(f'Сумма наибольших двух аргументов равна: {my_func_3(val1, val2, val3)}')



