#!/usr/bin/env python3
"""
This module defines a function `to_kv` that takes a string and a number (eithe
an integer or a floating-point value) and returns a tuple.

The tuple consists of:
1. The original string `k`.
2. The square of the input number `v`, represented as a floating-point value.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with:
    - The string `k` as the first element.
    - The square of the number `v` as the second element (as a float).

    Parameters:
    k (str): A string value.
    v (Union[int, float]): A number (either an int or a float) to be squared.

    Returns:
    Tuple[str, float]: A tuple where:
                        - The first element is the string `k`.
                        - The second element is the square of `v` as a float.

    Example:
    >>> to_kv("age", 5)
    ('age', 25.0)

    >>> to_kv("pi", 3.14)
    ('pi', 9.8596)
    """
    tt: tuple = (k, v * v)  # Create a tuple with the string k and the square
    return tt
