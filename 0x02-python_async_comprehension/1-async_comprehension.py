#!/usr/bin/env python3
"""
This module defines an asynchronous comprehension coroutine that collects 10
random numbers using the async_generator coroutine from the previous task.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronous comprehension coroutine that collects 10 random numbers
using the async_generator coroutine from the previous task.
    """
    results = [num async for num in async_generator()]
    return results
