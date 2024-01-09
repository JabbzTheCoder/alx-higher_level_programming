#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
    - filename: str (default is an empty string)

    Returns:
    - None
    """

    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')

