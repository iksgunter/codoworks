# ### Задание 4. Абстракция и интерфейс
# Используйте модуль abc.
# Создайте абстрактный класс Transport с абстрактными методами:
# - start_engine(),
# - stop_engine(),
# - move().
# Создайте классы Car и Boat, реализующие интерфейс Transport.
from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Car(Transport):
    def start_engine(self):
        print('Car start engine')

    def stop_engine(self):
        print('Car stop engine')

    def move(self):
        print('Car is moving')


class Boat(Transport):
    def start_engine(self):
        print('Boat start engine')

    def stop_engine(self):
        print('Boat stop engine')

    def move(self):
        print('Boat is sailing')
