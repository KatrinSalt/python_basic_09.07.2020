"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

Выполнено Салтыковой Екатериной.
28.07.20
"""

import os
from pathlib import Path

file_path = Path(os.path.dirname(__file__), 'task5.txt')

with open(file_path, 'w+', encoding='UTF-8') as file:
    numbers = [67, 89, 7, 2, 17, 23]
    file.write(' '.join(map(str, numbers)))
    file.seek(0)
    line = file.readline()
    my_sum = sum(map(int, line.split()))
    print(my_sum)





