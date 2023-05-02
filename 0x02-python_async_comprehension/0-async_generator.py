#!/usr/bin/env python3
"""This module contains a coroutine called async_generator that loops 10 times,
waits 1 second asynchronously, then yields a random number between 0 and 10.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine that yields a random number between 0 and 10, after waiting 1
second asynchronously, for 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
