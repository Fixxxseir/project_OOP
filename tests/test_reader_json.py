from unittest.mock import patch
from config import FILE_PATH
from src.reader_json import reader_json, object_json


@patch("json.load")
def test_data_from_json(mock_json_load, json_data):
    mock_json_load.return_value = json_data
    assert reader_json(FILE_PATH) == json_data


def test_objects_from_data_init(json_data):
    objects = object_json(json_data)
    assert objects[0].name == "Смартфоны"
    assert objects[1].name == "Телевизоры"
    assert (
        objects[1].description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
