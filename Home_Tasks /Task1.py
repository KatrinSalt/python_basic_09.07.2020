"""
 Создать список и заполнить его элементами различных типов данных.
 Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
 Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

 Выполнено Салтыковой Екатериной
 15.07.20
"""

user_list = [46, True, 'Chalmers', False, 5.67, None]

# Solution using 'for in range'
for i in range(0, len(user_list)):
    print(user_list[i], type(user_list[i]))

print('#'*30)

# solution using 'while' loop
index = 0
while index < len(user_list):
    print(user_list[index], type(user_list[index]))
    index += 1
