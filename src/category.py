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
        self.products = products
        Category.category_count += 1
        Category.product_count += len(self.products)

    def __repr__(self):
        return f"Category: {self.name}, products: {self.products}"

    def __str__(self):
        return f"Category: {self.name}, Products: {', '.join(str(p) for p in self.products)}"
