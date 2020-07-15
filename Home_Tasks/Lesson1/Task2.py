"""
Пользователь вводит время в секундах. Переведите время
в часы, минуты и секунды и выведете в формате чч:мм:сс.
Используйте форматирование строк.
Done by Saltykova Ekaterina
"""

while True:
    user_time = input("Привет! Введи пожалуйста время в секундах:\n")
    if user_time.isdigit():
        user_time = int(user_time)
        print(f'Ты ввел {user_time} секунд. Это время переконвертируется в формат чч:мм:сс.')
        break
    print ('Ошибка ввода, это не число')

hours = user_time//3600 # переводим в часы
minutes = (user_time - hours*3600)//60  # переводим в минуты
seconds = user_time % 60
result2 = f'Время в новом формате: {hours:>02}:{minutes:>02}:{seconds:>02}'
print(result2)




