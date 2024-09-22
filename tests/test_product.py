from unittest.mock import patch

import pytest

from src.product import Product


def test_product_init(product_1):
    assert product_1.name == "Cars"
    assert product_1.description == "BMW"
    assert product_1.price == 100000
    assert product_1.quantity == 4


def test_product_price(product_1, capsys):
    product_1.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product_1.price = 1000000
    assert product_1.price == 1000000


@patch("builtins.input", return_value="y")
def test_price_decrease_accept(mock_input, product_1, capsys):
    product_1.price = 50  # Ставим новую цену меньше текущей
    captured = capsys.readouterr()  # Считываем вывод
    assert product_1.price == 50
    assert "Цена была изменена на 50" in captured.out


def test_new_product(product_2):
    product_new = Product.new_product(product_2)
    assert product_new.name == "Cars"
    assert product_new.description == "BMW"
    assert product_new.price == 100000
    assert product_new.quantity == 4


def test_repr_product(product_1):
    assert repr(product_1) == "Product(Cars, BMW, 100000, 4)"


def test_str_product(product_3):
    assert str(product_3) == "Продукт_1, 10 руб. Остаток: 99 шт."


def test_price(product_1):
    assert product_1.price == 100000


def test_add_product(product_1, product_3):
    assert product_1 + product_3 == 400990


def test_add_product_typeerror(category_1):
    assert TypeError


def test_product_type_error(product_1):
    with pytest.raises(TypeError):
        product_1 + 123123
