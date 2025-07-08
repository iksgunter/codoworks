# ### Задание 3. Полиморфизм
# Создайте базовый класс Shape с методом area() и perimeter() (возвращает 0 по умолчанию).
# Создайте подклассы:
# - Rectangle (по width, height);
# - Circle (по radius).
# Продемонстрируйте работу полиморфизма: создайте список фигур и выведите площадь и периметр каждой из них
# с помощью одного и того же кода.
import math

class Shape:
    def area(self):
        return 0

    def perimetr(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimetr(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimetr(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)


lst_shapes = [Rectangle(2, 4), Circle(5)]
for shape in lst_shapes:
    print(f"Площадь: {shape.area()} Периметр: {shape.perimetr()}")

