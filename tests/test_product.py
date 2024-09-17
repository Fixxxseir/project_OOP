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


def test_new_product(product_2):
    product_new = Product.new_product(product_2)
    assert product_new.name == "Cars"
    assert product_new.description == "BMW"
    assert product_new.price == 100000
    assert product_new.quantity == 4


def test_repr_product(product_1):
    assert repr(product_1) == "Cars, 100000 руб. Остаток: 4 шт."


def test_price(product_1):
    assert product_1.price == 100000
