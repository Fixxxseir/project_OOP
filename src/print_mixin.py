class PrintMixin:
    def __init__(self):
        """Класс миксин, при создании объекта выводит в консоль информацию об объекте"""
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
