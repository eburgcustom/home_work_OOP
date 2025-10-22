import pytest


def test_smartphone_init(smartphone_1):
    """Тестирование инициализации продукта"""
    assert smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_1.price == 180000.0
    assert smartphone_1.quantity == 5
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.model == "S23 Ultra"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Серый"


def test_smartphone_add(smartphone_1, smartphone_2):
    """Тестирование сложения двух продуктов"""
    assert smartphone_1 + smartphone_2 == 2580000.0


def test_smartphone_add_error(smartphone_1):
    """Тестирование ошибки сложения"""
    with pytest.raises(TypeError):
        smartphone_1 + 1
