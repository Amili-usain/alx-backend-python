#!/usr/bin/env python3
"""Module with measure_runtime coroutine that executes async_comprehension
four times in parallel and measures the total execution time.
"""
import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension 4 times and measures the total execution
time."""
    start = time.time()
    res = await asyncio.gather(*(async_comprehension() for x in range(4)))
    total_runtime = time.time() - start
    return total_runtime
