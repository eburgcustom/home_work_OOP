
from unittest.mock import patch

import pytest

from src.base_product import BaseProduct
from src.product import Product


def test_product_init(product):
    """Тестирование инициализации продукта"""
    assert product.name == "43\" Xiaomi TV A Pro"
    assert product.description == "Яркий 4К QLED экран с естественными цветами"
    assert product.price == 27000.0
    assert product.quantity == 15


def test_price_property(product):
    """Тестирование геттера цены"""
    assert product.price == 27000.0


def test_price_setter_valid(product):
    """Тестирование сеттера цены с корректным значением"""
    product.price = 28000.0
    assert product.price == 28000.0


def test_price_setter_invalid(capsys, product):
    """Тестирование сеттера цены с некорректным значением"""
    # Очищаем буфер после создания объекта (который происходит в фикстуре)
    capsys.readouterr()

    product.price = -100.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 27000.0


def test_price_setter_decrease_with_confirmation(product):
    """Тестирование уменьшения цены с подтверждением"""
    with patch('builtins.input', return_value='y'):
        product.price = 800.0
    assert product.price == 800.0


def test_price_setter_decrease_without_confirmation(product):
    """Тестирование отмены уменьшения цены"""
    with patch('builtins.input', return_value='n'):
        with patch('builtins.print') as mock_print:
            product.price = 800.0
            mock_print.assert_called_with("Изменение отменено пользователем")
    assert product.price == 27000.0


def test_product_str(product):
    """Тестирование строкового представления товара в формате:
       Название товара, цена: X руб. Остаток: Y шт."""
    assert str(product) == "43\" Xiaomi TV A Pro, 27000.0 руб. Остаток: 15 шт."


def test_add_products_success():
    """Проверяет успешное сложение двух продуктов по общей стоимости."""
    p1 = Product("Samsung Galaxy S23", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    total = p1 + p2
    assert total == 2580000.0


def test_add_products_type_error():
    """Проверяет выброс TypeError при сложении с объектом другого типа."""
    p = Product("Телефон", "Модель A", 100.0, 3)

    with pytest.raises(TypeError, match="Можно складывать только объекты класса Product"):
        _ = p + 123


def test_baseproduct_is_abstract():
    """Проверяет, что BaseProduct нельзя инстанцировать напрямую."""
    with pytest.raises(TypeError):
        BaseProduct("Тест", "Описание", 100, 1)
