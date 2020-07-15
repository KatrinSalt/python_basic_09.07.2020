"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Done by Saltykova Ekaterina
"""

while True:
    a = input('Enter the amount of kilometers the runner runs today per day\n')
    b = input('Enter the amount of kilometers the runner wish to run per day\n')
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        break
    print('Entered values are not numbers')

day = 1
while a <= b:
    a *= 1.1
    day += 1
print(f'The progress is achieved on day {day}')
