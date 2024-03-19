import pandas as pd


def output_text_to_the_console(text):
    """
    Function displays the text in a console

    Args:
        text(str): The text that user wants to output in console

    Returns:
        None

    Raises:
        IOError: If user entered invalid data
    """
    try:
        print(text)
    except IOError:
        raise IOError("Input-output error occurred")


def write_information_to_file(text, file_path):
    """
        Function writes information to file using built-in python functions

        Args:
            text(str): The text that has to be written down in the file
            file_path(str): The path of the file in which the text will be written

        Returns:
            str: success message

        Raises:
            IOError: If user entered invalid data
        """
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        return print(f"\nText was successfully written to the file: '{file_path}'.")
    except IOError:
        raise IOError(f"Input-output error occurred while writing text to the file: '{file_path}'")


def write_information_to_file_with_pandas(text, file_path):
    """
    Function writes information to file using pandas library

    Args:
        text(str): The text that has to be written down in the file
        file_path(str): The path of the file in which the text will be written

    Returns:
        str: success message

    Raises:
            IOError: If user entered invalid data
    """
    try:
        data_frame = pd.DataFrame([text])
        data_frame.to_csv(file_path, index=False)
        return print(f"\nText was successfully written to the file: '{file_path}'.")
    except IOError:
        raise IOError(f"Input-output error occurred while writing text to the file: '{file_path}'")