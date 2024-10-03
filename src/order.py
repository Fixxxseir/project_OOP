from src.product import Product
from src.base_order import BaseOrderProduct


class Order(BaseOrderProduct):
    """Класс "заказ", информация о купленном товаре,
    кол-во а так же стоимость"""

    product: Product
    quantity: int

    def __init__(self, product, quantity):
        self.__products = product
        self.__quantity = quantity
        self.__total_price = 0

    @property
    def products(self):
        return f"{self.__products.name}, {self.__products.description}"

    @property
    def quantity(self):
        return self.__quantity

    @products.setter
    def products(self, new_product):
        raise ValueError("Добавлять новый товар в уже созданный заказ невозможно!")

    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity += new_quantity

    @property
    def total_price(self):
        self.__total_price = self.__quantity * self.__products.price
        return self.__total_price


# if __name__ == "__main__":
#     product = Product("Programs", "goodbyedpi", "free", quantity="infinite")
#     product2 = Product("Developer", "backend", 4000, quantity=1)
#
#     order = Order(product2, 2)
#     print(order.products)
#     print(order.quantity)
#     print(order.total_price)
#     order.quantity = 2
#     print(order.products)
#     print(order.quantity)
#     print(order.total_price)
