import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


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


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_2():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def lawngrass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass_2():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def json_data():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации,"
            " но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром,"
            " станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]
