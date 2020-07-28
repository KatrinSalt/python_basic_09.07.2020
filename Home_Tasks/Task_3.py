"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

Выполнено Салтыковой Екатериной.
27.08.20
"""

with open('task3.txt', 'r') as input_file:
    wage = 20000
    # workers = len(input_file.read().splitlines())
    workers = 0
    total_wage = 0
    # print(workers)
    for line in input_file:
        workers += 1
        info = line.split(':')
        if int(info[1]) < wage:
            print(info[0])
        total_wage += int(info[1])
    av_wage = total_wage/workers
    print(f'Средняя зарплата сотрудников: {av_wage}')
