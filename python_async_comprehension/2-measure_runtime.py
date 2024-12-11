#!/usr/bin/env python3
"""
Measures the runtime of an asynchronous function.

This function uses the asyncio library to measure the runtime
of the provided asynchronous function. It uses asyncio.gather()
to execute the function multiple times in parallel.
"""
import importlib
import asyncio
async_comprehension = importlib.import_module('1-async_comprehension').async_comprehension
import time

async def measure_runtime()->float:
    """measures runtime of async_comprehension 4 times in parallel"""
    start = time.time()
    asyncio.gather(async_comprehension(),async_comprehension(),
                   async_comprehension(),async_comprehension())
    end = time.time()
    return start - end
