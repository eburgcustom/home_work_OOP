# Каталог товаров

Проект представляет собой систему управления каталогом товаров, реализованную с использованием объектно-ориентированного программирования на Python.

## 📋 Описание

Проект позволяет:
- Создавать категории товаров
- Управлять товарами в категориях
- Загружать данные о товарах из JSON-файлов

## 🛠️ Зависимости

- Python 3.13+
- Poetry (для управления зависимостями)

## 🏗️ Структура проекта

```
home_work_OOP/
├── data/               # Файлы с данными (например, products.json)
├── src/                # Исходный код приложения
│   ├── __init__.py
│   ├── category.py     # Класс Category
│   ├── product.py      # Класс Product
│   └── utils.py        # Вспомогательные функции
├── tests/              # Тесты
├── pyproject.toml      # Конфигурация проекта и зависимости
└── README.md           # Этот файл
```


## 📝 Пример использования

```python
from src.category import Category
from src.product import Product
from src.utils import load_json, create_category_from_json

# Создание категории вручную
products = [
    Product("Телефон", "Смартфон", 50000.0, 10),
    Product("Ноутбук", "Игровой ноутбук", 150000.0, 5)
]
category = Category("Электроника", "Техника для дома и офиса", products)

# Загрузка категорий из JSON файла
categories_data = load_json("data/products.json")
categories = create_category_from_json(categories_data)
```