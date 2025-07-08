# 1. Singleton
# Условия:
# Реализуйте класс Logger с использованием паттерна Singleton, чтобы гарантировать, что в программе существует только один экземпляр логгера.
# Класс должен:
# - Иметь метод log(self, message: str), который добавляет сообщение в список логов.
# - Иметь метод get_logs(self), который возвращает список всех сообщений.
# - Покажите, что два экземпляра Logger — это один и тот же объект.
# Технические требования:
# - Реализация должна быть написана вручную, не использовать сторонние библиотеки.
# - Singleton можно реализовать через `__new__`, декоратор или метакласс (на выбор).
# Пример использования
# logger1 = Logger()
# logger2 = Logger()
# logger1.log("First message")
# logger2.log("Second message")
# assert logger1 is logger2, "Logger is not a singleton!"
# assert logger1.get_logs() == ["First message", "Second message"]


class Logger:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        self.list_logs = []

    def log(self, message: str):
        self.list_logs.append(message)

    def get_logs(self):
        return self.list_logs


logger1 = Logger()
logger2 = Logger()
logger1.log('First message')
logger2.log('Second message')
assert logger1 is logger2, "Logger is not a singleton!"
assert logger1.get_logs() == ["First message", "Second message"]
