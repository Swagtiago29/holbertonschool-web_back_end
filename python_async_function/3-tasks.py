#!/usr/bin/env python3
"""
This module defines a function `task_wait_random` which creates an asyncio task
that wraps the `wait_random` coroutine. The `wait_random` coroutine is expected
to simulate a random delay and return the delay after the sleep.

The `task_wait_random` function schedules the `wait_random` coroutine with a
specified `max_delay`, which is passed as an argument, and returns an asyncio task
that will execute the coroutine concurrently when awaited.

Modules Used:
- `importlib`: Used to dynamically import the `wait_random` coroutine from the
  `0-basic_async_syntax` module.
- `asyncio`: Used to create the asyncio task and manage asynchronous execution.

Functions:
- `task_wait_random`: Schedules the `wait_random` coroutine with the given
  `max_delay` and returns the resulting asyncio task.
"""
import importlib
import asyncio
wait_random = importlib.import_module('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Schedules the `wait_random` coroutine with the provided `max_delay` as the
    argument and returns the corresponding asyncio task.

    This function creates an asyncio task from the `wait_random` coroutine,
    which generates a random delay between 0 and `max_delay` and simulates
    waiting for that delay asynchronously.

    Args:
        max_delay (int): The maximum delay (in seconds) for the `wait_random`
                         coroutine. The coroutine will generate a random float
                         between 0 and `max_delay`.

    Returns:
        asyncio.Task: A Task object that represents the execution of the
                      `wait_random` coroutine.

    Example:
        >>> task = task_wait_random(5)
        >>> result = await task
        >>> print(result)  # Random delay between 0 and 5 seconds

    Explanation:
        The `task_wait_random` function wraps the `wait_random` coroutine into
        a task, which can be awaited to get the result (the delay time). The task
        will execute concurrently within an event loop.
    """
    # Create and return an asyncio task that runs the wait_random coroutine
    return asyncio.create_task(wait_random(max_delay))
