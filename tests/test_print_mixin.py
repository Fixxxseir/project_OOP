from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


def test_print_mixin(capsys):
    Product("BMW", "M5 e60", 300000, quantity=1)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(BMW, M5 e60, 300000, 1)"


def test_smartphone_mixin(capsys):
    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"


def test_lawngrass_mixin(capsys):
    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
