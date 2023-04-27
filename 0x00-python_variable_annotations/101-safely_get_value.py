#!/usr/bin/env python3
"""
This module provides a function to safely get the value associated with a key
in a dictionary.
"""

from typing import Any, Dict, TypeVar

K = TypeVar('K')
V = TypeVar('V')


def safely_get_value(dct: Dict[K, V], key: K, default: Any = None) -> Any:
    """
    Safely retrieves a value from a dictionary given a key. If the key is not
present in the dictionary, returns a default value.

    Args:
        dct: The dictionary to retrieve a value from.
        key: The key to use to retrieve the value.
        default: The default value to return if the key is not in the
dictionary. Defaults to None.

    Returns:
        The value associated with the key, if it exists, or the default value
if it does not.
    """
    if key in dct:
        return dct[key]
    else:
        return default
