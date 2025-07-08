# 5. SOLID (I)
# Представьте интерфейс Animal с методами: fly(), run(), swim().
# Реализуйте Lion(), которая умеет только бегать, не заставляя её реализовывать ненужные методы.
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def swim(self):
        pass


class Run(ABC):
    @abstractmethod
    def run(self):
        pass


class Lion(Run):
    def run(self):
        return 'runs!'


lion1 = Lion()
print(lion1.run())
