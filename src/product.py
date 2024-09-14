class Product:
    """Класс представления продукта"""

    name: str
    description: str
    price: int | float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
