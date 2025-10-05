import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def load_json(file_path: str) -> Any:
    full_path = os.path.abspath(file_path)
    with open(full_path, "r", encoding="utf-8") as file:
        return json.load(file)


def create_category_from_json(data: list[dict[str, Any]]) -> list[Category]:
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        categories.append(Category(**category))
    return categories
