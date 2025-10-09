
def test_category_init(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны, как средство не только коммуникации," \
                                     "но и получения дополнительных функций для удобства жизни"
    assert len(category_1.products.split('\n')) == 3
    assert category_2.name == "Телевизоры"
    assert category_2.description == "Современный телевизор, который позволяет наслаждаться просмотром," \
                                     "станет вашим другом и помощником"
    assert len(category_2.products.split('\n')) == 2

    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 5
    assert category_2.product_count == 5


def test_add_product(product):
    assert product.name == "43\" Xiaomi TV A Pro"
    assert product.description == "Яркий 4К QLED экран с естественными цветами"
    assert product.price == 27000.0
    assert product.quantity == 15


def test_products(category_2):
    products_str = category_2.products
    assert products_str == ('55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
                            '43" Xiaomi TV A Pro, 27000.0 руб. Остаток: 15 шт.')
