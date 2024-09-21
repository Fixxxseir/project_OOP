import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_1():
    return Product(name="Cars", description="BMW", price=100000, quantity=4)


@pytest.fixture
def product_2():
    return {"name": "Cars", "description": "BMW", "price": 100000, "quantity": 4}


@pytest.fixture
def product_3():
    return Product(name="Продукт_1", description="Описание продукта", price=10, quantity=99)


@pytest.fixture
def product_4():
    return Product(name="Auto", description="LADA", price=200, quantity=0)


@pytest.fixture
def category_1():
    return Category(
        name="Auto",
        description="Cars",
        products=[
            Product("BMW", "M5 e60", 300000, quantity=1),
            Product("Mers", "w140", 100000, quantity=2),
            Product("Lada", "Largus", 50, quantity=999),
        ],
    )


@pytest.fixture
def category_2():
    return Category(
        name="Мобильная техника",
        description="Телефоны и больше ничего",
        products=[
            Product("Iphone 15", "512GB, Gray space", 95000, quantity=8),
            Product("Iphone 16pro", "256, Black", 150000, quantity=16),
        ],
    )


@pytest.fixture
def category_3():
    return Category(
        name="Продукт",
        description="Описание продукта",
        products=[Product("Продукт_1", "Описание продукта", 20, quantity=99)],
    )


@pytest.fixture
def fake_product():
    return "fake_product"
