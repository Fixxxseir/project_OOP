import pytest

from src.category_iterator import IterCategory


def test_itercategory(category_2):
    iter_start = IterCategory(category_2)
    assert str(next(iter_start)) == "Iphone 15, 95000 руб. Остаток: 8 шт."
    assert str(next(iter_start)) == "Iphone 16pro, 150000 руб. Остаток: 16 шт."

    with pytest.raises(StopIteration):
        next(iter_start)
