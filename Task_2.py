"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Выполнено Салтыковой Екатериной.
19.07.20.
"""

user_name = input('Please enter your name:\n')
user_surname = input('Please enter your surname:\n')
user_date = input('Please enter your date of birth:\n')
user_city = input('Please enter your the name of the city where you live:\n')
user_email = input('Please enter your email:\n')
user_phone = input('Please enter your phone:\n')


def user_info(**kwargs):
    """
    The function is returning the user information
    :param kwargs: str
    :return: dict
    """
    return kwargs


result = ""
for key, value in user_info(name=user_name, surname=user_surname, date_of_birth=user_date,
                            city=user_city, email=user_email, phone=user_phone).items():
    result += f'{key}:{value}  '

print(result)
