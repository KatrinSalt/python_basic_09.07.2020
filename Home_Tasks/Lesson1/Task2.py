"""
HomeWork
Lesson 1
Done by Saltykova Ekaterina
"""

seconds = int(input("Привет! Введи пожалуйста время в секундах:\n"))
result1 = f'Ты ввел {seconds} секунд. Это время переконвертируется в формат чч:мм:сс.'
print(result1)

# переводим в часы
hours = seconds//3600
# переводим в минуты
minutes = (seconds - hours*3600)//60
seconds = seconds % 60
result2 = f'Время в новом формате: {hours}:{minutes}:{seconds}'
print(result2)




