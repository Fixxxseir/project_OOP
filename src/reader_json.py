import json

from config import FILE_PATH
from src.category import Category
from src.product import Product


def reader_json(path_to_file: str) -> dict:
    """Функция получения данных из json"""
    with open(path_to_file, "r", encoding="UTF-8") as file:
        data_json = json.load(file)
    return data_json


data = reader_json(FILE_PATH)


def object_json(json_file: dict):
    """Функция создания объектов класса из данных json"""
    categories = []
    for category in json_file:
        products_list = []
        for product in category["products"]:
            products_list.append(Product(**product))
        category["products"] = products_list
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    print(object_json(data))
