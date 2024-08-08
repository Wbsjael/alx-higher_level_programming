#!/usr/bin/python3
"""Defining text_indentation"""


def text_indentation(text):
    """
    Defining function text_indentation

    args:
        text (string): the text to be printed.

    Returns:
        Nothing

    Raises:
        TypeError: if the text is not a string
    """

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    lines = result.split("\n")
    for line in lines:
        print(line.strip())
