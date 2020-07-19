"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

Выполнено Салтыковой Екатериной.
19.07.20.
"""

arg_1, arg_2 = input('Введите два числа через пробел:\n').split()

while True:
    if arg_1.isdigit() and arg_2.isdigit():
        arg_1, arg_2 = float(arg_1), float(arg_2)
        break
    print('Ошибка ввода. Введенные вами аргументы не являются числами. Повторите ввод.')


def my_div(a, b):
    """
    Функция осуществляет деление двух чисел друг на друга.
    :param a: float
    :param b: float
    :return: float
    """
    if b == 0:
        return
    result = a / b
    return result


if my_div(arg_1, arg_2) is not None:
    print(f'Результат деления: {my_div(arg_1, arg_2):.2f}')
else:
    print('Деление на ноль невозможно. Введите в качестве второго аргумента другое число.')




