# 6. staticmethod, classmethod, property
# Создайте класс Temperature, который хранит температуру в градусах Цельсия, но:
# умеет создавать объект из градусов Фаренгейта (@classmethod),
# вычисляет температуру в Кельвинах как свойство (@property),
# предоставляет статический метод для проверки, является ли температура точкой замерзания воды (0°C или ниже).


class Temperature:
    def __init__(self, celcia):
        self.celcia = celcia

    @classmethod
    def from_farenheit(cls, farenheit):
        celcia = (farenheit - 32) * 5 / 9
        return cls(celcia)

    @property
    def kelvin(self):
        return self.celcia + 273.15

    @staticmethod
    def is_freezing(celcia):
        return celcia <= 0


temp1 = Temperature(28)
temp2 = Temperature.from_farenheit(240)
print(temp1.kelvin)
print(temp2.kelvin)
print(temp1.is_freezing(10))
print(Temperature.is_freezing(0))
