"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.

Выполнено Салтыковой Екатериной.
19.07.20.
"""

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


print(f'Сумма наибольших двух чисел равна: {my_func(user_val)}')


#user_val = [val for val in user_val if val != my_min(user_val)]

