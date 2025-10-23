from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    message = capsys.readouterr()
    assert message.out.strip() == "Создан объект класса Product('Iphone 15', '512GB, Gray space', 210000.0, 8)"

    Smartphone("Iphone 15", "512GB, Gray space",
               210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Создан объект класса Smartphone('Iphone 15', '512GB, Gray space', 210000.0, 8)"

    LawnGrass("Газонная трава 2",
              "Выносливая трава",
              450.0,
              15,
              "США",
              "5 дней",
              "Темно-зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "Создан объект класса LawnGrass('Газонная трава 2', 'Выносливая трава', 450.0, 15)"
