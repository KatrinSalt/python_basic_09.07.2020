"""
Запросите у пользователя значение выручки и издержки фирмы. Определите, с каким финансовым резульатом работает фирма:
прибыль - выручка больше издержек, или убыток - издержки больше выручки. Выведете соответсвующее сообщение. Если
фирма отработала прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность
сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
Done by Saltykova Ekaterina
"""

while True:
    revenue = input('Please, enter the revenue of the company\n')
    cost = input('Please, enter the expenses of the company\n')
    if revenue.isdigit() and cost.isdigit():
        revenue = int(revenue)
        cost = int(cost)
        break
    print('The input values are not numbers')

if revenue > cost:
    ratio = revenue/cost
    employee = int(input('Please enter the amount of employees in your company\n'))
    result = revenue / employee
    print(f'The revenue per employee is: {result:.2f}')
    print(f"Congrats, you've been working good lately: revenue exceeds expenses."
          f"The revenue profitability is: {ratio:.2f}")

elif revenue < cost:
    print(" Too bad. Seems like you don't have money left. Your expenses exceeds revenue.")
else:
    print('No revenue nor expenses.')

employee = int(input('Please enter the amount of employees in your company\n'))
result = revenue / employee
print(f'The revenue per employee is: {result:.2f}')





