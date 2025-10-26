from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """ Геттер для приватного атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """ Сеттер проверкой корректности цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            answer = input(
                f"Цена снижается с {self.__price} до {new_price}. Подтвердите (y/n): "
            ).strip().lower()
            if answer != "y":
                print("Изменение отменено пользователем")
                return

        self.__price = new_price

    def __str__(self) -> str:
        """Возвращает строковое представление товара в формате:
        Название товара, цена: X руб. Остаток: Y шт.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Абстрактный метод сложения стоимости продуктов"""
        pass
