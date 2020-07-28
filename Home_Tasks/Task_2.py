"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.

Выполнено Салтыковой Екатериной.
27.08.20
"""

with open(r"/Users/KatrinSalt/Documents/GeekBrains/python_basic_09.07.2020/Home_Tasks/text.txt", "r") as input_file:

    lines = 0
    words = 1
    for line in input_file:
        for word in line:
            if word == " ":
                words += 1
        lines += 1
        print(f'Строка {lines} : {words} слов')
        words = 1
    print(f'Всего строк: {lines}')
