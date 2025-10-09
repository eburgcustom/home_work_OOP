
import pytest
from unittest.mock import patch
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

