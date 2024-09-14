from src.product import Product


def test_product_repr():
    # Создаем продукт
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    # Ожидаемая строка для метода __repr__
    expected_repr = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

    # Проверяем, что метод __repr__ возвращает ожидаемое значение
    assert repr(product) == expected_repr


def test_product_initialization():
    # Создаем продукт
    product = Product("iPhone 15", "512GB, Gray space", 210000.0, 8)

    # Проверяем правильность инициализации атрибутов
    assert product.name == "iPhone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8
