class Product:
    """Класс представления продукта"""

    name: str
    description: str
    price: int | float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, dict_product):
        """Создает объект класса Product из словаря который подается на вход"""
        name = dict_product["name"]
        description = dict_product["description"]
        price = dict_product["price"]
        quantity = dict_product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            question = input("Новая цена меньше старой, заменить цену? Введите y/n ")
            if question == "y":
                self.__price = new_price
                print(f"Цена была изменена на {new_price}")
            else:
                print(f"Цена осталась прежней ({self.__price})")
        elif self.__price < new_price:
            self.__price = new_price
