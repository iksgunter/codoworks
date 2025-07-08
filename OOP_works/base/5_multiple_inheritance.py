# ### Задание 5. Множественное наследование
# Создайте два класса:
# - Flyable, с методом fly() (выводит I'm flying!);
# - Swimmable, с методом swim() (выводит I'm swimming!).
# Создайте класс Duck, наследующий оба класса. Добавьте метод make_sound() (выводит Quack!).
# Создайте экземпляр Duck и вызовите все три метода.


class Flyable:
    def fly(self) -> str:
        return "I'm flying!"


class Swimmable:
    def swim(self) -> str:
        return f"I'm swimming!"


class Duck(Flyable, Swimmable):
    def make_sound(self) -> str:
        return f"Quack!"


duck_man = Duck()
print(duck_man.make_sound())
print(duck_man.fly())
print(duck_man.swim())
