"""
Узнайте у пользователя число n. Найдите сумму чисел n+nn+nnn.
Например, пользователь ввел число 3. Считаем 3 + 33 + 333 = 369.
Done by Saltykova Ekaterina
"""

while True:
    user_input = input('Please, enter any natural number\n')
    if user_input.isdigit():
        user_num = int(user_input)
        break
    print('The input is not a number')
# считаем кол-во чисел в введенном числе
cnt = 0
tmp = user_num
while tmp:
    tmp //= 10
    cnt += 1
nn_div = 10 ** cnt + 1
nnn_div = 10 ** (cnt * 2) + nn_div
result1 = user_num + (user_num * nn_div) + (user_num * nnn_div)
print(result1)


print('#'*20)
# another (easier) solution
while True:
    user_input = input('Please, enter any natural number\n')
    if user_input.isdigit():
        break
    print('The input is not a number')
result2 = int(user_input) + int(user_input*2) + int(user_input*3)
print(result2)
