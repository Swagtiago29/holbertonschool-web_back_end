#!/usr/bin/env python3
"""
Module: wait_random.py

This module contains an asynchronous function that simulates a random delay.
It demonstrates the use of Python's `asyncio` library and the `random` modules
asynchronously sleep for a random amount of time within a given range.

The module includes the following:
- `wait_random`: A coroutine that waits for a random delay before returning th

Dependencies:
- random: To generate random numbers.
- asyncio: To handle asynchronous sleeping and concurrency.

Example usage:
    >>> import asyncio
    >>> result = asyncio.run(wait_random(5))
    >>> print(f"Random delay: {result}")
    Random delay: 3.145
"""

import random
import asyncio


async def wait_random(max_delay: int=10) -> float:
    """
    Asynchronously generates a random floating-point number and sleeps for tha
    amount of time.

    Args:
        max_delay (float, optional): The upper bound (in seconds) for the rand
                                      number to be generated. Defaults to 10.

    Returns:
        float: The random number generated, which represents the number of sec
               the program will "sleep" asynchronously.

    Example:
        >>> import asyncio
        >>> result = asyncio.run(wait_random(5))
        >>> print(result)
        3.145

    This function demonstrates a simple usage of asyncio.sleep() to simulate a
    non-blocking delay.
    """
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
