from app.io.input import input_from_console, read_file, read_file_with_pandas
from app.io.output import output_text_to_the_console, write_information_to_file


def main():
    print("Test 1:\n")
    # read a text from console and then output it to the console
    read_text_from_console = input_from_console()
    output_text_to_the_console("Text from console: ")
    output_text_to_the_console(read_text_from_console)
    print("--------------------------------------------------------------------\n")

    print("Test 2:\n")
    # read a text from file using built-in Python functions and then display this text to console
    read_text_from_file = read_file("D:\\pythonWorkspace\\python_template\\data\\song.txt")
    output_text_to_the_console("Text which was read from the file via built-in Python functions:\n")
    output_text_to_the_console(read_text_from_file)
    print("--------------------------------------------------------------------\n")

    print("Test 3:\n")
    # read a text from file using pandas library and then display this text to console
    read_text_from_file_via_pandas = read_file_with_pandas("D:\\pythonWorkspace\\python_template\\data\\starwars.txt")
    output_text_to_the_console("Text which was read from the file via pandas library:\n")
    output_text_to_the_console(read_text_from_file_via_pandas)
    print("--------------------------------------------------------------------\n")

    print("Test 4:\n")
    # write information to file using built-in Python functions
    text_to_write_in_file = input_from_console()
    write_information_to_file(text_to_write_in_file, "D:\\pythonWorkspace\\python_template\\data\\written text.txt")


if __name__ == "__main__":
    main()
