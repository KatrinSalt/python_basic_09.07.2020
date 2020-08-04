"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

Выполнено Салтыковой Екатериной
"""


def go():
    print('The car has started driving')


class Car:

    def __init__(self, speed: int, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car has started driving.')

    def stop(self):
        print('The car has stopped.')

    def turn(self, direction):
        print(f'The car is turning {direction}.')

    def show_speed(self):
        print(f'The current speed is {self.speed}.')


class TownCar(Car):

    def __init__(self, speed: int, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print('You exceeded the speed limit.')
        else:
            print(f'The current speed is {self.speed}.')


class SportCar(Car):

    def __init__(self, speed: int, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):

    def __init__(self, speed: int, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print('You exceeded the speed limit.')
        else:
            print(f'The current speed is {self.speed}.')


class PoliceCar(Car):

    def __init__(self, speed: int, color, name):
        super().__init__(speed, color, name, True)


if __name__ == '__main__':
    car_1 = PoliceCar(70, 'Red', 'Audi')
    car_1.go()
    car_1.stop()
    car_1.turn('Right')
    car_1.show_speed()


