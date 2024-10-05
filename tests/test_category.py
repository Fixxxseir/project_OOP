import pytest
from src.category import Category
from src.product import Product


def test_category(category_1, category_2, category_3):
    assert category_1.name == "Auto"
    assert category_2.description == "Телефоны и больше ничего"
    assert len(category_2.products_list) == 2
    assert category_1.category_count == 3
    assert category_1.category_count == 3
    assert category_1.category_count == 3
    assert len(category_3.products_list) == 1


def test_category_str(category_3):
    assert category_3.products == "Продукт_1, 20 руб. Остаток: 99 шт.\n"


def test_add_product(category_3, product_3):
    category_3.add_product(product_3)
    assert len(category_3.products_list) == 1
    for product in category_3.products_list:
        assert product.name == "Продукт_1"
        assert product.price == 20
        assert product.quantity == 198


def test_add_category_not_product(category_3, fake_product):
    with pytest.raises(TypeError):
        category_3.add_product(fake_product)


def test_str_category(category_1):
    assert str(category_1) == "Auto, количество продуктов: 1002 шт."


def test_repr_category(category_3):
    assert repr(category_3) == "Category(Продукт, Описание продукта, Продукт_1, 20 руб. Остаток: 99 шт.\n)"


def test_middle_price():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    assert category1.middle_price() == 31000.0


def test_return_zero_midl_price():
    category_empty1 = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty1.middle_price() == 0


# def test_str_method():
#     products = [
#         {"name": "BMW", "description": "black", "price": 1000000, "quantity": 1}
#     ]
#     category = Category("cars", "buying a car", products)
#
#     expected_str = ("Category: cars, Products: {'name': 'BMW', 'description': 'black', 'price': "
#                     "1000000, 'quantity': 1}")
#     assert str(category) == expected_str
