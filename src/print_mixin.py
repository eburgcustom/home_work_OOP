
class PrintMixin:
    """Миксин, который при создании объекта выводит информацию о классе и параметрах."""

    def __init__(self, *args):
        print(f"Создан объект класса {self.__class__.__name__}{args}")
        super().__init__(*args)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"
