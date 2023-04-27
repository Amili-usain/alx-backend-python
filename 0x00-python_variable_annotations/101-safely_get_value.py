#!/usr/bin/env python3
"""This module provides a function to safely get the value associated with a
key in a dictionary."""

from typing import TypeVar, Mapping, Union, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Safely retrieves a value from a dictionary given a key. If the key is
not present in the dictionary, returns a default value."""
    if key in dct:
        return dct[key]
    else:
        return default
