"""
Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).

Выполнено Салтыковой Екатериной
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')
        return self.name, self.surname

    def get_total_income(self):
        income = 0
        for value in self.__income.values():
            income += value
        print(f'Полная заработная плата сотрудника: {income}')
        return income


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)


worker = Position('Илья', 'Абрамович', 'официант', 20000, 5000)
worker.get_full_name()
worker.get_total_income()



