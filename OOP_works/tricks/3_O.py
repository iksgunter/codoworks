# 3. SOLID (O)
# Реализуйте систему оплаты: базовый класс PaymentProcessor, у которого есть метод pay().
# Добавьте поддержку разных способов оплаты (PayPal, CreditCard, Crypto) без изменения базового кода.
# Цель:
# Использовать полиморфизм или абстракции (например, через ABC).
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass


class PayPal(PaymentProcessor):
    def pay(self, amount: float) -> bool:
        print(f'Оплата {amount} через PayPal')
        # Логика оплаты...
        return True


class CreditCard(PaymentProcessor):
    def pay(self, amount: float) -> bool:
        print(f'Оплата {amount} через CreditCard')
        # Логика оплаты...
        return True


class Crypto(PaymentProcessor):
    def pay(self, amount: float) -> bool:
        print(f'Оплата {amount} через Crypto')
        # Логика оплаты...
        return True


class PaymentService:
    def __init__(self, gateway: PaymentProcessor):
        self.gateway = gateway

    def process_payment(self, amount: float):
        success = self.gateway.pay(amount)
        if success:
            print('Оплата прошла успешно')
        else:
            print('Ошибка при оплате')


paypal_gateway = PayPal()
paypal_payment = PaymentService(paypal_gateway)
paypal_payment.process_payment(1000.0)

crypto_gateway = Crypto()
crypto_payment = PaymentService(crypto_gateway)
crypto_payment.process_payment(10000000000.0)
