#!/usr/bin/python3
"""
Module 5-text_indentation
breaks text into single spaced lines
delimted at '.', '?' and ':'
"""


def text_indentation(text):
    """
    text_indentation: breaks text into
    singled spaced lines, delimited at '.', '?' and ':'
    Raises a TypeError if 'text' is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for ch in ['.', '?', ':']:
        if ch in text:
            text = text.replace(ch, ch+"\n\n")

    print("\n".join(line.strip() for line in text.split("\n")), end="")
