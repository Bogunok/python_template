import pandas


def input_from_console():
    """
    Function reads a text from console

    Args:
        None

    Returns:
        str: text which was read from the console

    Raises:
        IOError: If user enters incorrect file name or location
    """
    try:
        return input("Enter the text: ")
    except IOError:
        raise IOError("Input-output error occurred")


def read_file(file_path):
    """
    Function reads a file with a help of built-in functions in Python

    Args:
        file_path(str): The path of the file user wants to read

    Returns:
        None

    Raises:
        IOError: If user enters incorrect file name or location
        FileNotFoundError: If user wants to access a file that doesn't exist
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find the file '{file_path}'.")
    except IOError:
        raise IOError(f"Input-output error occurred while reading a file '{file_path}'")


def read_file_with_pandas(file_path):
    """
    Function reads file with a help of a pandas library

    Args:
        file_path(str): The path of the file user wants to read

    Returns:
        None

    Raises:
        IOError: If user enters incorrect file name or location
        FileNotFoundError: If user wants to access a file that doesn't exist
    """
    try:
        return pandas.read_csv(file_path).to_string(index=False)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find the file '{file_path}'.")
    except IOError:
        raise IOError(f"Input-output error occurred while reading a file '{file_path}'")
