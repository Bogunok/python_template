

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
        Function displays the text in a console

        Args:
            text(str): The text that has to written down in the file
            file_path(str): The path of the file in which the text will be written

        Returns:
            str: success message

        Raises:
            IOError: If user entered invalid data
        """
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        return f"Text was successfully written to the file: '{file_path}'."
    except IOError:
        raise IOError(f"Input-output error occurred while writing text to the file: '{file_path}'")