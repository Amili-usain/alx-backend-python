#!/usr/bin/env python3
"""A type-annotated function concat that takes a string str1 and a string str2
as arguments and returns a concatenated string"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two input strings and returns the result as a new string.

    Args:
        str1 (str): The first string to concatenate.
        str2 (str): The second string to concatenate.

    Returns:
        str: The concatenated string.
    """
    return str1 + str2
