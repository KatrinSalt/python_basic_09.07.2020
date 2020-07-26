"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.

Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].

Результат: [23, 1, 3, 10, 4, 11]

Выполнено Салтыковой Екатериной.
23.07.2020
"""

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(my_list)
# первый вариант, к которому я пришла в последнюю очередь:

new_list = [my_list[i] for i in range(0, len(my_list)) if my_list.count(my_list[i]) == 1]
print(new_list)

# второй вариант
# def idx_to_delete(list_ex):
#     index = []
#     i = 0
#     while i < len(list_ex):
#         amount = list_ex.count(list_ex[i])
#         if amount > 1:
#             index.append(i)
#         i += 1
#     return index
#
#
# new_list = [my_list[idx] for idx in range(0, len(my_list)) if idx not in idx_to_delete(my_list)]
# print(new_list)


# третий вариант, но он первым пришел в голову
# index = []
# i = 0
# while i < len(my_list):
#     for idx in range(0, len(my_list) - 1):
#         if my_list[i] == my_list[idx]:
#             index.append(idx)
#     print(index)
#     # print(1)
#     if len(index) > 1:
#         index.reverse()
#         for j in index:
#             my_list.pop(j)
#             print(my_list)
#     else:
#         i += 1
#     index = []









