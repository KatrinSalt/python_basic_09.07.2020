"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

Выполнено Салтыковой Екатериной.
23.07.2020
"""

from sys import argv

script_name, work_hours, rate_per_hour, bonus = argv


def is_number(a, b, c):
    try:
        int(a)
        int(b)
        int(c)
        return True
    except ValueError:
        return False


def employee_salary(hours, rate, bon):
    salary = (hours * rate) + bon
    return f"Зарплата сотрудника: {salary}"


def my_func(hours, rate, bon):
    if is_number(hours, rate, bon) is True:
        hours = int(hours)
        rate = int(rate)
        bon = int(bon)
        print(employee_salary(hours, rate, bon))
    else:
        print('Ошибка ввода. Введенные значения не являются числами. Повторите ввод.')


my_func(work_hours, rate_per_hour, bonus)






