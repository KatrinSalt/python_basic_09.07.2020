"""
Пользователь вводит целое положительное число. Найдите самую
большую цифру в числе. Для решения используйте цикл while и
аримфетические операции.
Done by Saltykova Ekaterina
"""

while True:
    user_num = input('Please, enter any natural number.\n')
    if user_num.isdigit():
        user_num = int(user_num)
        break
    print('The input is not a number')

max_dig = 0
while user_num and max_dig != 9:
    digit = user_num % 10
    if digit > max_dig:
        max_dig = digit
    user_num //= 10

print(f'The biggest digit in your number is: {max_dig}')
