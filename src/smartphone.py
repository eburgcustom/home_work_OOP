from src.product import Product


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float,
                 model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: 'Product') -> float:
        """Складывает смартфоны по общей стоимости (цена * количество).

        Возвращает:
            float: Суммарная стоимость всех смартфонов

        Исключения:
            TypeError: Если other не является экземпляром класса Smartphone
        """
        if type(other) is Smartphone:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError("Можно складывать только объекты класса Smartphone")
