from src.product import Product


class Category:
    """Класс представления категории продуктов."""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        if isinstance(product, Product):
            for product in self.__products:
                if product.name == product.name:
                    product.quantity += product.quantity
                    if product.price < product.price:
                        product.price = product.price
                    return
        else:
            raise TypeError("Продукт должен быть экземпляром класса Product")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Список товаров в виде строк в формате"""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт. "
        return product_str

    @property
    def products_list(self):
        return self.__products

    def __repr__(self):
        return f"Category: {self.name}, products: {self.__products}"

    def __str__(self):
        total_quantity = 0
        for item in self.__products:
            total_quantity += item.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."
