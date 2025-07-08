# ### Задание 1. Инкапсуляция
# Создайте класс BankAccount, который инкапсулирует данные о балансе.
# Реализуйте методы:
# - deposit(amount) — пополнение счёта;
# - withdraw(amount) — снятие средств (не должно позволять уйти в минус);
# - get_balance() — получить текущий баланс.
# Баланс должен быть защищён от прямого изменения (например, `self.__balance`).

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - amount < 0:
            print(f"Недостаточно средств. Баланс: {self.__balance}")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


bank1 = BankAccount(1000)
bank1.deposit(500)
bank1.withdraw(600)
print(bank1.get_balance())
print(bank1.__balance)
