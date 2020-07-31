"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color
(цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.

Выполнено Салтыковой Екатериной.
31.07.2020
"""
import time


class Colour:
    name = ""
    duration = 0
    __colours = ["Red", "Yellow", "Green"]

    def __init__(self, name):
        if name not in self.__colours:
            print(f'{name} is invalid input colour')
            return
        self.name = name
        self.update_duration()

    def update_duration(self):
        if self.name == "Red" or self.name == "Green":
            self.duration = 7
        elif self.name == "Yellow":
            self.duration = 2

    def next_colour(self):
        if self.name == "Red":
            self.name = "Yellow"
        elif self.name == "Yellow":
            self.name = "Green"
        elif self.name == "Green":
            self.name = "Red"

        time.sleep(self.duration)
        self.update_duration()


class TrafficLight:

    __colour = Colour("Red")

    def __init__(self, colour):
        self.__colour = colour

    def running(self):
        i = 0
        while i < 6:
            print(self.__colour.name)
            self.__colour.next_colour()
            i += 1


a = TrafficLight(Colour("Red"))
a.running()




