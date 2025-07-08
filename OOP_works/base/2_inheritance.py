# ### Задание 2. Наследование
# Создайте базовый класс Employee с атрибутами name, position, salary и методом get_info().
# Создайте подклассы:
# - Developer, у которого есть доп. атрибут programming_language;
# - Manager, у которого есть список подчинённых (employees).
# Каждый подкласс должен переопределять метод get_info().

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f"Имя: {self.name}, позиция: {self.position}, зарплата {self.salary}"


class Developer(Employee):
    def __init__(self, name, position, salary, programming_language):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def get_info(self):
        return f"{super().get_info()}, язык программирования: {self.programming_language}"


class Manager(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position, salary)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_info(self):
        employee_names = ', '.join(emp.name for emp in self.employees)
        return f"{super().get_info()}, сотрудники: {employee_names if employee_names else 'Сотрудников нет.'}"


dev1 = Developer('Петя', 'Бэкенд', 1000000, 'Python')
dev2 = Developer('Сеня', 'Мобилка', 750000, 'Swift')

man1 = Manager('Максим', 'Манагер', 250000)
man1.add_employee(dev1)
man1.add_employee(dev2)

print(dev1.get_info())
print(dev2.get_info())
print(man1.get_info())