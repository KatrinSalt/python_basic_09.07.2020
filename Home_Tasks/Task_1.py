"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.

Выполнено Салтыковой Екатериной.
28.07.20
"""
import os
from pathlib import Path

path = Path(os.path.dirname(__file__), 'task1.txt')
print(__file__)
print(path)
#file_path = os.path.join(os.path.dirname(__file__), 'task1.txt')
#file_name = input('Введите имя файла:\n')

#with open(f'{file_name}.txt', 'w') as user_file:
with open(path, 'w', encoding='UTF-8') as user_file:
    while True:
        user_input = input('Введите любой текст: \n')
        if len(user_input) == 0:
            break
        user_file.write(f'{user_input}\n')



# with open("user_text.txt", "r") as user_file:
#     content = user_file.read()
#     print(content)
