#!/usr/bin/env python3
"""
This module provides an asynchronous function `wait_n` that spawns multiple
tasks to execute the `wait_random` function concurrently.

It imports the `wait_random` function from the `0-basic_async_syntax` module
dynamically. The `wait_n` function allows for the execution of `n` concurrent
tasks, each calling `wait_random(max_delay)`, and returns a list of the delays
produced by each task.

Modules:
    importlib: A standard library used to import other modules dynamically.
    asyncio: A library used to write concurrent code using asynchronous I/O.
    typing: Provides type hinting for Python programs (used here to specify
    that `wait_n` returns a list of floats).
"""

import importlib
import asyncio
from typing import List

wait_random = importlib.import_module('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates and runs `n` asynchronous tasks that call `wait_random(max_delay)`
    concurrently.
    The function will spawn `n` asynchronous tasks that each call
    `wait_random(max_delay)`, where `wait_random` is expected to return a
    random delay between 0 and `max_delay`. The function waits for all the
    tasks to complete and returns a list of delays (floats) in the order the
    tasks finish.

    Args:
        n (int): The number of times to call `wait_random` concurrently.
        max_delay (int): The maximum delay (in seconds) to pass to
        `wait_random`.

    Returns:
        List[float]: A list of `n` float values representing the random delays
        generated
        by each task in the same order the tasks finish.

    Example:
        >>> asyncio.run(wait_n(3, 5))
        [1.2, 0.5, 3.0]
    """

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    for i in range(len(delays)):
        for j in range(0, len(delays) - i - 1):
            if delays[j] > delays[j + 1]:
                delays[j], delays[j + 1] = delays[j + 1], delays[j]
    return delays
