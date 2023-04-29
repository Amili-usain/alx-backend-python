#!/usr/bin/env python3
"""Takes code from wait_n and alters it into a new function task_wait_n that
calls task_wait_random"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random



async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times with the
specified max_delay.

    Args:
        n (int): Number of times to spawn the coroutine.
        max_delay (int): Maximum delay in seconds for each coroutine.

    Returns:
        List[float]: List of all the delays (float values) in ascending order.
    """
    tasks = []
    delays = []

    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
