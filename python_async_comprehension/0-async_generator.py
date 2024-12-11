#!/usr/bin/env python3
"""
Module: Random Integer Generator with Asynchronous Delays
--------------------------------------------------------

This module defines an asynchronous function `async_generator` that simulates
random delays while generating random integers. The function generates 10
random integers between 0 and 10, with each integer generation followed by a
random delay (in seconds). The results are returned in a list.

Usage:
    This script is intended to be run as a standalone program.
    The main function runs the async generator and prints the results.

Functions:
    - async_generator(): Asynchronously generates random integers with random
     delays.
    - main(): Test function that runs the async_generator and prints the
    result.

Example:
    To run the script and view the output, execute the module in an environmen
    that supports asynchronous programming.
"""
import asyncio
from random import randint
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates a list of 10 random integers (between 0 and 10),
    each followed by a random delay. The delay is simulated using
    asyncio.sleep().

    This function does not block the event loop, and it allows other tasks
    to run while the delays are in place.

    Returns:
        list: A list of 10 randomly generated integers (between 0 and 10).
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield randint(0, 10)
