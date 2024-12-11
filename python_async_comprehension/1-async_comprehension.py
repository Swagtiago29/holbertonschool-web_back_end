#!/usr/bin/env python3
"""
Module: async_comprehension_module

This module provides functionality to asynchronously generate random integers
using an asynchronous generator and collect them using an asynchronous
comprehension. It utilizes the async_generator function from an external
module (0-async_generator) and collects the generated values in a list.

Functions:
    - async_comprehension: Collects values asynchronously from the
    async_generator and returns them in a list.

External Dependencies:
    - async_generator: An asynchronous generator function that generate random
    integers with a delay.
"""
import importlib
from typing import List
async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronously collects random integers from a generator."""
    return [i async for i in async_generator()]
