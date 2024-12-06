#!/usr/bin/env python3

"""
8-make_multiplier.py

This module provides a function, `make_multipier`, that generates a multiplier
function. The multiplier function multiplies its input by a specified multipli
value provided when creating it.

The module demonstrates the concept of higher-order functions, where one
function returns another function, and the returned function "remembers" the
multiplier value.

Functions:
    make_multipier(multiplier: float) -> Callable[[float], float]:
        Creates and returns a function that multiplies its input by the multiplier.

Example usage:
    multiply_by_3 = make_multipier(3.0)
    result = multiply_by_3(4.0)  # result will be 12.0
    multiply_by_5 = make_multipier(5.0)
    result2 = multiply_by_5(4.0)  # result2 will be 20.0
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a given number by a specified multiplie

    Args:
        multiplier (float): The multiplier value that will be used to multiply
                             the input value.

    Returns:
        Callable[[float], float]: A function that takes a float as input and
                                  returns the product of the input and the
                                  multiplier.
    """
    def multi(x: float) -> float:
        """
        Multiplies the input value by the multiplier.

        Args:
            x (float): The value to be multiplied.

        Returns:
            float: The result of multiplying the input value by the multiplier.
        """
        return x * multiplier

    return multi
