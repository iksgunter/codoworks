# ### (Дополнительно) Задание 6. Комбинированное: Зоопарк
# Создайте абстрактный класс Animal с методами speak() и move().
# Создайте классы Dog, Bird, Fish. Пусть:
# - Dog говорит "Woof!" и бегает,
# - Bird говорит "Tweet!" и летает (наследует Flyable),
# - Fish молчит и плавает (наследует Swimmable).
# Положите всех животных в один список и вызовите методы speak() и move() в цикле.
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

    @abstractmethod
    def move(self) -> str:
        pass


class Swimmable:
    def move(self) -> str:
        return 'floats'


class Flyable:
    def move(self) -> str:
        return "flying"


class Dog(Animal):
    def speak(self) -> str:
        return f'Woof!'

    def move(self) -> str:
        return f"runs"


class Bird(Flyable, Animal):
    def speak(self) -> str:
        return 'Tweet!'


class Fish(Swimmable, Animal):
    def speak(self) -> str:
        return '...'


animals = [Dog(), Bird(), Fish()]

for animal in animals:
    print(animal.move(), animal.speak())
