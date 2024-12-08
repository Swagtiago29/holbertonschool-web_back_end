#!/usr/bin/env python3
import importlib
import time
import asyncio

wait_n = importlib.import_module('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay:int) -> float:
    startint_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    ending_time = time.time()
    runtime = ending_time - startint_time
    return runtime / n
