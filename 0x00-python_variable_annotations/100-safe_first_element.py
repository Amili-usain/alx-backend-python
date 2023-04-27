#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""

from typing import Any, List, Optional


def safe_first_element(lst: List[Any]) -> Optional[Any]:
    """
    Returns the first element of a list if it is not empty, otherwise returns
None.

    Args:
        lst: A list of any type.

    Returns:
        The first element of the list, if it exists, or None if the list i
empty.
    """
    if lst:
        return lst[0]
    else:
        return None
