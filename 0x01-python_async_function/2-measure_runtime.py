#!/usr/bin/env python3
"""
Imports wait_n into 2-measure_runtime.py from the previous file.

Creates a measure_time function with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay), and returns
total_time / n.

The function also returns a float and uses the time module to measur
approximate elapsed time.
"""

from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Asynchronous coroutine that measures the total execution time for
wait_n(n, max_delay), and returns the average time per call.

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay in seconds for wait_random
    Returns: Average time per call.
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - start
    return (total_time / n)
