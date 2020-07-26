"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
Выполнено Салтыковой Екатериной.
23.07.2020
"""

from itertools import count, cycle

my_list = []
for el in count(1):
    if el > 10:
        break
    my_list.append(el)
print(my_list)

list_1 = [1, 4, 6, 23, 54, 78]
list_2 = []
i = 0
for el in cycle(list_1):
    if i >= len(list_1):
        break
    list_2.append(el)
    i += 1
print(list_2)
