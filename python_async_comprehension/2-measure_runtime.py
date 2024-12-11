#!/usr/bin/env python3
"""
Measures the runtime of an asynchronous function.

This function uses the asyncio library to measure the runtime
of the provided asynchronous function. It uses asyncio.gather()
to execute the function multiple times in parallel.
"""
import importlib
import asyncio
import time
async_comprehension = importlib.import_module('1-async_comprehension').async_comprehension


async def measure_runtime()->float:
    """measures runtime of async_comprehension 4 times in parallel"""
    start = time.time()
    await asyncio.gather(async_comprehension(),async_comprehension(),
                   async_comprehension(),async_comprehension())
    end = time.time()
    return end - start
