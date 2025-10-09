

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
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

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Создает новый товар из словаря."""
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )
