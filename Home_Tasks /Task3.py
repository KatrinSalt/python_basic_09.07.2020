"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.

Выполнено Салтыковой Екатериной
15.07.20
"""

month = input('Введите любой месяц в виде целого числа от 1 до 12\n')
while True:
    if month.isdigit():
        month = int(month)
        break
    print('Ошибка ввода. Введеное вами значение не является числом. Попробуйте еще раз.')

# Решение через list
my_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
position = my_list.index(month)
if position < 3:
    print('Зима')
elif position < 6:
    print('Весна')
elif position < 9:
    print('Лето')
else:
    print('Осень')

print('#'*30)
# Решение через dict
month_new = input('Input any month as a number from 1 to 12\n')
while True:
    if month_new.isdigit():
        month_new = int(month_new)
        break
    print('Error. The input is not a digit. Try again.')

my_dict = {12: 'Winter', 1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer',
       8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn'}

season = my_dict.get(month_new)
print(season)

