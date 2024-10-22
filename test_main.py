"""
Test goes here

"""
import subprocess


def test_extract():
    result = subprocess.run(
        [
            "python",
            "main.py",
            "extract",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_load():
    result = subprocess.run(
        [
            "python",
            "main.py",
            "load",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_insert_row():
    result = subprocess.run(
        [
            "python",
            "main.py",
            "insert",
            "10/30/2016", 
            "Durham, NC", 
            "Durham", 
            "NC", 
            "35.99", 
            "78.89"
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0



def test_update_row():
    result = subprocess.run(
        [
            "python",
            "main.py",
            "update",
            "Durham", 
            "10/15/2022", 
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_delete_row():
    result = subprocess.run(
        [
            "python",
            "main.py",
            "delete",
            "Manchester", 
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


if __name__ == "__main__":
    # test_extract()
    # test_load()
    # test_insert_row()
    test_update_row()
    test_delete_row()