
from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product) -> None:
        """Добавляет объект Product в категорию."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self) -> str:
        """Возвращает строковое представление категории в формате:
        Название категории, количество продуктов: X шт.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self) -> str:
        """Геттер: возвращает строку со списком товаров."""
        result = ""
        for p in self.__products:
            result += f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n"
        return result.strip()
        
    def middle_price(self) -> float:
        """
        Рассчитывает средний ценник всех товаров в категории.
        
        Возвращает:
            float: Средняя цена товаров в категории
            
        Исключения:
            ZeroDivisionError: Если в категории нет товаров, возвращает 0
        """
        try:
            total_price = sum(product.price for product in self.__products)
            return round(total_price / len(self.__products), 1)
        except ZeroDivisionError:
            return 0.0
