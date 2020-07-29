"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

Выполнено Салтыковой Екатериной.
28.07.20
"""
import os
from pathlib import Path

file_path = Path(os.path.dirname(__file__), 'task4_russian.txt')

with open('task4.txt', 'r') as old_file:
    numbers = ['Один', 'Два', 'Три', 'Четыре']
    i = 0
    while i < len(numbers):
        for line in old_file:
            content = line.split()
            content[0] = numbers[i]
            print(type(content))
            with open(file_path, 'a', encoding='UTF-8') as new_file:
                new_file.write(' '.join(content)+'\n')
            i += 1



