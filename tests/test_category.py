import pytest

from src.category import Category


@pytest.fixture(autouse=True)
def reset_category_counts():
    """Сброс количества категорий и продуктов перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


def test_category_initialization():
    # Создаем "продукты" в виде словарей
    products = [
        {"name": "Product1", "description": "Description1", "price": 100.0, "quantity": 1},
        {"name": "Product2", "description": "Description2", "price": 200.0, "quantity": 2},
    ]

    # Создаем категорию
    category = Category("Category1", "Description of Category_1", products)

    # Проверяем правильность инициализации атрибутов
    assert category.name == "Category1"
    assert category.description == "Description of Category_1"
    assert len(category.products) == 2

    # Проверяем увеличение счетчиков
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_empty_category():
    # Создаем пустую категорию
    category = Category("zero", "Description zero", [])

    # Проверяем правильность инициализации атрибутов
    assert category.name == "zero"
    assert category.description == "Description zero"
    assert len(category.products) == 0

    # Проверяем увеличение счетчиков
    assert Category.category_count == 1
    assert Category.product_count == 0


# def test_multiple_categories():
#     # Создаем несколько категорий
#     products1 = [
#         {"name": "Product1", "description": "Description_1", "price": 100.0, "quantity": 1},
#         {"name": "Product2", "description": "Description_2", "price": 200.0, "quantity": 2}
#     ]
#     products2 = [
#         {"name": "Product3", "description": "Description3", "price": 300.0, "quantity": 3},
#         {"name": "Product4", "description": "Description4", "price": 400.0, "quantity": 4}
#     ]
#
#     category1 = Category("Category_1", "Description of Category1", products1)
#     category2 = Category("Category_2", "Description of Category2", products2)
#
#     # Проверяем правильность инициализации атрибутов для обеих категорий
#     assert category1.name == "Category_1"
#     assert len(category1.products) == 2
#     assert category2.name == "Category_2"
#     assert len(category2.products) == 2
#
#     # Проверяем увеличение счетчиков
#     assert Category.category_count == 2
#     assert Category.product_count == 4


def test_repr_method():
    products = [
        {"name": "chocolate", "description": "delicious", "price": 100.0, "quantity": 5}
    ]
    category = Category("Magazine", "buying a products", products)

    expected_repr = ("Category: Magazine, products: [{'name': 'chocolate', 'description': 'delicious', 'price': "
                     "100.0, 'quantity': 5}]")
    assert repr(category) == expected_repr


def test_str_method():
    products = [
        {"name": "BMW", "description": "black", "price": 1000000, "quantity": 1}
    ]
    category = Category("cars", "buying a car", products)

    expected_str = ("Category: cars, Products: {'name': 'BMW', 'description': 'black', 'price': "
                    "1000000, 'quantity': 1}")
    assert str(category) == expected_str
