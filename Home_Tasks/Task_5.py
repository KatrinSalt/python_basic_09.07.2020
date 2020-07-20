"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.

Выполнено Салтыковой Екатериной.
19.07.20.
"""


def is_number(a):
    try:
        float(a)
        return True
    except ValueError:
        return False


def my_func(values):
    s_sum = 0
    for val in values:
        if is_number(val):
            val = float(val)
            s_sum += val
        else:
            return s_sum, False
    return s_sum, True


result_sum = 0
should_continue = True
while should_continue:
    user_list = input('Введите несколько чисел через пробел: \n').split()
    (mid_sum, should_continue) = my_func(user_list)
    result_sum += mid_sum
    print(f'Сумма введенных чисел равна: {result_sum}')
else:
    print('Ввод данных завершен.')


