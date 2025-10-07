
def test_category_init(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны, как средство не только коммуникации," \
                                     "но и получения дополнительных функций для удобства жизни"
    assert len(category_1.products) == 3
    assert category_2.name == "Телевизоры"
    assert category_2.description == "Современный телевизор, который позволяет наслаждаться просмотром," \
                                     "станет вашим другом и помощником"
    assert len(category_2.products) == 2

    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 5
    assert category_2.product_count == 5
