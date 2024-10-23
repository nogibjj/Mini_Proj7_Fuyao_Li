"""
Test goes here

"""
import subprocess
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    insert_row,
    update_row,
    delete_row,
)


def test_extract():
    results = extract()
    assert results is not None


def test_load():
    results = load()
    assert results is not None


def test_insert_row():
    test_data = {
        "date": "10/30/2022",
        "location": "Durham, NC",
        "city": "Durham",
        "state": "NC",
        "lat": 35.99,
        "lng": 78.89,
    }

    # Insert the row
    insert_result = insert_row(
        test_data["date"],
        test_data["location"],
        test_data["city"],
        test_data["state"],
        test_data["lat"],
        test_data["lng"],
    )
    assert insert_result is True


def test_update_row():
    test_data = {
        "date": "10/30/2024",
        "city": "Durham",
    }

    update_result = update_row(test_data["city"], test_data["date"])
    assert update_result is True


def test_delete_row():
    test_data = {
        "city": "Durham",
    }
    delete_result = delete_row(test_data["city"])
    assert delete_result is True


if __name__ == "__main__":
    # test_extract()
    # test_load()
    # test_insert_row()
    test_update_row()
    test_delete_row()