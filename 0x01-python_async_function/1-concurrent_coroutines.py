#!/usr/bin/env python3
"""Imports wait_random from the previous python file written and
writes an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with the specified
max_delay, and returns the list of all the delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    tasks = []
    for i in range(n):
        task = wait_random(max_delay)
        tasks.append(task)
    delays = []
    for task in tasks:
        delay = await task
        delays.append(delay)
    delays.sort()
    return delays
