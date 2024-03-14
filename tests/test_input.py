import pytest

from app.io.input import read_file, read_file_with_pandas


#  function tests an existing file in directory 'data'
def test_read_existing_file():
    assert read_file("D:\\pythonWorkspace\\python_template\\data\\test_read_file.txt") == "diamonds"


#  function tests non-existent file
def test_read_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        assert read_file("D:\\pythonWorkspace\\python_template\\data\\nonexistent_file.txt")


if __name__ == "__main__":
    test_read_existing_file()
    test_read_nonexistent_file()
    print("Everything passed")

