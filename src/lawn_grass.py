from src.base_product import BaseProduct
from src.product import Product


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: BaseProduct) -> float:
        """Складывает газонную траву по общей стоимости (цена * количество).

        Возвращает:
            float: Суммарная стоимость всех трав

        Исключения:
            TypeError: Если other не является экземпляром класса LawnGrass
        """
        if type(other) is LawnGrass:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError("Можно складывать только объекты класса LawnGrass")
