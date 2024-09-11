import json

from config import FILE_PATH
from src.category import Category
from src.product import Product


def reader_json(path_to_file: str) -> dict:
    """Функция получения данных из json"""
    with open(path_to_file, encoding="UTF-8") as file:
        data_json = json.load(file)
    return data_json


data = reader_json(FILE_PATH)


def object_json(json_file: dict):
    """Функция создания объектов класса из данных json"""
    product_objects = []
    category_objects = []
    for category in json_file:
        category_objects.append(Category(**category))
        for product in category.get("products", []):
            product_objects.append(Product(**product))
    return category_objects, product_objects


if __name__ == "__main__":
    print(object_json(data))
