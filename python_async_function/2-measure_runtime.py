#!/usr/bin/env python3
import importlib
import time
import asyncio

# Importing the wait_n function from the 1-concurrent_coroutines module
wait_n = importlib.import_module('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time of the `wait_n` function, which runs `n`
    asynchronous tasks concurrently, and returns the average time per call.

    The function calculates the total time taken by the `wait_n` function to
    execute and then returns the average time taken for each individual call
    to `wait_random` (which is executed `n` times concurrently). The time is
    measured using the `time.time()` method, which provides an approximate
    time in seconds.

    Args:
        n (int): The number of concurrent tasks to run with `wait_n`. This
        determines how many times `wait_random` will be called.
        max_delay (int): The maximum delay (in seconds) for each individual
        `wait_random` call. `wait_random` generates a random float between
        0 and `max_delay`.

    Returns:
        float: The average execution time for each individual task
        (in seconds).
        The time is calculated by dividing the total runtime by `n`.

    Example:
        >>> measure_time(5, 10)
        Average time per call: 0.3567 seconds

    Explanation:
        The function will run `n` asynchronous tasks concurrently using the
        `wait_n` function, each with a random delay up to `max_delay`, and
        then return the average time per task.
    """
    startint_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    ending_time = time.time()
    runtime = ending_time - startint_time
    return runtime / n
