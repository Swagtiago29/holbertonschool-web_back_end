#!/usr/bin/env python3
import importlib
import time

wait_n = importlib.import_module('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay:int) -> float:
    runtime = time.time()
    return runtime / n