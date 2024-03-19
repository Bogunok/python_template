import pytest
from app.io.input import read_file, read_file_with_pandas


#  function tests 'read_file' on existing file
def test_read_existing_file():
    expected_result = 'diamonds'
    actual_result = read_file("D:\\pythonWorkspace\\python_template\\data\\test_read_file.txt")
    assert expected_result == actual_result


#  function tests 'read_file' on non-existent file
def test_read_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        assert read_file("D:\\pythonWorkspace\\python_template\\data\\nonexistent_file.txt")


#  function tests 'read_file_with_pandas' on existing file
def test_read_file_with_pandas_existing_file():
    assert read_file_with_pandas("D:\\pythonWorkspace\\python_template\\data\\test_pandas.csv")


#  function tests 'read_file_with_pandas' on non-existent file
def test_read_file_with_pandas_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        read_file_with_pandas("D:\\pythonWorkspace\\python_template\\data\\test_pandas2.csv")


if __name__ == "__main__":
    test_read_existing_file()
    test_read_nonexistent_file()
    test_read_file_with_pandas_existing_file()
    test_read_file_with_pandas_nonexistent_file()

