"""
Необходимо создать (не программно) текстовый файл, где каждая
строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

Выполнено Салтыковой Екатериной.
28.07.20
"""
import os
from pathlib import Path
file = Path(os.path.dirname(__file__), 'task6.txt')
my_dict = {}
with open(file, 'r') as inf_file:
    for line in inf_file:
        cl = line.split()
        subj = cl[0].replace(':', '')
        my_dict[subj] = cl[1:]
    print(my_dict)

    final = {}
    for key, value in my_dict.items():
        # for itm in value:
        #     tmp = itm.split('(')[0]
        #     print(tmp)
        final[key] = sum([int(itm.split('(')[0]) for itm in value if itm.split('(')[0].isdigit() ])
    print(final)




